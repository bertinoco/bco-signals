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

Figures below are as of **29 entries, 2026-08-05**. They move. Regenerate
`stats.md` before quoting any of them.

---

## Content standards are being pulled into central functions

**What the data shows.** Eight of 29 postings describe content standards owned
by one central or horizontal function, with distributed teams consuming them:
Adobe, Ally, JPMorgan Chase, LinkedIn, Meta (twice), Netflix, OpenAI. Seven
companies, six industries. They describe it in their own words rather than a shared
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

The 11 postings that omit it are not the ones you would guess. Whether a
content role involves AI does not track whether the employer builds AI. Two
excluded records are AI companies posting content roles with no AI in the work
at all: Google's YouTube Staff UX Content Designer, rejected because the JD
contains no occurrence of *ai, llm, model, generative, automation, machine
learning, agent* or *prompt*; and Nscale, which sells AI infrastructure and
posted for website copy, a style guide, and page-level information
architecture. Inside the dataset, LinkedIn's Staff Content Architect and
Netflix's Staff Content Designer, NCXD carry no AI cluster or signal either.

It runs the other way too. AI fluency is stated by a carmaker (GM), a meal-kit
company (HelloFresh), three fintechs (Sanna, Wealthsimple, Chime), a
consultancy (Accenture) and a rideshare platform (The Ride Platform).

**What I think it means.** The interesting thing is where it sits in the
postings — alongside portfolio requirements, in minimum qualifications, not in
a "nice to have" list. Two years ago this would have been a differentiator. It
now reads the way "proficiency in Figma" reads.

The counter-cases say something the headline number hides. AI in a content role
is a fact about the content function, not about the employer's product. An AI
infrastructure company can hire a content designer to write landing pages, and
a meal-kit company can require daily use of Claude Code. So "do they work on
AI?" is the wrong question to ask about a prospective employer. The one that
predicts the job is whether the content function has been given a systems
mandate — and that is visible in the posting, in whether the responsibilities
describe building mechanisms or producing pages.

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

**What the data shows.** 23 of 29 postings state where the role sits, and the
placements do not cluster in design. HelloFresh files its Staff AI Content
Designer under "Category: Software Engineering". Ally's Content Architect sits
in "Career area: Marketing". Notion's is in Customer Experience; LinkedIn's in
a Knowledge Management Solutions team under a department called GBO. Adobe's is
tagged to two categories at once — Design, and Engineering and Product.

Five postings sit in marketing or editorial functions while describing
substantive systems work: CoLab, Insurify, The Ride Platform, Ally, and Meta's
AI Content Strategy Lead, which sits in Business Marketing.

**What I think it means.** The discipline is being claimed by several
functions at once, and none of them has won. This is the most under-discussed
finding in the set — the conversation about content design's future tends to
assume it stays in design. The postings do not.

---

# Watching

Patterns with real evidence that have not been given a taxonomy key, recorded
so they are not rediscovered from scratch. Entries stay here after a key is
created, marked resolved, so the reasoning survives the promotion. Step 4's bar still applies: a new
instance updates a count, it does not promote a pattern to a finding.

**Measurement and evaluation frameworks — 12 instances.** OpenAI (evals,
evaluation rubrics), Netflix and Spotify (evaluation frameworks), Meta
(measurement frameworks, twice — the AI Content Strategy Lead states both
evaluation frameworks and business-impact measurement), LinkedIn (architecture health metrics), GM and Notion
(content QA), Ride Platform (success metrics), Chime (content quality metrics,
automated governance dashboards), Ally (success metrics and measurement
frameworks). The largest un-keyed pattern in the corpus. Held because it
overlaps `governance-as-value-prop` heavily and cannot yet be separated
cleanly.

The entry below suggests the separator: whether the measurement is executable.
A framework reported on quarterly is governance. An eval suite that runs
against a model and gates a release is engineering. The postings use the same
vocabulary for both, which is why the pattern will not split on wording alone.
*Trigger to revisit: a posting that states measurement running against system
output on a cadence the system sets — evals, regression suites, automated
scoring — rather than measurement reported to stakeholders.*

**Content built for machine consumption — resolved into `agent-retrieval`,
2026-08-05.** This entry named Notion and Spotify as the residue carrying
neither `geo-seo` nor `structured-data`, and set the trigger at a third such
instance. Checking that claim against the entries showed it was wrong: neither
Spotify posting is a retrieval case. The Annotation Manager is ML training data
(`classification-for-ml`) and the Conversation Designer is conversation design
(`model-behavior-design`). The residue was Notion alone.

Meta's AI Content Strategy Lead is therefore the second instance, not the
third — Notion's "so the right people (and the right agents) can retrieve the
right information at the right time" beside Meta's "for real-time access by AI
agents and content generation systems." Two companies, two industries, the same
structural move: a knowledge substrate a model reads from at generation time,
distinct from public search, from schema markup, and from training data.

Keyed at two instances rather than three, which is the floor of Step 4's bar
and not comfortably past it. If a third does not appear, this is the one to
revisit and consider folding back.

