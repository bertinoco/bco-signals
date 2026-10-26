Check the health of the whole codebase, fix what's safe to fix on a branch, and report everything else in plain language. Joe isn't a developer: he relies on this to keep the site efficient, secure, and tidy without reading the code himself. Treat the codebase with care. Its outputs — the dataset, the archive, the published site — are the point, so prefer leaving something alone to risking it.

Runs by hand (`/system-check`) and monthly as a scheduled cloud routine. Behave the same in both. The only difference is that nobody is watching the scheduled run, which is why the report always gets committed (Step 5).

## Step 1 — Start clean

- `git status`. If there's uncommitted work, stop and say so — don't stash, discard, or build on top of it. (In the scheduled run the tree is always clean.)
- `git checkout main && git pull --ff-only origin main`.

## Step 2 — Run the mechanical checks

```
python3 scripts/system-check.py
```

It's read-only and covers everything with a right answer: both builds' `--check`, the `jobs.json` validator, asset cache-bust versions, Python/JS syntax, stale `jd-insights` output, committed secrets, unused CSS classes, unreferenced and oversized images, docs that mention CSS classes that no longer exist, untracked files, third-party scripts, and page weight. FAIL items are the top of the report.

## Step 3 — The judgment pass

Read the code for what a script can't decide. In this repo, look especially at:

- **Generated vs. hand-written drift.** `scripts/build-home.py` mirrors `renderSignals`/`renderClusters`/`renderTitles` in `docs/js/scripts.js`; `scripts/build-findings.py` lifts the top bar and drawer out of `docs/index.html`. If one side changed without the other, the page shifts when the script takes over. Compare the logic, not just the data.
- **Dead or duplicated code** in `docs/js/`, `docs/css/styles.css`, and `scripts/` — functions nothing calls, rules nothing matches, the same logic written twice.
- **Comments and docs that describe the site as it used to be.** This has happened every time the site changed shape: `CLAUDE.md`, `findings/README.md`, `.claude/commands/*.md`, and code comments.
- **Efficiency.** Image file size against the size it's displayed at (the byline photo renders at 32px), CSS/JS weight, anything loaded and not used.
- **Security.** Third-party scripts, workflow permissions, anything taking input. The site is static, so the surface is small — say so rather than inventing risk.
- **Design-system adherence** where it's cheap to check: hard-coded colors or sizes where a token exists.

Then rotate one deeper review, by month: January, April, July, October → `/design-review`; February, May, August, November → `/llm-visibility`; March, June, September, December → `/security-review`. If the scheduled environment doesn't have that skill, say so in the report and skip it.

## Step 4 — Sort every finding

**Safe to fix — do these on autopilot.** All of these must hold: nothing a visitor sees changes (layout, copy, color, behavior), no content or data changes, and it's trivially reversible. That means:

- regenerating generated output that's stale (`build-findings.py`, `build-home.py`, `jd-insights/refresh.py`)
- a missed `?v=` cache-bust bump
- removing CSS rules or JS functions that nothing uses — confirmed by `system-check.py` and a search, not a hunch
- fixing code comments and docs (`CLAUDE.md`, READMEs, `.claude/commands/`) that describe something that no longer exists, to match what's there now
- shrinking an image file without changing how it looks at its displayed size: same filename, no more than 3× the displayed pixels, then confirm the rendered dimensions didn't change
- typos in comments and docs (never in site copy or JD content)

**Joe's call — report, don't touch:**

- anything visible on the site, including copy
- `docs/data/jobs.json`, `jd-source/`, `findings/*.md`, and the hand-written `jd-insights/` files (`findings.md`, `patterns.md`)
- the rules in `CLAUDE.md` — fixing a stale fact in it is safe; changing what a rule says is not
- CI workflows, `robots.txt`, analytics, and security policy (adding an integrity hash to the Plausible script is his call — he's already declined it once)
- deleting, renaming, or moving any image or other asset. He plans his own pass on `docs/images/`, and an unused-looking file may be one he means to use.
- new dependencies, or anything that changes how a build or check works

**FYI** — worth knowing, no action needed.

When in doubt, it's Joe's call.

## Step 5 — Fix, verify, commit, report

1. `git checkout -b system-check/YYYY-MM-DD` (today's date).
2. Make the safe fixes. After any CSS/JS change, bump its `?v=` in `docs/index.html` and rerun `python3 scripts/build-findings.py` (post pages embed the CSS version and the nav markup).
3. Rerun `python3 scripts/system-check.py`. It must have no FAIL items, and every OK it had at the start must still be OK. If a fix broke something, revert that fix and report it instead.
4. Write the report to `system-check/reports/YYYY-MM-DD.md` (format below) and commit it with the fixes. Commit message: what was fixed and why, ending with the co-author line from the current attribution guidance.
5. `git push -u origin system-check/YYYY-MM-DD`.
6. **Never merge to `main`.** Joe merges by saying so. When he does, merge with `--no-ff` and rerun `python3 scripts/system-check.py` on `main`. Only push if its exit status is 0. Check the real exit status: don't pipe it through `tail` or `grep`, which pass even when the check fails. Other sessions add JDs to `main` while a branch is open, so a clean branch can still merge into a failing `main`. If it fails, fix that first; regenerating stale output is a safe fix. Then push, delete the branch, and confirm the live site picked it up.

If the run found nothing safe to fix, still commit and push the report on its branch, so the monthly run always leaves a record.

### Report format

Write for someone who doesn't read code: what it is, why it matters, and what happens next — no jargon without a plain-language gloss. Short.

```markdown
# System check — YYYY-MM-DD

**Bottom line:** one or two sentences. Healthy? Anything urgent?

## Fixed on this branch
- What changed, in plain words, and why it's safe. (Or "Nothing needed fixing.")

## Your call
- The finding, why it matters, what I'd recommend, and what it would cost.

## FYI
- Worth knowing, no action needed.

## Checks
The `system-check.py` summary line, plus which deeper review ran this month.

To merge the fixes, say "merge the system check".
```

In a live session, also give Joe the report directly in the reply, with the branch name.
