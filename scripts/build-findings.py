#!/usr/bin/env python3
"""Build the Findings posts from findings/*.md.

Each post is a Markdown file with a short front-matter header. This script
turns every published post into a static page and keeps the files that list
the posts in step with them:

    docs/findings/<slug>/index.html   one page per post
    docs/index.html                   the Read our findings list, between the
                                      findings:start/end markers only
    docs/findings/index.html          a redirect to /#findings (the list used
                                      to live here)
    docs/data/findings.json           the post list as JSON (no longer read
                                      by the site itself)
    docs/sitemap.xml                  the post URLs (the root entry is untouched)
    docs/llms.txt                     the "Findings" section

See findings/README.md for the post format and CLAUDE.md's Findings tab
promotion process for what a post may say.

Run from the repo root:

    python3 scripts/build-findings.py          # write everything
    python3 scripts/build-findings.py --check  # exit 1 if anything is stale
"""

import html
import json
import os
import re
import shutil
import sys
import textwrap
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(ROOT, "findings")
JD_SOURCE_DIR = os.path.join(ROOT, "jd-source")
DOCS = os.path.join(ROOT, "docs")
OUT_DIR = os.path.join(DOCS, "findings")
INDEX_HTML = os.path.join(DOCS, "index.html")
FINDINGS_JSON = os.path.join(DOCS, "data", "findings.json")
SITEMAP = os.path.join(DOCS, "sitemap.xml")
LLMS = os.path.join(DOCS, "llms.txt")

SITE = "https://signals.bertino.co"
OG_IMAGE = SITE + "/images/og-image.png"
JOBS_JSON = os.path.join(DOCS, "data", "jobs.json")
REQUIRED_FIELDS = ("title", "date", "signals")
OPTIONAL_FIELDS = ("updated", "draft")

# Posts shown in the home page's Read our findings section before "Read
# more". The rest are still rendered, just hidden, so crawlers see them all.
# Matches SECTION_LIMIT in docs/js/scripts.js, so every section stops at 6.
FINDINGS_LIMIT = 6
FINDINGS_MARKERS = re.compile(
    r"(<!-- findings:start[^>]*-->\n)(.*?)(^ *<!-- findings:end -->)", re.S | re.M
)


class BuildError(Exception):
    pass


# ── Parsing ─────────────────────────────────────────────────

