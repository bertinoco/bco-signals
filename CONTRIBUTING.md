# Contributing a job description

This dataset is built from individual job postings, audited one at a time
against the criteria in `CLAUDE.md`. If you've come across a posting that
fits — content design, UX writing, content strategy, or a technical content
discipline, doing something that isn't standard for the role yet — submit it
and we'll run it through that process.

## Before you submit

Skim the "Entry eligibility" section of `CLAUDE.md` for the full criteria.
The short version: the role has to be primarily about content craft or
systems (not headcount, budget, or executive alignment), specific enough to
pull at least two distinct responsibilities out of, and it has to do
something that isn't standard for the discipline yet — new framing, explicit
AI/governance/model-behavior responsibilities, or a title/scope placement
that signals the work is being valued differently.

Submitting a posting isn't a guarantee it gets added. Most of the audit
happens after submission, not before — see "What happens next" below.

## How to submit

**[Submit a job posting →](https://github.com/bertinoco/bco-signals/issues/new?template=submit-a-jd.yml)**

That link opens a short form on GitHub (a free account, signed in, is all it
takes — no coding involved). The field that actually matters is the full text
of the posting, pasted in as-is.

- **Paste the text now, even if you also have a link.** Postings get taken
  down or edited within days on some job boards, and a submission with no
  text and a dead link can't be audited. The text is the record; the URL is
  a courtesy, not a substitute.
- **A source URL is optional.** Some postings come from a screenshot, a
  forward, or a platform that doesn't give you a stable link. Leave it
  blank rather than holding up the submission to go find one.
- **Don't clean it up.** Page chrome — an "Apply now" button's text, a
  LinkedIn applicant count, site navigation — is fine to leave in. It gets
  stripped or noted during the audit, not before.

## What happens next

Every submission gets an independent audit, not a rubber stamp of what's in
the issue. Clusters, signals, and eligibility are re-derived from the posting
text directly, whatever the issue says about them.

Two outcomes:

- **Included** — the entry is added to `docs/data/jobs.json`, and the
  submitted text is archived verbatim in `jd-source/`.
- **Excluded** — the posting is archived in `jd-source/` with the reasoning
  recorded, so it doesn't get re-audited from scratch or quietly added
  later. Nothing is added to `jobs.json`.

Either way, you'll hear back on the issue.
