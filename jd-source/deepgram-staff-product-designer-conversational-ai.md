---
id: deepgram-staff-product-designer-conversational-ai
company: Deepgram
title: Staff Product Designer, Conversational AI
sourceUrl: null
sourcePlatform: company-site
orgPlacement: "Product (reports to the Director of Product Design, Staff IC)"
postedDate: null
reqId: null
dateAdded: 2026-10-19
captured: 2026-10-19
captureMethod: pasted-from-claude-chat
captureNote: >
  Title discrepancy: the ATS header/job-board title ("Staff Product Designer,
  Conversational AI") was stored verbatim as `title` in jobs.json per the
  user's explicit choice, specifically because it captures the "uniqueness"
  of a role with no established title equivalent elsewhere — even though the
  JD body separately self-names the role "Staff Conversational Designer" in
  its own prose ("We are hiring a Staff Conversational Designer to own
  them"). Both names refer to the same role in the same posting; the user
  chose the ATS/header form for the stored field.

  Cluster/signal grounding, assessed against the corpus's existing
  conversation/voice-design precedent set (Spotify, Gen Digital, UKG, UHG,
  GDS, and Anthropic's Product Designer, Evals & Prompts):

  - model-behavior-design: the role's core charter is authoring the agent's
    conversational behavior itself — persona, turn-taking, repair,
    confirmation, pacing — with zero UI/screen surface anywhere in the
    posting. Assessed as possibly the purest instance of this signal in the
    corpus so far, since for every comparable entry there is at least some
    adjacent screen or UI surface in scope; here confirmation strategy,
    turn-taking, and repair ARE the entire interface.
  - eval-infrastructure: "Establish conversational-quality evals and a
    transcript review practice that turns production failures into a
    repeatable design loop" is direct evaluation-harness/grader ownership,
    not a reported metric.
  - ai-native-expectation: grounded via the "Company Operating Rhythm"
    section's AI-fluency expectations ("AI use and comfort aren't
    optional... every team member... expected to actively use and
    experiment with advanced AI tools"), not via the role's own
    model-behavior work (that grounds ai-tooling instead, per the
    description-versus-use note below).
  - central-standards-function: "Set the conversation-design principles,
    review standards, and shared vocabulary the broader team adopts" —
    a single accountable owner publishing standards other teams consume,
    the structural pattern this signal tracks.
  - governance-as-value-prop: the guardrail language ("confirms something
    consequential before acting," "guardrails that require confirmation
    before high-stakes actions") frames governance/safety behavior as part
    of the product's value, not just an internal QA step.
  - content-systems-design / ai-content-governance / enablement / ai-tooling
    (clusters): grounded in the persona/voice-system ownership, the
    guardrail and confirmation-strategy design, the developer-facing
    enablement work (reference experiences, design guidance for the Voice
    Agent API), and the role's own hands-on eval/model-behavior tooling
    work respectively.

  ai-tooling was resolved per jd-insights/findings.md's documented
  "description versus use" pattern for this key: assigned here via the
  role's own model-behavior/eval-ownership work (building evals, tuning
  behavior against ML/Engineering tradeoffs), not via the JD's
  company-wide AI-fluency section, which grounds ai-native-expectation
  instead.

  technical-writing was considered and explicitly declined. The candidate
  language ("sample dialogs, design guidance... APIs, SDKs, and
  documentation surfaces") is a genuinely different flavor from every
  current technical-writing holder in the corpus, which document internal
  systems, governance models, or data structures — not external
  developer/API-facing documentation. A single instance doesn't clear Step
  4's bar to extend the cluster's actual pattern of use, so this is flagged
  as a first-instance item to watch rather than stretching an existing key
  or creating a new one.
---

Staff Product Designer, Conversational AI
Location

San Francisco, CA
Employment Type

Full time
Location Type

Remote
Department

Product
Compensation

$180K – $240K • Offers Equity • Offers Bonus
See More
Overview
Application
Company Overview
Deepgram is the leading platform underpinning the emerging trillion-dollar Voice AI economy, providing real-time APIs for speech-to-text (STT), text-to-speech (TTS), and building production-grade voice agents at scale. More than 200,000 developers and 1,300+ organizations build voice offerings that are 'Powered by Deepgram', including Twilio, Cloudflare, Sierra, Decagon, Vapi, Daily, Cresta, Granola, and Jack in the Box. Deepgram's voice-native foundation models are accessed through cloud APIs or as self-hosted and on-premises software, with unmatched accuracy, low latency, and cost efficiency. Backed by a recent Series C led by leading global investors and strategic partners, Deepgram has processed over 50,000 years of audio and transcribed more than 1 trillion words. There is no organization in the world that understands voice better than Deepgram.
Company Operating Rhythm
At Deepgram, we expect an AI-first mindset—AI use and comfort aren't optional, they're core to how we operate, innovate, and measure performance.
Every team member who works at Deepgram is expected to actively use and experiment with advanced AI tools, and even build your own into your everyday work. We measure how effectively AI is applied to deliver results, and consistent, creative use of the latest AI capabilities is key to success here. Candidates should be comfortable adopting new models and modes quickly, integrating AI into their workflows, and continuously pushing the boundaries of what these technologies can do.
Additionally, we move at the pace of AI. Change is rapid, and you can expect your day-to-day work to evolve just as quickly. This may not be the right role if you're not excited to experiment, adapt, think on your feet, and learn constantly, or if you're seeking something highly prescriptive with a traditional 9-to-5.
Note: This is a remote role based in Pacific Time, with a preference for candidates located in San Francisco.
About The Role
Deepgram builds the models and APIs that put voice agents into production at scale. What decides whether those agents feel human is not a screen. It is whether the agent knows when you have finished speaking, what it does when you cut it off, how it recovers from a misheard word, how it confirms something consequential before acting, and how it covers the milliseconds it cannot remove.
Today those decisions live inside prompts and pipeline config, made ad hoc by whoever is closest to the problem. No one owns them end to end. We are hiring a Staff Conversational Designer to own them.
You will define how Deepgram's voice agents converse: persona, turn-taking, repair, confirmation, and pacing. You will work directly with ML and Engineering on the tradeoffs that make those behaviors real, including endpointing, barge-in, and latency budgets. You will build the evals that tell us whether a conversation is actually good, and publish the guidance and reference experiences that show developers how to build natural conversations on the Voice Agent API.
This is a leading edge role. Very few companies have a titled equivalent. You will be defining this discipline at Deepgram, not inheriting it.
You'll report directly to the Director of Product Design. This is a Staff IC role, and your impact shows up mostly in the leverage you create for others: the patterns our own experiences run on, and the guidance our customers build against.
Your first chapter: a documented persona and voice system, and turn-taking and repair behavior designed and shipped with Engineering. From there, scope expands into conversational-quality evals and developer-facing guidance.
What You'll Do
Define the persona and voice system for Deepgram voice agents, and keep it coherent across experiences and use cases
Design turn-taking, barge-in, and end-of-turn behavior with ML and Engineering, tuning responsiveness against the risk of interrupting the user, per use case
Design conversational repair, no-match and no-input handling, and confirmation strategy, including guardrails that require confirmation before high-stakes actions
Own latency-aware pacing and perceived responsiveness: brevity, backchanneling, hold and filler speech, all against real-time budgets
Establish conversational-quality evals and a transcript review practice that turns production failures into a repeatable design loop
Build the reference agent experiences and developer-facing design guidance that demonstrate best-practice conversation on the Voice Agent API
Partner with ML and Research on ASR and TTS behavior, and on the quality criteria that define a good conversation
Set the conversation-design principles, review standards, and shared vocabulary the broader team adopts
You'll Love This Role If You
Believe conversation is an interface with real craft behind it, not a prompt someone tunes on the side
Want the hard real-time problems: endpointing, barge-in, and the half-second you cannot design away
Get energized by being foundational, defining what good means for a discipline that does not exist here yet
Think the fastest way to raise quality is to make it measurable, then make it repeatable
Are excited by a category still inventing its interaction patterns, where the work is invention rather than iteration
It's Important To Us That You Have
We care more about expertise and leadership than years of experience.
Deep experience designing conversational behavior for LLM-based voice agents or assistants, not only scripted IVR flows
Real fluency with the speech pipeline, from ASR through LLM to TTS, and a working understanding of where design decisions actually live inside it
A track record designing turn-taking, interruption, repair, and confirmation patterns that shipped and held up in production
Evidence of building quality measurement into the practice: evals, transcript review, benchmarks, or a structured failure-analysis loop
Exceptional writing craft, including sample dialogs, design guidance, and documentation that others can build against
Experience influencing engineering and ML partners on behavior they own, without authority over them
Experience designing for developers or technical users, including APIs, SDKs, and documentation surfaces
A working AI practice, with a point of view on where these tools help and where they mislead
It Would Be Great If You Had
Time on a named assistant or a production voice agent platform
Practice with Wizard of Oz testing and sample dialog methods
Hands-on work with eval tooling for LLM or voice quality
Experience in high-stakes or regulated conversation domains where confirmation and recovery carry real cost
Multilingual or cross-locale conversation design experience
Background in high-growth B2B companies with both self-serve and enterprise motions
