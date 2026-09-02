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

## Titles are failing in both directions at once

**What the data shows.** `title-dilution` (a title claims more systems/AI
substance than the stated responsibilities support) and
`title-responsibility-gap` (the title claims less than the responsibilities
actually cover) each have exactly two holders: `title-dilution` on Insurify's
"Editor, AI Content Systems" and Intercept's "Content Engineer";
`title-responsibility-gap` on Wellhub's "Senior Global UX Writer, Content
Systems" and Figma's "UX Writer, AI" — the latter posting disclaiming its own
title outright, in its second paragraph: "While the title of this role is
'UX Writer,' you might think of yourself as a content engineer as much as a
writer." Separately, `jd-insights/patterns.md`'s "Roles defined by what they
are not" device — a posting stating explicitly what its own role does *not*
cover — is now at six instances (Adobe, Sanna, Wealthsimple, HelloFresh,
Meta, UKG), up from the five recorded when that pattern note was last
written, and has grown a second form: UKG states a matched "is / is not"
pair rather than an exclusion sentence alone.

**What I think it means.** This is the same underlying claim as "Nobody
agrees what this work is worth" above, from a different angle: that finding
showed compensation ranges spanning an order of magnitude under nearly
identical "Systems" titles; this one shows titles failing in both
directions — overclaiming and underclaiming — at the same time, on the same
small scale. Six employers have now judged their own titles insufficiently
self-explanatory and appended a disclaimer, an unusual thing for a title to
need. Read together, both findings point at the same mechanism rather than
two separate ones: titles have stopped reliably carrying scope information,
and employers are compensating for it in the two places that show up in a
posting — the number, and the paragraph right under the title.

This is thinner evidence than the compensation finding — four total
signal/pattern holders plus six disclaimer instances, no time dimension, and
no claim here should be read as the problem worsening rather than simply
being visible once enough postings are collected to notice it.

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

**Conversation design shows the identical placement chaos, not a resolution
toward content design.** The corpus's conversation/AI-model-design entries
split almost evenly on where they sit. Wise's Principal AI Model Designer and
Gen Digital's Staff AI Conversation Designer are placed inside a
content-design-labeled function ("Content Design Guild," "Content Design
team"). UKG's Lead Conversational Designer and GDS's Senior Interaction
Designer (Conversation) state the opposite outright — "This is a systems
design role, not a copywriting role... This role is not: Writing UI copy or
chatbot scripts... Pure UX or visual design" (UKG); "the first permanent
conversation design role at GDS" (GDS, a founding claim, not an absorption
claim). Amazon's Sr. UX Conversation Designer sits on a team named "Word and
Voice Design" — the two disciplines merged into one unit, neither
subordinated to the other. Widen the lens to the excluded model-design
lineage (Fin, Notion, Redpine, Basis — all explicitly placed outside content
design, all excluded partly on that basis) and only 2 of 6 comparable
postings claim any content-design lineage at all.

What this reframes, rather than answers: conversation design is not being
absorbed into content design, and it is not clearly separating from it
either. It is being scattered across org charts in parallel with content
design itself — the same placement chaos this finding already documents,
now visible a second time in an adjacent discipline. Six of the seven
relevant entries were added within a single two-week window, which is a
sourcing artifact of when they were submitted, not evidence that either
direction is accelerating. Nothing here should be read as a trend over time.

---

# Watching

Patterns with real evidence that have not been given a taxonomy key, recorded
so they are not rediscovered from scratch. Entries stay here after a key is
created, marked resolved, so the reasoning survives the promotion. Step 4's bar still applies: a new
instance updates a count, it does not promote a pattern to a finding.

**Measurement and evaluation frameworks — 14 instances.** OpenAI (evals,
evaluation rubrics), Netflix and Spotify (evaluation frameworks), Meta
(measurement frameworks, twice — the AI Content Strategy Lead states both
evaluation frameworks and business-impact measurement), LinkedIn (architecture health metrics), GM and Notion
(content QA), Ride Platform (success metrics), Chime (content quality metrics,
automated governance dashboards), Ally (success metrics and measurement
frameworks), Wix (evaluation workflows for generated UX content), Engrain
(documentation engagement metrics tracked to accelerate self-service adoption
and time-to-market value). The largest
un-keyed pattern in the corpus. Held because it overlaps
`governance-as-value-prop` heavily and cannot yet be separated cleanly.

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