def parse_post(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    name = os.path.relpath(path, ROOT)

    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not match:
        raise BuildError(f"{name}: missing front matter (--- ... ---)")
    header, body = match.groups()

    meta = {}
    for line in header.splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        key = key.strip()
        if not sep or key not in REQUIRED_FIELDS + OPTIONAL_FIELDS:
            raise BuildError(f"{name}: unknown front-matter line: {line!r}")
        meta[key] = value.strip()

    missing = [f for f in REQUIRED_FIELDS if not meta.get(f)]
    if missing:
        raise BuildError(f"{name}: missing front-matter field(s): {', '.join(missing)}")
    for field in ("date", "updated"):
        if field in meta:
            try:
                date.fromisoformat(meta[field])
            except ValueError:
                raise BuildError(f"{name}: {field} must be YYYY-MM-DD, got {meta[field]!r}")

    # The <aside> is the "My take" section. Exactly one, and last, so the
    # data a post reports and the opinion it offers never interleave.
    opens = re.findall(r"^<aside>\s*$", body, re.M)
    closes = re.findall(r"^</aside>\s*$", body, re.M)
    if len(opens) != 1 or len(closes) != 1:
        raise BuildError(f"{name}: needs exactly one <aside> ... </aside> block for My take")
    data_md, _, rest = re.split(r"^(<aside>)\s*$", body, maxsplit=1, flags=re.M)
    take_md, _, after = re.split(r"^(</aside>)\s*$", rest, maxsplit=1, flags=re.M)
    if after.strip():
        raise BuildError(f"{name}: nothing may follow </aside>")
    if not data_md.strip() or not take_md.strip():
        raise BuildError(f"{name}: both the data section and the <aside> need content")

    slug = os.path.splitext(os.path.basename(path))[0]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        raise BuildError(f"{name}: filename must be a lowercase-hyphenated slug")

    return {
        "slug": slug,
        "source": name,
        "title": smart_quotes(meta["title"]),
        "date": meta["date"],
        "updated": meta.get("updated", meta["date"]),
        "summary": derive_summary(data_md, name),
        "signals": [s.strip() for s in meta["signals"].split(",") if s.strip()],
        "draft": meta.get("draft", "false").lower() == "true",
        "data_md": data_md,
        "take_md": take_md,
    }


# ── Markdown subset ─────────────────────────────────────────
# Deliberately small: headings (## and ###), paragraphs, "- " lists,
# "> " blockquotes, **bold**, *italic*, [links](url), @video <url>. Anything
# else is an error rather than a guess, so a post can't drift into syntax
# that renders differently from how it reads in the source.

UNSUPPORTED_BLOCK = re.compile(r"^(#(?!#)|#{4,}|\* |\+ |\d+[.)] |\||!\[|```|<|@(?!video ))")

# youtube.com/watch, youtu.be, youtube.com/embed, and vimeo.com are the only
# recognized @video providers -- the id capture group feeds straight into a
# known embed-URL shape, so a URL that doesn't match one of these can't
# produce a bad iframe src by accident; it just fails the build instead.
VIDEO_PATTERNS = [
    (re.compile(r"^https://(?:www\.)?youtube\.com/watch\?v=([\w-]{11})(?:&\S*)?$"), "youtube"),
    (re.compile(r"^https://youtu\.be/([\w-]{11})(?:\?\S*)?$"), "youtube"),
    (re.compile(r"^https://(?:www\.)?youtube\.com/embed/([\w-]{11})(?:\?\S*)?$"), "youtube"),
    (re.compile(r"^https://(?:www\.)?vimeo\.com/(\d+)$"), "vimeo"),
]


def render_video_embed(url, title, where):
    for pattern, provider in VIDEO_PATTERNS:
        match = pattern.match(url)
        if match:
            vid = match.group(1)
            src = (f"https://www.youtube-nocookie.com/embed/{vid}" if provider == "youtube"
                   else f"https://player.vimeo.com/video/{vid}")
            iframe_title = html.escape(title or "Embedded video", quote=True)
            return (f'<div class="post-video"><iframe src="{src}" title="{iframe_title}" '
                    f'loading="lazy" allow="accelerometer; autoplay; clipboard-write; '
                    f'encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')
    raise BuildError(
        f"{where}: unsupported @video URL (only youtube.com, youtu.be, and vimeo.com "
        f"links are recognized): {url!r}"
    )


def smart_quotes(text):
    """Straight quotes to curly. A quote opens at the start of the text or
    after whitespace or an opening bracket/dash; anything else closes it, so
    apostrophes become ’."""
    text = re.sub(r'(^|[\s(\[—])"', "\\1“", text)
    text = text.replace('"', "”")
    text = re.sub(r"(^|[\s(\[—])'", "\\1‘", text)
    return text.replace("'", "’")


def derive_summary(data_md, where):
    """The one-line summary shown on the Findings tab, the findings index,
    and in meta/OG/JSON-LD description tags -- the post's own opening
    sentences, not a separately hand-written field. Finds the first true
    paragraph (skipping any leading heading), takes its first two sentences,
    then a hard length backstop in case that's still too long."""
    lines = data_md.splitlines()
    i = 0
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith(("## ", "### ", "- ", ">", "@video "))):
        i += 1
    para = []
    while i < len(lines) and lines[i].strip() and not lines[i].startswith(("## ", "### ", "- ", ">", "@video ")):
        para.append(lines[i].strip())
        i += 1
    if not para:
        raise BuildError(f"{where}: no opening paragraph found to derive a summary from "
                          "(the data section can't open with a heading, list, or blockquote)")

    plain = " ".join(para)
    plain = re.sub(r"\*\*(.+?)\*\*", r"\1", plain)
    plain = re.sub(r"(?<!\w)\*(?=\S)(.+?)(?<=\S)\*(?!\w)", r"\1", plain)
    plain = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", plain)
    plain = smart_quotes(plain)

    sentences = re.split(r"(?<=[.!?])\s+", plain)
    summary = " ".join(sentences[:2]).strip()
    if len(summary) > 200:
        summary = summary[:197].rsplit(" ", 1)[0].rstrip(",;:—") + "…"
    return summary


def render_inline_segment(text, where):
    out = html.escape(smart_quotes(text), quote=False)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    out = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\w)\*(?=\S)(.+?)(?<=\S)\*(?!\w)", r"<em>\1</em>", out)
    if "*" in out or "](" in out:
        raise BuildError(f"{where}: unsupported inline syntax in {text!r}")
    return out


