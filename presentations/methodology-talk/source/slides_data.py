# Slide data for the methodology talk. One dict per slide.
# Structure: the idea, how it's set up, what it found. Findings are the bulk.
# types: section, statement, quote, finding, contrast, rows
# Keys: kicker, headline, body, quotes[(text, attr)], aside(label, text),
#       numeral, caption, cards[(label, value, note)], rows[(label, desc)],
#       notes, ph (placeholder flag)
# Quote text carries no outer quote marks; CSS adds them.

SECTIONS = {
    2: ("02", "How it’s set up"),
    3: ("03", "What it found"),
}

S = []

# =====================================================================
# 01  THE IDEA
# =====================================================================
S.append(dict(type="quote", kicker="Cold open",
    quotes=[("Automate the frontend.", "Design leader at an AI-native startup")],
    body="That\u2019s when I started noticing the other signals, and tracking them to stay ahead.",
    notes="From your account of the conversation. Confirm that \u201cautomate the frontend\u201d is the phrase as it was said, since the quote marks claim it was verbatim. The company is deliberately not named."))

S.append(dict(type="contrast", kicker="The idea",
    headline="Track the postings that signal change.",
    cards=[("What I track", "Interesting, ambitious, forward-leaning postings.", "Mostly senior-level individual contributor roles."),
           ("What I look for", "Where the description is signaling change.", "Not the median content design job.")],
    notes="Paraphrased from the README pitch: “I’ve started to track interesting, ambitious, or forward leaning job postings. These are mostly senior-level IC roles where the description is signaling change.” That filter is the whole idea, and also the main limit: this shows what ambitious employers ask for."))

S.append(dict(type="contrast", kicker="The ground rules",
    headline="Every finding keeps two things apart.",
    cards=[("What the data shows", "You can defend it by linking to a posting.", ""),
           ("What I think it means", "A byline opinion, labeled as one.", "")],
    body="And a finding is never evidence for a cluster or signal assignment. Assignments come from posting text alone.",
    notes="This is the rule that makes everything after it checkable. Source: findings.md preamble. Point back at it every time a slide is labeled “My take.”"))

# =====================================================================
# 02  HOW IT'S SET UP  (a walkthrough of the README)
# =====================================================================
S.append(dict(type="section", sec=2))

S.append(dict(type="rows", kicker="Setup · Structure",
    headline="Four folders and a rulebook.",
    rows=[("docs/data/jobs.json", "The dataset. One structured entry per role."),
          ("jd-source/", "The posting text, word for word. One file each."),
          ("jd-insights/", "Stats, quotes, patterns, findings."),
          ("jd-scout/", "The weekly search for new postings."),
          ("CLAUDE.md", "The rulebook: criteria and audit steps.")],
    notes="This is the README’s structure section. The dataset also publishes as the site at signals.bertino.co. CLAUDE.md is the file both Claude and I work from."))

S.append(dict(type="rows", kicker="Setup · Data schema",
    headline="What one entry holds.",
    rows=[("title", "Verbatim, as the posting words it."),
          ("clusters", "Responsibility areas, from the posting’s stated text."),
          ("signals", "Skills and observable patterns."),
          ("compRange", "Min, max, currency, and what the range covers."),
          ("quote", "One verbatim line that anchors the assignments.")],
    notes="Example entry to show on screen if you want one: CoLab, Content Systems Architect. clusters: content-systems-design, ai-tooling, enablement. signals: ai-native-expectation, content-marketing-adjacent. Other fields: company, domain, location, remote, sourceUrl, dateAdded, note. Two optional fields, quoteTranslatedFrom and titleTranslatedFrom, exist for non-English postings and render as a visible caption so a translation is never mistaken for verbatim text."))

S.append(dict(type="finding", kicker="Setup · The taxonomy",
    headline="Assigned only when the posting says so.",
    numeral="8 · 16", caption="clusters and signals. A responsibility the posting doesn’t state doesn’t get the tag, however likely it seems.",
    notes="8 clusters (responsibility areas) and 16 signals (skills and patterns). A new key needs evidence across multiple postings; a single instance is noted but doesn’t get one. That rule is in CLAUDE.md, Step 4 of the audit."))

