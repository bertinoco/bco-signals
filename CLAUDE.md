# BCO Signals — Claude Instructions

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

Some keys have a documented gap between their user-facing label/description
and how they've actually been assigned across the corpus — see
`jd-insights/findings.md`'s "description versus use" notes (currently
`content-marketing-adjacent`, `ai-native-expectation`, `ai-tooling`). For
these, resolve the assignment against the documented pattern of actual use,
not the literal wording of the description — read the note and the entries it
cites before deciding. This is not a judgment call to bring to the user each
time; decide it directly from precedent, and only flag if the JD in front of
you doesn't fit the pattern the note already describes.

**Step 3 — Flag potential new additions**
If a finding does not map to any existing cluster or signal, flag it explicitly before writing the entry. Do not silently add new keys.

**Step 4 — Backcheck before creating anything new**
Before proposing a new cluster or signal key, scan all existing entries to see if the pattern appears elsewhere. A new grouping requires evidence across multiple JDs, not a single instance. The bar is: would a second reader independently notice this as a distinct, recurring pattern? If only one JD shows it, note it in the audit but do not create a new key — revisit when a second example appears.

Distinct companies are not the whole test. Two employers can still be drawing
from the same well — shared industry conventions, recruiter language, or
competitive pressure to match a rival's posting — so recurrence confined to
one `domain` is weaker evidence of a discipline-wide shift than recurrence
across domains. When backchecking a candidate key, note each instance's
`domain` alongside its company. A key can still be created at the 2-instance
floor even if every instance shares a domain — this does not raise the
floor — but flag it as domain-clustered rather than confirmed cross-industry,
and record the trigger to revisit: a differently-domained instance. This is a
check for new signal proposals going forward, not a retroactive test — it
does not reopen or gate keys already created.

**Step 5 — Report the audit**
Before writing the entry, summarize: which clusters and signals were assigned and why, and whether anything was flagged as a potential new addition. Wait for confirmation if a new key is being proposed.

Report the title too, quoted exactly as the posting words it. If it carries a
separator, say which one and what it will render as under the Title field rule —
`Content Strategist | Agentic Commerce` stored, `Content Strategist, Agentic
Commerce` rendered. A separator matching neither rule is the user's call, not
something to settle by widening the rule.

**Step 6 — Archive the source text and update metadata after writing**
After writing the entry to `jobs.json`, always complete all seven of the
following in the same pass:
- write the raw JD text to `jd-source/{id}.md`, following the file format in `jd-source/README.md`
- `meta.totalEntries` in `jobs.json`
- `meta.lastUpdated` in `jobs.json`
- `<lastmod>` in `docs/sitemap.xml`
- the entry count and date in the "What this dataset tracks" section of `docs/llms.txt`
- the citation date in the "How to cite this work" section of `docs/llms.txt`
- run `python3 jd-insights/refresh.py`, which regenerates `jd-insights/stats.md` and `jd-insights/quotes.md`

All seven must stay in sync. Never write an entry without completing this step.
The same applies when an entry is removed, not only when one is added.

Then check, but only update if the entry warrants it:

- `jd-insights/patterns.md` — add an observation when the posting does something
  notable in how it is written: a rhetorical device, boilerplate reuse, jargon,
  a formatting artifact, an unusual way of stating compensation. Most entries
  add nothing. Name the company so a reader can check it against the archive.
- `jd-insights/findings.md` — rarely. A new instance of a known pattern updates
  a count, it does not promote a pattern to a finding or make an existing
  finding newsworthy again. Step 4's bar applies here too. If the entry is a
  first instance of something with no key, add it to the Watching section
  rather than writing a finding.

The archive is the JD text as submitted, stored verbatim — no cleanup,
reformatting, or truncation, including any job-board chrome around the posting.
It is what Step 1 was read from, and what a later Step 4 backcheck reads when
scanning for a recurring pattern that has no cluster or signal key yet.

Before committing, confirm two things against the archived text.

