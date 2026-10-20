#!/usr/bin/env python3
"""Add VC portfolio companies to the scout's board list.

Reads the boards in vc-boards.json, finds each portfolio company's job board,
and writes the ones on Greenhouse, Lever or Ashby that aren't on the list yet
as companies/ documents for the triage page's database. Companies the scout
can't check are listed in not-covered.md.

    python3 jd-scout/vc_import.py --db-dump DUMP_DIR --out OUT_DIR [--board NAME ...]

DUMP_DIR is the triage database's companies collection saved with ArtifactData
list (out_dir), as in ROUTINE.md step 1. Write OUT_DIR/companies-new/*.json to
the companies collection with ArtifactData batch, as in ROUTINE.md step 4.

Platforms:
- getro: Getro's public job search, the same call the board page makes.
- consider: the board page's own session (cookie and CSRF token), as a browser
  does. Greenhouse jobs embedded on a company's site are matched to a board by
  checking that the job id exists on it.
- index-portfolio: Index Ventures' public portfolio page. Its job board needs
  credentials embedded in the page script, which this deliberately doesn't use.
  Each company's website domain is probed for a board; Greenhouse matches must
  carry the company's name, and Ashby or Lever matches must mention it in their
  job text, or they're listed as unconfirmed instead of added.
"""

import argparse
import http.cookiejar
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scout  # noqa: E402

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
PAUSE = 0.3  # between paged requests to the same board

_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))


def request(url, data=None, headers=None, as_json=False):
    h = {"User-Agent": UA, "Accept": "application/json, text/html"}
    h.update(headers or {})
    r = urllib.request.Request(url, data=data, headers=h, method="POST" if data else "GET")
    with _opener.open(r, timeout=30) as resp:
        body = resp.read().decode("utf-8", "replace")
    return json.loads(body) if as_json else body


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def record(companies, key, name, url):
    """Note which board a company's job link points to."""
    c = companies.setdefault(key, {"name": name, "boards": set(), "otherHosts": {}, "ghJobIds": []})
    hit = scout.parse_board_url(url or "")
    if hit:
        c["boards"].add((hit["ats"], hit["slug"]))
        return c
    q = parse_qs(urlparse(url or "").query)
    if "gh_jid" in q:
        c["ghJobIds"].append(q["gh_jid"][0])
    host = urlparse(url or "").netloc.lower()
    if host:
        c["otherHosts"][host] = c["otherHosts"].get(host, 0) + 1
    return c


# --- platforms ----------------------------------------------------------

def read_getro(board):
    html = request(board["url"])
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    net = json.loads(m.group(1))["props"]["pageProps"].get("network") if m else None
    if not net:
        raise RuntimeError("not a Getro board")
    origin = "{0.scheme}://{0.netloc}".format(urlparse(board["url"]))
    companies, page = {}, 0
    while True:
        body = json.dumps({"hitsPerPage": 20, "page": page, "filters": "", "query": ""}).encode()
        d = request("https://api.getro.com/api/v2/collections/{}/search/jobs".format(net["id"]), body,
                    {"Content-Type": "application/json", "Origin": origin, "Referer": board["url"]}, True)
        jobs, total = d["results"]["jobs"], d["results"]["count"]
        for j in jobs:
            org = j.get("organization") or {}
            record(companies, org.get("slug") or org.get("name"), org.get("name"), j.get("url"))
        page += 1
        if not jobs or page * 20 >= total:
            return companies
        time.sleep(PAUSE)


def _greenhouse_ids(slug, cache):
    if slug not in cache:
        try:
            raw = scout.fetch_json(scout.FEEDS["greenhouse"].format(slug=slug))
            cache[slug] = {str(j["id"]) for j in raw.get("jobs", [])}
        except (urllib.error.URLError, ValueError, TimeoutError):
            cache[slug] = None
    return cache[slug]


