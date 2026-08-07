Process a new job description for possible addition to `docs/data/jobs.json`, following the eligibility and audit rules in `CLAUDE.md`. The research-heavy and mechanical steps run in subagents so the main conversation only carries what needs your judgment or the user's confirmation — this is what keeps repeated JD submissions from burning through the main thread's context.

## Input

The JD text should already be in the conversation, pasted by the user, chrome and all. If it isn't there, ask for it before doing anything else.

## Step A — Eligibility + audit (subagent, foreground)

Spawn a `general-purpose` agent (`run_in_background: false`) with a fully self-contained prompt. It hasn't seen this conversation, so include:

- The complete JD text as submitted, verbatim, including any platform chrome
- An instruction to follow this repo's `CLAUDE.md` — specifically the "Entry eligibility" section and Steps 1–4 of "Entry audit process" (it will have `CLAUDE.md` loaded automatically as project context; point it at these sections by name rather than re-deriving the rules yourself)
- An instruction to read `docs/data/jobs.json` for the current `clusters`, `signals`, and `domain` taxonomy, and `jd-source/README.md` for the archive format
- An instruction to check `docs/data/jobs.json` for any existing entries from the same company, for precedent/consistency
- An instruction to return *only* a structured report, not raw file dumps: eligibility verdict with reasoning, proposed cluster/signal assignments each with the grounding quote from the JD, any ambiguous calls flagged rather than resolved, any new cluster/signal/domain candidates per Step 4's backcheck bar (flagged, not created), proposed `title` (verbatim, separator noted), `domain`, `location`, `engagement`, `remote`, a proposed `id`, a proposed `compRange` with reasoning for `covers`/`scope`/`extras`, and a proposed `quote`.

The subagent must not write to any files in this step — research and judgment only.

## Step B — Present and confirm

Relay the subagent's report to the user yourself, in the same format used for manual audits in this project (clear assignments as a table, ambiguous items called out individually). Wait for the user's confirmation, including resolution of anything flagged, before proceeding.

If the user says the JD should be excluded instead, do not use a subagent for this — it's a small, single-file write. Follow CLAUDE.md's "Note on rejected roles" directly: write `jd-source/{id}.md` with `excluded` and `excludedReason` set, and write nothing to `jobs.json`.

## Step C — Write (subagent, foreground)

Once the user confirms, spawn a second `general-purpose` agent (`run_in_background: false`) to carry out CLAUDE.md Step 6 in full, using the now-confirmed field values from Step B:

- Append the entry to `docs/data/jobs.json`, preserving existing field order and formatting
- Archive the JD verbatim to `jd-source/{id}.md` per `jd-source/README.md`
- Update `meta.totalEntries` and `meta.lastUpdated` in `jobs.json`
- Update `<lastmod>` in `docs/sitemap.xml`
- Update the entry count/date in `docs/llms.txt` (both the dataset-description section and the citation line)
- Run `python3 jd-insights/refresh.py`
- Verify the archived `quote` and `title` match the archive verbatim (only the three permitted normalizations), and fail loudly if they don't
- Check whether `jd-insights/patterns.md` or `jd-insights/findings.md` warrant an update per CLAUDE.md's rules — most entries add nothing; only propose an addition if it clears Step 4's bar (evidence across multiple JDs) or is explicitly a first-instance item for the Watching section
- Return a short summary, `git diff --stat`, and anything it flagged for `patterns.md`/`findings.md` — added or just proposed, your call which

## Step D — Review and ship

Read the subagent's diff summary yourself before acting on it — don't relay it unchecked. Per CLAUDE.md Step 7, the user's Step B confirmation already covers commit/push/merge for JD entries specifically, so commit, push, and merge to `main` without asking again — unless the subagent's output looks wrong, in which case stop and show the user what's off.