The entry's `quote` appears in it. A mismatch beyond the three permitted
normalizations is a discrepancy to resolve, not a formatting detail — the quote
is wrong, or the archived text is not the posting the entry was audited from.

The entry's `title` matches the posting verbatim, separator included. Check the
stored value, never the rendered one: the site normalizes separators at render,
so the two are expected to differ and a title that matches the site is the one
to worry about. The title is what links an entry to its archive, so a tidied
title breaks that link silently.

**Step 7 — Commit, push, and merge**
Once the user confirms the audit (including any new cluster/signal/domain proposal), that confirmation also counts as approval to merge directly to `main` — no separate merge confirmation is needed for JD entry additions specifically. Commit the entry on the working branch, push it, then merge directly to `main` and push. This does not extend to other kinds of changes (site code, design, CLAUDE.md itself, etc.) — those still follow normal confirm-before-merge practice.

## Spelling standard

US English is the base for everything owned and created by us in this
repo — site copy, `jd-insights/` prose, `CLAUDE.md` itself, commit messages,
and any other writing that isn't a verbatim excerpt from a source JD.

This does not touch JD text. A UK-English (or any other regional) JD is
quoted, titled, and archived verbatim, per the Quote and Title field rules —
those fields are never normalized toward US spelling. The base applies only
to language we author ourselves.

## Voice & copy decisions

These rules apply to all user-facing copy on signals.bertino.co: card descriptions, section intros, header copy, and any editorial text rendered in the browser — except the hero, which is scoped out below.

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

**Brand copy exception**
The hero headline and pull-quote in `docs/index.html`, and the opening
pitch in `README.md`, are brand assets, not data reporting — the argument
for why the dataset exists, not a claim the dataset backs number-for-number.
They may state an industry-level trend and be more overtly persuasive than
anything else on the site, including projections and claims broader than
what a single dataset can prove on its own. This is the only copy on the
site exempted from the no-projections and no-overpromising rules above.

Keep this exception narrow. It covers only that headline/pull-quote and
that pitch — nowhere else. Section intros, card descriptions (beyond the
light editorializing already permitted above), cluster/signal text, JD
entries, and quotes all stay reportorial and grounded, no exceptions.

**Loading, empty, and error states**
See `copy-patterns.md` for the rules and current copy. Strings live in the `COPY`
object at the top of `docs/js/scripts.js` — add or change them there, not inline
in a render function.

## Domain field

The `domain` field describes the broad industry or sector the company operates in. It is a reusable taxonomy value — not a role-specific descriptor.

**Rules**
- Prefer a single word. No slashes, no parentheticals: `Finance`, not `Financial services / fintech` or `Fintech (accounting)`.
- Broad enough to apply across related companies and JDs. If a second JD from a similar company would use the same value, that's the right level of specificity.
- Err generic. A value that groups several companies is doing its job; a value with one entry usually means the taxonomy is tracking the company rather than the sector.
- Check existing values before creating a new one. Reuse where the fit is clear.

**Current taxonomy**

| Value | Example companies |
|---|---|
| `Agency` | Phase2, Accenture |
| `Automotive` | GM |
| `Big Tech` | Apple, Google, Meta, LinkedIn, OpenAI |
| `Cybersecurity` | Gen Digital (Norton, Avast) |
| `E-commerce` | HelloFresh, Wellhub, The Ride Platform |
| `Finance` | JPMorgan Chase, Ally, Sanna, Wealthsimple, Chime, Insurify |
| `Government` | Government Digital Service |
| `Healthcare` | Atria, UnitedHealth Group |
| `Logistics` | Relay |
| `Media` | Netflix, Spotify |
| `SaaS` | Notion, Zoom, Figma, CoLab |

If a new company doesn't fit any existing value, propose the new domain before writing the entry. New domains should be broad enough to accommodate at least two companies.

## Remote field

`remote` records what the JD states about work location, read off the text
directly rather than inferred from the company or role.

- `true` — the JD states the role is remote, with no fixed in-office
  requirement.
