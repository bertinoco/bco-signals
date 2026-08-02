# Patterns in how job descriptions are written

Observations about the postings as documents — how employers structure, word,
and format them. Distinct from what the roles ask for, which is the dataset's
job.

Hand-written. Add to it when a posting does something notable; most don't.
Every claim here should name the companies it came from, so a reader can go to
`jd-source/` and check.

---

## Roles defined by what they are not

Four postings define scope by exclusion, and the more senior the role, the more
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
- **Figma** mixes typographic and straight apostrophes within single sections —
  "Figma’s platform" and "whether you're brainstorming" sit in the same
  sentence, and "We’d love to hear from you" in the body becomes "We'd love to
  hear from you if you have:" as a heading four paragraphs later. Consistent
  with a posting assembled from more than one source document.

Six of the stored quotes needed a character corrected to match their source —
five apostrophes and one hyphen. None was visible on screen.

## Where the posting was captured from changes what you get

Company careers pages give clean text, and often a requisition number and
posted date. LinkedIn captures carry applicant counts, Premium upsell prompts,
alumni modules, and "No longer accepting applications" banners — but sometimes
also carry the only surviving copy of a posting that has since closed.

Insurify's own careers page opens with a fraudulent-job-advert warning before
the posting begins.
