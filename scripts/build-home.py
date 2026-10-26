#!/usr/bin/env python3
"""Write the home page's dataset sections into docs/index.html from
docs/data/jobs.json, so they're in the page without JavaScript.

scripts.js still renders these sections on load: it wires up the cards and
role rows and keeps "New" chips current. But crawlers and LLM fetchers that
don't run JavaScript (GPTBot, ClaudeBot, PerplexityBot) would otherwise see
"Loading…" where the dataset should be, and readers would see that flash
before the data arrived. This writes the same markup scripts.js produces, so
the hand-off is invisible.

What it writes, all in docs/index.html:

    <!-- signals:start/end -->   the Signals card grid and its "View all"
    <!-- clusters:start/end -->  the Clusters card grid and its "View all"
    <!-- roles:start/end -->     the roles list and its "View all"
    #hero-role-count             the role count in the hero line
    #footer-date                 the footer's "Last updated" date
    Dataset "dateModified"       in the JSON-LD

Everything else in index.html stays hand-written. The findings list is
build-findings.py's job.

Run from the repo root after any change to jobs.json:

    python3 scripts/build-home.py          # write index.html
    python3 scripts/build-home.py --check  # exit 1 if it's stale
"""

import html
import json
import math
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
INDEX_HTML = os.path.join(DOCS, "index.html")
JOBS_JSON = os.path.join(DOCS, "data", "jobs.json")
SCRIPTS_JS = os.path.join(DOCS, "js", "scripts.js")

# Mirrors CURRENCY_SYMBOLS in scripts.js. A currency missing from both still
# renders: no symbol, just the number and code.
CURRENCY_SYMBOLS = {"USD": "$", "GBP": "£", "CAD": "$", "EUR": "€"}

# Mirrors COPY.empty in scripts.js. Only reachable with an empty dataset.
EMPTY = {
    "clusters": ("No responsibilities yet",
                 "Responsibilities appear here once the first job description is audited successfully."),
    "signals": ("No skills yet", "Skills appear here once {threshold} or more postings ask for them."),
    "titles": ("No roles yet", "Roles appear here as job descriptions are added to the dataset."),
}

CLOSE_SVG = (
    '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">\n'
    '  <path d="M1 1L13 13M13 1L1 13" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>\n'
    '</svg>'
)


class BuildError(Exception):
    pass


def e(text):
    return html.escape(str(text), quote=False)


def ea(text):
    return html.escape(str(text), quote=True)


def js_constant(source, name):
    """A numeric constant out of scripts.js, so the limits and thresholds
    here can't drift from the ones the page uses live."""
    match = re.search(rf"^const {name} = (\d+);", source, re.M)
    if not match:
        raise BuildError(f"docs/js/scripts.js: no `const {name} = <number>;` found")
    return int(match.group(1))


def js_round(x):
    """Math.round, not Python's round(), which rounds halves to even."""
    return math.floor(x + 0.5)


def indent(block, spaces):
    pad = " " * spaces
    return "\n".join(pad + line if line else line for line in block.splitlines())


def state(kind, title, body):
    return (f'<div class="state state--{kind}">\n'
            f'  <p class="state-title">{e(title)}</p>\n'
            f'  <p class="state-body">{e(body)}</p>\n'
            f'</div>')


def show_more(id_, visible):
    # scripts.js sets style.display and the label the same way.
    if visible:
        return (f'<div id="{id_}" style="display:block;">\n'
                f'  <button class="show-more-btn">View all</button>\n'
                f'</div>')
    return (f'<div id="{id_}" style="display:none;">\n'
            f'  <button class="show-more-btn"></button>\n'
            f'</div>')