def render_inline(text, where, corpus=None):
    """As render_inline_segment, but every "quoted span" that matches exactly
    one jd-source posting (see find_source) becomes a link to it -- split on
    quote marks first so only the quotation itself, not the surrounding
    sentence, ends up inside the <a>."""
    if corpus is None:
        return render_inline_segment(text, where)

    pieces = re.split(r'("[^"\n]+")', text)
    out = []
    for i, piece in enumerate(pieces):
        rendered = render_inline_segment(piece, where)
        if i % 2 == 1:  # a captured "..." span, quote marks included
            source = find_source(piece[1:-1], corpus)
            if source:
                rendered = f'<a href="{archive_url(source)}">{rendered}</a>'
        out.append(rendered)
    return "".join(out)


def render_blocks(markdown, where, corpus=None):
    lines = markdown.splitlines()
    out = []
    i = 0

    def starts_block(line):
        return line.startswith(("## ", "### ", "- ", ">", "@video "))

    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{render_inline(line[4:], where, corpus)}</h3>")
            i += 1
        elif line.startswith("## "):
            out.append(f"<h2>{render_inline(line[3:], where, corpus)}</h2>")
            i += 1
        elif line.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(f"  <li>{render_inline(lines[i][2:].strip(), where, corpus)}</li>")
                i += 1
            out.append("<ul>\n" + "\n".join(items) + "\n</ul>")
        elif line.startswith(">"):
            quoted = []
            while i < len(lines) and lines[i].startswith(">"):
                quoted.append(lines[i][1:].strip())
                i += 1
            text = " ".join(q for q in quoted if q)
            # A blockquote is entirely a quotation (no surrounding sentence
            # the way an inline "..." span has), so when it matches a single
            # source, the whole rendered line links rather than just a span.
            rendered = render_inline_segment(text, where)
            source = find_source(text, corpus) if corpus else None
            if source:
                rendered = f'<a href="{archive_url(source)}">{rendered}</a>'
            out.append(f"<blockquote><p>{rendered}</p></blockquote>")
        elif line.startswith("@video "):
            match = re.match(r'^@video (\S+)(?:\s+"([^"]+)")?$', line)
            if not match:
                raise BuildError(f"{where}: malformed @video line: {line!r}")
            out.append(render_video_embed(match.group(1), match.group(2), where))
            i += 1
        elif UNSUPPORTED_BLOCK.match(line):
            raise BuildError(f"{where}: unsupported syntax: {line!r}")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not starts_block(lines[i]):
                if UNSUPPORTED_BLOCK.match(lines[i]):
                    raise BuildError(f"{where}: unsupported syntax: {lines[i]!r}")
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{render_inline(' '.join(para), where, corpus)}</p>")
    return "\n".join(out)


# ── Quote check ─────────────────────────────────────────────
# Every quotation in a post's data section must appear in jd-source/, under
# the same three normalizations the Quote field allows (CLAUDE.md): a
# capitalized first letter, spaces around an em dash, a terminal period.
# Straight and curly quote marks are treated as the same character.

