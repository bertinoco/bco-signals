# Patterns in how job descriptions are written

Observations about the postings as documents — how employers structure, word,
and format them. Distinct from what the roles ask for, which is the dataset's
job.

Hand-written. Add to it when a posting does something notable; most don't.
Every claim here should name the companies it came from, so a reader can go to
`jd-source/` and check.

---

## Roles defined by what they are not

Five postings define scope by exclusion, and the more senior the role, the more
formal the device gets.

**Adobe** goes furthest, with a headed section:

> **What this role Is not**
> Not editorial standard-setting or voice and tone definition
> Not AI behavior governance or policy
> Not platform rollout, adoption programs, or measurement
> Not product-level content decisions or UI copy (that lives with embedded
> product and domain content teams)

Three others do it in a sentence: Sanna's "This isn't a traditional content
role", Wealthsimple's "This isn't a polish-the-copy-at-the-end role",
HelloFresh's "This isn't a chatbot role."

**Meta**'s AI Content Strategy Lead uses it to fence off authority rather than
craft: "The role will not directly manage teams or own AI platforms, but will
influence and align stakeholders across organizations." The other four exclude
kinds of work. This one excludes the levers for doing it, in a posting that
also asks the holder to define requirements the platform teams build to.

Worth noticing because it is doing real work. Adobe's disclaimers rule out
three cluster assignments that its surface language would otherwise support —
it says "Define how terminology, patterns, and guidance are modeled" and also
says it is not standard-setting. An employer that specific about its own
boundaries is describing a discipline that has become crowded enough to need
them.

## A posting that disclaims its own title

Figma's "UX Writer, AI" tells the reader in its second paragraph that the title
is not the job:

> While the title of this role is “UX Writer,” you might think of yourself as a
> content engineer as much as a writer—someone who uses language to shape how
> people interact with AI, from crafting better inputs to defining clear,
> consistent outputs.

Adjacent to the roles-defined-by-exclusion device above, but not the same move.
Those postings rule out work the title would imply. This one keeps the work and
disowns the title, naming the discipline it thinks the role actually belongs to.

Worth recording because the dataset carries a `title-responsibility-gap` signal
that is otherwise assigned by reading a posting against its own name. Here the
employer states the gap directly, which makes this the clearest single instance
of a pattern usually inferred.

## Boilerplate reuse inside one employer

Google runs the same "As a UX writer, you are an advocate for Google design…"
paragraph, and near-identical Responsibilities bullets, across the Search,
Chrome, and YouTube postings. Only the role-specific middle paragraph differs.

DeepMind's Senior Manager posting is the counter-example, and the only one in
the corpus. It carries neither the shared "As a UX writer, you are an advocate
for Google design…" paragraph nor the near-identical Responsibilities list, and
is role-specific from its first sentence. The template is a default for Google
product postings, not a rule for everything the company posts — worth knowing
before treating shared phrasing as proof two postings came from the same team.

The consequence is practical: a quote pulled from the shared section says
nothing about the role. The quote originally anchoring the YouTube entry —
"Lead the establishment and improvement of holistic UX writing and content
design processes, systems, frameworks or patterns across multiple teams or
products" — appears verbatim in the Search posting too. When one employer has
several entries, check whether a candidate quote is role-specific before using
it as evidence.

## Requisition numbers are not titles

Apple has posted at least two distinct requisitions titled "UX Writer, Systems"
— `200641533-0836` and `200672377-0836`. Same title, same URL slug pattern,
different postings.

Anything that identifies a posting by title alone will eventually attach the
wrong text to an entry. This is why `reqId` is recorded where stated.

## Which employers state metadata

Netflix, Apple, JPMorgan Chase, Ally, and Adobe state an explicit posting date
and requisition number on their own careers pages. LinkedIn-sourced captures
give only relative strings — "3 weeks ago", "1 month ago" — which are ambiguous
about when they were read.

Where both a posted date and an added date exist, the gap runs from zero days
(Adobe, posted and audited the same day) to sixty-six (JPMorgan Chase). One is
not a proxy for the other.

