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
- The role is primarily content marketing or editorial production, and its systems or AI responsibilities are thin — the systems language is doing the work of a title rather than describing the job
- The role has no meaningful connection to product, platform, or language infrastructure
- The JD is too generic to yield distinct cluster or signal assignments

**Note on marketing-sited roles**
Sitting in a marketing or editorial function is not disqualifying on its own.
Where the JD's systems or AI responsibilities are substantive and specific,
include the role and assign `content-marketing-adjacent`. Content design and
content strategy straddle marketing and product, and where that boundary
falls is one of the things the dataset tracks — excluding every role on the
marketing side of it would discard the evidence for it. Exclude when the
systems framing is not backed by stated responsibilities; tag, don't exclude,
when it is.

**Note on seniority**
Level is not a hard gate — seniority varies significantly across companies and the same title can mean different things. Flag (don't auto-exclude) roles where people management is listed but craft responsibilities are still substantive and specific. Push back on roles where management, headcount, or executive stakeholder navigation dominate the stated responsibilities.

**Note on rejected roles**
A JD that fails these criteria is still worth archiving. Write it to
`jd-source/{id}.md` with `excluded` and `excludedReason` set, as described in
`jd-source/README.md`, so the reasoning survives and the same posting is not
re-audited from scratch or quietly added later. Nothing is written to
`jobs.json` for a rejected role.

If a submitted JD has no matching entry in `jobs.json`, do not assume it is
being added. Say so and ask whether it was rejected and should be archived as
excluded, or was submitted in error.

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

**Step 6 — Archive the source text and update metadata after writing**
After writing the entry to `jobs.json`, always complete all six of the following
in the same pass:
- write the raw JD text to `jd-source/{id}.md`, following the file format in `jd-source/README.md`
- `meta.totalEntries` in `jobs.json`
- `meta.lastUpdated` in `jobs.json`
- `<lastmod>` in `docs/sitemap.xml`
- the entry count and date in the "What this dataset tracks" section of `docs/llms.txt`
- the citation date in the "How to cite this work" section of `docs/llms.txt`

All six must stay in sync. Never write an entry without completing this step.
The same applies when an entry is removed, not only when one is added.

The archive is the JD text as submitted, stored verbatim — no cleanup,
reformatting, or truncation, including any job-board chrome around the posting.
It is what Step 1 was read from, and what a later Step 4 backcheck reads when
scanning for a recurring pattern that has no cluster or signal key yet.

Before committing, confirm the entry's `quote` appears in the archived text.
A mismatch beyond the two permitted normalizations is a discrepancy to resolve,
not a formatting detail — the quote is wrong, or the archived text is not the
posting the entry was audited from.

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

**Loading, empty, and error states**
See `copy-patterns.md` for the rules and current copy. Strings live in the `COPY`
object at the top of `docs/js/scripts.js` — add or change them there, not inline
in a render function.

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

- Must be a verbatim quote from the JD. Do not paraphrase, reword, condense, or change meaning.
- Three typographic normalizations are permitted, and nothing else:
  - capitalizing the first letter, when the excerpt is lifted from mid-sentence and needs to read as a standalone sentence
  - adding spaces around an em dash
  - adding a terminal period, when the excerpt is lifted from a list item that carries no terminal punctuation of its own

  Never normalize to make a quote sound stronger, cleaner, or more on-message than the source. These three cannot change what a quote says; anything that can is paraphrase, not normalization.
- Choose the line or sentence that most clearly justifies the clusters and signals assigned.
- Prefer a line legible to a general content design reader over one dense with employer-specific jargon — acronyms, internal system names, team names. The quote must still ground the assigned clusters and signals; legibility breaks ties among lines that do, it does not override grounding. If the only line that grounds an assignment is unavoidably jargon-heavy, keep it and reconsider whether the assignment is well grounded.
- If no single excerpt is definitive, leave the field null rather than stitching sentences together.
- The field is optional. Omit it (or set to null) if no suitable quote exists.
