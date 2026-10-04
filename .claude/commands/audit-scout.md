Audit the postings queued on the JD Scout triage page, using `/add-jd` for each one. This command only feeds `/add-jd` and closes the loop on the triage page afterwards. Eligibility, assignments, the write and the merge all follow `/add-jd` (`.claude/commands/add-jd.md`) and `CLAUDE.md` unchanged. Every posting still gets its own audit and the user's own confirmation.

Triage page: https://claude.ai/artifact/JgK9ZkqrKmRt2Zj6KkMXuK. Load `ArtifactData` with ToolSearch to read and write its database.

## Step 1 — Read the queue

`ArtifactData` `query` on collection `candidates` with `where: [["status", "==", "audit"]]`. Note each document's `version`, which every later write must pass as `if_version`.

If the queue is empty, say so in one line and stop. Otherwise list the queue to the user in one short table (title verbatim, company, posted date), and say whether you will work through it one at a time or in groups (Step 3).

## Step 2 — Fetch each posting's text

For each candidate:

    python3 jd-scout/scout.py fetch <candidate id>

- **Exit 0:** stdout is the posting. Save it to the scratchpad as `<candidate id>.txt`. This fetched text is the JD "as submitted" for `/add-jd` and `CLAUDE.md`: it is what Step A audits and what Step C archives, verbatim, header lines included. It has no job-board page chrome because the source is the ATS feed, not a web page.
- **Exit 3:** the posting has closed. Don't audit it. Tell the user, and leave it queued so they can skip it on the page or keep it for reference.
- **Any other failure:** report the error and carry on with the rest of the queue.

## Step 3 — Audit, one at a time or in groups

**One at a time** when 1 or 2 postings are queued: run `/add-jd` Steps 0–D for the posting, then move to the next.

**In groups** of up to 5 when more are queued:

1. Run `/add-jd` Step 0 and Step A for every posting in the group, launching the Step A agents together in one message so they run in parallel. Each agent gets one posting's fetched text, exactly as `/add-jd` Step A specifies.
2. Present all the reports together for `/add-jd` Step B, numbered, each in the usual format. Ask the user to answer each one: confirm, exclude, or change something.
3. Run `/add-jd` Step C and Step D for the confirmed postings **one after another, never in parallel**. Each write changes `meta.totalEntries`, the sitemap and `llms.txt`, so parallel writes would conflict. Each entry is committed and merged on its own, as `/add-jd` Step D already does.
4. Postings the user excludes are archived as excluded per `/add-jd` Step B.
5. Start the next group only after this one is fully written.

The user can switch modes at any time ("just do the next one", "show me the rest together").

## Archive fields for fetched postings

In `jd-source/{id}.md`, for every posting audited from the queue, included or excluded:

- `captureMethod: fetched`
- `sourceUrl`: the candidate's `url`
- `sourcePlatform`: the ATS, as `greenhouse`, `lever` or `ashby` (drop any `-eu` suffix)
- `postedDate`: the `Posted:` line from the fetched text, when it has a date
- `captureNote`: "Fetched from the <ATS> job board feed by JD Scout (candidate <candidate id>)."

Tell the Step C agent these values alongside the confirmed entry fields.

## Step 4 — Close the loop on the triage page

After each posting's write is merged, or its exclusion is archived, `ArtifactData` `update` the candidate, passing `if_version`:

- `status: "done"`
- `outcome`: `"included"` or `"excluded"`
- `entryId`: the `jobs.json` / `jd-source` id
- `statusAt`: the current time, ISO 8601

If an update fails because the version changed, the user edited the posting on the page in the meantime. Re-read it and report what changed instead of overwriting it.

## Step 5 — Report

End with one short summary: how many were added, excluded, closed or left queued, with each entry id.
