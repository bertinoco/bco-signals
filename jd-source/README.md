# JD source corpus

Verbatim source text for each entry in `docs/data/jobs.json`.

## Why this lives outside `docs/`

`docs/` is the GitHub Pages root (see `docs/CNAME`) — everything in it is served
publicly at signals.bertino.co. This corpus is a research archive, not site
content, so it stays in the repo but off the published site.

It is also kept out of `jobs.json` itself: `docs/js/scripts.js` fetches that file
on every page load, and inlining full JD text would multiply the payload for data
the site never renders.

## Join key

Filenames match the `id` field of the corresponding entry in `jobs.json`:

    jd-source/{id}.md  ->  entries[].id

The file exists or it doesn't — there is no flag in `jobs.json` to keep in sync.

## File format

Front matter, then the raw text:

```markdown
---
id: sanna-content-engineer
company: Sanna
title: Content Engineer
sourceUrl: null
dateAdded: 2026-05-24
captured: 2026-07-27
captureMethod: pasted-from-claude-chat
---

[raw JD text]
```

`dateAdded` mirrors the `jobs.json` entry. `captured` is when the text was
archived here. `captureMethod` records provenance — `pasted-from-claude-chat`,
`pasted-from-source`, or `fetched` with a live `sourceUrl`.

## Rules

- Text is stored **verbatim**. No cleanup, reformatting, summarizing, or
  truncation. The value of the archive is that it is unedited.
- If the text is partial (e.g. responsibilities captured but not the
  qualifications section), note that in the front matter with
  `partial: true` rather than presenting it as complete.
- Never reconstruct or infer JD text that wasn't captured. A missing file is
  an accurate record of a missing capture.

## What this enables

Step 4 of the entry audit process in `CLAUDE.md` asks for a backcheck across
existing entries before creating a new cluster or signal key. Without source
text that scan can only see keys already assigned, which cannot surface a
pattern that was never given a key. With the corpus, the scan reads the actual
language.
