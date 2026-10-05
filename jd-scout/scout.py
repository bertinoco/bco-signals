#!/usr/bin/env python3
"""Poll public ATS job boards for postings worth triaging.

Greenhouse, Lever and Ashby each publish a free, unauthenticated JSON feed of
every open job on a company's board. This script reads those feeds for a list
of companies, keeps postings that match jd-scout/keywords.json, drops anything
already archived in jd-source/, and writes the result as JSON documents ready
for the triage page's database.

It never decides eligibility. That stays with the add-jd audit.

Run from the repo root:

    # weekly poll (see ROUTINE.md for the full weekly run)
    python3 jd-scout/scout.py poll --companies jd-scout/seed-companies.json \\
        [discovered.json ...] --db-dump DUMP_DIR --out OUT_DIR

    # company slugs from discovery search result URLs (one per line on stdin)
    python3 jd-scout/scout.py slugs < urls.txt

    # one posting's full text, for archiving to jd-source/ after an audit
    python3 jd-scout/scout.py fetch greenhouse-figma-5512345
"""

import argparse
import difflib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, "jd-scout")
JOBS = os.path.join(ROOT, "docs", "data", "jobs.json")
SOURCE_DIR = os.path.join(ROOT, "jd-source")

TIMEOUT = 20

# Postings older than this, by the date the board says they were posted, are
# never added. A posting with no date is kept, since its age can't be checked.
MAX_AGE_DAYS = 30
USER_AGENT = "bco-signals-jd-scout/1.0 (+https://signals.bertino.co)"

# Board feed per ATS. "-eu" variants are boards hosted in the vendor's EU region.
# Greenhouse serves EU-hosted boards from its main API too.
FEEDS = {
    "greenhouse": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
    "greenhouse-eu": "https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true",
    "lever": "https://api.lever.co/v0/postings/{slug}?mode=json",
    "lever-eu": "https://api.eu.lever.co/v0/postings/{slug}?mode=json",
    "ashby": "https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true",
}

# Public board hosts, for turning a search result URL into (ats, slug).
HOSTS = {
    "boards.greenhouse.io": "greenhouse",
    "job-boards.greenhouse.io": "greenhouse",
    "boards.eu.greenhouse.io": "greenhouse-eu",
    "job-boards.eu.greenhouse.io": "greenhouse-eu",
    "jobs.lever.co": "lever",
    "jobs.eu.lever.co": "lever-eu",
    "jobs.ashbyhq.com": "ashby",
}
NOT_SLUGS = {"embed", "api", "v1", "search", ""}


# --- text ---------------------------------------------------------------

class _Text(HTMLParser):
    BLOCK = {"p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5",
             "h6", "tr", "section", "article", "header", "footer"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.parts.append("\n- ")
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)


def html_to_text(markup):
    """Plain text from posting HTML. Greenhouse double-escapes its content."""
    if not markup:
        return ""
    if "&lt;" in markup:
        markup = html.unescape(markup)
    p = _Text()
    p.feed(markup)
    text = "".join(p.parts).replace("\xa0", " ")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n- \n", "\n- ", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# --- feeds --------------------------------------------------------------

def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.load(resp)


def _ms_to_date(ms):
    if not ms:
        return None
    return datetime.fromtimestamp(ms / 1000, timezone.utc).date().isoformat()


def _iso_date(value):
    return value[:10] if value else None


def normalize(ats, slug, raw):
    """Feed payload -> list of postings in one shape."""
    out = []
    if ats.startswith("greenhouse"):
        for j in raw.get("jobs", []):
            out.append({
                "jobId": str(j["id"]),
                "title": j.get("title", ""),
                "company": j.get("company_name"),
                "url": j.get("absolute_url"),
                "location": (j.get("location") or {}).get("name"),
                "workplace": None,
                "comp": None,
                "postedDate": _iso_date(j.get("first_published")),
                "text": html_to_text(j.get("content", "")),
            })
    elif ats.startswith("lever"):
        for j in raw if isinstance(raw, list) else []:
            sections = [j.get("descriptionPlain") or html_to_text(j.get("description", ""))]
            for lst in j.get("lists", []):
                sections.append(lst.get("text", "") + "\n" + html_to_text(lst.get("content", "")))
            sections.append(j.get("additionalPlain") or html_to_text(j.get("additional", "")))
            cats = j.get("categories") or {}
            sal = j.get("salaryRange") or {}
            comp = None
            if sal.get("min") is not None:
                comp = "{} {:,}–{:,} {}".format(sal.get("currency", ""), sal["min"],
                                               sal.get("max") or sal["min"],
                                               sal.get("interval", "")).strip()
            out.append({
                "jobId": j["id"],
                "title": j.get("text", ""),
                "company": None,
                "url": j.get("hostedUrl"),
                "location": cats.get("location"),
                "workplace": j.get("workplaceType"),
                "comp": comp,
                "postedDate": _ms_to_date(j.get("createdAt")),
                "text": "\n\n".join(s.strip() for s in sections if s and s.strip()),
            })
    elif ats == "ashby":
        for j in raw.get("jobs", []):
            if j.get("isListed") is False:
                continue
            c = j.get("compensation") or {}
            out.append({
                "jobId": j["id"],
                "title": j.get("title", ""),
                "company": None,
                "url": j.get("jobUrl"),
                "location": j.get("location"),
                "workplace": j.get("workplaceType") or ("Remote" if j.get("isRemote") else None),
                "comp": c.get("scrapeableCompensationSalarySummary") or c.get("compensationTierSummary"),
                "postedDate": _iso_date(j.get("publishedAt")),
                "text": j.get("descriptionPlain") or html_to_text(j.get("descriptionHtml", "")),
            })
    return out


