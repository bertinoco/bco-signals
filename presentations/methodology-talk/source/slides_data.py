# Slide data for the methodology talk. One dict per slide.
# types: section, statement, quote, finding, contrast, evidence
# Keys: kicker, headline, body, quotes[(text, attr)], aside(label, text),
#       numeral, caption, cards[(label, value, note)], notes, ph (placeholder flag)
# Quote text carries no outer quote marks; CSS adds them.

SECTIONS = {
    2: ("02", "The process catching itself"),
    3: ("03", "What messy data looks like"),
    4: ("04", "What the discipline produced"),
    5: ("05", "What this can’t tell you"),
    6: ("06", "Where it’s headed"),
}

S = []

# ---------- SECTION 1 ----------
S.append(dict(type="statement", kicker="Cold open",
    headline="[Why I started counting job postings]",
    body="[Your reason for building the dataset, in your words. One or two sentences.]",
    ph=True,
    notes="PLACEHOLDER. This is your story, not something to draft for you. Replace the headline and body, or turn it into a single quote slide."))

S.append(dict(type="contrast", kicker="The ground rules",
    headline="Every finding keeps two things apart.",
    cards=[("What the data shows", "You can defend it by linking to a posting.", ""),
           ("What I think it means", "A byline opinion, labeled as one.", "")],
    body="And a finding is never evidence for a cluster or signal assignment. Assignments come from posting text alone.",
    notes="This is the rule that makes everything after it checkable. Source: findings.md preamble. Say it plainly, then point at it every time a slide is labeled “My take.”"))

# ---------- SECTION 2 ----------
S.append(dict(type="section", sec=2))

S.append(dict(type="statement", kicker="The correction",
    headline="I claimed two instances. There was one.",
    body="Notion and Spotify were my two examples of content built for machine consumption. Checked against the entries, Spotify’s Annotation Manager is ML training data and its Conversation Designer is model behavior. Neither is retrieval. What remained was Notion alone.",
    aside=("What I did", "Corrected it in place and recorded it as a correction, not a quiet fix."),
    notes="The point of this slide is that the process catches its own claims. Keep it short and unembarrassed."))

S.append(dict(type="quote", kicker="Then the data answered",
    headline="Two real instances arrived on their own.",
    quotes=[("…for real-time access by AI agents and content generation systems.", "Meta, AI Content Strategy Lead"),
            ("content knowledge assets that AI can call on and reuse", "Alibaba, AI Content Strategist")],
    notes="Confirms the corrected claim rather than the wrong one. Verify the Alibaba wording against the stored quote before presenting."))

S.append(dict(type="quote", kicker="The near-miss",
    headline="Reads like the thing we track. Excluded.",
    quotes=[("Agents are only as good as the knowledge they can reach.", "Redpine, Senior Knowledge Graph Engineer")],
    body="It classifies real-world entities (drugs, trials, companies, filings) for machine reasoning. Not content for navigation. A trigger was written down for what would change the call.",
    notes="Redpine is dense, specific, and well argued, which is exactly why it is a good test. Terminology: ontology here means entity types and relations for real-world facts, not the taxonomy cluster."))

S.append(dict(type="quote", kicker="The trigger, tested",
    headline="Ontology work paired with a content deliverable.",
    quotes=[("Develop and extend ontologies and structured content systems that enable scalable, consistent AI behavior.", "UKG")],
    body="The pairing, in the same responsibility, grounds the assignment. It was withheld from Redpine.",
    notes="This is the trigger from the Redpine exclusion resolving months later. The boundary holds under a real test, not just an assertion."))

S.append(dict(type="statement", kicker="A second test",
    headline="Same boundary, different industry.",
    body="Schneider Electric’s ontology lead builds ontologies for “products, systems, devices, points, relationships, behaviors, and operational concepts.” Real-world things, not content. Two unrelated domains is stronger evidence than repetition inside one.",
    notes="An industrial conglomerate versus an early-stage AI startup. The backcheck treats cross-domain recurrence as stronger than same-domain repetition."))

S.append(dict(type="quote", kicker="The closest call",
    headline="Denser writing language than some entries we included. Excluded.",
    quotes=[("Writing as a craft. You treat language as load-bearing. You catch the sentence that will be misread before it ships.", "Basis, Intelligence Architect")],
    body="The posting itself names seven co-equal candidate backgrounds, among them engineers, philosophers, lawyers, accountants, editors, and academics.",
    notes="Verify the list of seven against jd-source/basis before presenting. The reason is new: the posting’s own theory of who succeeds denies that any single discipline defines the role."))

