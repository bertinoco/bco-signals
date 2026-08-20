---
id: redpine-senior-knowledge-graph-engineer
company: Redpine
title: Senior Knowledge Graph Engineer
sourceUrl: null
sourcePlatform: company-site
orgPlacement: "Department: Tech"
postedDate: null
reqId: null
dateAdded: null
captured: 2026-08-17
captureMethod: pasted-from-claude-chat
excluded: 2026-08-17
excludedReason: >
  Excluded on the required "primarily in content design, UX writing, content
  strategy, or a technical content discipline" criterion, not on thinness —
  most exclusions in this dataset fail on thinness, this one fails on scope.
  Nothing is written to jobs.json.

  A full literal-text check found zero occurrences of "content," "writing,"
  "language," "copy," "tone," "voice," or "terminology" anywhere in the
  posting. This is a cleaner zero than the excluded Fin "Staff AI Designer"
  posting managed — Fin at least argued for its place inside a Design org
  ("AI Design team," "product designers," "not a traditional product design
  role"), while Redpine sits in "Department: Tech" and never engages design
  discourse at all. The only occurrences of "design" here are engineering
  usages: "Ontology and schema design," "design a schema that survives
  contact with reality."

  The posting's own framing — "Agents are only as good as the knowledge they
  can reach," provenance-bearing graph nodes "served directly to agents,"
  multi-hop traversal — reads like a literal engineering implementation of
  what this dataset's `agent-retrieval` signal describes in the abstract
  ("the knowledge layer a model reads from before it writes"). That thematic
  closeness was seriously considered, not waved off. It doesn't hold:
  `agent-retrieval`'s holders (Notion, Meta, Alibaba) are content
  professionals restructuring their own content so agents can retrieve it —
  upstream of the retrieval layer, shaping what goes in. This role builds
  the retrieval layer itself, over other people's licensed documents, with
  no content deliverable anywhere in the posting. The same test applies to
  `taxonomy`: "define the entity types, relations, and constraints that
  licensed data from each domain maps into" sounds like taxonomy work, but
  every taxonomy-cluster entry classifies content (product copy, UX strings,
  support docs) for navigation, while this classifies real-world entities
  (drugs, trials, companies, filings) for machine reasoning — same
  technique, different object.

  No cluster is grounded either way, which is a second, independent basis
  for exclusion under the required "at least two distinct cluster
  assignments" criterion.

  Recorded at length (see also jd-insights/findings.md's Watching section
  and CLAUDE.md's Terminology section, "Words that mark the edge of scope")
  because this posting stress-tests the eligibility criteria more usefully
  than most exclusions do, and the terms it introduced — ontology, data
  schema, knowledge graph — are worth having on hand the next time a posting
  sits this close to the boundary.
---
Senior Knowledge Graph Engineer
Location

Redpine HQ, central Stockholm
Address

Stockholm, Stockholm
Employment Type

Full time
Location Type

On-site
Department

Tech
Overview
Application
The role
Agents are only as good as the knowledge they can reach. Most retrieval today is flat: chunk a document, embed it, hope the nearest vector is the right answer. That breaks the moment a question needs more than one hop, needs to know which source to trust, or needs to distinguish two entities that happen to share a name. Redpine is building the layer that fixes this: a knowledge graph over the licensed data we hold across medicine, science, law, and finance, served directly to agents over our API, MCP, and CLI.
You will own that graph end to end, from raw multimodal sources to the structured, provenance-bearing knowledge that agents query in production. This is an early, high-ownership role. The decisions you make about how we model and link knowledge will shape what every agent built on Redpine can actually reason about.
What you'll do
Ontology and schema design. Define the entity types, relations, and constraints that licensed data from each domain maps into, building on the established ontologies those fields already use rather than reinventing them. You will decide where a shared ontology helps and where a domain needs its own.
Entity resolution at scale. Deduplicate, canonicalize, and disambiguate entities across heterogeneous, multimodal sources, so the same thing in the world is one node in the graph.
Confidence and conflict. Attach confidence to every link, and define what happens when two sources disagree. Decide what the graph asserts, what it flags, and what it surfaces to the agent.
Provenance as a first-class property. Preserve attribution on every node and edge, back to the source document and the license that covers it. At Redpine this is not optional, it is the product.
Keeping the graph live. Detect when an upstream source changes and propagate that change, so the graph reflects current knowledge instead of a stale snapshot.
Graph-powered retrieval. Build multi-hop traversal, hybrid graph-and-vector retrieval, and the kind of structure a reranker can actually exploit.
What we're looking for
Deep, direct experience with knowledge graphs: graph databases, property or RDF graphs, entity resolution, and ontology design. You have shipped one, not just read about them.
Strong Python and a track record of building data pipelines from scratch.
Real experience with retrieval and RAG, ideally graph-backed, plus the judgment to know when a graph earns its keep and when it is just overhead.
Judgment about messy data. You can look at multi-source, contradictory input and design a schema that survives contact with reality.
A bias toward small, clear systems. You question whether something needs to be built before you build it.
A genuinely curious mind, the kind that wants to understand a domain well enough to model it honestly.
Why this role
Agents don't just look things up, they traverse. They follow a claim to its source, a company to its filings, a drug to its trials to the patients those trials enrolled. That kind of multi-hop reasoning needs explicit structure: typed entities, named relations, and a graph a planner can walk.
Practical details
Based at Redpine HQ in central Stockholm. Office-first, with real autonomy for deep-work days and life admin.
Requires a valid Swedish work permit or similar eligibility. Relocation support available.
Competitive salary and meaningful equity.
Small team, high ownership. The same people design, ship, and run the systems.
About Redpine
If models were the first wave of AI, and compute the second, we are building the data layer that comes next. Only a small fraction of the world's data is on the open internet. The rest, high-quality, domain-specific, often critical, sits behind paywalls, in databases, or with rights holders. Redpine is building the infrastructure to unlock it.

We provide AI builders and autonomous agents with access to licensed, high-quality, multimodal data through a unified platform and API. The goal is simple: make AI systems more accurate, more useful, and grounded in real-world information.

You will work closely with the founding team, including Anders (ex-partner at VC, McKinsey) and David (ex-tech and product leader at Spotify, Zettle, and Lunar). We are backed by Nordic Ninja, Node VC, and Luminar, alongside angels from OpenAI, Spotify, and Perplexity.

If you are eager to make a meaningful impact in the AI space, we would love to hear from you. We are committed to building a diverse and inclusive team. If you are excited about this role but your experience does not align perfectly with every qualification, we encourage you to apply anyway.
