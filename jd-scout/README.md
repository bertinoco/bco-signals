# JD Scout

Finds content design, UX writing, content strategy and content systems postings
on Greenhouse, Lever and Ashby job boards, many of which never reach LinkedIn,
and lists them for triage.

It only finds candidates. Whether a posting enters the dataset is still decided
by the add-jd audit in `CLAUDE.md`, one posting at a time, with your
confirmation.

## How it works

Every Sunday at 19:52 Stockholm time a Routine starts a fresh Claude Code
session that follows `ROUTINE.md`:

1. **Discovery.** Runs the `site:` searches in `discovery.json` to find company
   boards that aren't on the list yet.
2. **Poll.** Reads each board's public JSON feed and keeps postings that match
   `keywords.json`.
3. **Filter.** Drops postings already archived in `jd-source/` (included or
   excluded), already in `jobs.json`, or already on the triage page, whatever
   their status. A posting counts as already archived when its job id appears
   in an archived `sourceUrl`, or when the company matches loosely ("NiCE
   (Cognigy)" and "NICE") and the title matches exactly. A title that is close
   but not identical isn't dropped. It shows on the page as "Similar to
   archived", so you can decide whether it's a repost or a new role.
4. **Write.** Adds the new postings to the triage page's database.

Triage page: https://claude.ai/artifact/JgK9ZkqrKmRt2Zj6KkMXuK
(`triage.html` is its source. Republish it from this path after editing.)

## Matching

The match runs in two passes:

- **Title match:** a `title_terms` pattern appears in the title.
- **Body-only match:** no title term, but a `body_phrases` pattern appears in
  the JD text. These show in a collapsed section on the page, since they are
  noisier. They are how titles like Product Designer, Evals & Prompts or
  User Guidance Lead get found.

`title_exclude` drops a posting before either pass, for titles like content
marketing, moderation, game design and engineering roles on "content platform"
teams. A body-only match also needs a `body_only_title_require` word in the
title (design, writing, editing, guidance, documentation), so a credit risk
role that mentions a tone of voice guide doesn't qualify.

`test_scout.py` runs every entry in `docs/data/jobs.json` through the filter
and fails if any would be missed. When a new entry fails it, widen
`keywords.json`.

    python3 -m unittest jd-scout/test_scout.py

## Triage

On the page, each posting gets one of three actions:

- **Audit:** queues it.
- **Later:** keeps it in view.
- **Skip:** hides it for good. Skipped postings never come back.

You can also add a board by slug or URL there.

## Auditing queued postings

In a Claude Code session, ask to "audit the queued JD Scout candidates." For
each candidate with status `audit`:

1. Get the full posting text:

       python3 jd-scout/scout.py fetch <candidate id>

2. Run the add-jd audit on that text, as for any submitted JD. Archive it with
   `captureMethod: fetched`, the posting URL as `sourceUrl`, and the ATS as
   `sourcePlatform`. The fetched text is the ATS feed's rendering of the
   posting, stored as fetched.
3. Once the entry is written or archived as excluded, set the candidate's
   `status` to `done`, with `outcome` (`included` or `excluded`) and
   `entryId`.

## Network access

The feeds live at `boards-api.greenhouse.io` (which also serves EU-hosted boards),
`api.lever.co`, `api.eu.lever.co` and `api.ashbyhq.com`. The cloud environment
must allow those hosts, or every board fails and the page reports it.
