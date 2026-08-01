# Findings

**This is the only editorialized file in the repository.** Everything else —
`jobs.json`, the site, `jd-source/`, `stats.md`, `quotes.md` — reports what
postings say and nothing more. Here, the reading is allowed.

Two rules keep that contained.

**1. Every finding separates what the data shows from what it is taken to
mean.** The first part you can defend by linking to a posting. The second is a
byline opinion. When lifting a line into something published, know which one
you are holding.

**2. This file reads from the dataset and never into it.** A finding is never
evidence for a cluster or signal assignment. Assignments derive from JD text
alone — that is Step 2 of the audit process and this file does not amend it. If
a finding here seems to justify an assignment, the finding has drifted from its
evidence.

Figures below are as of **29 entries, 2026-08-01**. They move. Regenerate
`stats.md` before quoting any of them.

---

## Content standards are being pulled into central functions

**What the data shows.** Seven of 29 postings describe content standards owned
by one central or horizontal function, with distributed teams consuming them:
Adobe, Ally, JPMorgan Chase, LinkedIn, Meta, Netflix, OpenAI. Seven companies,
six industries. They describe it in their own words rather than a shared
vocabulary — Netflix's "centralized authority" over "a decentralized content
design community", Ally's "sits above channels and formats", LinkedIn's "single
accountable owner", JPMorgan's "partner playbooks and variation guidelines",
OpenAI's "domain playbooks that scale across teams".

Adobe states both sides of the arrangement in one clause: this role is "not
product-level content decisions or UI copy (that lives with embedded product
and domain content teams)."

Wealthsimple is the counter-case, and it is explicit too: "You'll be embedded
on product teams."

**What I think it means.** Content design is being reconstituted as
infrastructure. The embedded model is not dead — Wealthsimple is hiring for it
at staff level — but for the most senior systems work it is no longer the
default. What is emerging looks like the design systems team of ten years ago:
a small central group that owns the primitives, and product teams that consume
them. That has a career implication the postings do not state. The path that
ends in "principal content designer embedded in a product org" now has a fork,
and the other branch ends somewhere closer to platform engineering.

## The work has moved from producing content to producing systems

**What the data shows.** Content systems design appears in 26 of 29 postings
(90%). Enablement — building templates, playbooks, and guidance so other people
can write — appears in 24 (83%). Both are more common than any craft
responsibility.

Several postings say outright that writing is not the job. CoLab: "not by
writing content yourself, but by building AI-powered systems." Ally: "focused
less on creating content and more on making content work." Adobe's role does no
product writing at all.

**What I think it means.** The unit of work is shifting from the artifact to
the mechanism that produces artifacts. This is the same move software went
through when it stopped shipping features by hand and started shipping
platforms — and it arrives with the same uncomfortable implication, which is
that the people who are excellent at the artifact are not automatically the
people who are excellent at the mechanism.

## AI fluency is a baseline, not a differentiator

**What the data shows.** 18 of 29 postings (62%) expect the candidate to
already be working with AI tools — not curious about them. HelloFresh names the
tools: "Active usage of AI as a core part of your daily workflow… building
rapid interactive prototypes (using tools like Claude Code, Gemini, or Figma
AI)." Wealthsimple asks for "shipping your own code changes" via AI.

**What I think it means.** The interesting thing is where it sits in the
postings — alongside portfolio requirements, in minimum qualifications, not in
a "nice to have" list. Two years ago this would have been a differentiator. It
now reads the way "proficiency in Figma" reads, and the roles that omit it are
the more notable ones.

## Nobody agrees what this work is worth

**What the data shows.** Stated ranges run from **$65,000** (Insurify, Editor,
AI Content Systems) to **$710,000** (Netflix, Staff Systems Designer,
Language). Both have "Systems" in the title. 22 of 29 postings state a range.
Adobe alone states two different ranges in one posting depending on location.

**What I think it means.** An order of magnitude between two roles whose titles
would sit next to each other in a search result is not a seniority gap; it is
an absence of consensus about what the discipline is. Titles are not yet
carrying reliable information about scope, which is a problem for anyone trying
to navigate the market by title — and an opportunity for anyone able to
articulate scope precisely in an interview.

## Content roles are appearing outside design orgs

**What the data shows.** 21 of 29 postings state where the role sits, and the
placements do not cluster in design. HelloFresh files its Staff AI Content
Designer under "Category: Software Engineering". Ally's Content Architect sits
in "Career area: Marketing". Notion's is in Customer Experience; LinkedIn's in
a Knowledge Management Solutions team under a department called GBO. Adobe's is
tagged to two categories at once — Design, and Engineering and Product.

Four postings sit in marketing or editorial functions while describing
substantive systems work: CoLab, Insurify, The Ride Platform, Ally.

**What I think it means.** The discipline is being claimed by several
functions at once, and none of them has won. This is the most under-discussed
finding in the set — the conversation about content design's future tends to
assume it stays in design. The postings do not.

---

# Watching

Patterns with real evidence that have not been given a taxonomy key, recorded
so they are not rediscovered from scratch. Step 4's bar still applies: a new
instance updates a count, it does not promote a pattern to a finding.

**Measurement and evaluation frameworks — 11 instances.** OpenAI (evals,
evaluation rubrics), Netflix and Spotify (evaluation frameworks), Meta
(measurement frameworks), LinkedIn (architecture health metrics), GM and Notion
(content QA), Ride Platform (success metrics), Chime (content quality metrics,
automated governance dashboards), Ally (success metrics and measurement
frameworks). The largest un-keyed pattern in the corpus. Held because it
overlaps `governance-as-value-prop` heavily and cannot yet be separated
cleanly. *Trigger to revisit: a posting where measurement is the work rather
than a governance byproduct.*

**Content built for machine consumption — 7 instances.** Ally, Phase2,
LinkedIn, Netflix, Ride Platform, Notion, Spotify. Held because five of the
seven are already covered by `geo-seo` or `structured-data`; a new key would
mostly restate them. The interesting residue is Notion and Spotify, which
describe optimizing for machine retrieval with no search or schema dimension —
Notion's "Optimize the KB for AI retrieval" is internal knowledge retrieval.
*Trigger to revisit: a third instance carrying neither existing key.*

**`ai-native-expectation` label versus description.** The label reads "AI
fluency expected", broad enough to cover roles that optimize content *for* AI
consumption. The description narrows it to "actively working with AI tools",
and all 18 assignments follow the narrow reading. Ally was declined on that
basis. Left alone deliberately; noted because the gap makes the call look
arbitrary from the label alone.

---

# What this data cannot support

Read this before writing anything public.

**It is not a market sample.** Entries are admitted only if they pass a signal
test — novel framing, AI referenced as the work, or a structural shift in
positioning. The dataset is filtered *toward* forward-leaning roles by
construction. It shows what ambitious employers are asking for. It says nothing
about the median content design job.

**n = 29, over about ten weeks.** Enough to notice a pattern across companies.
Not enough for a trend over time, and the entries are unevenly distributed —
16 landed in a single seeding batch in May.

**`dateAdded` is not a posting date.** Where both are known the gap runs from
zero to sixty-six days. Any claim about change over time needs `postedDate`,
which only a minority of postings state.

**Taxonomy keys understate their own frequency.** A key created in July was not
retroactively applied to entries audited in May unless someone went back —
`accessibility-as-constraint` was missing from Phase2 for exactly this reason
until it was caught. Frequency counts are a floor, not a measurement.