- `false` — the JD states the role is on-site, with no remote option.
- `"hybrid"` — the JD states a mixed arrangement: some days in the office,
  some remote (e.g. "3 days at the office/2 days at home"). Not rendered on
  the site (`remote` is data-only, like `domain`), so a string value here
  doesn't affect the page, only the dataset. Evinova's Content Design Lead
  is the entry `"hybrid"` was added for — `false` would have overstated the
  on-site requirement, and `true` would have understated it.
- `null` — the JD does not say. Use this rather than guessing from location
  or company norms.

## Comp range field

`compRange` is optional. When present it carries the stated range plus three
structured fields. Nothing about the range is inferred from prose at render
time — the display reads these fields directly, so they must be right.

```json
"compRange": {
  "min": 460000,
  "max": 710000,
  "currency": "USD",
  "covers": "total",
  "scope": null,
  "extras": null
}
```

**`covers`** — what the range measures. One of:

- `"base"` — the JD states this is base salary or base pay.
- `"total"` — the JD states the range is the whole package. Netflix is the
  current example: "our compensation structure consists solely of an annual
  salary; we do not have bonuses. You choose each year how much of your
  compensation you want in salary versus stock options."
- `null` — the JD does not say. Use this rather than assuming base. Zoom
  labels its range "Salary Range or On Target Earnings" and HelloFresh says
  only "Pay Range"; neither commits, so neither entry does either.

Only `"total"` is displayed, because a total-comp figure is not comparable to
the base ranges beside it. `"base"` and `null` show nothing — a bare number
claims no more than the JD did.

**`scope`** — the location the range is tied to, when it is narrower than the
posting itself: `"New York, NY"`, `"Illinois"`, `"Toronto, ON"`. Use `null`
when the range applies to the whole posting. A country-wide qualifier like
"US locations" is not a scope.

Recorded always; never displayed on the Roles tab. Location strings wrap and
extend the card at narrow widths, so `scope` stays in `jobs.json` as data only.

**`extras`** — what sits on top of the range: `"bonus + equity"`,
`"annual incentive plan"`. Recorded because the JD states it, never displayed.
It is not part of the number, so showing it beside the number only invites the
reader to add it in.

**Rules**

- Read all three off the JD text, not off the company's reputation.
- If the JD does not state whether the range is base or total, `covers` is
  `null`. Do not resolve the ambiguity.
- `extras` records what the JD lists as additional, not what the company is
  assumed to offer. Benefits and health coverage are not extras.
- Where an entry has no `jd-source` archive, these fields cannot be verified.
  Archive the posting first.
- When a JD lists separate ranges for multiple co-equal locations with no
  single primary location, use the range for the largest city among them by
  population, and set `scope` to that city.

## Title field

`title` is stored verbatim, exactly as the posting words it. It is the field
that ties an entry back to its `jd-source` archive, so it is never edited to
tidy it up.

Separators are normalised for display only, in `formatTitle` in
`docs/js/scripts.js`. The site and `jobs.json` are therefore expected to differ
on some entries. **Do not "correct" a title in `jobs.json` to match what the
site renders** — that breaks the link to the archive.

**What normalises**

Em dash, en dash, pipe, and a *spaced* hyphen all join a role to its scope, which is what a comma does:

- `Annotation Manager — Content Platform` renders as `Annotation Manager, Content Platform`
- `Content Strategist | Agentic Commerce` renders as `Content Strategist, Agentic Commerce`
- `Lead Conversational Designer - Agentic Experiences` renders as `Lead Conversational Designer, Agentic Experiences`

`formatTitle`'s regex already covers all four the same way, keyed on the
surrounding whitespace rather than which dash character is used — a hyphen
with a space on both sides is a separator; one with no space on either side
is a compound (see below). UKG's Lead Conversational Designer entry is the
first title using a spaced hyphen rather than an em dash or pipe; it needed
no code change, only this note, since the existing regex already matched it
correctly.

**What does not**

- A forward slash joins two titles naming one role — Zoom's
  `AI Information Architect / Content Strategist` is both titles for the same
  job, not a role plus a team. A comma would read as scope, so the slash stays.