S.append(dict(type="statement", kicker="A title match, the wrong discipline",
    headline="Content Designer, at a game studio.",
    body="Scopely’s posting lists “content design, game design, narrative design, game writing, creative development” as interchangeable. None of its ten responsibilities mapped to any cluster.",
    aside=("Compare", "Roblox’s Content Designer was also excluded, but it was genuine product content design that only failed the signal test. Scopely never reaches that question."),
    notes="Same title, different discipline underneath. Quote on the slide is a fragment of the qualifications line; full line is in the CLAUDE.md terminology section."))

S.append(dict(type="statement", kicker="Excluding without discarding",
    headline="Excluded does not mean irrelevant.",
    body="DeepMind’s Senior Manager role was excluded because management dominates its responsibilities. It still held responsibilities that ground cleanly.",
    aside=("The rule", "An exclusion record names exactly which clusters and signals would have applied, with the grounding quotes. It never goes in the dataset, but the archive carries the evidence."),
    notes="That record later supplied an existence-only instance for the judgment-and-taste finding (slides 24 to 27)."))

S.append(dict(type="statement", kicker="Testing the safeguard",
    headline="A longer word list wouldn’t have helped.",
    body="The pre-check scans for seven words: content, writing, language, copy, tone, voice, terminology. Notion’s Model Behavior Engineer scored two hits, and both were idioms: “Be the voice of quality in the room” and “help write the playbook.”",
    aside=("The actual safeguard", "Read each hit in context. Widen the list only when a real miss appears. None has."),
    notes="A stemmed or wider list would have logged the same false positive twice."))

# ---------- SECTION 3 ----------
S.append(dict(type="section", sec=3))

S.append(dict(type="statement", kicker="Titles lie about identity",
    headline="Same title, two different postings.",
    body="Apple posted two requisitions titled “UX Writer, Systems,” with different req IDs. Anything keyed on title alone eventually attaches the wrong text to an entry.",
    aside=("So", "Every entry stores a reqId when the posting states one."),
    notes=""))

S.append(dict(type="quote", kicker="A quote needs to be role-specific",
    headline="Boilerplate isn’t evidence.",
    quotes=[("As a UX writer, you are an advocate for Google design…", "Google, Search, Chrome, and YouTube postings alike")],
    body="Only the middle paragraph differs. A quote lifted from the shared section says nothing about the role. DeepMind shares none of it.",
    notes=""))

S.append(dict(type="quote", kicker="A quote can fail on legibility",
    headline="An acronym nobody defined.",
    quotes=[("You’re the design DRI, in Figma or with agentic tools, through to shipped.", "Bolt.new, first choice, rejected")],
    aside=("The fix", "DRI is never defined in the posting. The same paragraph family said it without jargon: “You can take a content-led feature from problem to shipped without a product designer.”"),
    notes="Rule: read a candidate quote as a first-time visitor would. Documented in CLAUDE.md after this miss."))

S.append(dict(type="statement", kicker="Invisible errors",
    headline="Some mistakes don’t show on screen.",
    body="Six stored quotes needed one character fixed: five apostrophes and one hyphen. DeepMind’s scraped text carries icon-font names where the page showed icons: “corporate_fare,” “place,” “info_outline.”",
    aside=("Left in on purpose", "The archive keeps the text verbatim. Its value is that it’s unedited."),
    notes=""))

S.append(dict(type="statement", kicker="Building the schema live",
    headline="Two languages, two new fields.",
    body="Coupang’s posting arrived in Korean. Alibaba’s arrived in Chinese. Two fields, quoteTranslatedFrom and titleTranslatedFrom, were built when the data demanded them, not before.",
    aside=("On the site", "Both render as a visible caption, so a reader never mistakes a translation for verbatim source text."),
    notes=""))

S.append(dict(type="quote", kicker="Relevant, and still held out",
    headline="A genre problem, not a content problem.",
    quotes=[("We’re building a new Content Foundations team… we’re hiring a Design and Language Standards Lead.", "An Adobe content design leader, on her own LinkedIn feed")],
    body="No requisition, no title header, no applicant system. The audit assumes an institutional posting to audit.",
    notes=""))

# ---------- SECTION 4 ----------
S.append(dict(type="section", sec=4))

S.append(dict(type="finding", kicker="Finding",
    headline="Content standards are being pulled into central functions.",
    numeral="19", caption="of 78 postings (24%), as of Oct 2026, on a close read. The raw tag count is 22.",
    quotes=[("…serve as Netflix’s centralized authority for scaling language standards.", "Netflix, from the posting")],
    notes="MY TAKE: content design is being reconstituted as infrastructure, a small central group owning primitives and product teams consuming them. Not the only model: Wealthsimple is hiring for “You’ll be embedded on product teams.” A fork, not a replacement. GDS and Vinted carry the tag but don’t hold on a close read. This number moved from 8 of 29 to 19 of 78 as the corpus grew, which is why every count carries a date. Also verify Robinhood (tagged, not supported by source text). Ally: “sits above channels and formats” is from the posting text, not the stored quote."))

