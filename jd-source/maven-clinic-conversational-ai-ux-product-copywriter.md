---
id: maven-clinic-conversational-ai-ux-product-copywriter
company: Maven Clinic
title: Conversational AI & UX/Product Copywriter (Contract)
sourceUrl: null
sourcePlatform: company-site
orgPlacement: "Member Copy, Comms & Content team"
postedDate: null
reqId: null
dateAdded: 2026-10-28
captured: 2026-10-28
captureMethod: pasted-from-claude-chat
captureNote: >
  `compRange` is omitted entirely (not recorded as `null` with a stated
  figure) because the JD states an hourly rate ("$90-100 per hour for 20 hrs
  a week"), not an annual figure, and every existing `compRange` entry in the
  corpus stores an annualized range. There is no schema convention for
  hourly rates, so rather than inventing one or risking the figure being
  misread as an annual salary if stored under the existing fields, the
  structured field is left off the `jobs.json` entry. The stated hourly rate
  is preserved verbatim in this archived text ("Engagement Details" section)
  for anyone checking it directly.

  `engagement` is recorded as "Part-time contract (20 hrs/week, 3 months)" —
  a new value, grounded directly in the JD's own language: "managing your own
  time within a part-time schedule," plus the stated "Time commitment: 20
  hours/week" and "Duration: 3 months, with potential to extend based on
  needs and fit." The JD also explicitly confirms 1099/contractor status:
  "These benefits are applicable to Maven Clinic Co., US-based, full-time
  employees only. 1099/Contract Providers are ineligible for these
  benefits."

  `location` is recorded as "Remote (US)." The JD states only "Remote" with
  no city, but separately states "This role requires active work
  authorization in the US," which grounds the "(US)" qualifier in stated
  text rather than inference from company norms. Consistent with the
  existing "Remote (US)" convention used elsewhere in the corpus (e.g.
  Zoom, Chime, Huge).

  `model-behavior-design` (signal) was a genuine judgment call. The JD
  repeatedly states "Engineering owns prompts and configuration," meaning
  this role does not author prompt text directly. It was assigned anyway
  because the corpus already treats advisory/framework-defining language one
  level removed from literal prompt authorship as satisfying this signal's
  bar — the closest precedent is Coupang's Senior Content Strategist
  ("Redefines format and tone guidelines into requirements that engineers
  can use for model training and prompt improvement"), a structurally
  identical hand-off pattern. The tipping lines for Maven: "Define and
  champion what AI at Maven sounds like, translating our brand voice into
  clear language principles that work within the realities and limits of
  LLM-generated responses" combined with "Advise on the anatomy of agent
  responses (e.g., when to offer options, when to ask a follow-up question,
  how to structure a reply) and recommend patterns for Engineering and
  Clinical to implement and approve."

  `eval-infrastructure` (signal) was considered and explicitly declined. The
  same "Engineering owns..." hand-off logic that did not defeat
  model-behavior-design cuts the opposite way here, because the JD
  explicitly extends Engineering's ownership to evaluations too: "distill
  the findings into what Engineering needs to improve prompts and
  evaluations (Engineering owns prompts and configuration)." Every existing
  eval-infrastructure holder in the corpus (Etsy, Glean, Deliveroo, Intuit)
  directly creates an eval artifact; this role only feeds input into
  Engineering's eval work and never creates the artifact itself.

  `ai-native-expectation` (signal) was considered and declined. The JD's AI
  language ("understands the nuances of prompting and its limitations,"
  "strong understanding of how LLM agents are built and evaluated")
  describes working on an AI product, not using AI tools in the
  practitioner's own content-production workflow, which is the established
  narrow reading this signal requires per the documented description-vs-use
  pattern — consistent with why Ally was declined on the same basis.

  `terminology-governance` and `ai-tooling` (clusters/signals) were both
  considered and declined. `terminology-governance` was declined because
  "taxonomy" appears as a single unglossed word in a four-item list
  ("voice, tone, taxonomy and language") with no actual glossary or
  controlled-vocabulary deliverable described anywhere else in the JD.
  `ai-tooling` was a candidate under the documented description-vs-use
  pattern but was declined at the user's direction.

  `human-in-the-loop` (signal) is grounded in "Review real AI agent
  conversations and give expert feedback on tone, emotional register,
  reading level, and word choice" and "Strong judgment about when AI should
  answer, defer, or escalate, with help from the internal team." This is a
  very recently introduced signal (added 2026-10-26, two days before this
  entry); current holders include notion-cx-knowledge-architect,
  evinova-content-design-lead, bofa-xd-ii-content-design,
  huge-director-ai-content-strategy,
  glean-content-systems-engineer-technical-documentation,
  redbull-senior-specialist-knowledge-semantics-ai-ready-content, and
  intuit-staff-conversation-designer-ai-design-technologist.
---

Conversational AI & UX/Product Copywriter (Contract)
Remote

Maven Clinic is the world's largest virtual clinic for women and families on a mission to make healthcare work for all of us. Through Maven Enterprise, the company partners with more than 2,300 employers and health plans to provide end-to-end women's and family health programs spanning fertility and family building, maternity and newborn care, parenting and pediatrics, and menopause and midlife — improving clinical outcomes, reducing healthcare costs, and expanding equitable access to high-quality care at scale. Through its consumer platform, Maven provides direct access to virtual care across 30+ specialties, as well as dedicated hormone and GLP-1 care programs purpose-built for women. Founded in 2014 by CEO Kate Ryder, Maven Clinic has raised more than $425 million from leading healthcare and technology investors including General Catalyst, Sequoia, Dragoneer Investment Group, Oak HC/FT, StepStone Group, Icon Ventures, and Lux Capital. Recognized for innovation and industry leadership, Maven has been named to the TIME100 Most Influential Companies, CNBC Disruptor 50, Fast Company's Most Innovative Companies, and FORTUNE Best Places to Work. Learn more at mavenclinic.com

An award-winning culture working towards an important mission –  Maven Clinic is a recipient of over 30 workplace and innovation awards, including: 

TIME 100 Most Influential Companies (2023, 2026)
Fortune Change the World (2024)
CNBC Disruptor 50 List (2022, 2023, 2024)
Fortune Best Workplaces for Millennials (2024)
Fortune Best Workplaces in Health Care (2024)
Fast Company Most Innovative Companies (2020, 2023)
Fortune Best Workplaces NY (2020, 2021, 2022, 2023, 2024)
About the Role:

We’re looking for a conversational AI UX writer and voice partner who can define what Maven’s product and AI agents sounds like. You’ll be the expert eye on the language across our product—from navigation to CTAs, clinical modules to our AI agents: calling out when copy could be clearer or more compelling, or an agent response is too clinical, emotional, or complex. You’ll also help shape how we position and showcase AI in the product, including how we educate members about it and how we write disclaimers. Just as importantly, you’ll write and refine UX copy for core member experiences, such as care plan screens and AI agent intro and onboarding screens.

This is a hands-on, high-autonomy role for someone who has worked in both UX product copy and conversational AI and understands the nuances of prompting and its limitations. You will partner directly with Engineering, who owns prompts and configuration, as well as Clinical and Product to bring a single, consistent point of view on voice, tone, taxonomy and language, and to hold a high bar for usability, clinical integrity, clarity, and the right amount of empathy in a health context.

This position is expected to last 3 months, with the potential to extend based on business needs and fit. The expected commitment is 20 hours per week.

What You’ll Do:

AI voice, tone & language

Review real AI agent conversations and give expert feedback on tone, emotional register, reading level, and word choice (e.g., “this is too emotional,” “let’s use simpler words to explain this,” “we missed a chance to be more empathetic”)
Define and champion what AI at Maven sounds like, translating our brand voice into clear language principles that work within the realities and limits of LLM-generated responses
Synthesize voice and language feedback coming from many places (Clinical, Product, Engineering, Brand, coaches) into a clear, prioritized set of themes, and act as the decision-maker when the team needs one voice
Work with Clinical and Engineering to find conversations where a theme went well and where it didn’t, workshop them with users, and distill the findings into what Engineering needs to improve prompts and evaluations (Engineering owns prompts and configuration)
Advise on the anatomy of agent responses (e.g., when to offer options, when to ask a follow-up question, how to structure a reply) and recommend patterns for Engineering and Clinical to implement and approve
Partner with product, engineering, clinical, and legal/compliance teams to translate requirements into clear language guidance
Product & UX copy, including AI positioning

Position how we showcase AI in the product, including how we introduce AI to members, how we handle education, and how we write disclaimers and expectation-setting language
Write and refine UX copy for in-product experiences such as care plan screens, AI agent intro and onboarding screens, navigation and CTAs, empty and error states, and in-app education
Craft language that is empowering and action-oriented, balancing clinical accuracy and compliance with a human, non-alarming Maven-branded tone
Work within design systems and with product designers to balance copy density, hierarchy, and usability
Name products, features, programs, and agents as needed, using a structured approach to generating, screening, and recommending names with rationale
Cross-functional collaboration

Work closely and directly with the Member Copy, Comms & Content team, clinicians, product managers, designers, and engineers
Expected to attend weekly check-in meetings; as well as brainstorm sessions as needed
Document your approach (voice and tone principles, language patterns, conversation theme summaries, naming frameworks) and share a summary of what changed whenever updates go out, so the team can continue to build on it
What You’ll Bring:

5+ years of experience in UX writing or product copywriting, plus direct experience in conversation design or LLM-powered AI products, with a strong online portfolio included in your application
Experience working within AI (e.g., conversational AI, virtual assistants, or LLM-powered products), with a strong understanding of how LLM agents are built and evaluated to work directly with Engineering on feedback
Ideally have direct experience in healthcare AI or digital health, including working alongside clinical stakeholders and legal compliance
Experience reviewing real conversations or user feedback and distilling them into clear themes and recommendations that engineering teams can act on
Exceptional writing and editing instincts, especially for sensitive, emotional, or clinical subject matter, including calibrating empathy, tone, and reading level
Experience applying and evolving brand tone & voice guidelines for product/UX copy and AI/agent conversation
Ability to synthesize feedback from many stakeholders (clinical, compliance, product, engineering) and drive to a single point of view without losing clarity or voice
Naming experience (product, feature, or program naming), including a structured approach to generating, screening, and recommending names as needed
Comfort working independently, managing your own time within a part-time schedule, and communicating progress clearly
Strong judgment about when AI should answer, defer, or escalate, with help from the internal team
Engagement Details

The compensation for this role is $90-100 per hour for 20 hrs a week. Individual pay decisions are based on a number of factors, including qualifications for the role, experience level, and skillset.

Time commitment: 20 hours/week with weekly syncs
Duration: 3 months, with potential to extend based on needs and fit
Deliverables (examples):  A documented voice and tone framework defining what AI at Maven sounds like; synthesized themes and recommendations from conversation reviews, with examples of what worked and what didn’t, for Engineering and Clinical; guidance on AI education and disclaimer language; final UX copy for assigned experiences 
This role requires active work authorization in the US.

At Maven we believe that a diverse set of backgrounds and experiences enrich our teams and allow us to achieve above and beyond our goals. If you do not have experience in all of the areas detailed above, we hope that you will share your unique background with us in your application and how it can be additive to our teams.

Benefits That Work For You

Our benefits are designed to support your health, well-being and career development, helping you thrive both personally and professionally. We remain focused on providing a competitive benefits package for our employees. On top of standards such as employer-covered health, dental, and insurance plan options, we offer an inclusive approach to benefits:

Maven for Mavens: access to the full platform and specialists, including care for mental health, reproductive health, family planning and pediatrics.
Whole-self care through wellness partnerships
Hybrid work, in office meals, and work together days 
16 weeks 100% paid parental leave and new parent stipend (for Mavens who've been with us for 1 year+)
Annual professional development stipend and access to a personal career coach through Maven for Mavens
401K matching for US-based employees, with immediate vesting
These benefits are applicable to Maven Clinic Co., US-based, full-time employees only. 1099/Contract Providers are ineligible for these benefits. 

Maven is an affirmative action and equal opportunity employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex, disability, age, sexual orientation, gender identity, national origin, veteran status, or genetic information. Maven is committed to providing access, equal opportunity and reasonable accommodation for individuals with disabilities in employment, its services, programs, and activities. Maven Clinic interview requests and job offers only originate from an @mavenclinic.com email address (e.g jsmith@mavenclinic.com). Maven Clinic will never ask for sensitive information to be delivered over email or phone. If you receive a scam issue or a security issue involving Maven Clinic please notify us at: security@mavenclinic.com. For general and additional inquiries, please contact us at careers@mavenclinic.com.