# --- matching -----------------------------------------------------------

def load_keywords(path=os.path.join(HERE, "keywords.json")):
    with open(path) as fh:
        kw = json.load(fh)
    compile_all = lambda key: [re.compile(p, re.I) for p in kw[key]]
    return {k: compile_all(k) for k in kw if not k.startswith("_")}


def _hits(patterns, text):
    return [p.pattern for p in patterns if p.search(text)]


def classify(title, text, kw):
    """Return (matchType, matchedTerms) or (None, []) when the posting is out."""
    if _hits(kw["title_exclude"], title):
        return None, []
    terms = _hits(kw["title_terms"], title)
    if terms:
        return "title", terms
    if not _hits(kw["body_only_title_require"], title):
        return None, []
    terms = _hits(kw["body_phrases"], text)
    if terms:
        return "body", terms
    return None, []


def snippet(text, patterns, width=220):
    """The first sentence-ish span around a matched term."""
    for p in patterns:
        m = re.search(p, text, re.I)
        if m:
            start = max(text.rfind("\n", 0, m.start()), text.rfind(". ", 0, m.start()) + 1, 0)
            span = text[start:start + width].strip(" .\n-")
            return re.sub(r"\s+", " ", span) + ("…" if len(text) - start > width else "")
    return re.sub(r"\s+", " ", text[:width]).strip()


# --- known postings -----------------------------------------------------

def _norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


COMPANY_SUFFIXES = r"\b(inc|llc|ltd|plc|gmbh|corp|corporation|co|company|technologies|financial|group)\b"


def company_key(name):
    """'NiCE (Cognigy)' and 'NICE' both become 'nice'; 'Gusto, Inc.' becomes 'gusto'."""
    name = re.sub(r"\(.*?\)", " ", (name or "").lower())
    return _norm(re.sub(COMPANY_SUFFIXES, " ", name))


def same_company(a, b):
    a, b = company_key(a), company_key(b)
    if not a or not b:
        return False
    return a == b or (min(len(a), len(b)) >= 3 and (a.startswith(b) or b.startswith(a)))


def archived():
    """Job ids from archived source URLs, plus one record per archived or listed posting.

    Reads jd-source/ (included and excluded) and jobs.json, so a posting that was
    already audited either way is never offered again.
    """
    ids, records = set(), []
    for name in os.listdir(SOURCE_DIR):
        if not name.endswith(".md"):
            continue
        with open(os.path.join(SOURCE_DIR, name)) as fh:
            head = fh.read(4000)
        fm = dict(re.findall(r"^(\w+):\s*\"?(.*?)\"?\s*$", head.split("\n---", 1)[0], re.M))
        ids.update(re.findall(r"[0-9a-f]{8}-[0-9a-f-]{27}|\d{6,}", fm.get("sourceUrl", "")))
        records.append({"id": name[:-3], "company": fm.get("company", ""), "title": fm.get("title", ""),
                        "excluded": bool(fm.get("excluded"))})
    with open(JOBS) as fh:
        for e in json.load(fh)["entries"]:
            records.append({"id": e["id"], "company": e.get("company", ""), "title": e.get("title", ""),
                            "excluded": False})
    return ids, records


SIMILAR_TITLE = 0.8


