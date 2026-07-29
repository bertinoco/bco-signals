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
sourcePlatform: linkedin
dateAdded: 2026-05-24
captured: 2026-07-27
captureMethod: pasted-from-claude-chat
captureNote: >
  Optional free-text note about the capture itself.
---

[raw JD text]
```

`dateAdded` mirrors the `jobs.json` entry. `captured` is when the text was
archived here. `captureMethod` records provenance — `pasted-from-claude-chat`,
`pasted-from-source`, or `fetched` with a live `sourceUrl`.

`sourcePlatform` (optional) records where the text was captured from, e.g.
`linkedin` or `company-site`. Worth setting when the capture includes platform
chrome, since that chrome is retained rather than trimmed.

`postedDate` and `reqId` (both optional) record what the listing itself states —
the date the posting went up, and the employer's requisition or role number.
Set them only when the source states them; do not derive `postedDate` from a
relative string like "2 weeks ago", which is ambiguous about when it was read.
`reqId` is what pins an entry to a specific requisition: employers reuse titles
across postings, so a same-titled listing is not necessarily the same posting.

`team` (optional) records the product or org the role sits in when that is
known but not stated in the posting text. Use it only for attribution that
comes from outside the capture, and say so in `captureNote`.

`orgPlacement` records where the posting says the role sits — the department,
team, business unit, or reporting line, in the posting's own words. Set it to
`null` when the posting does not say; that absence is a fact about the posting
and is worth recording as one.

Record what is stated, not what it implies. Where a posting names a partner or
reporting relationship instead of a department, say so plainly — "Not stated as
a department; the role works closely with the CMO" — rather than inferring a
placement from it. Do not classify: grouping these values into categories is a
reading of the corpus, and belongs in analysis rather than in the archive.

`captureNote` (optional) records anything a later reader needs to know about
the capture — retained page chrome, ambiguous dates, sections known to be
missing. Use it to flag ambiguity rather than resolving it.

## Excluded roles

A file may outlive its `jobs.json` entry. When a role is removed from the
dataset — or reviewed and rejected before it was ever added — the source text
stays here with `excluded` (the date) and `excludedReason` (why) in the front
matter.

These files have no corresponding entry in `jobs.json`. That is intentional:
the archive records the reasoning behind an exclusion, so the same JD is not
re-evaluated from scratch or quietly re-added later. Check for an `excluded`
field before treating a file as backing a live entry.

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