## Internal jargon

Chime writes in abbreviations that only make sense inside Chime — "Inspect
Content efficacy using existing metrics across LOBs", "ensure our process
enables the team to meet SLAs". LinkedIn's posting runs on DITA, KMS, AEM
Guides, and a department called GBO.

Both are legible to the people already doing the work and opaque to everyone
else, which is a choice about who the posting is addressed to.

## Voice experiments

HelloFresh sets its section headings as food puns — "S'more about the role",
"Lettuce share what this role will be responsible for", "Sound a-peeling?",
"Let's cut to the cheese" — and then names the device in the benefits list:
"Food Puns - this one is kind of a big dill if you haven't already noticed."

The only posting in the corpus where the JD is itself a demonstration of the
brand voice the role would be hired to maintain.

## Compensation is presented in incompatible ways

- **Netflix** states a philosophy rather than a component: "our compensation
  structure consists solely of an annual salary; we do not have bonuses. You
  choose each year how much of your compensation you want in salary versus
  stock options." The number is the whole package.
- **Adobe** states two ranges in one posting — a US range and a higher
  California range.
- **Zoom** labels its range "Salary Range or On Target Earnings", committing to
  neither.
- **HelloFresh** says only "Pay Range", in Canadian dollars.

A stated range is not a comparable number without knowing what it measures.
This is what the `covers` field in `compRange` exists to record, and why it is
left null rather than assumed.

**Roblox**, also held as an excluded record, states a range and withdraws the
commitment in the same paragraph: "in some circumstances, the actual salary
could fall outside of this expected range. This pay range is subject to change
and may be modified in the future." Every other posting in the corpus states a
range and stops. This one qualifies the figure into a non-claim, which is a
different failure from not stating what the range measures — the number is
there and disowned rather than there and unlabelled.

The inverse also occurs. **Nscale**, a London posting held as an excluded
record, names every component and no figure: "Highly competitive package (base
+ equity + bonus) with reviews every 12 months." Enough structure to look like
a disclosure, nothing in it to compare. Every posting in the corpus that states
a number is US or Canadian.

**Capital One** states three ranges rather than one or two, and none is
marked as primary: McLean, VA ($200,700–$229,100), New York, NY
($219,000–$249,900), and Richmond, VA ($182,500–$208,300), each labeled "for
Sr. Manager, Design" with no location called out as the base or the
exception. Adobe's two-range posting still reads as a primary US figure plus
a named California premium; this one gives three co-equal locations and lets
the reader pick. The dataset records the largest-city figure (New York) per
the comp range rule for co-equal locations with no stated primary.

## Formatting artifacts survive into the archive

Retained deliberately in `jd-source`, since they are facts about the posting:

- **Wellhub** terminates every bullet with a semicolon rather than a period.
- **GM** uses non-breaking hyphens (U+2011) throughout — "human‑centered",
  "AI‑enabled" — visually identical to a plain hyphen, a different character.