def normalize(text):
    text = text.replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    text = re.sub(r"\s*—\s*", "—", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def load_taxonomy():
    """{key: label} for every cluster and signal in jobs.json, so a post's
    front-matter `signals:` keys (which may actually be cluster keys too --
    the post doesn't distinguish) can be rendered with their real label
    instead of the raw key."""
    with open(JOBS_JSON, encoding="utf-8") as fh:
        data = json.load(fh)
    labels = {}
    for group in ("clusters", "signals"):
        for key, info in data[group].items():
            labels[key] = info["label"]
    return labels


def load_corpus():
    """One (jd-source id, normalized full text) pair per archived posting,
    kept separate rather than concatenated so a matched quote can be traced
    back to the specific posting it came from, not just "somewhere in the
    archive." """
    corpus = []
    for name in sorted(os.listdir(JD_SOURCE_DIR)):
        if name.endswith(".md") and name != "README.md":
            with open(os.path.join(JD_SOURCE_DIR, name), encoding="utf-8") as fh:
                corpus.append((name[:-3], normalize(fh.read())))
    return corpus


def quotations(markdown):
    found = re.findall(r'"([^"\n]+)"|“([^”\n]+)”', markdown)
    spans = [a or b for a, b in found]
    spans += re.findall(r"^>\s?(.+)$", markdown, re.M)
    return spans


def unmatched_quotes(markdown, corpus):
    missing = []
    for span in quotations(markdown):
        needle = normalize(span).rstrip(".,;:")
        if needle and not any(needle in text for _, text in corpus):
            missing.append(span)
    return missing


def find_source(span, corpus):
    """The single jd-source id a quotation came from, or None if it matches
    zero or more than one archived posting -- linking confidently requires
    an unambiguous match, not just *a* match."""
    needle = normalize(span).rstrip(".,;:")
    if not needle:
        return None
    hits = [cid for cid, text in corpus if needle in text]
    return hits[0] if len(hits) == 1 else None


def archive_url(source_id):
    return f"https://github.com/bertinoco/bco-signals/blob/main/jd-source/{source_id}.md"


# ── Output ──────────────────────────────────────────────────

def site_assets():
    """Everything the post pages share with the home page, read out of
    docs/index.html so it's the one source: the styles.css and menu.js
    cache-bust versions, and the top bar and drawer markup itself. A change
    to either in index.html shows up here on the next build, and --check
    fails until it does."""
    with open(INDEX_HTML, encoding="utf-8") as fh:
        text = fh.read()

    def version(asset):
        match = re.search(rf"{re.escape(asset)}\?v=(\d+)", text)
        if not match:
            raise BuildError(f"docs/index.html: no {asset}?v= version string found")
        return match.group(1)

    def block(start, end, label):
        match = re.search(rf"^( *){re.escape(start)}.*?{re.escape(end)}", text, re.S | re.M)
        if not match:
            raise BuildError(f"docs/index.html: {label} markup not found")
        return textwrap.dedent(match.group(0))

    return {
        "css": version("css/styles.css"),
        "menu": version("js/menu.js"),
        "bar": block('<header class="site-bar">', "</header>", "top bar"),
        "drawer": block('<div class="site-menu-backdrop"', "</nav>", "site menu"),
    }


def post_url(post):
    return f"{SITE}/findings/{post['slug']}/"


def indent(block, spaces):
    pad = " " * spaces
    return "\n".join(pad + line if line else line for line in block.splitlines())


def render_page(post, assets, corpus, taxonomy):
    e = lambda s: html.escape(s, quote=True)
    url = post_url(post)
    where = post["source"]
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post["title"],
        "description": post["summary"],
        "url": url,
        "mainEntityOfPage": url,
        "image": OG_IMAGE,
        "datePublished": post["date"],
        "dateModified": post["updated"],
        "author": {"@type": "Person", "@id": "https://bertino.co/#joe",
                   "name": "Joe Bertino", "url": "https://bertino.co",
                   "image": SITE + "/images/joebertino.jpg"},
        "publisher": {"@type": "Organization", "@id": "https://bertino.co/#org",
                      "name": "Bertino Consulting", "url": "https://bertino.co"},
        "isPartOf": {"@id": SITE + "/#website"},
        "about": {"@id": SITE + "/#dataset"},
    }
    ld_json = json.dumps(ld, indent=2, ensure_ascii=False).replace("</", "<\\/")
    signals = "\n".join(f'<li class="signal-chip">{e(taxonomy[s])}</li>' for s in post["signals"])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- GENERATED FILE — do not edit by hand.
       Source: {where}. Regenerate with: python3 scripts/build-findings.py -->
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{e(post['title'])} — Signals</title>
  <meta name="description" content="{e(post['summary'])}">
  <link rel="canonical" href="{url}">

  <!-- Privacy-friendly analytics by Plausible -->
  <script async src="https://plausible.io/js/pa-WoV37_cSYerP-bLuBDf5L.js"></script>
  <script>
    window.plausible=window.plausible||function(){{(plausible.q=plausible.q||[]).push(arguments)}},plausible.init=plausible.init||function(i){{plausible.o=i||{{}}}};
    plausible.init()
  </script>

  <!-- Favicon -->
  <link rel="icon" href="/images/circle-icon-b.png" type="image/png">
  <link rel="apple-touch-icon" href="/images/circle-icon-b.png">

  <!-- OpenGraph -->
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{e(post['title'])}">
  <meta property="og:description" content="{e(post['summary'])}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="article:published_time" content="{post['date']}">

  <meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
  <meta name="theme-color" content="#0D0D0D" media="(prefers-color-scheme: dark)">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css?v={assets['css']}">

  <script type="application/ld+json">
{indent(ld_json, 2)}
  </script>
</head>
<body>

  <a class="skip-link" href="#main">Skip to content</a>

