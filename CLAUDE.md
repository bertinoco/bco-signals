# BCO Skills Tracker — Claude Instructions

## Data integrity rules

When adding or reviewing entries in `docs/data/jobs.json`, follow these rules without exception:

- Report only what the JD states. Do not infer intent, project trends, or editorialize.
- Clusters and signals must be grounded in stated responsibilities. If a JD does not explicitly mention a responsibility, do not assign the corresponding cluster.
- Descriptions must be neutral. Describe what the JD says, not what it implies.
- If a responsibility is ambiguous, note the ambiguity rather than resolving it.
- No projections. Do not predict where the market is heading. The data speaks for itself.
- No value judgments. Do not rank roles, call one "more comprehensive" than another, or label work as "lower-complexity."

## Entry eligibility

Before auditing a new JD, evaluate whether it should be included at all. The default is to exclude unless all required criteria are met and at least one signal test passes. Flag concerns rather than silently adding borderline entries.

**Required — all must be true**
- The role is primarily in content design, UX writing, content strategy, or a technical content discipline (content engineering, content architecture, language systems)
- The JD is specific enough to extract at least two distinct cluster assignments from stated responsibilities
- The JD's stated responsibilities are primarily about craft, systems, or discipline-building — not headcount management, budget ownership, or executive alignment

**Signal test — at least one must be true**
- The JD introduces a responsibility or framing not common in traditional content roles
- The JD explicitly references AI tooling, governance, or model behavior as part of the work
- The title, scope, or team placement signals a structural shift in how content work is valued or positioned

**Exclusion flags — any one disqualifies**
- The role is primarily content marketing or editorial production, even if it uses systems language
- The role has no meaningful connection to product, platform, or language infrastructure
- The JD is too generic to yield distinct cluster or signal assignments

**Note on seniority**
Level is not a hard gate — seniority varies significantly across companies and the same title can mean different things. Flag (don't auto-exclude) roles where people management is listed but craft responsibilities are still substantive and specific. Push back on roles where management, headcount, or executive stakeholder navigation dominate the stated responsibilities.

## Entry audit process

When a new JD is submitted for addition, always perform an independent audit before writing to `jobs.json`. Do not trust pre-assigned clusters or signals — derive them from the JD text directly.

**Step 1 — Read the raw JD**
Identify every stated responsibility, skill requirement, and process expectation. Flag anything ambiguous.

**Step 2 — Map against existing clusters and signals**
For each finding, check whether it maps to an existing cluster or signal key in `jobs.json`. Assign only those that are explicitly grounded in the JD text. Do not assign a cluster or signal because it "probably applies."

**Step 3 — Flag potential new additions**
If a finding does not map to any existing cluster or signal, flag it explicitly before writing the entry. Do not silently add new keys.

**Step 4 — Backcheck before creating anything new**
Before proposing a new cluster or signal key, scan all existing entries to see if the pattern appears elsewhere. A new grouping requires evidence across multiple JDs, not a single instance. The bar is: would a second reader independently notice this as a distinct, recurring pattern? If only one JD shows it, note it in the audit but do not create a new key — revisit when a second example appears.

**Step 5 — Report the audit**
Before writing the entry, summarize: which clusters and signals were assigned and why, and whether anything was flagged as a potential new addition. Wait for confirmation if a new key is being proposed.

**Step 6 — Update metadata and sitemap after writing**
After writing the entry to `jobs.json`, always update all three of the following in the same pass:
- `meta.totalEntries` in `jobs.json`
- `meta.lastUpdated` in `jobs.json`
- `<lastmod>` in `docs/sitemap.xml`

All three must stay in sync. Never write an entry without completing this step.

## Quote field

Each entry may include an optional `quote` field — a direct excerpt from the JD that anchors the cluster and signal assignments. Rules:

- Must be a verbatim quote from the JD. Do not paraphrase or edit.
- Choose the line or sentence that most clearly justifies the clusters and signals assigned.
- If no single excerpt is definitive, leave the field null rather than stitching sentences together.
- The field is optional. Omit it (or set to null) if no suitable quote exists.
