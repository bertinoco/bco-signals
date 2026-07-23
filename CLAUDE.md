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

**Step 7 — Commit, push, and merge**
Once the user confirms the audit (including any new cluster/signal/domain proposal), that confirmation also counts as approval to merge directly to `main` — no separate merge confirmation is needed for JD entry additions specifically. Commit the entry on the working branch, push it, then merge directly to `main` and push. This does not extend to other kinds of changes (site code, design, CLAUDE.md itself, etc.) — those still follow normal confirm-before-merge practice.

## Voice & copy decisions

These rules apply to all user-facing copy on signals.bertino.co: card descriptions, section intros, header copy, and any editorial text rendered in the browser.

**Who we're writing for**
Content designers, UX writers, and content strategists who want to understand where the discipline is heading. They read closely and notice when copy hedges or generalizes.

**Voice**
Direct. Grounded in data. Lightly opinionated only when the evidence supports it. We're not cheerleading the future of content design — we're reporting what we see and noting what it implies. We speak to the reader as "you." We use "we" when describing our observations or the dataset. Never "I."

**Card description structure**
Signal + implication. State what the data shows, then note what it means for the reader. Two to three sentences is the target. Fragments are acceptable when they add punch.

**Punctuation**
- Em dashes: use sparingly — only when the contrast is sharp enough that a period or comma would soften it too much. Do not use to introduce lists or as a substitute for a period.
- Colons: only when introducing a list. Not as a pivot or lead-in to a clause.
- Fragments: acceptable, especially to land a specific example after a declarative sentence.

**What to avoid**
- Hedging language: "opportunities for improvement," "may suggest," "could indicate"
- Generic consulting tone: "actionable insights," "drive alignment," "at scale" used without specifics
- Overpromising: don't imply the site offers career advice or preparation guidance it doesn't provide
- Value judgments: don't rank roles or label responsibilities as basic or advanced
- Projections: don't predict where the market is heading beyond what the data shows

**Reporting vs. editorializing**
Card descriptions are the one place we editorialize lightly — stating an implication based on evidence. Everywhere else (cluster/signal assignments, JD entries, quotes) stays neutral and reportorial.

## Domain field

The `domain` field describes the broad industry or sector the company operates in. It is a reusable taxonomy value — not a role-specific descriptor.

**Rules**
- No parentheticals. `Fintech`, not `Fintech (accounting)`.
- Broad enough to apply across related companies and JDs. If a second JD from a similar company would use the same value, that's the right level of specificity.
- Keep it short — aim for 30 characters or fewer.
- Check existing values before creating a new one. Reuse where the fit is clear.

**Current taxonomy**

| Value | Example companies |
|---|---|
| `Agency` | Phase2 |
| `AI / technology` | OpenAI, Google |
| `Automotive / connected products` | GM |
| `B2B SaaS` | CoLab |
| `Computer & Electronics` | Apple |
| `Consulting / agency` | Accenture |
| `Design tools / SaaS` | Figma |
| `Financial services` | JPMorgan Chase |
| `Fintech` | Sanna, Insurify, Wealthsimple |
| `Healthcare / longevity` | Atria |
| `Marketplace / mobility` | The Ride Platform |
| `Media / advertising` | YouTube |
| `Media / streaming` | Spotify, Netflix |
| `SaaS / productivity` | Notion |
| `Social media` | Meta, LinkedIn |
| `Wellness / marketplace` | Wellhub |

If a new company doesn't fit any existing value, propose the new domain before writing the entry. New domains should be broad enough to accommodate at least two companies.

## Quote field

Each entry may include an optional `quote` field — a direct excerpt from the JD that anchors the cluster and signal assignments. Rules:

- Must be a verbatim quote from the JD. Do not paraphrase or edit.
- Choose the line or sentence that most clearly justifies the clusters and signals assigned.
- If no single excerpt is definitive, leave the field null rather than stitching sentences together.
- The field is optional. Omit it (or set to null) if no suitable quote exists.