S.append(dict(type="finding", kicker="Setup · The archive",
    headline="Every posting is kept, word for word.",
    numeral="131", caption="archived postings: 78 in the dataset, 53 excluded with the reason written down.",
    aside=("Why", "Nothing is cleaned up, and page chrome stays in. The archive is what every audit and recount reads from, so it has to be unedited."),
    notes="One markdown file per posting in jd-source/, front matter plus the raw text. An excluded file records why, so the same posting isn’t re-audited from scratch or quietly added later."))

S.append(dict(type="rows", kicker="Setup · Automation, finding",
    headline="A weekly search finds candidates. A person decides.",
    rows=[("1  Discover", "Searches for company boards not yet on the list."),
          ("2  Poll", "Reads Greenhouse, Lever, and Ashby job feeds."),
          ("3  Filter", "Drops anything already archived or already seen."),
          ("4  Triage", "A page where each posting is Audit, Later, or Skip.")],
    aside=("Every Sunday", "An unattended Claude Code session runs it. It never audits, writes data, or commits."),
    notes="JD Scout, in jd-scout/. A scheduled Routine starts a fresh session that follows ROUTINE.md. Matching is keyword-based (title terms, plus body phrases for noisier matches). Postings from boards that never reach LinkedIn are the point."))

S.append(dict(type="rows", kicker="Setup · Automation, audit",
    headline="One posting, one confirmation.",
    rows=[("Eligibility", "Required criteria, then a signal test."),
          ("Audit", "Clusters and signals from the text alone."),
          ("Report", "What was assigned and why. New keys flagged, not created."),
          ("Confirm", "I approve, or the posting is archived as excluded."),
          ("Write", "Entry, archive, and stats updated in one pass.")],
    aside=("/add-jd", "A slash command. Subagents do the reading, so the main conversation only carries the decisions that need me."),
    notes="This is the audit process in CLAUDE.md, run through the /add-jd command. Depth is a judgment call per posting: shallow for a clean match to an existing pattern, deep for anything borderline or new."))

S.append(dict(type="rows", kicker="Setup · The loops",
    headline="Checks that close the loop.",
    rows=[("test_scout.py", "Every entry must pass the scout’s filter. If one wouldn’t have been found, the keywords get widened."),
          ("refresh.py", "Regenerates stats and quotes from the data. Never edited by hand."),
          ("check-jobs-json.py", "Runs in CI: unknown keys, duplicate ids, drifting counts."),
          ("asset version check", "Fails if a changed script or stylesheet ships without a version bump.")],
    notes="The first one is the real feedback loop: what the dataset includes tunes what the scout looks for. The asset check exists because a missed cache bump shipped a stale site twice."))

# =====================================================================
# 03  WHAT IT FOUND  (the bulk of the talk)
# =====================================================================
S.append(dict(type="section", sec=3))

S.append(dict(type="finding", kicker="Finding",
    headline="The work moved from producing content to producing systems.",
    numeral="72", caption="of 78 postings (92%), as of Oct 2026. A direct cluster count.",
    quotes=[("Not by writing content yourself, but by building AI-powered systems.", "CoLab, from the dataset")],
    notes="MY TAKE: the unit of work shifted from the artifact to the mechanism that produces artifacts. Ally: “focused less on creating content and more on making content work.”"))

S.append(dict(type="finding", kicker="Finding",
    headline="Content standards are being pulled into central functions.",
    numeral="19", caption="of 78 postings (24%), as of Oct 2026, on a close read. The raw tag count is 22.",
    quotes=[("…serve as Netflix’s centralized authority for scaling language standards.", "Netflix, from the posting")],
    notes="MY TAKE: content design is being reconstituted as infrastructure, a small central group owning primitives and product teams consuming them. Not the only model: Wealthsimple is hiring for “You’ll be embedded on product teams.” A fork, not a replacement. GDS and Vinted carry the tag but don’t hold on a close read. This number moved from 8 of 29 to 19 of 78 as the corpus grew, which is why every count carries a date. Also verify Robinhood (tagged, not supported by source text). Ally: “sits above channels and formats” is from the posting text, not the stored quote."))