def match_archive(company, slug, title, records):
    """('same', record) for the same posting, ('similar', record) for a close title, else (None, None)."""
    best, best_ratio = None, 0.0
    for r in records:
        if not (same_company(r["company"], company) or same_company(r["company"], slug)):
            continue
        if _norm(r["title"]) == _norm(title):
            return "same", r
        ratio = difflib.SequenceMatcher(None, _norm(r["title"]), _norm(title)).ratio()
        if ratio > best_ratio:
            best, best_ratio = r, ratio
    if best_ratio >= SIMILAR_TITLE:
        return "similar", best
    return None, None


def doc_id(ats, slug, job_id):
    return re.sub(r"[^A-Za-z0-9_\-.~:@+]", "-", "{}-{}-{}".format(ats, slug, job_id))[:200]


# --- commands -----------------------------------------------------------

def load_companies(paths):
    out = []
    for path in paths or []:
        with open(path) as fh:
            data = json.load(fh)
        out.extend(data if isinstance(data, list) else data.get("companies", []))
    return out


def load_companies_list(boards):
    """First occurrence of each (ats, slug) wins; disabled boards are dropped after dedupe."""
    seen, out = set(), []
    for c in boards:
        key = (c["ats"], c["slug"].lower())
        if key in seen:
            continue
        seen.add(key)
        if not c.get("disabled"):
            out.append(c)
    return out


def read_dump(dump):
    """Board docs and candidate ids from an ArtifactData list saved with out_dir."""
    boards, known = [], set()
    if not dump:
        return boards, known
    for sub in ("companies", "candidates"):
        d = os.path.join(dump, sub)
        if not os.path.isdir(d):
            continue
        for name in os.listdir(d):
            if not name.endswith(".json"):
                continue
            if sub == "candidates":
                known.add(name[:-5])
            else:
                with open(os.path.join(d, name)) as fh:
                    boards.append(json.load(fh))
    return boards, known


def company_id(ats, slug):
    return re.sub(r"[^A-Za-z0-9_\-.~:@+]", "-", "{}-{}".format(ats, slug.lower()))[:200]


