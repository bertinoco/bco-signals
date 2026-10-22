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
summary: One reportorial sentence, shown on the Findings tab and in link previews.
companies: Netflix, Wix, Adobe
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

**Front matter.** `title`, `date` (YYYY-MM-DD), `summary`, and `companies`
(comma-separated) are required. `updated` (YYYY-MM-DD) is optional and sets the
sitemap date after an edit. `draft: true` keeps a post out of the build until
it is approved for publishing.

**Body.** Everything before `<aside>` is the data section; everything inside it
is "My take". Exactly one `<aside>`, and nothing after it.

**Supported syntax**: `##` and `###` headings, paragraphs, `- ` lists, `> `
blockquotes, `**bold**`, `*italic*`, and `[links](https://…)`. Anything else
fails the build rather than rendering unpredictably. No `#` heading, since the
title comes from front matter.

## Building

```sh
python3 scripts/build-findings.py          # write the pages and listings
python3 scripts/build-findings.py --check  # what CI runs
```

The build fails if a quotation in the data section can't be found in
`jd-source/`. Commit the source file and everything the build writes together.