S.append(dict(type="finding", kicker="Finding",
    headline="AI fluency is a baseline, not a differentiator.",
    numeral="52", caption="of 78 postings (67%), as of Oct 2026, expect the candidate to already work with AI tools.",
    quotes=[("Claude Code, Gemini, or Figma AI", "HelloFresh, naming the tools")],
    notes="MY TAKE: whether a role touches AI does not track whether the employer builds AI. What predicts the job is whether the content function has a systems mandate. Wealthsimple asks for “shipping your own code changes.” HelloFresh fragment verified against the source."))

# Judgment and taste: full depth
S.append(dict(type="finding", kicker="Finding, in full",
    headline="Judgment and taste are what’s asked for once AI does the drafting.",
    numeral="10", caption="included postings across five domains: SaaS, Agency, Big Tech, Finance, Retail.",
    body="Each pairs judgment or taste directly against AI-generated output. Not a soft-skill throwaway.",
    notes="What the data shows, part 1. CoLab, Docebo, Fin, Soda, Glean (SaaS); Intercept (Agency); Meta (Big Tech); Sanna, Ethos (Finance); Gap (Retail, the first in that domain). SaaS has five of the ten and Finance two. Glean and Ethos were added on a recount against the source texts in Oct 2026; findings.md still says eight. Ethos is the softer fit. A second Meta posting (AI Content Strategy Lead) is borderline and not counted."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="Two of the ten, in their own words.",
    quotes=[("you’ll act as Editor in Chief: orchestrating AI agents and applying editorial judgment across outputs.", "CoLab"),
            ("Taste is the bar. Anti-slop is the whole point. An engine that ships slop faster has negative value, and most of them do.", "Soda")],
    notes="Others in the count: Intercept (“Strong editorial judgment and comfort challenging weak AI-generated outputs”), Sanna (“We value judgment, taste, and learning ability over years of experience or specific tools”), Docebo, Fin, Meta. Soda’s line is now the full source sentence."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="And the first one in retail.",
    quotes=[("AI will write plausible copy at volume all day, which makes judgment about what is worth saying the scarce skill rather than the throughput.", "Gap Inc.")],
    aside=("Checked and left out", "Wealthsimple’s one “judgment” hit is about AI screening job applicants, not the role’s own work."),
    notes="A ninth instance sits in an excluded record (DeepMind: “high taste, creativity… high judgement in order to define what good quality looks like”), existence evidence only. Gap is the first instance in the Retail domain."))

S.append(dict(type="statement", kicker="My take",
    headline="What’s left for the human once fluency is assumed.",
    body="This is a sharper version of the AI-fluency finding. That one says AI use is the baseline. This one says the postings draw a line between what the tool produces and what a person is still accountable for deciding is good.",
    aside=("Caveat", "Five domains with no repeated employer is real spread, though SaaS accounts for five of the ten. This counts postings that use certain words. It doesn’t measure how much judgment the work needs."),
    notes="Label this slide as opinion, per the ground rules."))

# Evaluation infrastructure: full depth
S.append(dict(type="finding", kicker="Finding, in full",
    headline="Evaluation infrastructure is generative work, built as software.",
    numeral="6", caption="postings across five domains: Media, Big Tech, SaaS, Agency, E-commerce.",
    body="Generative content work authors a generator\u2019s constraints and the criteria for judging what it emits. An eval harness is that criteria, operationalized as software rather than a hand-run rubric.",
    notes="What the data shows, part 1. Count verified against the source texts as of Oct 2026: Spotify, Anthropic, Soda, Glean, Etsy (\u201cset the eval framework that determines if the output meets the quality bar\u201d), and Huge (\u201cDevelop golden queries and responses to benchmark quality and ensure safe, consistent outputs\u201d). findings.md still says four companies in three domains; the live signal and the source texts say six in five."))

S.append(dict(type="quote", kicker="What the data shows",
    headline="The work, in the postings’ words.",
    quotes=[("Build evaluation frameworks to measure and improve conversation quality, accuracy, task completion, and user impact.", "Spotify"),
            ("Serious prompt engineering: multi-step LLM pipelines with structured outputs and evals, not chatting with a model.", "Soda")],
    notes="Anthropic, verbatim from the posting: “Write and revise the prompts behind Claude’s tools, features, and behaviors on a product surface” and “Build the graders that prove a prompt fix and rerun on the next model.”"))