- Unspaced hyphens are compounds, not separators. `AI-Powered Content Systems
  Specialist` renders unchanged.

If a new posting uses a separator that fits neither case, leave the title
verbatim and raise it rather than widening the rule.

**Non-English JDs.** The same verbatim principle applies: a Chinese posting's
`title` is Chinese text, unaltered, unless translated under the exception
below. Silently storing an English gloss would break the same tie back to the
archive this field exists to protect.

The one exception, mirroring the Quote field's non-English exception: `title`
may hold an English translation instead of the verbatim original when
`titleTranslatedFrom` is also set to the source language — and only then. The
site renders that field as a visible caption under the title, the same
mechanism `quote` uses. Set `titleTranslatedFrom` only when `title` is
actually a translation; leave both fields alone for English-language JDs. The
archived source's own front-matter `title:` field records the posting's
actual title in its original language regardless of what `jobs.json`
stores — this exception touches the `jobs.json` field only, never the
archive.

Before committing (Step 6), confirm the original-language title actually
appears in the archived source text, the same way a translated `quote` is
checked against its original-language sentence rather than a literal string
match.

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

  This rule was missed once: Bolt.new's Staff Content Designer entry initially
  used "You're the design DRI, in Figma or with agentic tools, through to
  shipped." DRI (Directly Responsible Individual) is never defined anywhere in
  the JD — a reader outside Bolt has no way to resolve it. The posting had an
  equally strong, jargon-free line available in the same paragraph family
  ("You can take a content-led feature from problem to shipped without a
  product designer. That means designing it in Figma, or building it with
  agentic tools, to a standard we'd actually ship.") that grounds the same
  assignments without the acronym. Read a candidate quote as a first-time
  visitor would — an unglossed acronym or internal term is a legibility
  failure even when the surrounding sentence is otherwise clear, and is worth
  checking for specifically before treating a quote as settled.
- If no single excerpt is definitive, leave the field null rather than stitching sentences together.
- The field is optional. Omit it (or set to null) if no suitable quote exists.

**Non-English JDs.** "Verbatim" means the original language — a Korean JD's
`quote` is Korean text, unaltered, same as an English JD's `quote` is English
text, unaltered. A translation is a rewording, not a normalization, so it
never substitutes for the verbatim excerpt silently.

The one exception: `quote` may hold an English translation instead of the
verbatim original when `quoteTranslatedFrom` is also set to the source
language (e.g. `"Korean"`) — and only then. The site renders that field as a
visible caption under the quote, so a reader never mistakes a translation for
verbatim source text the way they would if the two were indistinguishable.
Set `quoteTranslatedFrom` only when `quote` is actually a translation; leave
both fields alone for English-language JDs. The archived source in
`jd-source/{id}.md` stays in the original language regardless — this
exception touches `quote` only, never the archive.

## Site code

`docs/index.html` loads its assets with a query-string cache-buster:

    <link rel="stylesheet" href="css/styles.css?v=N">
    <script src="js/scripts.js?v=N"></script>

Read `index.html` for the current numbers. They are not reproduced here,
because a version written into this file goes stale the next time an asset
changes and then reads as the value to restore.

Browsers cache those files against that string. A change to `scripts.js` or
`styles.css` that does not bump the matching `?v=` number ships to nobody —
visitors keep running the previously cached version, and the deployed site
silently disagrees with the repo.

Bump the version in the same commit as the change. Never bump one asset's
version to publish a change to the other; they are cached independently.

`index.html` carries no version string of its own, so a change to it is not
gated behind a bump the way the assets are. Some state copy exists twice — as
static markup in `index.html` and as a string in the `COPY` object in
`scripts.js`. Changing one is a reason to check the other, in both directions. A missed bump on a shared string is worse than a
missed bump elsewhere: instead of shipping nothing, the page paints the new
copy from the HTML and the cached script replaces it with the old.

To check whether an asset is in sync, compare the commit that last touched it
against the commit that last set its version:

    git log -1 --format='%h %s' -- docs/js/scripts.js
    git log -G'scripts\.js\?v=' -1 --format='%h %s' -- docs/index.html

If the first is newer than the second, the change has not shipped. Use `-G`,
not `-S`: a bump does not change how many times `scripts.js?v=` appears in the
file, so `-S` matches only the commit that first added the line.

This has now been missed twice.

- `?v=4` was set in `abc7714`, `scripts.js` changed afterwards in `f149926`,
  and the footer went on rendering a date format the source had already
  stopped producing.
- `?v=16` was set in `c1bce75`. `b628392` rewrote all ten strings in the
  `COPY` object without bumping it, and `c00fd9f` then changed the same
  loading string in `index.html`. The page painted "Loading…" from the markup
  and the cached script re-rendered the slot as "Loading the dataset…".
  Fixed in `d7f9113`.

## Design tokens

`--radius` and `--radius-sm` cover small controls — buttons, chips, inputs.
`--radius-lg` (20px) is for panel-scale surfaces, currently just the
flip-card overlay. Reach for it instead of a hardcoded radius value when a
new surface needs rounding at that scale, and add a new token rather than
repeating a raw number if a third scale turns out to be needed.

Any offscreen measurement used to precompute a layout value — height,
width — must mirror the padding, width, and box-sizing of what actually
renders, not an approximation of it. The flip-card overlay's height was
originally measured against a narrower horizontal padding than
`.flip-card--overlay .flip-card-back` actually applies, so the estimate
came in short. It hadn't visibly clipped anything yet — current entries
still had margin to spare — but a description or roles list one wrap
longer would have clipped silently under `overflow-y: auto`, with no
visible scrollbar to hint at it (macOS renders overlay-style scrollbars).
Fixed by making the probe's padding match the CSS exactly instead of
approximating it.

## Terminology

Two kinds of term live here. Neither is taxonomy: nothing in this section is
a cluster or signal, and nothing here is ever assigned to an entry.

The first kind is words the dataset adopted because it needed one the
postings do not supply — a gap in how the *included* work gets described.

The second kind is words that mark where the dataset's scope ends — vocabulary
from an adjacent discipline whose posting stress-tested the eligibility
criteria and lost, recorded so the next boundary case doesn't have to
re-derive why. See the "Note on rejected roles" for how those postings
themselves get archived; this section is for the *words*, not the postings.

### Words for the work inside scope

**Deterministic**, and its counterpart **generative** — the two sides of what
a content role authors.

Deterministic content work authors the artifact. You write the string, the
string ships, the user sees that string every time, and review means reading
it. Generative content work authors a generator's constraints and the criteria
for judging what it emits: output varies per invocation and most of it is
never read by its author. Use the pair together; neither term carries the
distinction alone.

The term was borrowed from practice, where it appeared as "deterministic UX
writing" set against "model design". It earns its place because the dataset
had no word for the non-generative side, which left every description of the
shift reaching for "AI versus not-AI" — a distinction that turned out not to
track the work, as the AI fluency finding sets out.

**It describes the work; it never ranks it.** Deterministic is not legacy,
lesser, or superseded, and the pairing is not a maturity ladder. Most entries
in the dataset are wholly or partly deterministic. Writing that implies
otherwise breaks the no-value-judgments rule under Data integrity rules, and
outruns the evidence besides — the corpus contains almost no postings that
ask for the generative side by name.

### Words that mark the edge of scope

Terms from Redpine's Senior Knowledge Graph Engineer posting — excluded, but
kept because the posting sounds close enough to what this dataset tracks
that the words separating it are worth having on hand.

**Ontology**, here, means a formal specification of entity types, relations,
and constraints for real-world domain facts — "the entity types, relations,
and constraints that licensed data from each domain maps into." This is not
the same activity as the `taxonomy` cluster, even though both "define types
and relations." `taxonomy` classifies *content* — product copy, UX strings,
support docs — so people or an agent can navigate it; every entry that
carries the cluster has a content deliverable underneath the classification
work. An ontology in Redpine's sense classifies drugs, trials, companies, and
filings: real-world things, not content about them. Same technique, different
object — the distinction Redpine's exclusion turned on.

**Data schema** (or **schema design**) — the structural definition of how
entities and their relations are represented in a database or knowledge
store: field types, constraints, what a record can and can't hold. Distinct
from a content template or a structured-data-for-retrieval responsibility
(which the `agent-retrieval` and `structured-data` signals already track) —
those describe a content professional shaping *content* for machine
consumption. Schema design in Redpine's sense has no content professional
anywhere upstream or downstream; it's the storage layer, not what the
storage holds.

**Knowledge graph** — a graph-structured store of typed entities and named
relations, usually with provenance and a confidence score attached to each
link, built for an agent or planner to traverse and query rather than for a
person to read. Adjacent to what the `agent-retrieval` signal describes in
the abstract ("the knowledge layer a model reads from before it writes"), but
`agent-retrieval`'s three holders are all content professionals restructuring
their own content for retrieval — the discipline stays inside content design.
Building the knowledge graph itself, as infrastructure, is a different job
with no content deliverable in it at all.

**Context engineering**, from Microsoft's Senior Language Engineer posting —
excluded, but the term is worth having on hand because it is a near-miss for
"content engineering," a named technical content discipline in this file's
required criteria, and the two are easy to conflate on a skim. Context
engineering means managing what's fed into an LLM's context window — prompt
design, context window management, the data that steers a model's
response — not structuring content for a product. The Microsoft posting's
responsibilities ("Craft and refine the context and prompts... that steer,
train and evaluate the language models," "Research & implement novel
prompting techniques") are all model-behavior work; nothing in it describes
a content deliverable. Same category of near-miss as Redpine's
"ontology"/`taxonomy` confusability above — different discipline, similar
vocabulary.

**The literal-text check, and why the word list stays short.** Audits of
boundary cases (Fin, Redpine, Notion's Model Behavior Engineer) have used a
fast pre-check: scan the JD for *content, writing, language, copy, tone,
voice,* and *terminology*. A clean zero across all seven is supporting
evidence for exclusion — not the required-criteria test itself, which stays
a qualitative read of the role's primary discipline, but a fast way to
confirm a JD never even gestures at this discipline's own words.

Notion's posting is the reason the list stays this short rather than
growing. It scored a zero on six of the seven, and the seventh — "Be the
voice of quality in the room" — is the idiom ("be the advocate for X"), not
a content/brand-voice usage; reading it in context resolves it as a false
positive, not a hit. The same posting also contains "help write the
playbook" — a stem-match on *writing* that is exactly as idiomatic. A wider
list, or a stemmed match, would not have caught anything real here; it would
have logged a second false positive of the identical kind. The fix was never
a longer list — it's reading each hit in context before it counts, which
Steps 1–4 already require. Widen the list only when a real miss shows up: a
JD that deserved inclusion and would have failed the check outright. None
has yet.

## Insights directory

`jd-insights/` holds what the dataset adds up to — current stats, every stored
quote, observations about how postings are written, and the findings drawn from
them. It sits outside `docs/` so it is not published.

`stats.md` and `quotes.md` are generated by `jd-insights/refresh.py` and must
never be hand-edited; the next run overwrites anything typed into them.
`patterns.md` and `findings.md` are hand-written.

**`findings.md` is the only editorialized file in this repository.** It is the
one place a claim may go beyond what a posting literally states. Two rules keep
that contained:

- Every finding separates what the data shows from what it is taken to mean.
  The first is defensible by citation; the second is opinion and is marked as
  such.
- **This directory reads from the dataset and never into it.** Nothing in
  `jd-insights/` is evidence for a cluster or signal assignment. Assignments
  derive from JD text alone, per Step 2. If a finding appears to justify an
  assignment, the finding has drifted from its evidence — revisit the finding,
  not the entry.

Everything else in the repository stays reportorial, including `patterns.md`,
which describes what postings do without arguing about what it means.