def read_consider(board):
    html = request(board["url"])
    token = re.search(r'"csrfToken":"([^"]+)"', html).group(1)
    board_id = re.search(r'"board":\{"id":"([^"]+)"', html).group(1)
    origin = "{0.scheme}://{0.netloc}".format(urlparse(board["url"]))
    companies, seq, pages, info = {}, None, 0, {}
    while True:
        meta = {"size": 100}
        if seq:
            meta["sequence"] = seq
        body = json.dumps({"meta": meta, "board": {"id": board_id, "isParent": True}, "query": {}}).encode()
        d = request(origin + "/api-boards/search-jobs", body, {
            "Content-Type": "application/json", "x-csrf-token": token, "Origin": origin,
            "Referer": board["url"]}, True)
        jobs = d.get("jobs") or []
        for j in jobs:
            key = j.get("companySlug") or j.get("companyName")
            record(companies, key, j.get("companyName"), j.get("applyUrl") or j.get("url"))
            info[key] = (j.get("companySlug"), j.get("companyDomain"), j.get("companyName"))
        pages += 1
        seq = (d.get("meta") or {}).get("sequence")
        if not jobs or not seq or pages > 200:
            break
        time.sleep(PAUSE)
    # Greenhouse jobs embedded on a company's own site: guess the board, confirm by job id.
    cache = {}
    for key, c in companies.items():
        if c["boards"] or not c["ghJobIds"]:
            continue
        for base in info.get(key, ()):
            base = (base or "").lower()
            base = base.split(".")[0] if "." in base else base
            guess = norm(base)
            ids = _greenhouse_ids(guess, cache) if len(guess) >= 3 else None
            if ids and c["ghJobIds"][0] in ids:
                c["boards"].add(("greenhouse", guess))
                break
    return companies


def _probe(slug, name):
    """(ats, confirmed) for a board under slug, or (None, False)."""
    try:
        b = request("https://boards-api.greenhouse.io/v1/boards/{}".format(slug), as_json=True)
        bn, n = norm(b.get("name")), norm(name)
        if bn and (bn.startswith(n[:5]) or n.startswith(bn[:5])):
            return "greenhouse", True
    except (urllib.error.URLError, ValueError, TimeoutError):
        pass
    for ats in ("ashby", "lever"):
        try:
            jobs = scout.normalize(ats, slug, scout.fetch_json(scout.FEEDS[ats].format(slug=slug)))
        except (urllib.error.URLError, ValueError, TimeoutError):
            continue
        if jobs:
            text = norm(" ".join(j["text"][:3000] for j in jobs[:5]))
            return ats, norm(name.split("(")[0])[:8] in text
    return None, False


def read_index_portfolio(board):
    html = request(board["url"])
    items = re.findall(r'"url": "https://www\.indexventures\.com/companies/([^"/]+)/", "name": "([^"]+)"', html)
    companies, seen = {}, set()
    for slug, name in items:
        if slug in seen:
            continue
        seen.add(slug)
        c = companies.setdefault(slug, {"name": name, "boards": set(), "otherHosts": {}, "ghJobIds": []})
        try:
            page = request("https://www.indexventures.com/companies/{}/".format(slug))
        except urllib.error.URLError:
            c["note"] = "portfolio page unavailable"
            continue
        sites = [u for u in re.findall(r'href="(https?://[^"]+)"', page)
                 if not re.search(r"indexventures|linkedin\.com|notoptional|twitter\.com|x\.com/", u)]
        domain = urlparse(sites[0]).netloc.lower().replace("www.", "") if sites else ""
        c["domain"] = domain
        guesses = []
        for g in (norm(domain.split(".")[0]), norm(slug), slug.lower()):
            if len(g) >= 3 and g not in guesses:
                guesses.append(g)
        for g in guesses:
            ats, confirmed = _probe(g, name)
            if ats and confirmed:
                c["boards"].add((ats, g))
                break
            if ats:
                c["note"] = "possible {} board `{}`, not confirmed by name".format(ats.capitalize(), g)
                break
            time.sleep(0.1)
        if not c["boards"] and "note" not in c:
            c["note"] = "no Greenhouse, Lever or Ashby board found"
    return companies