S.append(dict(type="quote", kicker="What the data shows",
    headline="And what excluded the near-misses.",
    quotes=[("Create evaluations and guardrails for AI-generated and AI-maintained documentation, investigate failures, and improve the context, tools, prompts, and systems that shape output quality.", "Glean")],
    aside=("Audit work", "Notion and Microsoft do real eval work and stay excluded: no design org, no content or design title, a clean literal-text check. Anthropic clears all three bars."),
    notes="Not a loosening of eligibility: the audit rules kept those two out for reasons independent of this pattern."))

S.append(dict(type="statement", kicker="My take",
    headline="Hiring filters built on writing craft will undercount this.",
    body="The most technical generative-side postings gate on engineering skill, not a writing portfolio, because validating language at scale is an engineering problem even when the thing validated is language.",
    aside=("Caveat", "Expect this signal to stay thin for a while. It names a real pattern, not yet a common one."),
    notes="This finding is the dataset’s blind side showing up concretely: the deterministic side is easier to catch than the generative side."))

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

S.append(dict(type="statement", kicker="Finding",
    headline="Nobody agrees what this work is worth.",
    body="Stated ranges run from $62,120 to $710,000. 51 of 78 postings state one, as of Oct 2026.",
    aside=("My take", "An order of magnitude between roles with adjacent titles is not a seniority gap. It’s an absence of consensus about what the discipline is."),
    notes="Insurify ($65,000 USD) and Netflix ($710,000) were the original endpoints and both carried “Systems” in the title. Don’t put comp on a slide as a comparison across currencies."))

S.append(dict(type="finding", kicker="Finding",
    headline="Content roles are appearing outside design orgs.",
    numeral="57", caption="of 78 postings state where the role sits, as of Oct 2026, and placements don’t cluster in design.",
    body="HelloFresh: Software Engineering. Ally: Marketing. Notion: Customer Experience. Trustly: Tech.",
    notes="MY TAKE: the discipline is being claimed by several functions at once and none has won. The conversation about content design’s future assumes it stays in design. The postings don’t. Five more postings record that they don’t state a placement; 16 are null."))

S.append(dict(type="contrast", kicker="Still forming",
    headline="Two kinds of work are getting their own titles.",
    cards=[("Taxonomy", "Meta, Vinted", "\u201cTaxonomist, Content Design.\u201d \u201cTaxonomist, Supply.\u201d"),
           ("AI content strategy", "Meta, Alibaba, Huge", "\u201cAI Content Strategy Lead.\u201d \u201cDirector, AI Content Strategy.\u201d")],
    aside=("My take", "Early and thin: two postings, and three. As the work matures it may claim its own title instead of staying a line item."),
    notes="Both findings say they are thin. Taxonomy: the cluster is on 28 entries now, but only Meta and Vinted make it the whole title, and Vinted\u2019s posting never invokes content design (placement is Product Management), so it survives on what the work classifies. Trigger to revisit: a third taxonomy title with no content-design framing. AI content strategy: Meta and Alibaba share a domain; Huge adds Agency and the first Director level. Trigger: a fourth outside Big Tech and Agency."))

S.append(dict(type="rows", kicker="What this can’t tell you",
    headline="Five limits, stated plainly.",
    rows=[("Not a market sample", "Admitted only if they pass a signal test. It says nothing about the median job."),
          ("No pivots", "Role change inside an existing team produces no posting."),
          ("Existence, not rate", "An excluded record proves a pattern exists, not how often."),
          ("Counts are a floor", "A tag created later isn’t applied to older entries unless someone goes back."),
          ("A blind side", "The generative side is harder to catch than the deterministic side.")],
    notes="The first four rows follow findings.md’s “What this data cannot support” section (verified against the current file). The last is not from that section: it echoes CLAUDE.md’s Terminology note that the corpus contains almost no postings that ask for the generative side by name. The “floor” row is that section’s own point: frequency counts are a floor, not a measurement. Worth saying aloud, given how many counts are in this deck."))

S.append(dict(type="statement", kicker="Explore it",
    headline="Read the postings yourself.",
    body="signals.bertino.co",
    aside=("What’s there", "Every entry, cluster, and signal is browsable on the site. No GitHub account needed."),
    notes="Confirm the closing claim and URL before presenting. Counts are as of Oct 2026 (78 postings); every number in this deck was recomputed that day, which is also why the site’s public Findings tab carries no counts."))