- **Sanna** drops a space between two sentences ("scales quality.This is a
  foundational role") and leaves a stray closing quotation mark at the end.
- **Ally** carries a trailing period in the title itself ("Content Architect .")
  and a subject-verb disagreement in the body ("standards that turns content
  into a high-performing business asset").
- **Google** runs paragraphs together without a break ("...images.Google Ads is
  helping power...").
- **DeepMind** leaks Material Symbols ligature names into the captured text
  where the page renders icons — "corporate_fare", "place", "info_outline".
  The scrape took the icon font's text content rather than the glyph. A reader
  who does not recognise them may mistake them for field labels; they are
  neither labels nor posting text.
- **DeepMind** also leaves a preferred qualification unfinished: "emerging
  interaction modalities such as voice-driven or platform." The sentence does
  not complete in the source.
- **Figma** mixes typographic and straight apostrophes within single sections —
  "Figma’s platform" and "whether you're brainstorming" sit in the same
  sentence, and "We’d love to hear from you" in the body becomes "We'd love to
  hear from you if you have:" as a heading four paragraphs later. Consistent
  with a posting assembled from more than one source document.

Six of the stored quotes needed a character corrected to match their source —
five apostrophes and one hyphen. None was visible on screen.

## AI language in the narrative, absent from the qualifications

**Amazon**'s Sr. UX Conversation Designer, Amazon Customer Service posting
names AI/LLM work twice in its body copy: "You'll also be involved in
building AI and Large Language Models (LLMs), creating writing guidelines to
raise the bar" in the role description, and "Lead the strategic vision for
several products that include generative AI/Large Language Models" as a key
responsibility.

Neither Basic Qualifications nor Preferred Qualifications mentions AI, LLMs,
generative, or model behavior in any form. Both lists read as a conventional
conversation-design hiring bar instead: portfolio, 5+ years of conversation
design/content design/UX writing/voice design experience, a degree in
English, Journalism, Marketing/Communications, HCI, or Design, and experience
leading review sessions.

Worth recording because it runs the opposite direction from the pattern
`ai-native-expectation` describes elsewhere in the corpus — there, AI fluency
shows up as a qualification, not just a duty. Here the AI framing sits in the
narrative and the responsibilities, and the qualifications that would actually
gate a hire don't ask for it. First Amazon entry in the corpus, so there is
nothing yet to compare it against within the same employer.

## Where the posting was captured from changes what you get

Company careers pages give clean text, and often a requisition number and
posted date. LinkedIn captures carry applicant counts, Premium upsell prompts,
alumni modules, and "No longer accepting applications" banners — but sometimes
also carry the only surviving copy of a posting that has since closed.

Insurify's own careers page opens with a fraudulent-job-advert warning before
the posting begins.

## Three headers that don't match their own body

Three postings so far state one title at the top and a different one in the
body text — and no two of them drift the same way.

**Fin**'s posting is headed "Staff AI Designer," but the body repeatedly calls
the role "Staff AI Product Designer": "We're looking for a Staff AI Product
Designer..." Same seniority level, different role name.

**Wise**'s Staff AI Content Designer, FinCrime is headed at Staff level, but
the body twice self-describes the role a level up: "an AI Principal Content
Designer will work on..." and "You're an accomplished and experienced
Principal Content Designer..." Same role name, different level.

**Intercept**'s posting is headed "Content Engineer," but the body opens with
"We're looking for a Content Engineer, Human + AI Workflows:" Same role name
and level — the body appends a scope qualifier the header drops.

All three entries store the header as `title`, per the Title field rule, and
record the body's alternate self-description in the archive's `captureNote`
rather than resolving it. Three instances, three different kinds of drift —
role name (Fin), seniority level (Wise), scope qualifier (Intercept) — which
is enough to call header/body mismatch itself a recurring feature of how
these postings are laid out, even though no two instances substitute the same
thing. The title-then-location or title-then-department header line evidently
invites a fuller self-description once the body gets going; worth a fourth
instance to see whether a fourth kind of drift shows up or one of these three
repeats.

## First non-English posting

**Coupang**'s Senior Content Strategist (Core UX) is the first entry in the
corpus written in a language other than English — the posting is entirely in
Korean, with a single exception: the job title itself is stated in English,
verbatim, inside an otherwise Korean document. `title` stores that English
string unchanged, same as any other entry.

This is also the first use of `quoteTranslatedFrom`, added to the schema
alongside this entry. `quote` holds an English translation of the JD's
own line about redefining format and tone guidelines into requirements
engineers can use for model training and prompt improvement, and
`quoteTranslatedFrom: "Korean"` marks it as a translation rather than a
verbatim excerpt — the site renders that field as a visible caption so a
reader never mistakes the two. The Korean sentence the translation is drawn
from is preserved unaltered in `jd-source`, per the Quote field rule that
"verbatim" means the original language, not the English translation.

One instance, so nothing yet to compare it against — worth recording because
it's the first time the archive itself has had to represent a posting in a
language other than English, not because of anything the posting's content
does.

## First inferred currency

**Intercept**'s Content Engineer states a compensation figure with no
currency attached anywhere in the source: "$80,000-$90,000." Every other
compRange in the corpus states its currency directly in the posting text —
including HelloFresh's CAD entry, which labels its range "$116,130—$134,000
CAD" in the source itself.

`compRange.currency` is recorded as `CAD` on this entry, inferred from the
posting's Toronto, Ontario location and confirmed by the user as a deliberate,
acknowledged exception to reading only what a JD states — not a silent
assumption. This is the first entry in the dataset where a `compRange` field
is filled in from something other than the JD's own text. Recorded here, and
in the archive's `captureNote`, so a later reader auditing this entry (or
building the next one with an unlabelled figure) knows the currency was
inferred rather than stated, and doesn't read it as a second instance of
HelloFresh's pattern.

## A marketing-agency posting carrying both `content-marketing-adjacent` and `title-dilution`

**Intercept**'s Content Engineer is the first entry in the corpus to carry
both signals together. Five other entries carry `content-marketing-adjacent`
alone or alongside other signals (CoLab, Insurify, Ride Platform, Ally, Meta's
AI Content Strategy Lead); none of them also carries `title-dilution`.

The posting is explicit about sitting on both sides at once. It states "This
is not a traditional copywriter role" and describes a title-page role called
"Content Engineer," but the bulk of the stated responsibilities are
traditional B2B agency copywriting and editing — eBooks, whitepapers, blogs,
case studies, landing page copy, campaign copy — for an "award-winning B2B
marketing agency." `title-dilution` is grounded in that gap between the
systems-sounding title and the largely conventional content-production work
underneath it.

What keeps the entry in the dataset despite that gap, and grounds
`content-marketing-adjacent` rather than exclusion, is that the AI-workflow
responsibilities sitting alongside the copywriting are specific, named
deliverables rather than framing: "Develop prompts, prompt patterns, reusable
instructions, and workflow templates," "Document source requirements, prompt
inputs, review steps, QA criteria, and output expectations," "Help build QA
checklists and editorial review standards for AI-supported content
workflows." CLAUDE.md's marketing-sited note asks exactly this question —
whether the systems language is doing the work of a title or is backed by
stated responsibilities — and this posting answers it both ways depending on
which responsibility you read.

One instance, so nothing yet to compare it against. Recorded because a
posting landing on both sides of that line at once is the situation the two
signals exist to distinguish between, and this is the first time a single
entry has needed both.

## First new domain value since the taxonomy consolidation

**Gen Digital**'s Staff AI Conversation Designer is filed under `Cybersecurity`
— the first new value added to the domain taxonomy since `75cb703` collapsed
16 granular values (things like "Fintech", "Media / streaming", "Social
media") down to the current 8 single-word categories. No entry between that
consolidation and this one introduced a value the table didn't already have;
every new company since has fit an existing one.

Gen Digital owns Norton, Avast, LifeLock, Avira, AVG, ReputationDefender and
CCleaner — consumer digital-safety brands with no fit among Agency,
Automotive, Big Tech, E-commerce, Finance, Healthcare, Media, or SaaS. Worth
recording because it's the first real test of whether the 8-value taxonomy
holds up as new sectors show up, rather than just accumulating companies
inside the categories it already has.

## Second non-English posting, and the first translated title

**Alibaba**'s AI内容策略师 (AI Content Strategist) is the second entry in the
corpus written in a language other than English — Chinese this time, after
Coupang's Korean. Unlike Coupang, where the title itself was stated in
English inside an otherwise Korean posting, Alibaba's title is Chinese
throughout with no English variant anywhere in the source. That makes this
the first entry to need `titleTranslatedFrom`, added to the schema alongside
this one and mirroring `quoteTranslatedFrom`: `jobs.json` stores the English
translation "AI Content Strategist" as `title` with `titleTranslatedFrom:
"Chinese"`, while the archive's own front matter and body keep the original
"AI内容策略师" unaltered, per the Title field's non-English rule.

`quote` is translated the same way, with `quoteTranslatedFrom: "Chinese"`
alongside it — so this entry uses both translation mechanisms at once, the
first to need both. Two non-English entries, two different languages, two
different reasons the title needed translating (Coupang's was already
English in the source; Alibaba's wasn't) — worth recording because it's the
first time the title mechanism has been exercised at all, not because a
second instance yet exists to compare it against.

## First posting captured from phone screenshots

**Alibaba**'s AI Content Strategist is the first entry in the corpus
captured by transcribing phone screenshots of a LinkedIn posting rather than
pasting text directly. The method left one short fragment ("言内容库。")
stranded at a screenshot scroll boundary with no confident place in the
sequence; it's excluded from the archive rather than guessed at, and
`captureNote` records that all eight responsibilities, five background
items, and eight competency items were otherwise confirmed complete against
the submitter's own translation. `captureMethod` still reads
`pasted-from-claude-chat` — the closest existing enum value — with the actual
provenance carried in `captureNote` instead, since the README's three
methods don't have a value for this.

Distinct from the "Where the posting was captured from" pattern above, which
is about platform (LinkedIn vs. a company site) rather than capture
mechanism. One instance, so nothing yet to compare it against — worth
recording because it's a new way source text can arrive incomplete that
isn't covered by any existing `captureMethod` value.

## "Guild" as a name for the content community

Two companies now describe their content people as a "Guild" rather than a
department or team. **Wise** places three entries in a "Content Guild" or
"Content Design Guild": "You'll also be part of the Content Guild, and will
regularly collaborate with the content community across Wise" (Senior Content
Designer, Spend), and "This role will sit within the Content Design Guild as
part of our Design team, as the disciplines share a common skill set and
design process" (Principal AI Model Designer). **Wix**'s Content Designer,
Language & Systems opens "you'll join a core team within the Writers Guild."

Both uses describe the same kind of thing: a cross-team community of practice
for writers/content designers, distinct from a reporting line or department —
Wise's guild sits alongside a separately-named product team (FinCrime, Spend),
and Wix's posting names the Guild as the home team itself rather than a
department. Two companies, so this crosses the bar for recording it as a
naming pattern rather than one company's house style, though not for reading
anything into it beyond the word choice.

## Recruiting calls versus job postings, and contract roles as a first

**Lisa Jennings Young**, a Content Design Leader at Adobe, posted directly to
her LinkedIn feed rather than to a careers site: "Hello content friends!
We're building a new Content Foundations team in Adobe Content Strategy and
we're hiring a Design and Language Standards Lead to help build it." The
post carries none of the apparatus every entry's source text has — no
requisition ID, no Responsibilities/Requirements structure, no stated title
header, no ATS. Applicants route to a named mailbox instead: "Please send
your resume and portfolio to contentfoundationscontractor@adobe.com. (I
won't be able to respond to DMs, so please do use that email address.)"

The role described sits close to the Content Systems Architect role already
in the dataset — terminology systems, voice and tone frameworks "for
traditional UX and conversational AI," cross-functional influence across
design, product, and engineering — and may be the same "Content Foundations"
initiative described from the inside rather than a second one.

It's also the first **contract** engagement surfaced anywhere in the
corpus's research to date: six months initial, "full-time... 40 hours/week,"
extended "as budget allows" — everything else has been permanent hiring.

Held out of `jobs.json` on genre grounds, not content grounds: the schema
and audit process both assume an institutional posting to audit, and a
hiring manager's personal, first-person solicitation isn't one, whatever
else is true about the role underneath it. Not archived to `jd-source`
either, since there's no posting text separate from this LinkedIn post to
preserve against re-audit.

Recorded as a category to watch, not a single incident: informal, off-ATS,
personally-voiced recruiting calls — especially for contract or interim
roles — are a genre the dataset holds out deliberately. A second instance,
of either the informality or the contract-engagement type, is the one to
compare this against; if either recurs, it's worth deciding then whether the
exclusion should become a documented rule rather than a one-off judgment
call.
