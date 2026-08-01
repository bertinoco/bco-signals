#!/usr/bin/env python3
"""Regenerate the derived files in jd-insights/ from the dataset.

Writes stats.md and quotes.md. Both are generated in full every run — never
hand-edit them, since the next run overwrites whatever you wrote.

patterns.md and findings.md are hand-written and are never touched here.

Run from the repo root:

    python3 jd-insights/refresh.py
"""

import json
import os
import re
import statistics
from collections import Counter
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOBS = os.path.join(ROOT, "docs", "data", "jobs.json")
SOURCE_DIR = os.path.join(ROOT, "jd-source")
OUT_DIR = os.path.join(ROOT, "jd-insights")

BANNER = (
    "<!-- GENERATED FILE — do not edit by hand.\n"
    "     Regenerate with: python3 jd-insights/refresh.py -->\n"
)


def load():
    with open(JOBS) as fh:
        return json.load(fh)


def front_matter(path):
    """Return the YAML-ish front matter block of a jd-source file as text."""
    with open(path) as fh:
        text = fh.read()
    parts = text.split("---", 2)
    return parts[1] if len(parts) > 2 else ""


def source_field(eid, field):
    path = os.path.join(SOURCE_DIR, eid + ".md")
    if not os.path.exists(path):
        return None
    match = re.search(rf"^{field}:\s*(.+?)$", front_matter(path), re.M)
    if not match:
        return None
    value = match.group(1).strip()
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    value = value.replace('\\"', '"')
    return None if value in ("null", "") else value


def pct(count, total):
    return round(100 * count / total)


def write_stats(data):
    entries = data["entries"]
    n = len(entries)
    lines = [BANNER, "# Stats", ""]
    lines.append(
        f"Dataset state: **{n} entries**, `meta.lastUpdated` {data['meta']['lastUpdated']}. "
        f"Generated {date.today().isoformat()}."
    )
    lines.append("")
    lines.append(
        "Every figure here is counted from `docs/data/jobs.json`. If you quote one "
        "in something published, quote the entry count with it — these move."
    )
    lines.append("")

    companies = {e["company"] for e in entries}
    lines += [
        "## Headline",
        "",
        f"- **{n}** entries across **{len(companies)}** companies and "
        f"**{len({e['domain'] for e in entries})}** domains",
        f"- Date range: {min(e['dateAdded'] for e in entries)} to "
        f"{max(e['dateAdded'] for e in entries)}",
        "",
    ]

    for label, key, taxonomy in (("Responsibility clusters", "clusters", "clusters"),
                                 ("Skill signals", "signals", "signals")):
        counts = Counter(k for e in entries for k in e[key])
        lines += [f"## {label}", "", "| | Entries | Share |", "|---|---:|---:|"]
        for k, v in counts.most_common():
            lines.append(f"| {data[taxonomy][k]['label']} | {v} | {pct(v, n)}% |")
        lines.append("")

    comps = [e["compRange"] for e in entries if e.get("compRange")]
    lines += ["## Compensation", ""]
    if comps:
        by_ccy = Counter(c["currency"] for c in comps)
        usd = [c for c in comps if c["currency"] == "USD"]
        lines += [
            f"- Stated in **{len(comps)} of {n}** entries "
            f"({', '.join(f'{v} {k}' for k, v in by_ccy.most_common())})",
            f"- Full spread: **${min(c['min'] for c in comps):,}** to "
            f"**${max(c['max'] for c in comps):,}**",
        ]
        if usd:
            lines.append(
                f"- USD medians: **${int(statistics.median(c['min'] for c in usd)):,}** low, "
                f"**${int(statistics.median(c['max'] for c in usd)):,}** high"
            )
        covers = Counter(c.get("covers") for c in comps)
        lines.append(
            "- `covers`: "
            + ", ".join(f"{v} {k or 'unstated'}" for k, v in covers.most_common())
        )
    lines.append("")

    lines += ["## Domains", "", "| | Entries | Companies |", "|---|---:|---|"]
    for dom, v in Counter(e["domain"] for e in entries).most_common():
        names = sorted({e["company"] for e in entries if e["domain"] == dom})
        lines.append(f"| {dom} | {v} | {', '.join(names)} |")
    lines.append("")

    placed = [(e, source_field(e["id"], "orgPlacement")) for e in entries]
    stated = [(e, p) for e, p in placed if p]
    lines += [
        "## Stated org placement",
        "",
        f"Recorded in `jd-source` front matter. **{len(stated)} of {n}** postings say "
        "where the role sits; the rest do not, which is itself a fact about the posting.",
        "",
        "| Company | Placement as stated |",
        "|---|---|",
    ]
    for e, p in sorted(stated, key=lambda x: x[0]["company"]):
        lines.append(f"| {e['company']} | {p} |")
    lines.append("")

    dated = [(e, source_field(e["id"], "postedDate")) for e in entries]
    dated = [(e, d) for e, d in dated if d]
    lines += [
        "## Stated posting dates",
        "",
        f"**{len(dated)} of {n}** postings state a date. Where both exist, the gap to "
        "`dateAdded` varies enough that one is not a proxy for the other.",
        "",
        "| Company | Posted | Added |",
        "|---|---|---|",
    ]
    for e, d in sorted(dated, key=lambda x: x[1]):
        lines.append(f"| {e['company']} | {d} | {e['dateAdded']} |")
    lines.append("")

    with open(os.path.join(OUT_DIR, "stats.md"), "w") as fh:
        fh.write("\n".join(lines))
    return n


def write_quotes(data):
    entries = sorted(data["entries"], key=lambda e: e["company"].lower())
    quoted = [e for e in entries if e.get("quote")]
    lines = [BANNER, "# Quotes", ""]
    lines.append(
        f"Every stored quote, verbatim from the posting. **{len(quoted)} of "
        f"{len(entries)}** entries carry one."
    )
    lines.append("")
    lines.append(
        "These are the lines that anchor each entry's cluster and signal assignments, "
        "so they are the strongest citable evidence in the dataset. Each is checked "
        "against its `jd-source` archive before commit."
    )
    lines.append("")
    for e in quoted:
        lines += [
            f"### {e['company']} — {e['title']}",
            "",
            f"> {e['quote']}",
            "",
            f"`{e['id']}` · added {e['dateAdded']}",
            "",
        ]
    with open(os.path.join(OUT_DIR, "quotes.md"), "w") as fh:
        fh.write("\n".join(lines))
    return len(quoted)


if __name__ == "__main__":
    data = load()
    n = write_stats(data)
    q = write_quotes(data)
    print(f"stats.md   regenerated — {n} entries")
    print(f"quotes.md  regenerated — {q} quotes")