class Dataset:
    def __init__(self, data, consts):
        self.data = data
        self.entries = data["entries"]
        self.total = len(self.entries)
        self.c = consts
        # "New" chips are measured against the data's own last update, not
        # today, so the output -- and --check -- doesn't change by itself
        # when a chip ages out. scripts.js recomputes against today live.
        self.as_of = date.fromisoformat(data["meta"]["lastUpdated"])

    def entries_for(self, key, field):
        return [x for x in self.entries if key in (x.get(field) or [])]

    def pct(self, key, field):
        n = len(self.entries_for(key, field))
        return js_round(n / self.total * 100) if self.total else 0

    def is_new(self, key, field):
        # Mirrors keyIntroducedDate in scripts.js: an explicit `introduced`
        # date on the key wins over its earliest holder's dateAdded.
        explicit = self.data[field][key].get("introduced")
        if explicit:
            introduced = date.fromisoformat(explicit)
        else:
            dates = [date.fromisoformat(x["dateAdded"]) for x in self.entries_for(key, field)]
            if not dates:
                return False
            introduced = min(dates)
        return (self.as_of - introduced).days < self.c["NEW_KEY_WINDOW_DAYS"]

    def signal_counts(self):
        counts = {k: 0 for k in self.data["signals"]}
        for x in self.entries:
            for s in x.get("signals") or []:
                if s in counts:
                    counts[s] += 1
        return counts

    def displayed_signals(self):
        return {k for k, n in self.signal_counts().items() if n >= self.c["SIGNAL_THRESHOLD"]}

    # ── Cards ──────────────────────────────────────────────

    def card(self, key, field, label_html_tag):
        item = self.data[field][key]
        pct = self.pct(key, field)
        new = self.is_new(key, field)
        entries = self.entries_for(key, field)
        roles = (f'<div class="flip-card-roles">\n'
                 f'  <p class="flip-card-roles-label">Appears in {len(entries)} of {self.total} roles</p>\n'
                 f'</div>\n') if entries else ""
        kind = "cluster-card" if field == "clusters" else "signal-card"
        front_label = (f'<h3>{e(item["label"])}</h3>' if label_html_tag == "h3"
                       else f'<div class="signal-label">{e(item["label"])}</div>')
        return (
            f'<div class="flip-card {kind}" data-key="{ea(key)}" role="button" tabindex="0" '
            f'aria-label="Expand {ea(item["label"])}, {pct}% of roles{", newly added" if new else ""}">\n'
            f'  <div class="flip-card-front{" has-new-chip" if new else ""}">\n'
            f'    {front_label}\n'
            + ('    <span class="new-chip">New</span>\n' if new else '')
            + f'    <div class="flip-card-stat">{pct}%</div>\n'
            f'  </div>\n'
            f'  <div class="flip-card-back">\n'
            f'    <button type="button" class="flip-card-close" aria-label="Close">\n'
            f'{indent(CLOSE_SVG, 6)}\n'
            f'    </button>\n'
            f'    <div class="flip-card-back-content">\n'
            f'      <h3 class="flip-card-back-title">{e(item["label"])}</h3>\n'
            f'{indent(roles, 6)}' + ('\n' if roles else '')
            + f'      <p class="flip-card-back-desc">{e(item["description"])}</p>\n'
            f'    </div>\n'
            f'  </div>\n'
            f'</div>'
        )

    def signals_block(self):
        limit = self.c["SECTION_LIMIT"]
        counts = self.signal_counts()
        # Most-attested first; sorted() is stable, like Array.prototype.sort,
        # so ties keep jobs.json's own order in both.
        keys = [k for k, n in sorted(counts.items(), key=lambda kv: -kv[1])
                if n >= self.c["SIGNAL_THRESHOLD"]]
        if not keys:
            title, body = EMPTY["signals"]
            inner = state("empty", title, body.format(threshold=self.c["SIGNAL_THRESHOLD"]))
            return self.panel("signal-list", "signal-list", inner, "signals-show-more", False)
        cards = "\n".join(self.card(k, "signals", "div") for k in keys[:limit])
        return self.panel("signal-list", "signal-list", cards, "signals-show-more", len(keys) > limit)

    def clusters_block(self):
        limit = self.c["SECTION_LIMIT"]
        keys = list(self.data["clusters"])
        if not keys:
            inner = state("empty", *EMPTY["clusters"])
            return self.panel("cluster-grid", "cluster-grid", inner, "clusters-show-more", False)
        # renderClusters sorts by how many times each key appears across
        # entries; that's what this counts.
        tally = {k: sum((x.get("clusters") or []).count(k) for x in self.entries) for k in keys}
        keys.sort(key=lambda k: -tally[k])
        cards = "\n".join(self.card(k, "clusters", "h3") for k in keys[:limit])
        return self.panel("cluster-grid", "cluster-grid", cards, "clusters-show-more", len(keys) > limit)

    # ── Roles ──────────────────────────────────────────────

    def role(self, x, displayed):
        def fmt(n, currency):
            return CURRENCY_SYMBOLS.get(currency, "") + f"{n:,}"

        c = x.get("compRange")
        comp = ""
        if c:
            qualifiers = ["total comp"] if c.get("covers") == "total" else []
            comp = (f'<span class="title-comp">{fmt(c["min"], c["currency"])}–{fmt(c["max"], c["currency"])} '
                    f'{e(c["currency"])}' + "".join(f" · {q}" for q in qualifiers) + "</span>")

        shown = [s for s in (x.get("signals") or []) if s in displayed]
        signals = ('<ul class="title-signals">'
                   + "".join(f'<li class="signal-chip">{e(self.data["signals"][s]["label"])}</li>' for s in shown)
                   + "</ul>") if shown else ""

        has_quote = bool(x.get("quote"))
        has_detail = has_quote or bool(shown)
        lang = x.get("quoteTranslatedFrom") or x.get("titleTranslatedFrom")
        translation = (f'<p class="quote-translation-note">Translated from {e(lang)}</p>'
                       if has_detail and lang else "")
        detail = ('<div class="title-detail"><div class="title-detail-inner">'
                  + (f"<blockquote>{e(x['quote'])}</blockquote>" if has_quote else "")
                  + translation + signals + "</div></div>") if has_detail else ""
        expand = ('<button class="title-expand" aria-expanded="false" aria-label="Show details">+</button>'
                  if has_detail else "")

        sep = '<span class="title-sep">·</span>'
        attrib = (f'<div class="title-attrib"><span class="title-company">{e(x["company"])}</span>'
                  + (f"{sep}{comp}" if comp else "") + "</div>")
        when = f'<div class="title-date">{e(x["dateAdded"])}</div>' if x.get("dateAdded") else ""
        # formatTitle: spaced dash, en/em dash, or pipe join a role to its scope.
        title = re.sub(r"\s+[-—–|]\s+", ", ", x["title"])

        lines = [
            f'<div class="title-entry{" is-expandable" if has_detail else ""}">',
            '  <div class="title-header">',
            f'    <div class="title-name">{e(title)}</div>',
        ]
        if expand:
            lines.append(f"    {expand}")
        lines += ["  </div>", f"  {attrib}"]
        if when:
            lines.append(f"  {when}")
        if detail:
            lines.append(f"  {detail}")
        lines.append("</div>")
        return "\n".join(lines)

    def roles_block(self):
        limit = self.c["SECTION_LIMIT"]
        if not self.entries:
            inner = state("empty", *EMPTY["titles"])
            return self.panel("title-list", "title-list", inner, "titles-show-more", False)
        # Newest first; reverse=True keeps equal dates in jobs.json order,
        # as the comparator sort in renderTitles does.
        ordered = sorted(self.entries, key=lambda x: x["dateAdded"], reverse=True)
        displayed = self.displayed_signals()
        rows = "\n".join(self.role(x, displayed) for x in ordered[:limit])
        return self.panel("title-list", "title-list", rows, "titles-show-more", len(ordered) > limit)

    @staticmethod
    def panel(cls, id_, inner, more_id, more_visible):
        return (f'<div class="{cls}" id="{id_}">\n{indent(inner, 2)}\n</div>\n'
                f'{show_more(more_id, more_visible)}\n')