**Deterministic and generative content work are separating — and only one
side is visible here.**

*Source note.* This entry draws on practitioner testimony from a public
professional-network thread, not on postings. It is a reliable industry
channel and the participants describe roles they hold rather than roles they
want filled, which makes it more direct than a JD and less checkable: nothing
in it can be verified the way archived posting text can. It grounds no cluster
or signal assignment, and it is recorded here because it names a distinction
the dataset lacks a word for. Participants are not named. One claim in the
thread — about layoffs at a specific employer — is omitted as unverifiable and
not load-bearing.

*The vocabulary.* The thread's author, working solo across both, splits the
work into "deterministic UX writing, in close collaboration with product
designers" and "model design (shaping system instructions and LLJ in the
codebase with eng/ML teams)". **Deterministic** is the useful word. It and its
counterpart **generative** are defined under Vocabulary in CLAUDE.md, which is
where the pairing is maintained. Deterministic content work authors the artifact: you
write the string, the string ships, the user sees that string every time, and
review means reading it. Generative content work authors the constraints on a
generator and the criteria for judging what it emits. The output varies per
invocation and most of it is never read by its author.

That reframes the shift. It is not AI versus no-AI, and not upstream versus
downstream. It is artifact-authoring versus spec-and-test-authoring — and it
explains why evaluation appears the moment model design does. Once output is
probabilistic, quality cannot be checked by reading, so measurement stops
being a governance byproduct and becomes the only available instrument.

*Two moves get conflated.* Both read as "technical content work" and they are
different jobs.

- **Enforcement.** Content moves into the repository. Strings become YAML or
  JSON, changes become pull requests, style rules become lint rules that fail
  a build. Still fully deterministic — the artifact has relocated and gained
  automated checking. The demanding part is that a rule must become
  falsifiable: guidance that cannot be expressed as a check is either genuinely
  contextual or was never a rule.
- **Specification.** The generator's behavior is authored instead of the
  output — system instructions, retrieval context, guardrails — and an eval
  harness with model-graded rubrics reports whether it worked. The rubric is
  the editorial standard written as a prompt and executed at scale.

*What the corpus can see.* Model behavior shaping is keyed at six entries.
Evals are named twice: OpenAI's "prompt creation, model-generated content,
AI-assisted workflows, evals, quality rubrics" and Spotify's "writing and
running evaluations". Structured formats twice: Spotify's "JSON, YAML, Python"
and Netflix's "how those rules map to a JSON schema, metadata pipeline, or
platform component". Working in code three times: Spotify's "comfortable
working directly with LLMs and code", Wealthsimple's "shipping your own code
changes", Figma's "design and technical environments, like Figma and GitHub".
Spotify's Senior Conversation Designer is the only posting spanning nearly the
whole picture, and it is from May.

*What it cannot.* Lint rules: one near-match, GM's "linting engines", and that
is adopting a purchased tool rather than authoring rules. LLM-as-judge: zero —
every "judge" string in the corpus is "judgment". The two artifacts
practitioners name most specifically are the two no posting asks for.

*What I think it means.* The gap is a fact about the method, not about the
practice. The testimony describes content designers at a large technology
employer pivoting into building lint rules and YAML to catch content issues at
the code source — a role that changed inside an existing org, with no new
requisition. A dataset built from job postings cannot see role change that
happens without a hiring event, and this is the clearest instance of that
limit in the corpus. Expect the postings to lag this by some margin.

*Trigger to revisit: a posting that names an eval harness, model-graded
rubrics, or authored lint rules as a stated responsibility rather than as tool
familiarity.* Two would justify separating the practice from
`model-behavior-design`, which currently covers both writing a system
instruction and building the harness that tests it.

*A posting-based instance, not just testimony — excluded.* Fin's "Staff AI
Designer" (page header; the body calls itself "Staff AI Product Designer"
throughout) was excluded from the dataset: no occurrence of *content,
writing, copy, language, tone, voice,* or *terminology* anywhere in the text,
which fails the required content-discipline criterion outright. But most of
its stated responsibilities — "Define what AI should do—and just as
importantly, what it should not do," "Establish decision frameworks: when
systems should act, ask, escalate, or defer," "Define what 'good' looks
like... Design evaluation scenarios and feedback loops" — read as the
specification side of the deterministic/generative split: authoring a
generator's constraints and judging criteria, not an artifact. The
maintainer's read is that, apart from "Deep understanding of LLMs and their
limitations, along with a grounding in traditional ML approaches" and "You
will not be training models or building ML infrastructure" (the two lines
that place this closer to an ML-adjacent product discipline than to content
work), the posting could pass for a generative-focused content design role
in different vocabulary. That reframing is the maintainer's own, not a claim
the posting makes — Fin never uses content-design language, and the posting
was excluded on exactly that absence. Recorded because it is the first
JD-based instance of the "model design" side of the split, where the source
note above draws only on practitioner testimony. One instance; a second
similarly language-free posting would be the one to compare it against.