S.append(dict(type="finding", kicker="Finding",
    headline="The work moved from producing content to producing systems.",
    numeral="72", caption="of 78 postings (92%), as of Oct 2026. A direct cluster count.",
    quotes=[("Not by writing content yourself, but by building AI-powered systems.", "CoLab, from the dataset")],
    notes="MY TAKE: the unit of work shifted from the artifact to the mechanism that produces artifacts. Ally: “focused less on creating content and more on making content work.”"))

S.append(dict(type="finding", kicker="Finding",
    headline="AI fluency is a baseline, not a differentiator.",
    numeral="52", caption="of 78 postings (67%), as of Oct 2026, expect the candidate to already work with AI tools.",
    quotes=[("Claude Code, Gemini, or Figma AI", "HelloFresh, naming the tools")],
    notes="MY TAKE: whether a role touches AI does not track whether the employer builds AI. What predicts the job is whether the content function has a systems mandate. Wealthsimple asks for “shipping your own code changes.” Verify the HelloFresh fragment against the stored quote."))

# Judgment and taste: full depth
S.append(dict(type="finding", kicker="Finding, in full",
    headline="Judgment and taste are what’s asked for once AI does the drafting.",
    numeral="8", caption="included postings across five domains: SaaS, Agency, Big Tech, Finance, Retail.",
    body="Each pairs judgment or taste directly against AI-generated output. Not a soft-skill throwaway.",
    notes="What the data shows, part 1. CoLab, Docebo, Fin, Soda (SaaS); Intercept (Agency); Meta (Big Tech); Sanna (Finance); Gap (Retail, the first in that domain). SaaS is the only domain repeated."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="Two of the eight, in their own words.",
    quotes=[("you’ll act as Editor in Chief: orchestrating AI agents and applying editorial judgment across outputs.", "CoLab"),
            ("Taste is the bar. Anti-slop is the whole point. An engine that ships slop faster has negative value.", "Soda")],
    notes="Others in the count: Intercept (“Strong editorial judgment and comfort challenging weak AI-generated outputs”), Sanna (“We value judgment, taste, and learning ability over years of experience or specific tools”), Docebo, Fin, Meta. Soda quote: check whether to add “and most of them do.”"))

S.append(dict(type="quote", kicker="What the data shows",
    headline="And the first one in retail.",
    quotes=[("AI will write plausible copy at volume all day, which makes judgment about what is worth saying the scarce skill rather than the throughput.", "Gap Inc.")],
    aside=("Checked and left out", "Wealthsimple’s one “judgment” hit is about AI screening job applicants, not the role’s own work."),
    notes="A ninth instance sits in an excluded record (DeepMind: “high taste, creativity… high judgement in order to define what good quality looks like”), existence evidence only. Gap is the first instance in the Retail domain."))

S.append(dict(type="statement", kicker="My take",
    headline="What’s left for the human once fluency is assumed.",
    body="This is a sharper version of the AI-fluency finding. That one says AI use is the baseline. This one says the postings draw a line between what the tool produces and what a person is still accountable for deciding is good.",
    aside=("Caveat", "Five domains with no repeated employer is real spread, though SaaS accounts for four of the eight. This counts postings that use certain words. It doesn’t measure how much judgment the work needs."),
    notes="Label this slide as opinion, per the ground rules."))

# Evaluation infrastructure: full depth
S.append(dict(type="statement", kicker="Finding, in full",
    headline="Evaluation infrastructure is generative work, built as software.",
    body="Generative content work authors a generator’s constraints and the criteria for judging what it emits. An eval harness is that criteria, operationalized as software rather than a hand-run rubric.",
    aside=("Placeholder: decide the count", "findings.md names four companies in three domains (Spotify, Anthropic, Soda, Glean). The signal is now on six entries in five domains. Etsy is verified; Huge’s grounding is not."),
    ph=True,
    notes="What the data shows, part 1. Replace the placeholder aside with the chosen count before presenting."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="The work, in the postings’ words.",
    quotes=[("Build evaluation frameworks to measure and improve conversation quality, accuracy, task completion, and user impact.", "Spotify"),
            ("Serious prompt engineering: multi-step LLM pipelines with structured outputs and evals, not chatting with a model.", "Soda")],
    notes="Anthropic is built around writing and revising the prompts behind Claude’s product surfaces, then building the graders and harness that prove a prompt fix holds across model releases. That is a paraphrase from the finding; pull the verbatim line from the posting."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="And what excluded the near-misses.",
    quotes=[("Create evaluations and guardrails for AI-generated and AI-maintained documentation, investigate failures, and improve the context, tools, prompts, and systems that shape output quality.", "Glean")],
    aside=("Audit work", "Notion and Microsoft do real eval work and stay excluded: no design org, no content or design title, a clean literal-text check. Anthropic clears all three bars."),
    notes="This calls back to the Section 2 near-misses: not a loosening of eligibility."))

