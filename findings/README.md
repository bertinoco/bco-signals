# Findings posts

Each Markdown file here is one post on the site's Findings tab. The filename is
the post's URL slug: `content-design-central-systems.md` publishes to
`signals.bertino.co/findings/content-design-central-systems/`.

What a post may say is set by `CLAUDE.md` (the Findings tab exception and the
Findings tab promotion process). This file covers only the format.

## Format

```markdown
---
title: Content design is becoming a central systems discipline
date: 2026-10-22
signals: central-standards-function, content-systems-design, enablement
draft: true
---

## A section heading

What the postings say. Quote them: "single accountable owner"

- Netflix: "a list item"

> A longer quotation from one posting

<aside>

My take. Everything inside the aside renders under the "My take" label.

</aside>
```

**Front matter.** `title`, `date` (YYYY-MM-DD), and `signals` (comma-separated
cluster and/or signal keys from `docs/data/jobs.json`) are required. The build
fails if a key doesn't exist in either taxonomy. `updated` (YYYY-MM-DD) is
optional and sets the sitemap date after an edit. `draft: true` keeps a post
out of the build until it is approved for publishing.

There is no `summary` field to write. A one-line summary is still derived
automatically from the post's own opening sentences — the first one or two
sentences of the data section's opening paragraph, truncated if that's still
too long — and used in meta/OG/JSON-LD description tags and `llms.txt`.
Neither the Findings tab nor the `/findings/` index display it anymore (that
was dropped — a post's title was doing that job on its own), but it's still
worth writing that opening paragraph with the summary in mind, since it's
what search results and link previews show.

**Body.** Everything before `<aside>` is the data section; everything inside it
is "My take". Exactly one `<aside>`, and nothing after it.

**Supported syntax**: `##` and `###` headings, paragraphs, `- ` lists, `> `
blockquotes, `**bold**`, `*italic*`, `[links](https://…)`, and `@video
<url>` (see below). Anything else fails the build rather than rendering
unpredictably. No `#` heading, since the title comes from front matter.

**Embedding video.** A line of the form:

```markdown
@video https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

on its own (blank line before and after, same as a blockquote or a list)
embeds a responsive 16:9 player. Works in either section — the data section
for supporting external material, or inside `<aside>` for something the
"My take" is reacting to. Only `youtube.com/watch?v=…`, `youtu.be/…`,
`youtube.com/embed/…`, and `vimeo.com/<id>` URLs are recognized; anything
else fails the build rather than embedding an unverified URL. A plain
`[link](url)` still works anywhere inline, for anything that isn't video —
an article, a tweet, a talk's writeup.

## Style

`content-design-central-systems.md` is the reference to copy the shape of,
not just the one example in the Format section above. What makes it work:

- **The opening paragraph doubles as the summary.** It's the first thing
  `derive_summary()` reads for every meta/OG/JSON-LD description tag and
  `llms.txt` — write it as a standalone sentence or two that could survive
  being read completely out of context and shown nowhere near the rest of
  the post, not as a lead-in to the list right under it.
- **Each `##` section opens with a claim, then grounds it.** A sentence
  stating what the postings show, then the postings themselves — inline
  `"quoted"` fragments for a quick scan across several companies, a `>`
  blockquote when one posting's own wording carries the point better than a
  paraphrase could. Don't stack more than two or three quotes under one
  claim; if a fourth company says the same thing, that's a sign the claim
  itself could be sharper, not that it needs a longer list.
- **The data section stays reportorial even while it's persuasive.** Strong
  verbs are fine ("say outright," "spells out"); conclusions the quotes
  don't support aren't. That's what `<aside>` is for.
- **`<aside>` is a real shift in register, not a recap.** It should read like
  Joe talking, not like the data section restated in first person — a
  genuine reaction, a prediction, a tension the data raises without
  resolving. CLAUDE.md's Findings tab exception spells out exactly how much
  license this section has; use it.
- **Length is a paragraph or two per idea, not an essay.** The published
  post runs two `##` sections and a four-paragraph take. That's the scale to
  aim for — long enough to ground the claim, short enough that a reader
  finishes it.

## Building

```sh
python3 scripts/build-findings.py          # write the pages and listings
python3 scripts/build-findings.py --check  # what CI runs
```

The build fails if a quotation in the data section can't be found in
`jd-source/`. Commit the source file and everything the build writes together.

Any `"quoted span"` or `> blockquote` that matches exactly one archived
posting becomes a link to it on GitHub, in both the data section and "My
take." A quote that happens to also appear verbatim in a different posting
stays unlinked rather than risk pointing at the wrong one — nothing to fix,
that's the intended behavior, not a bug.
