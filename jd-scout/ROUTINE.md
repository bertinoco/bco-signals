# JD Scout weekly run

Instructions for the Sunday Routine. The Routine's prompt points here, so
changing the weekly run means editing this file, not the Routine.

The run is unattended. It finds postings and lists them on the triage page. It
never audits, never writes to `docs/data/jobs.json` or `jd-source/`, and never
commits or pushes.

Triage page (its database is where every result goes):
https://claude.ai/artifact/JgK9ZkqrKmRt2Zj6KkMXuK

Use `$RUN` for a scratch directory: `RUN=$(mktemp -d)`.

## 1. Read the triage database

Save both collections as files with `ArtifactData` `list`, using `out_dir`.
Page with `query.cursor` until there is no `next_cursor`.

- collection `companies`, `out_dir: $RUN/dump`
- collection `candidates`, `out_dir: $RUN/dump`

The second holds every posting already shown, including skipped ones. That is
how skipped postings stay hidden.

## 2. Discover new boards

For each host and each query in `jd-scout/discovery.json`, run `WebSearch` with
`site:<host> <query>` and `allowed_domains: [<host>]`. Collect every result URL
into `$RUN/urls.txt`, one per line. Then:

    python3 jd-scout/scout.py slugs < $RUN/urls.txt > $RUN/discovered.json

If a search errors, note it and carry on. Discovery is best effort.

## 3. Poll the boards

    python3 jd-scout/scout.py poll \
      --companies jd-scout/seed-companies.json $RUN/discovered.json \
      --db-dump $RUN/dump --out $RUN/out

This writes:

- `$RUN/out/companies-new/*.json`: boards not yet in the database
- `$RUN/out/candidates/*.json`: postings not yet in the database
- `$RUN/out/summary.json`: counts, failed boards, and `openIds` (every matching
  posting still open, used by the page to mark closed ones)

## 4. Write the results

Create the new documents with `ArtifactData` `batch`, at most 50 writes per
call. Each write is `{op: "set", collection, doc_id: <filename without .json>,
file_path: <the file>}` with no `if_version`, since these documents are new.

- every file in `$RUN/out/companies-new/` into collection `companies`
- every file in `$RUN/out/candidates/` into collection `candidates`

Then record the run. Build one JSON object from `summary.json`, leaving out
`newIds` and adding
`"discovery": {"queries": <searches run>, "failedQueries": <count>, "newCompanies": <newBoards from summary>}`.
Write it to:

- collection `meta`, doc `run`. `get` it first; pass its `version` as
  `if_version` if it exists.
- collection `runs`, doc `<YYYY-MM-DD>`: the same object without `openIds`.

## 5. Report

End with a short summary: new postings (title matches and body-only matches
counted separately), boards checked, boards failed, and boards discovered. If
every board failed with a connection error, say the environment's network
policy is probably blocking `boards-api.greenhouse.io`, `api.lever.co` or
`api.ashbyhq.com`, and that the fix is in the environment's network settings.