def cmd_poll(args):
    kw = load_keywords()
    db_boards, known = read_dump(args.db_dump)
    file_boards = load_companies(args.companies)
    db_keys = {company_id(c["ats"], c["slug"]) for c in db_boards}
    # Boards in the db win, so a board switched off on the page stays off.
    skip = skip_boards()
    companies = [c for c in load_companies_list(db_boards + file_boards)
                 if "{}/{}".format(c["ats"], c["slug"]).lower() not in skip]
    today = datetime.now(timezone.utc).date().isoformat()
    cutoff = (datetime.now(timezone.utc) - timedelta(days=args.max_age)).date().isoformat()
    board_dir = os.path.join(args.out, "companies-new")
    os.makedirs(board_dir, exist_ok=True)
    for c in file_boards:
        cid = company_id(c["ats"], c["slug"])
        if cid not in db_keys and "{}/{}".format(c["ats"], c["slug"]).lower() not in skip:
            doc = {"ats": c["ats"], "slug": c["slug"], "name": c.get("name") or c["slug"],
                   "source": c.get("source", "seed"), "addedAt": today}
            with open(os.path.join(board_dir, cid + ".json"), "w") as fh:
                json.dump(doc, fh, ensure_ascii=False, indent=2)
    arch_ids, arch_records = archived()
    seen_jobs = set()

    cand_dir = os.path.join(args.out, "candidates")
    os.makedirs(cand_dir, exist_ok=True)
    open_ids, new_ids, failed = [], [], []
    too_old = 0

    for c in companies:
        ats, slug = c["ats"], c["slug"]
        if ats not in FEEDS:
            failed.append({"ats": ats, "slug": slug, "error": "unknown ats"})
            continue
        try:
            raw = fetch_json(FEEDS[ats].format(slug=slug))
        except urllib.error.HTTPError as e:
            failed.append({"ats": ats, "slug": slug, "error": "HTTP {}".format(e.code)})
            continue
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            failed.append({"ats": ats, "slug": slug, "error": str(getattr(e, "reason", e))[:120]})
            continue

        for job in normalize(ats, slug, raw):
            match, terms = classify(job["title"], job["text"], kw)
            if not match:
                continue
            company = job["company"] or c.get("name") or slug
            if job["jobId"] in arch_ids:
                continue
            kind, rec = match_archive(company, slug, job["title"], arch_records)
            if kind == "same":
                continue
            # The same Greenhouse board can be listed under both its US and EU host.
            job_key = (ats.split("-")[0], slug.lower(), job["jobId"])
            if job_key in seen_jobs:
                continue
            seen_jobs.add(job_key)
            did = doc_id(ats, slug, job["jobId"])
            open_ids.append(did)
            if did in known:
                continue
            if job["postedDate"] and job["postedDate"] < cutoff:
                too_old += 1
                continue
            pats = terms if match == "body" else kw_patterns(kw["body_phrases"]) + terms
            doc = {
                "title": job["title"],
                "company": company,
                "ats": ats,
                "slug": slug,
                "jobId": job["jobId"],
                "url": job["url"],
                "location": job["location"],
                "workplace": job["workplace"],
                "comp": job["comp"],
                "postedDate": job["postedDate"],
                "matchType": match,
                "matchedTerms": terms,
                "snippet": snippet(job["text"], pats),
                "firstSeen": today,
                "status": "new",
                "similarTo": ({"id": rec["id"], "title": rec["title"], "excluded": rec["excluded"]}
                              if kind == "similar" else None),
            }
            with open(os.path.join(cand_dir, did + ".json"), "w") as fh:
                json.dump(doc, fh, ensure_ascii=False, indent=2)
            new_ids.append(did)

    summary = {
        "finishedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "companiesChecked": len(companies) - len(failed),
        "companiesFailed": failed,
        "maxAgeDays": args.max_age,
        "skippedTooOld": too_old,
        "newCount": len(new_ids),
        "newBoards": len(os.listdir(board_dir)),
        "newIds": new_ids,
        "openIds": open_ids,
    }
    with open(os.path.join(args.out, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
    print("checked {} companies, {} failed, {} matching open, {} new".format(
        summary["companiesChecked"], len(failed), len(open_ids), len(new_ids)))


def kw_patterns(patterns):
    return [p.pattern for p in patterns]


def parse_board_url(url):
    m = re.match(r"https?://([^/]+)/([^/?#]*)", url.strip())
    if not m or m.group(1).lower() not in HOSTS:
        return None
    slug = m.group(2)
    if slug.lower() in NOT_SLUGS:
        return None
    return {"ats": HOSTS[m.group(1).lower()], "slug": slug}


def skip_boards():
    with open(os.path.join(HERE, "discovery.json")) as fh:
        return {b.lower() for b in json.load(fh).get("skip_boards", {}).get("boards", [])}


def cmd_slugs(_args):
    skip = skip_boards()
    seen, out = set(), []
    for line in sys.stdin:
        hit = parse_board_url(line)
        if hit and "{}/{}".format(hit["ats"], hit["slug"]).lower() in skip:
            continue
        if hit and (hit["ats"], hit["slug"].lower()) not in seen:
            seen.add((hit["ats"], hit["slug"].lower()))
            hit["source"] = "discovered"
            out.append(hit)
    json.dump(out, sys.stdout, indent=2)
    print()


def cmd_fetch(args):
    ats = next((a for a in sorted(FEEDS, key=len, reverse=True)
                if args.id.startswith(a + "-")), None)
    if not ats:
        sys.exit("unrecognized candidate id: " + args.id)
    rest = args.id[len(ats) + 1:]
    # Ashby and Lever ids are UUIDs; Greenhouse ids are integers. Either way the
    # job id is the trailing part, and the slug is whatever precedes it.
    m = re.match(r"(.+)-([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|\d+)$", rest)
    if not m:
        sys.exit("unrecognized candidate id: " + args.id)
    slug, job_id = m.groups()
    for job in normalize(ats, slug, fetch_json(FEEDS[ats].format(slug=slug))):
        if job["jobId"] == job_id:
            # The header lines are the ATS's own structured fields, printed as
            # labeled lines so the archive keeps them alongside the posting text.
            print("# " + job["title"])
            print("URL: {}\nPosted: {}\nLocation: {}\nWorkplace: {}\nCompensation: {}\n".format(
                job["url"], job["postedDate"], job["location"], job["workplace"], job["comp"]))
            print(job["text"])
            return
    # Exit code 3 signals the posting has closed, as distinct from an error.
    print("posting {} is no longer on the {} board for {}".format(job_id, ats, slug), file=sys.stderr)
    sys.exit(3)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("poll")
    p.add_argument("--companies", nargs="+", default=[], help="board lists: seed-companies.json, discovered.json")
    p.add_argument("--max-age", type=int, default=MAX_AGE_DAYS,
                   help="skip postings posted more than this many days ago (default %(default)s)")
    p.add_argument("--db-dump", help="directory holding companies/ and candidates/ saved from the triage db")
    p.add_argument("--out", required=True)
    p.set_defaults(func=cmd_poll)
    sub.add_parser("slugs").set_defaults(func=cmd_slugs)
    p = sub.add_parser("fetch")
    p.add_argument("id")
    p.set_defaults(func=cmd_fetch)
    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