{indent(assets['bar'], 2)}

  <div class="container">
    <main id="main">
      <article class="post">
        <a class="post-back" href="/#findings"><span aria-hidden="true">← </span>All findings</a>
        <h1 class="post-title">{e(post['title'])}</h1>
        <div class="post-body">
{indent(render_blocks(post['data_md'], where, corpus), 10)}
        </div>
        <aside class="post-take" aria-labelledby="post-take-label">
          <h2 class="post-label" id="post-take-label">My take</h2>
{indent(render_blocks(post['take_md'], where, corpus), 10)}
          <div class="post-byline">
            <img class="post-byline-photo" src="/images/joebertino.jpg" alt="" width="32" height="32">
            <p class="post-byline-text">By <a href="https://bertino.co">Joe Bertino</a> · <time datetime="{post['date']}">{post['date']}</time></p>
          </div>
        </aside>
        <section class="post-signals" aria-labelledby="post-signals-label">
          <h2 class="post-label" id="post-signals-label">Signals cited</h2>
          <ul>
{indent(signals, 12)}
          </ul>
        </section>
      </article>
    </main>
  </div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-inner">
        <div class="footer-brand">A project by <a href="https://bertino.co">Bertino Consulting</a>, with help from Claude &amp; Freddie Gibbs.</div>
        <div class="footer-meta">Published <time datetime="{post['date']}">{post['date']}</time></div>
      </div>
    </div>
  </footer>

{indent(assets['drawer'], 2)}

  <script src="/js/menu.js?v={assets['menu']}"></script>
</body>
</html>
"""


def render_home_findings(posts):
    """The Read our findings list, written into docs/index.html between the
    findings:start/end markers. Static rather than fetched, so the post
    links are in the page for crawlers and the list shows without waiting
    on JavaScript. Posts past FINDINGS_LIMIT are rendered hidden, with a
    "Read more" button that scripts.js wires up to reveal them."""
    e = lambda s: html.escape(s, quote=True)
    pad = " " * 8

    if not posts:
        # Moved here from scripts.js's COPY object, since the list is no
        # longer rendered by script. The other empty states still live there.
        return textwrap.indent(textwrap.dedent("""\
            <div class="finding-list" id="finding-list">
              <div class="state state--empty">
                <p class="state-title">No findings yet</p>
                <p class="state-body">Findings will appear here once confirmed across multiple job descriptions.</p>
              </div>
            </div>
            """), pad)

    items = "".join(textwrap.dedent(f"""\
          <a class="finding" href="/findings/{p['slug']}/"{' hidden' if i >= FINDINGS_LIMIT else ''}>
            <div class="finding-header">
              <h3 class="finding-title">{e(p['title'])}</h3>
              <span class="finding-arrow" aria-hidden="true">→</span>
            </div>
            <time class="finding-date" datetime="{p['date']}">{p['date']}</time>
          </a>
        """) for i, p in enumerate(posts))
    block = '<div class="finding-list" id="finding-list">\n' + textwrap.indent(items, "  ") + "</div>\n"
    if len(posts) > FINDINGS_LIMIT:
        block += textwrap.dedent("""\
            <div id="findings-show-more">
              <button type="button" class="show-more-btn">Read more</button>
            </div>
            """)
    return textwrap.indent(block, pad)


def render_findings_redirect():
    """/findings/ listed every post until the home page took the list over.
    It stays as a redirect so links and bookmarks to it still land on the
    list; noindex and the canonical point search engines at the home page."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- GENERATED FILE — do not edit by hand.
       Regenerate with: python3 scripts/build-findings.py -->
  <meta charset="UTF-8">
  <title>Findings — Signals</title>
  <meta name="robots" content="noindex, follow">
  <link rel="canonical" href="{SITE}/">
  <meta http-equiv="refresh" content="0; url=/#findings">
</head>
<body>
  <p>Findings are on the <a href="/#findings">home page</a> now.</p>