**Update, 2026-08-16: a third instance has appeared.** Alibaba's AI Content
Strategist states the same move in its fourth responsibility — building,
across B2B industries, terminology, buyer concerns, and product language
"形成可被 AI 调用和复用的内容知识资产" ("as content knowledge assets that AI
can call on and reuse"). Same structural move as Notion and Meta: content
prepared as a substrate a model reads from and draws on at generation time,
not published for public search or reduced to schema markup. Three companies
now carry the key — Notion, Meta, and Alibaba. The key is comfortably past
Step 4's floor, not merely at it.

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
counterpart **generative** are defined under Terminology in CLAUDE.md, which is
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
shifted." All six holders contradict it — CoLab, Insurify, Ride Platform, Ally,
Meta, and Booking.com were each admitted *because* their systems
responsibilities were substantive, and CLAUDE.md's marketing-sited note
instructs assigning the key on placement rather than on hollowness. The key is
doing one job and its description claims another. Noted rather than rewritten,
because the description is user-facing card copy.

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

**A single governance framework named for both human and agentic workflows —
one instance.** Wix's Content Designer, Language & Systems states the role is
"central to defining how content governance works across both human and
agentic workflows" — one governance framework, explicitly scoped to cover
both. The closest existing language in the corpus is Figma's UX Writer, AI,
which asks for "taxonomies, glossaries, and other artifacts for both human and
agentic ingestion" — but that line is about content built to be read by both
audiences, not about a governance process applied to both. Different framing:
Figma's is what the content is for, Wix's is how the process that produces and
polices it is structured. Not a clean second instance of the same pattern.
First instance, so it stays here rather than becoming a key or a finding.
*Trigger to revisit: a second posting that states one governance, standards,
or review process explicitly scoped to cover both human-authored and
agent-generated content, rather than either a process for one audience or an
artifact built for both.*

**Named AI tools — 5 instances, one of them gating.** Of the entries carrying
`ai-native-expectation`, five name a specific product rather than the
category. HelloFresh: "building rapid interactive prototypes (using tools
like Claude Code, Gemini, or Figma AI)." Coupang's Senior Content Strategist,
Core UX (Korean posting): "ChatGPT, Claude, Gemini 등의 다양한 생성형 AI"
("ChatGPT, Claude, Gemini, and other generative AI tools"). Intercept:
"Hands-on experience using LLMs or AI writing tools such as ChatGPT, Claude,
Copilot, Jasper, or similar platforms." Function Health: "You use AI tooling
actively. Claude, Cursor, or equivalent — to accelerate ideation, draft
generation, and iteration without sacrificing voice quality." All four list
one or more tools as interchangeable examples of the category ("or similar,"
"or equivalent," "등의"), not a required one.

The Ride Platform is the different case: "Jasper is core to how we work,"
"Jasper embedded as the core engine for content creation," "with Jasper
strongly preferred." One named tool, stated as the standard the role is
built around, not an example among several.