def replace_marked(text, name, block, pad):
    pattern = re.compile(rf"(<!-- {name}:start[^>]*-->\n)(.*?)(^ *<!-- {name}:end -->)", re.S | re.M)
    match = pattern.search(text)
    if not match:
        raise BuildError(f"docs/index.html: {name}:start / {name}:end markers not found")
    return text[:match.start(2)] + indent(block, pad) + "\n" + text[match.end(2):]


def replace_one(text, pattern, repl, label, flags=0):
    new, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise BuildError(f"docs/index.html: {label} not found")
    return new


def build(index_text, data, scripts_js):
    consts = {name: js_constant(scripts_js, name)
              for name in ("SECTION_LIMIT", "SIGNAL_THRESHOLD", "NEW_KEY_WINDOW_DAYS")}
    ds = Dataset(data, consts)
    out = index_text
    out = replace_marked(out, "signals", ds.signals_block(), 10)
    out = replace_marked(out, "clusters", ds.clusters_block(), 10)
    out = replace_marked(out, "roles", ds.roles_block(), 8)

    # Same values renderMeta sets live: entries.length (not meta.totalEntries,
    # which is hand-maintained) and meta.lastUpdated.
    updated = data["meta"]["lastUpdated"]
    out = replace_one(out, r'(<span id="hero-role-count">)\d+(</span>)',
                      rf"\g<1>{len(data['entries'])}\g<2>", "#hero-role-count")
    out = replace_one(out, r'(<span id="footer-date"><time datetime=")[^"]*(">)[^<]*(</time>)',
                      rf"\g<1>{updated}\g<2>{updated}\g<3>", "#footer-date")
    out = replace_one(out, r'("@type": "Dataset",.*?"dateModified": ")[^"]*(")',
                      rf"\g<1>{updated}\g<2>", 'Dataset "dateModified"', flags=re.S)
    return out


def main():
    check = "--check" in sys.argv[1:]
    with open(INDEX_HTML, encoding="utf-8") as fh:
        current = fh.read()
    with open(JOBS_JSON, encoding="utf-8") as fh:
        data = json.load(fh)
    with open(SCRIPTS_JS, encoding="utf-8") as fh:
        scripts_js = fh.read()

    built = build(current, data, scripts_js)

    if check:
        if built != current:
            print("out of date: docs/index.html")
            print("Run: python3 scripts/build-home.py")
            sys.exit(1)
        print("OK: docs/index.html home sections up to date")
        return
    if built == current:
        print("docs/index.html home sections already up to date")
        return
    with open(INDEX_HTML, "w", encoding="utf-8") as fh:
        fh.write(built)
    print("wrote docs/index.html")


if __name__ == "__main__":
    try:
        main()
    except BuildError as err:
        print(f"error: {err}", file=sys.stderr)
        sys.exit(1)