</body>
</html>
"""


def render_findings_json(posts):
    data = {"findings": [{
        "id": p["slug"],
        "title": p["title"],
        "date": p["date"],
        "summary": p["summary"],
        "url": f"findings/{p['slug']}/",
        "signals": p["signals"],
    } for p in posts]}
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def render_sitemap(current, posts):
    kept = re.sub(r"\s*<url>\s*<loc>[^<]*/findings/[^<]*</loc>.*?</url>", "", current, flags=re.S)
    entries = "".join(
        f"\n  <url>\n    <loc>{post_url(p)}</loc>\n    <lastmod>{p['updated']}</lastmod>\n"
        f"    <changefreq>yearly</changefreq>\n    <priority>0.7</priority>\n  </url>"
        for p in posts
    )
    if "</urlset>" not in kept:
        raise BuildError("docs/sitemap.xml: no </urlset> found")
    return kept.replace("\n</urlset>", entries + "\n</urlset>", 1)


def render_llms(current, posts):
    lines = [
        "## Findings",
        "",
        "Written posts drawn from the dataset. Each separates what the postings say from a "
        "section labeled \"My take,\" which is Joe Bertino's personal view and not a claim "
        "the dataset backs.",
        "",
    ]
    lines += [f"- [{p['title']}]({post_url(p)}) ({p['date']}): {p['summary']}" for p in posts]
    section = "\n".join(lines) + "\n\n"

    without = re.sub(r"## Findings\n.*?(?=^## )", "", current, flags=re.S | re.M)
    anchor = "## How to cite this work"
    if anchor not in without:
        raise BuildError(f"docs/llms.txt: no '{anchor}' section to place Findings before")
    if not posts:
        return without
    return without.replace(anchor, section + anchor, 1)


def read(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def main():
    check = "--check" in sys.argv[1:]

    sources = sorted(
        os.path.join(SOURCE_DIR, n) for n in os.listdir(SOURCE_DIR)
        if n.endswith(".md") and n != "README.md"
    )
    parsed = [parse_post(p) for p in sources]
    posts = sorted((p for p in parsed if not p["draft"]),
                   key=lambda p: (p["date"], p["slug"]), reverse=True)

    corpus = load_corpus()
    taxonomy = load_taxonomy()
    for post in parsed:
        missing = unmatched_quotes(post["data_md"], corpus)
        if missing:
            raise BuildError(
                f"{post['source']}: quoted text not found in jd-source/:\n"
                + "\n".join(f"    {m!r}" for m in missing)
            )
        for span in unmatched_quotes(post["take_md"], corpus):
            print(f"note: {post['source']}: My take quotes text not in jd-source/: {span!r}")
        unknown = [s for s in post["signals"] if s not in taxonomy]
        if unknown:
            raise BuildError(
                f"{post['source']}: unknown cluster/signal key(s): {', '.join(unknown)}"
            )

    assets = site_assets()
    outputs = {os.path.join(OUT_DIR, p["slug"], "index.html"): render_page(p, assets, corpus, taxonomy)
               for p in posts}
    outputs[os.path.join(OUT_DIR, "index.html")] = render_findings_redirect()
    outputs[FINDINGS_JSON] = render_findings_json(posts)

    index_text = read(INDEX_HTML)
    match = FINDINGS_MARKERS.search(index_text)
    if not match:
        raise BuildError("docs/index.html: findings:start / findings:end markers not found")
    outputs[INDEX_HTML] = index_text[:match.start(2)] + render_home_findings(posts) + index_text[match.end(2):]
    outputs[SITEMAP] = render_sitemap(read(SITEMAP), posts)
    outputs[LLMS] = render_llms(read(LLMS), posts)

    # Only per-post subdirectories are orphan candidates -- OUT_DIR's own
    # index.html (the plain-HTML listing) is a file, not a post, and
    # shutil.rmtree below would error on it if it were swept in here.
    published = {p["slug"] for p in posts}
    orphans = [os.path.join(OUT_DIR, d) for d in sorted(os.listdir(OUT_DIR))
               if os.path.isdir(os.path.join(OUT_DIR, d)) and d not in published] \
              if os.path.isdir(OUT_DIR) else []

    stale = [path for path, content in outputs.items() if read(path) != content]
    rel = lambda p: os.path.relpath(p, ROOT)

    if check:
        if stale or orphans:
            for path in stale:
                print(f"out of date: {rel(path)}")
            for path in orphans:
                print(f"no matching post: {rel(path)}")
            print("Run: python3 scripts/build-findings.py")
            sys.exit(1)
        print(f"OK: {len(posts)} finding(s) up to date")
        return

    for path in stale:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(outputs[path])
        print(f"wrote {rel(path)}")
    for path in orphans:
        shutil.rmtree(path)
        print(f"removed {rel(path)}")
    if not stale and not orphans:
        print(f"{len(posts)} finding(s) already up to date")


if __name__ == "__main__":
    try:
        main()
    except BuildError as err:
        print(f"error: {err}", file=sys.stderr)
        sys.exit(1)