Adobe's Staff Content Strategist names Firefly, but as part of describing
Adobe's own product portfolio the role writes about, not a tool the
candidate is expected to use — checked and excluded on that basis. Fin's
"Claude Code" mention (a perks line, "Unlimited access to Claude Code and
best-in-class AI tools") is not counted as an instance here: the posting is
excluded from the dataset outright (no occurrence of *content, writing,
copy, language, tone, voice,* or *terminology*, per the entry above), so
nothing in it is available to cite as corpus evidence.

Held here rather than promoted: four of the five instances are examples,
not requirements, and the one gating instance (Ride Platform) is a single
company's procurement choice, not evidence of a market standard. *Trigger to
revisit: a second posting that gates on one specific named tool as a stated
requirement, the way Ride Platform gates on Jasper — or the same tool named
across three or more postings.*

The second half of that trigger is now met on its own terms: Claude appears
by name, as an interchangeable example, in four of the five instances
(HelloFresh, Coupang, Intercept, Function Health) — Ride Platform's Jasper is
the exception. Not treated as a promotion here, since the pattern is "one
tool keeps showing up in example lists," not "the market has converged on
one tool" — Claude's appearances are still framed as one option among
several ("or similar," "or equivalent," "등의") in every instance, the same
framing the trigger was written to distinguish from a genuine convergence.
Flagged for a second reader to weigh in on rather than resolved unilaterally,
since the corresponding action — sharpening `ai-native-expectation`'s card
description in `jobs.json` to name the tool(s) — is a user-facing copy
change. If either half of the trigger is judged met, the promotion should
also change that card description: it currently states the expectation
generically ("AI fluency… baseline"), and naming the tool(s) the postings
actually converge on would sharpen the description as directly as the
evidence supports — consistent with `CLAUDE.md`'s card-copy rule to state
what the data shows, not the category it falls under, once the data shows
something more specific.

**Explicit "human-in-the-loop" framing for AI content QA.** Evinova's Content
Design Lead states it as a stated responsibility of the role itself: "while
ensuring that AI processes retain a human-in-the-loop approach." Checked
against a few other AI-heavy entries for the same framing before logging this
as new: Gen Digital's Staff AI Conversation Designer and Wise's Staff AI
Content Designer, FinCrime carry no equivalent language, explicit or
otherwise, despite both discussing AI output and model behavior at length.
Spotify's Annotation Manager does — "familiar with LLM or AI-driven annotation
workflows and human-in-the-loop systems" — and was added to the dataset
2026-05-24, three months before this entry, without the phrase ever being
logged here.

That backcheck means this is the first time the phrase is tracked as a
pattern in this file, but not the first time it appears in the corpus, and not
a first instance in the Step 4 sense — two postings already carry it. The two
uses differ in kind: Spotify's is a qualification the candidate is expected to
already have ("familiar with… systems"), Evinova's is a commitment the role
itself makes ("ensuring that AI processes retain" the approach). Recorded here
rather than promoted, since two data points aren't enough to say whether that
difference is a real split or coincidence, and since this note is the
mechanism surfacing the pattern for the first time at all. *Trigger to
revisit: a third posting using "human-in-the-loop" or an equivalent explicit
framing for AI output review — distinct from editing/QA responsibilities that
imply review without naming it — or a reason to treat the Spotify and Evinova
instances as two different patterns rather than one.*

**Regulatory or compliance framing bounding the content work — three
instances.** Wise's Staff AI Content Designer, FinCrime states the role must
"balance meeting regulatory obligations with building world-class customer
experiences." Evinova's Content Design Lead states the parallel constraint for
a different regulatory regime: "a deep awareness of the regulatory and
ethical requirements that are not only considerations for our content design
responsibilities but also for those who use our tools," and separately that
its Content Design Guidance document must stay current "as our products and
the regulatory landscape evolve." Ethos's Staff Content Designer states the
same move for a third regime: "Comfort in Figma and with regulatory
constraints, since in an industry like life insurance, clarity and compliance
are the same job." Same structural move in all three — content
responsibilities explicitly bounded by a named external compliance regime
(financial crime for Wise, clinical/health regulation for Evinova, life
insurance regulation for Ethos), not just by internal brand or product
standards.

Three companies, three named regimes, but two of the three (Wise, Ethos) sit
in the Finance domain and the third (Evinova) in Healthcare — both regulated
industries. Per Step 4's domain-clustering guidance, this reads as
domain-leaning rather than confirmed cross-industry: recurrence inside
regulated-industry hiring specifically is weaker evidence of a discipline-wide
pattern than recurrence spanning unrelated domains would be. *Trigger to
revisit: a fourth posting that states its content responsibilities are
bounded by a named regulatory or compliance framework, from a domain outside
Finance and Healthcare — needed to confirm this is a cross-industry pattern
rather than one specific to regulated-industry hiring.*

**Excluded on eligibility, not on thinness — Redpine's Senior Knowledge Graph
Engineer.** Every other exclusion in the corpus fails on thinness: an AI
mention confined to a qualifications line, a systems-sounding title over
otherwise-conventional production work. Redpine is a different kind of
exclusion — the posting is dense, specific, and well-argued about a real
discipline, it just isn't this one. A full literal-text check found zero
occurrences of *content, writing, language, copy, tone, voice,* or
*terminology* anywhere in it — a cleaner zero than Fin's "Staff AI Designer"
managed, since Fin at least argued for its place inside a Design org ("AI
Design team," "product designers") while Redpine sits in "Department: Tech"
and never engages design discourse at all.

The posting's own framing — "Agents are only as good as the knowledge they
can reach," provenance-bearing graph nodes served "directly to agents,"
multi-hop retrieval — reads like a literal engineering implementation of what
the `agent-retrieval` signal describes in the abstract: "the knowledge layer
a model reads from before it writes." That thematic closeness was the actual
temptation to include it, and the reason it's worth recording here rather
than filing the exclusion silently. It doesn't hold up: `agent-retrieval`'s
three holders (Notion, Meta, Alibaba) are content professionals restructuring
their *own* content so agents can retrieve it — upstream of the retrieval
layer, shaping what goes in. Redpine's engineer builds the retrieval layer
itself, over other people's licensed documents, with no content deliverable
anywhere in the posting. Assigning the signal on thematic resemblance would
have made Redpine the odd one out among its holders, not a fourth confirming
instance — the signal tracks a shift *inside* content roles, not a general
tag for agent-facing retrieval infrastructure.

The same test applies to `taxonomy`: Redpine's "define the entity types,
relations, and constraints that licensed data from each domain maps into"
sounds like taxonomy work, but every taxonomy-cluster entry classifies
*content* (product copy, UX strings, support docs) for navigation; Redpine
classifies real-world entities (drugs, trials, companies, filings) for
machine reasoning. Same technique — define types and relations — applied to
a categorically different object. See CLAUDE.md's Terminology section
("Words that mark the edge of scope") for `ontology`, `data schema`, and
`knowledge graph`, added there rather than to the taxonomy — these describe
what's outside this dataset's scope, not a pattern within it, so they aren't
tracked as instances toward a future key the way the rest of this section
works. *Trigger to revisit: a posting doing comparable graph/ontology
engineering that also states a content, writing, or language deliverable
somewhere in scope — that would be the actual boundary case this one only
resembles.*

**A second, more extreme instance — Notion's Model Behavior Engineer, and
what it settles about the literal-text check.** Same underlying question as
Redpine, arrived at from a different direction: `context engineering,`
system prompts, tool prompts, eval design, and model launch work that reads
almost exactly like Wise's Principal AI Model Designer and Gen Digital's
Staff AI Conversation Designer — both included. This one is excluded, and
more clearly than Fin was: Fin at least sat inside an "AI Design team" and
used "product designers" as its home discipline; Notion's posting sits in
`Department: Engineering`, in "our AI engineering team," and names design
only as one of four external partners it works with ("engineering, product,
design, and data") — the same structural position as "data." Neither of the
two things that got Wise or Gen Digital included is present: no title
naming a content discipline, and no bridge sentence framing the role as a
second path into one ("Model Designer, or a systems-focused Content
Designer who has already made this transition"). Zero clusters ground, not
merely fewer than the required two.

This is also the posting that answers the open question about whether the
seven-word literal-text check (see CLAUDE.md's Terminology section) is too
narrow. Six of the seven are a clean zero; the seventh, "Be the voice of
quality in the room," is the idiom, not a content/brand-voice usage — a
genuine false positive, read in context rather than counted mechanically.
The same posting also has "help write the playbook," an equally idiomatic
stem-match on `writing`. Widening the list to catch stems would have
produced a second false positive here, not a real hit — evidence that the
list's current shortness isn't an oversight to fix, and the actual
safeguard is reading each hit in context, which the audit process already
requires. Recorded together with Redpine as two data points on the same
pattern (model-design work with zero content vocabulary, outside any design
org) — the trigger set for Redpine above still applies to both.

**AI-assisted maintenance of the documentation system itself — one
instance.** Anthropic's Technical Documentation and Content Engineer, Claude
Docs states "self-healing pipelines, AI-assisted review and maintenance" as
a stated responsibility, twice — once in the role description and again
verbatim in the first key responsibility. This is distinct from the
content-production automation frame `ai-tooling`'s description states and
most of its holders carry: those entries use AI to help produce or evaluate
content itself. Here the AI is applied to maintaining the documentation
*system* — catching and fixing problems in already-published docs — closer
in kind to the "Enforcement" move described above (content in a repository,
checked by automated rules) than to content generation, but with the
checking itself framed as AI-assisted rather than lint-rule-based. Still
assigned `ai-tooling` per the description-versus-use note above, since no
more specific key exists yet. One instance, so it stays here rather than
becoming a key. *Trigger to revisit: a second posting naming AI-assisted
maintenance, repair, or health-checking of an existing documentation or
content corpus as a stated responsibility, distinct from producing new
content or reviewing single drafts.*

**Sole production ownership with no design partner at all — one instance.**
Bolt.new's Staff Content Designer states the role ships "content-led
features end to end, on your own," as "the design DRI, in Figma or with
agentic tools, through to shipped," and separately in the qualifications
section: "If your process depends on someone else turning your words into
screens, this role will frustrate us both." This is a different claim from
the "first content designer" or "newly forming team" framing several other
entries carry (Sanna, Wise's earlier hires): those describe joining before a
practice exists, but still leave room for a product designer somewhere in
the loop once one is hired. Bolt's posting removes that role from the
picture explicitly, permanently, not just for an interim period before the
team grows. The stated route to shipping is design in Figma, or build with
agentic tools — treated by this audit as parallel evidence to entries where
a content designer ships their own code, which is why `ai-tooling` and
`ai-native-expectation` are both assigned here on this line rather than on
qualifications-section AI mentions alone.

One instance, so it stays here rather than becoming a key. *Trigger to
revisit: a second posting stating a content design role ships product
changes to production with no design partner at any stage, on an ongoing
basis rather than as a temporary condition of an early hire.*

**Autonomy-spectrum framing surfacing inside an included entry, not just
exclusions.** UKG's Lead Conversational Designer, Agentic Experiences states
"Define how agents operate across a spectrum of autonomy from suggesting,
confirming to acting on the user's behalf" and, separately, "Define how and
when AI should ask, confirm, defer, or act." This is the same structural
framing as Fin's excluded "Establish decision frameworks: when systems
should act, ask, escalate, or defer," and closely adjacent to what the
deterministic/generative testimony above describes as the specification
side of the split. What's different here is where the framing shows up:
Fin and the testimony are an exclusion and non-posting evidence,
respectively; this is the first instance of the act/ask/escalate/defer
framing inside an entry that clears eligibility outright — the title names
conversation design directly, the posting sits on an "AI Design Systems"
team inside UKG's design function, and the text carries content vocabulary
throughout ("structured content systems," "structured content models").
One instance, so it stays here rather than becoming a key — recorded because
it's the case the Fin discussion above was implicitly watching for without
naming it as a trigger. *Trigger to revisit: a second included entry using
the same autonomy-spectrum or act/ask/escalate/defer framing as a stated
responsibility.*

**Redpine's open trigger, tested — and resolved without promoting or
reopening anything.** Redpine's exclusion entry above set a trigger: "a
posting doing comparable ontology engineering that also states a content,
writing, or language deliverable somewhere in scope." UKG's Lead
Conversational Designer, Agentic Experiences is the first posting to test
it. It states ontology work explicitly and pairs it, in the same
responsibility, with a content deliverable: "Develop and extend ontologies
and structured content systems that enable scalable, consistent AI
behavior," alongside "Translate brand voice, policy, and UX principles into
machine-interpretable frameworks."

That pairing, not the word "ontology" alone, is why `taxonomy` is assigned
to this entry where it was withheld from Redpine. Redpine's ontologies
classify real-world entities — drugs, trials, companies, filings — with no
content object anywhere in the posting. UKG's ontologies classify and
structure *content* itself (conversation response patterns, structured
content models, machine-interpretable frameworks translated from brand
voice and policy) for the purpose of consistent AI behavior — the same
content-classification sense every other `taxonomy`-cluster entry carries,
not Redpine's real-world-entity sense.

This settles the trigger rather than reopening the exclusion it came from:
Redpine's own text still names no content deliverable and stays excluded on
that basis. What UKG's entry shows is that the boundary Redpine's exclusion
drew is a real dividing line running through language that otherwise looks
identical ("ontology," "structured content") — a second instance of similar
vocabulary landed on the content side of the line rather than collapsing
it. No new trigger to set here; the open question the Redpine note raised
now has an answer, on the strength of one clean test.

**Explicit discipline-founding framing — one clear instance.** GDS's Senior
Interaction Designer (Conversation) states plainly: "This is the first
permanent conversation design role at GDS, and you'll help establish the
discipline here," and separately asks the hire to "help establish
conversation design as a discipline at GDS, contributing to a community of
practice, sharing knowledge across teams, and helping others develop their
skills in this emerging area." This is more explicit than anything
previously on record — the framing above (see "Sole production ownership")
noted, only in passing, that Sanna's and Wise's earlier hires carry a softer
"first content designer" or "newly forming team" framing, without treating
that framing as a pattern in its own right. GDS names the act of founding a
discipline as a stated responsibility, not just a fact about hiring order.

Two of the three instances so far (Sanna, Wise) share the Finance domain;
GDS is the first non-Finance instance, but three data points across two
domains does not clear Step 4's cross-industry bar on its own — flagged here
as domain-clustered pending a wider spread. No key proposed; this stays a
Watching entry. *Trigger to revisit: a second posting using comparably
explicit "first/founding a discipline" language, ideally in a domain other
than Finance or Government.*

**Excluded on eligibility, but the closest call in the model-design lineage
yet — Basis's "Intelligence Architect" fails on writing-craft density, not
its absence.** Every prior lineage exclusion (Fin, Redpine, Notion) failed on
a clean or idiom-only literal-text check — none of them used writing or
language vocabulary in a way that could plausibly ground a content-discipline
read. Basis inverts this. The posting's "What you'll bring" section states
outright: "Writing as a craft. You treat language as load-bearing. You catch
the sentence that will be misread before it ships. You have excellent
taste." "The writing work is yours" appears as a stated division of labor
against a separate "measurement work." This is denser, more central,
non-idiomatic writing-craft language than any prior exclusion in this corpus
— arguably denser than some included entries. And yet the word "content"
does not appear once in the roughly 1,000-word posting, a clean zero on the
one trigger word every included lineage entry (Wise, Gen Digital, UKG, GDS)
uses somewhere in its body even when the title doesn't. Title ("Intelligence
Architect") and org placement ("Department: Technical," with the word
"design" appearing nowhere in the text — a step below even Notion's
placement, which at least named design as one of four partner functions)
give this posting no support either.

**The reason for exclusion is the posting's own explicit, structural denial
that writing is the role's primary discipline — not a euphemism problem the
way Microsoft's context-engineering exclusion was.** Both postings center
"context" as the object of the work ("we treat context like a product" here;
prompt/context-window management at Microsoft), which invites treating them
as the same near-miss. They aren't. Microsoft was excluded because the
underlying skill was ML/software engineering wearing "context" vocabulary
with zero writing-craft substance anywhere — the vocabulary itself was doing
the work of a euphemism. Basis's writing-craft vocabulary is real and
substantial; the posting still fails, on a different axis, because it states
directly that no single discipline is what the role is "primarily" about.
Required criterion 1 asks whether a role is primarily a content discipline —
and a JD can pass the literal-text check strongly and still fail that
"primarily" clause when it says so itself.

**The clearest evidence for this reading is structural, not lexical: how the
posting frames who should apply.** "This role doesn't have a standard
background. The people who do it well come from many places" introduces
seven co-equal candidate pools, given equal weight and equal-length
treatment: engineers and PMs "who've drifted from building systems to
questioning whether the system is doing the right thing"; philosophers
"who've spent years writing precise prose about systems no one else
understood"; lawyers who "write the kind of language other people have to
follow"; accountants "who appreciate language and want to shape the future
of your profession"; editors and writers "who treat structured prose as
engineering"; academics "tired of producing work that nobody acts on"; and
"anyone who reads about what we're doing and recognizes the work as theirs."
Writers and editors are one-seventh of the stated hiring pool, not the
target the other six are bridging toward.

Compare this against Wise's Principal AI Model Designer, the entry that
established what a working bridge sentence looks like: "an accomplished and
experienced Model Designer, or a systems-focused Content Designer who has
already made this transition in your day-to-day work." Two paths, not seven.
Both paths already inside or transitioning into a content identity,
reinforced by the role's actual placement in a "Content Design Guild." The
sentence's function is to assert continuity — this new role and content
design are the same skill set wearing a different name. Basis's seven-path
list does the opposite: it asserts that no single named discipline, content
design included, is what unifies the people who succeed at this job. The
"What you'll bring" list reinforces the same point from another angle — of
its seven listed traits, only one ("Writing as a craft") is language-specific;
the other six (systems reasoning, causal thinking, comfort with ambiguity,
learning velocity, holding multiple threads at once) are generic analytical
traits with no connection to language or content. The posting's own theory of
who succeeds is a general precision-reasoning-expressed-in-binding-language
aptitude, not a writing or content discipline that happens to recruit
broadly — closer to how a law firm might describe the temperament needed for
contract drafting than to how any included entry in this corpus describes
itself.

One instance, so no key of any kind is proposed — this is recorded as a
structural counterpoint to Wise's bridge-sentence precedent, not as evidence
toward a new signal. *Trigger to revisit: a second posting pairing dense,
non-idiomatic writing-craft language with an explicit multi-path,
discipline-agnostic hiring philosophy (three or more co-equal, mostly
non-content candidate backgrounds) — distinct from Wise's two-path,
both-already-in-content bridge, and distinct from a role that simply fails
to name any discipline at all (Fin, Redpine, Notion).*

Ambiguous call recorded rather than resolved in the exclusion itself: whether
"Who might be a fit" should be read as authoritative on primary discipline —
the reading applied here — or discounted as recruiting-funnel copy. A reader
who discounts it and weights "What you'll be doing" instead (three of its
four bullets anchored in writing or standards-for-writing) could reasonably
land on include. See `jd-source/basis-intelligence-architect.md` for the full
reasoning.

**Whole-posting generic strategic language — 2 instances, cross-domain.**
O.C. Tanner's Principal Product Content Strategist and Verily's Content
Designer III were both excluded on the same failure mode: every
responsibility restates the same handful of abstract nouns — governance,
standards, consistency, scalability, cross-functional alignment — without
ever naming a concrete object the work produces or touches. O.C. Tanner's
four "Key Responsibilities" subheads recombine "governance," "AI readiness,"
"scalable," and "cross-functional" across every section, and its "Success
Looks Like" section restates the identical claims a third time with no new
information; the posting never once names a style guide, a taxonomy, a
governed term, a described workflow, a tool, or an evaluation process.
Verily's excludedReason independently reached for the same description:
"too thin and too vague to support a confident entry... generic UX-strategy
language with no reusable-template, taxonomy, or cross-team-scale
specifics, the weakest grounding for that cluster anywhere in the corpus."

Both postings pass the required criteria and the signal test on a literal
read of their vocabulary — the failure isn't an absence of the right words,
it's an absence of anything concrete behind them. This is what distinguishes
the pattern from entries that clear the bar: UKG names "ontologies and
structured content systems" and "a spectrum of autonomy from suggesting,
confirming to acting"; GDS names "dialogue patterns, prompts, and
interaction flows." A posting in this pattern never drops to that level of
specificity once, no matter how many times it restates its strategic intent.

Two instances, two different domains (Healthcare, SaaS) — clears Step 4's
floor without being domain-clustered. *Trigger to revisit: a third instance,
to confirm this is a recurring authorial style (templated senior-strategist
language reused across companies) rather than coincidence.*

**AI mentions that name no tool, governed object, or model behavior — a
placeholder pattern already precedented five times over, never centralized
until now.** Roblox, Checkout.com, TCGplayer, Meta's WhatsApp, and Wise's
Senior Content Designer, Spend were each excluded in part or in full on the
same specific test, cited directly in each successive exclusion's own
reasoning without ever being written up as its own pattern: an AI mention
that names no tool, no governed object, and no model behavior fails the
signal test's AI-tooling/governance/model-behavior prong, regardless of how
many times "AI" appears. Roblox's "Identify and implement AI solutions to
improve content quality and scale" was the first to fail this way — "AI
solutions" is a placeholder, not a described responsibility. TCGplayer's "AI-
assisted tools where they strengthen quality or efficiency" repeated the
same gap as a subordinate clause rather than a responsibility of its own.
Checkout.com and Wise's Spend entry failed the same test from the
qualifications side — AI-assisted-tools experience listed as a *preferred*
qualification, never a stated responsibility. WhatsApp's AI material sits
entirely in Preferred Qualifications ("integrate AI tools to optimize/
redesign workflows," "prompt/context engineering, agent orchestration")
while its stated Responsibilities are standard product content design.

Five instances across four domains (Media, Finance, E-commerce, Big Tech) —
this has been operating as settled, self-citing precedent since Roblox first
established it, but had never been pulled into one place. No new key
proposed: this describes a recurring way postings fail the existing signal
test, not a new cluster or signal to assign to an included entry. Recorded
here so the next boundary case can cite the pattern directly instead of
re-deriving it from a chain of cross-references between exclusion files.

**Guild/craft-authority posed as an alternative to direct management — one
instance.** Vinted's Content Design Lead states twice that the org structure
around the role is not yet decided: "Depending on the organisation's evolving
structure, this may involve direct people leadership, a guild model built on
craft authority, or both" (role overview), and "Demonstrated ability to lead
a content design function through direct management, craft authority, or
guild-style leadership" (About You). This is a different use of "guild" than
the one already on record in `patterns.md` ("Guild" as a name for the content
community — Wise, Wix), where the word names an existing cross-team community
of practice alongside a separately-named reporting line. Vinted instead names
guild-authority and direct management as two candidate *organizational
structures*, contingent on a decision the posting says has not been made.

Joe's read, recorded as interpretation and not something the JD states or the
data confirms: this framing may be a deliberate way to keep the org structure
open — leaving people-management scope and expectations unresolved until
after hiring, so the company can decide based on whether the person it
actually hires has the management experience to take on direct reports. The
posting supports the observation that the structure is stated as undecided;
it does not state a reason why, and the reason above is Joe's inference, not
a finding this dataset can independently support.

One instance, so no key is proposed. *Trigger to revisit: a second posting
explicitly framing guild/craft-authority leadership as an alternative
organizational mode to direct management — rather than as a name for a
cross-team community of practice.*

**Solo content-design hires absorbing an expanding, sometimes atypical
scope — one instance.** Relay's Senior Content Designer states, as one of
seven "What you'll do" bullets for a role explicitly billed as "Relay's
first Content Designer": "Be ready to jump into an incident and support
with crisis messaging and recovery comms in the event that things go
wrong." The same posting separately asks the same solo hire to "occasionally
... take on graphic design and copywriting for high-consequence marketing
materials such as investor decks, client pitch decks, candidate pitch decks
and the Relay website." Checked directly against the full `jd-source/`
corpus: no other entry states crisis or incident messaging as a content
responsibility — the only other hits for "crisis" or "incident" anywhere in
the archive are unrelated (DeepMind's "not incidental," dxw's "incidental
boilerplate," Insurify's fraud-warning "incidents"). This is a genuine first
instance, not merely a first instance outside conversation-design or
CX-leaning roles.

Joe's read, recorded as interpretation and not something the JD states or
the data confirms: this is part of a broader pattern worth tracking in its
own right, distinct from the "explicit discipline-founding framing" entry
above (which is about postings stating they are founding a discipline).
This is about scope — a solo or first content-design hire being asked to
absorb an expanding and sometimes atypical range of responsibilities (crisis
comms here, alongside the marketing-collateral spillover in the same
posting), regardless of whether founding language is present. Whether this
reflects a real hiring trend or is one company's unusual scope for one role
is exactly what a second instance would help settle.

One instance, so no key is proposed. *Trigger to revisit: a second posting
showing a solo or first content-design hire taking on a stated
responsibility outside the traditional content design brief — crisis or
incident comms, marketing collateral, or a comparably atypical ask.*

**Personalization as an explicit design responsibility — 1 included instance,
1 cross-domain excluded sighting.** UnitedHealth Group's Principal
Conversational AI Designer lists "Personalization in AI Design" as its own
named responsibility: "Anticipate user needs and use cases using design
methods that proactively adapt to individual users over time, creating more
relevant and meaningful interactions." No other *included* entry in the
corpus states adaptive, over-time personalization as a stated responsibility
of the content/conversation design role itself. One instance, one domain
(Healthcare) — below Step 4's floor for a jobs.json-grounded key.

Pinterest's Content Designer II, Personalization — excluded (only one cluster,
`content-systems-design`, grounded; nothing written to jobs.json) — is a
second, cross-domain sighting of the same framing: a role and team built
entirely around adaptive personalization, tasked to "explain why people are
seeing content and how they can shape their experience." Recorded here
because it satisfies this note's own trigger ("a second instance, ideally in
a different domain") on text alone, even though the posting carries no
jobs.json entry to ground an assignment from — the same limitation noted for
eDreams' human-in-the-loop instance. *Trigger to revisit: a third instance,
this one grounded in an included entry, which would clear Step 4's floor for
real.*

**Craft standard-bearer for internally-consumed artifacts, not product
surfaces — one instance.** Salesforce's Experience Design Lead scopes the
role's quality ownership to decks, Slack messages, prototypes, and
field-facing materials for an internal team (Customer Success Managers), not
to a product surface end users see: "the design and content standard-bearer
for our team," covering "a prototype, a field-facing deck, or a Slack message
that lands," and separately, "Design and produce polished decks and
communications that represent the team well at all levels — from field CSMs
to exec stakeholders." The corpus is near-universally about content on a
product surface; this is the first entry whose stated deliverables are
internal-audience artifacts throughout, with no product-surface content
named. One instance, so no key is proposed. *Trigger to revisit: a second
posting asking a content designer to be the craft standard-bearer for
internal team artifacts — decks, comms, prototypes — rather than
product-facing content.*

**AI-in-hiring disclosures, stated by the employer — 3 instances, 3 domains.**
Three postings disclose using AI tools to screen or evaluate applications, in
near-identical language. Wealthsimple's Staff Content Designer, Investing:
"We may use artificial intelligence (AI) tools to support parts of our hiring
process, such as reviewing applications, analyzing resumes, or assessing
responses. These tools assist our team but don't replace human judgment –
all final hiring decisions are made by people." Salesforce's Experience
Design Lead: "Salesforce uses artificial intelligence (AI) tools to help our
recruiters assess and evaluate candidates' resumes and qualifications
throughout the recruiting process. Humans will always make any candidate
selection and hiring decisions." Verily's Content Designer III — excluded
from `jobs.json` on thinness grounds, cited here only for an existence claim,
consistent with how excluded postings are used elsewhere in this file: "We
use artificial intelligence (AI) tools to help screen and/or assess
applications for this role. These tools analyze information you provide (for
example, your résumé or answers to application questions) to support our
hiring team's review."

All three pair the disclosure with an explicit human-final-decision
assurance, worded almost identically across employers sharing no domain
(Finance, SaaS, Verily's health-tech). That similarity, more than any one
company's wording, is what makes this read as compliance boilerplate (several
jurisdictions now require an AI-in-hiring disclosure) rather than a
distinctive claim by any one employer.

This describes the hiring process, not a stated job responsibility, so it
isn't a cluster or signal candidate — recorded so a fourth instance updates a
count rather than being rediscovered from scratch. *Trigger to revisit: a
posting that goes beyond disclosure and states what the tool actually
evaluates or how (a rubric, a scoring criterion) — the first instance with
enough specificity to say something beyond "this is now standard
boilerplate."*

**Employer restricts or polices candidate use of AI in the application
itself — 2 instances, 2 domains.** Two postings run the opposite direction
from the above, addressing AI use *by the candidate* rather than by the
company. GDS's Senior Interaction Designer (Conversation): "Artificial
intelligence can be a useful tool to support your application, however, all
examples and statements provided must be truthful, factually accurate and
taken directly from your own experience. Where plagiarism has been
identified (presenting the ideas and experiences of others, or generated by
artificial intelligence, as your own) applications may be withdrawn and
internal candidates may be subject to disciplinary action." The Ride
Platform's Content Systems Specialist, inside its own "AI Fluency"
qualifications bullet: "We encourage you to use AI responsibly as you
prepare your application. Please don't use it to fabricate experiences or
answer questions live in interviews."

Two companies, two domains (Government, E-commerce) — clears Step 4's floor
without domain-clustering. Figma's UX Writer, AI states a camera-on
requirement for video interviews "to ensure the integrity of our hiring
process," which plausibly addresses the same concern but never names AI —
not counted as a third instance on that basis. Same caveat as the entry
above: this is hiring-process commentary, not a stated responsibility, so
it's not a cluster or signal candidate. *Trigger to revisit: a third
instance, or one specific enough to describe how the restriction is
enforced (an interview format change, a live verification step) rather than
a general conduct warning.*

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