S.append(dict(type="statement", kicker="My take",
    headline="Hiring filters built on writing craft will undercount this.",
    body="The most technical generative-side postings gate on engineering skill, not a writing portfolio, because validating language at scale is an engineering problem even when the thing validated is language.",
    aside=("Caveat", "Expect this signal to stay thin for a while. It names a real pattern, not yet a common one."),
    notes="This finding is the dataset’s blind side showing up concretely. It sets up slide 40."))

S.append(dict(type="statement", kicker="Finding",
    headline="Nobody agrees what this work is worth.",
    body="Stated ranges run from $62,120 to $710,000. 51 of 78 postings state one, as of Oct 2026.",
    aside=("My take", "An order of magnitude between roles with adjacent titles is not a seniority gap. It’s an absence of consensus about what the discipline is."),
    notes="Insurify ($65,000 USD) and Netflix ($710,000) were the original endpoints and both carried “Systems” in the title. Don’t put comp on a slide as a comparison across currencies."))

S.append(dict(type="contrast", kicker="Finding",
    headline="Titles are failing in both directions at once.",
    cards=[("Claims more than the job", "Insurify, Intercept", "“Editor, AI Content Systems.” “Content Engineer.”"),
           ("Claims less than the job", "Wellhub, Figma, Splunk", "“UX Writer, AI.” “Content Designer.”")],
    notes="title-dilution has two holders; title-responsibility-gap has three. Six employers have now appended a disclaimer to their own title."))

S.append(dict(type="quote", kicker="The posting disclaims its own title",
    headline="Employers compensate in the paragraph under the title.",
    quotes=[("While the title of this role is “UX Writer,” you might think of yourself as a content engineer as much as a writer.", "Figma, from the dataset")],
    aside=("An excluded case", "TikTok’s “Content Design Manager, AI” has AI in the title and nowhere else in the posting. Existence evidence only."),
    notes="MY TAKE: titles have stopped reliably carrying scope, and employers compensate in the two places that show up in a posting: the number, and the paragraph under the title."))

S.append(dict(type="finding", kicker="Finding",
    headline="Content roles are appearing outside design orgs.",
    numeral="57", caption="of 78 postings state where the role sits, as of Oct 2026, and placements don’t cluster in design.",
    body="HelloFresh: Software Engineering. Ally: Marketing. Notion: Customer Experience. Trustly: Tech.",
    notes="MY TAKE: the discipline is being claimed by several functions at once and none has won. The conversation about content design’s future assumes it stays in design. The postings don’t. Five more postings record that they don’t state a placement; 16 are null."))

# ---------- SECTION 5 ----------
S.append(dict(type="section", sec=5))

S.append(dict(type="quote", kicker="Not a market sample",
    headline="This shows one slice of the market.",
    quotes=[("Entries are admitted only if they pass a signal test… It shows what ambitious employers are asking for. It says nothing about the median content design job.", "findings.md")],
    notes="Near-verbatim from the findings file’s own admissions. Confirm the exact wording against the current file before presenting."))

S.append(dict(type="statement", kicker="Invisible change",
    headline="Role change without a hiring event leaves no trace.",
    body="Work that arrives by internal pivot produces no posting. The clearest example on file is practitioners already doing systems and model-design work inside existing orgs, with no new requisition.",
    notes=""))

S.append(dict(type="statement", kicker="Existence, not rate",
    headline="Excluded records prove a pattern exists. Not how often.",
    body="YouTube and Nscale are AI companies posting content roles with no AI in the work. TikTok has AI in a title and nowhere else. DeepMind is a ninth judgment-and-taste instance. None of them supports “X% of postings do this.”",
    notes=""))

S.append(dict(type="quote", kicker="The known blind side",
    headline="The generative side is harder to catch.",
    quotes=[("The corpus contains almost no postings that ask for the generative side by name.", "CLAUDE.md, Terminology")],
    body="The evaluation-infrastructure finding is that gap showing up concretely.",
    notes="Sets up the closing section: the instrument is still being tuned."))

# ---------- SECTION 6 ----------
S.append(dict(type="section", sec=6))

S.append(dict(type="finding", kicker="Still growing",
    headline="A live instrument, not a survey taken once.",
    numeral="78", caption="entries, as of Oct 2026. The dataset had 30 when the first version of this talk was drafted.",
    body="Every number here was recomputed the day it was written. The repo’s public Findings tab carries no counts, for the same reason.",
    notes=""))

S.append(dict(type="statement", kicker="Explore it",
    headline="Read the postings yourself.",
    body="signals.bertino.co",
    aside=("What’s there", "Every entry, cluster, and signal is browsable on the site. No GitHub account needed."),
    notes="Confirm the closing claim and URL before presenting."))