READERS = {"getro": read_getro, "consider": read_consider, "index-portfolio": read_index_portfolio}


# --- output -------------------------------------------------------------

def known_boards(db_dump):
    keys = {scout.company_id(c["ats"], c["slug"]) for c in scout.load_companies(
        [os.path.join(scout.HERE, "seed-companies.json")])}
    db_boards, _ = scout.read_dump(db_dump)
    keys |= {scout.company_id(c["ats"], c["slug"]) for c in db_boards}
    return keys


def feed_works(ats, slug):
    try:
        scout.normalize(ats, slug, scout.fetch_json(scout.FEEDS[ats].format(slug=slug)))
        return True
    except urllib.error.HTTPError:
        return False
    except (urllib.error.URLError, ValueError, TimeoutError):
        return True  # a dropped connection isn't a missing board; the weekly poll will report it


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--db-dump", help="companies/ saved from the triage database")
    ap.add_argument("--out", required=True)
    ap.add_argument("--board", nargs="*", help="only these board names from vc-boards.json")
    args = ap.parse_args()

    with open(os.path.join(scout.HERE, "vc-boards.json")) as fh:
        boards = json.load(fh)["boards"]
    if args.board:
        boards = [b for b in boards if b["name"] in args.board]
    known, skip = known_boards(args.db_dump), scout.skip_boards()
    today = datetime.now(timezone.utc).date().isoformat()
    new_dir = os.path.join(args.out, "companies-new")
    os.makedirs(new_dir, exist_ok=True)

    report = ["# VC portfolio companies the scout can't check", "",
              "These post jobs somewhere other than Greenhouse, Lever or Ashby, or no board was found "
              "for them, so the weekly scout doesn't see them.", ""]
    written = {}
    for board in boards:
        try:
            companies = READERS[board["platform"]](board)
        except Exception as e:  # one board failing shouldn't stop the rest
            print("FAIL {}: {}".format(board["name"], e), file=sys.stderr)
            report += ["## {}".format(board["name"]), "", "Couldn't read this board: {}".format(e), ""]
            continue
        added, uncovered = 0, []
        for c in companies.values():
            for ats, slug in sorted(c["boards"]):
                cid = scout.company_id(ats, slug)
                if cid in known or "{}/{}".format(ats, slug).lower() in skip:
                    continue
                if cid in written:
                    written[cid]["vcs"].append(board["name"])
                    continue
                if not feed_works(ats, slug):
                    continue
                written[cid] = {"ats": ats, "slug": slug, "name": c["name"] or slug, "source": "vc-board",
                                "vcs": [board["name"]], "addedAt": today}
                added += 1
            if not c["boards"]:
                hosts = sorted(c["otherHosts"], key=lambda h: -c["otherHosts"][h])[:2]
                uncovered.append((c["name"] or "?", ", ".join(hosts) or c.get("domain") or "—",
                                  c.get("note", "")))
        print("{}: {} companies, {} new boards, {} not covered".format(
            board["name"], len(companies), added, len(uncovered)), file=sys.stderr)
        report += ["## {} ({})".format(board["name"], len(uncovered)), "",
                   "| Company | Jobs link to / website | Note |", "|---|---|---|"]
        report += ["| {} | {} | {} |".format(*u) for u in sorted(uncovered, key=lambda u: u[0].lower())]
        report.append("")

    for cid, doc in written.items():
        with open(os.path.join(new_dir, cid + ".json"), "w") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(args.out, "not-covered.md"), "w") as fh:
        fh.write("\n".join(report) + "\n")
    print("wrote {} new boards to {}".format(len(written), new_dir))


if __name__ == "__main__":
    main()