*The second instance is not language-free — it is the opposite case, and it
was admitted.* Wise's Principal AI Model Designer, posted days after Fin, is
titled for the same discipline but states its own continuity with content
design rather than omitting the connection: "This role will sit within the
Content Design Guild as part of our Design team, as the disciplines share a
common skill set and design process," and, load-bearing for the entry's
inclusion, "You're an accomplished and experienced Model Designer, or a
systems-focused Content Designer who has already made this transition in
your day-to-day work." That sentence treats Model Designer and Content
Designer as two entry paths into one role, which is a first-party claim of
skill continuity, not just shared reporting lines — the reason the entry was
admitted where Fin, with the same category of day-to-day work, was not.

This is the clearest confirmation the corpus has that the practitioner
testimony's split is materializing in live postings, not only in how
individual practitioners describe their own work: a title change ("Model
Designer") arriving before the reporting line does ("Content Design Guild").
Two companies, two instances, in opposite configurations — one excluded for
naming no content discipline at all, one included for naming the transition
explicitly — which is itself the finding: the shift is real, and it is
surfacing under new titles inside old org charts before it reorganizes them.
Still two data points. The trigger from the Fin entry (a second
language-free posting) is still open and separate from this one; the
trigger to revisit here is a second posting that, like Wise's, names the
Model-Designer-or-transitioning-Content-Designer path explicitly rather than
implying it through guild placement alone.

**`content-marketing-adjacent` description versus use.** The description reads
"systems and architecture language is being used to describe what is
fundamentally content marketing work… the core responsibilities haven't
shifted." All five holders contradict it — CoLab, Insurify, Ride Platform, Ally
and Meta were each admitted *because* their systems responsibilities were
substantive, and CLAUDE.md's marketing-sited note instructs assigning the key
on placement rather than on hollowness. The key is doing one job and its
description claims another. Noted rather than rewritten, because the
description is user-facing card copy.

**`ai-native-expectation` label versus description.** The label reads "AI
fluency expected", broad enough to cover roles that optimize content *for* AI
consumption. The description narrows it to "actively working with AI tools",
and all 18 assignments follow the narrow reading. Ally was declined on that
basis. Left alone deliberately; noted because the gap makes the call look
arbitrary from the label alone.

**`ai-tooling` description versus use.** The description reads "Building and
operationalizing AI-powered workflows... goes beyond using AI tools...
evaluate, configure, and own the workflow end to end" — a content-production
automation frame. Spotify's Senior Conversation Designer already carries the
key for the other kind of work: prompt engineering, model behavior guardrails,
and evaluation frameworks for a conversational AI product, not a content
workflow. Gen Digital's Staff AI Conversation Designer reinforces it —
prompt structures, model persona and tone, and behavioral standards for an
agentic AI Assistant, with no content-production workflow described anywhere
in the posting. Two entries now use the key for AI-behavior and model-design
ownership rather than the workflow-automation frame the description states.
Noted rather than rewritten, same as the two entries above — the description
is user-facing card copy.

**A dedicated single-discipline title for taxonomy work — one instance.**
15 entries carry the `taxonomy` cluster, and in 14 of them taxonomy is one
responsibility folded into a broader content-design, architecture, or
strategy title: Wellhub's "Senior Global UX Writer, Content Systems", LinkedIn's
"Staff Content Architect", Ally's "Content Architect", and so on. Meta's
Taxonomist, Content Design is the first title in the corpus that names the
discipline itself rather than a content role that happens to include it.
First instance, so it stays here rather than becoming a key or a finding.
*Trigger to revisit: a second posting titled for the classification
discipline on its own — Taxonomist, Ontologist, Information Architect — rather
than for a content role with taxonomy folded in.*

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
15 landed in May, nine of them on a single day.

**`dateAdded` is not a posting date.** Where both are known the gap runs from
zero to sixty-six days. Any claim about change over time needs `postedDate`,
which only a minority of postings state.

**It cannot see role change without a hiring event.** Every entry exists
because someone opened a requisition. Work that arrives by internal pivot —
an existing team taking on new responsibilities under unchanged titles —
produces no posting and leaves no trace here. Practitioner testimony says this
is how at least some codebase-level content work arrived. Treat the absence of
a responsibility from the corpus as evidence about what employers advertise,
never as evidence about what practitioners do.

**Excluded records prove existence, not rate.** The AI fluency finding cites
two postings that were never admitted to the dataset — YouTube and Nscale — to
show that AI companies do post content roles with no AI in the work. That is a
fair use of them: an existence claim needs one instance and survives the
selection filter, because a rejected posting was still read in full. It does
not license a rate. Nothing here supports "x% of AI companies do this", since
excluded postings are archived only when someone happened to submit one.

**Taxonomy keys understate their own frequency.** A key created in July was not
retroactively applied to entries audited in May unless someone went back —
`accessibility-as-constraint` was missing from Phase2 for exactly this reason
until it was caught. Frequency counts are a floor, not a measurement.
