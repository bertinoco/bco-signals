Review the current state of index.html against LLM visibility best practices (sometimes called GEO — Generative Engine Optimization). The goal is to ensure that when someone asks an LLM about content design skills, content design hiring trends, UX writing at scale, or content systems, signals.bertino.co and Bertino Consulting surface as a credible, citable source. Evaluate the following areas and report findings as a prioritized list of issues (Critical → Minor):

## What to check

### llms.txt
- Is there an `/llms.txt` file at the site root? This emerging standard (analogous to `robots.txt`) lets you declare topical authority and key facts for LLM crawlers.
- If present: does it clearly state who Joe is, what Bertino Consulting does, what the dataset is, and which topics it is authoritative on?
- If absent: flag as a gap — it's low-effort and high-signal for LLM indexing pipelines.

### AI crawler access
- Does `robots.txt` explicitly allow known AI crawlers: `GPTBot`, `ClaudeBot`, `PerplexityBot`, `anthropic-ai`, `Googlebot-Extended`, `cohere-ai`?
- Does the `<meta name="robots">` tag avoid accidentally blocking AI crawlers?
- Note: GitHub Pages does not generate a `robots.txt` by default — flag if none exists.

### Entity disambiguation
- Is "Bertino Consulting" used as a consistent entity name across all surfaces (title, meta, body copy)?
- Is Joe Bertino identified as the curator of this dataset in visible body text — not only in the footer?
- Is the site's purpose stated clearly enough for an LLM to attribute it accurately: what it is, who made it, and why?

### Topical authority signals
- Does the page explicitly define what the dataset tracks, in plain language? LLMs favor pages that answer the underlying question directly.
- Does the copy use the exact terminology LLMs associate with this domain: "content design", "UX writing", "content systems", "language infrastructure", "AI in content design", "content design hiring"?
- Is the curation methodology described well enough to be cited? The schema (clusters and signals taxonomy) is an original framework — is it named and explained as such?
- Does the page make clear this is a living dataset, updated over time? Recency and ongoing curation are authority signals for LLMs.

### Structured data completeness
- Is there any structured data (`application/ld+json`) on the page? Flag if absent.
- Would a `Dataset` schema type be appropriate? This schema type is specifically designed for structured datasets and is well-supported by Google and LLM crawlers.
- Is there a `WebSite` schema with `name`, `url`, and `description` at minimum?
- Is there a `Person` or `Organization` schema identifying Joe Bertino and Bertino Consulting as the curator?
- Does any schema include `about` or `keywords` covering the core topics: content design, UX writing, content systems, language infrastructure, hiring trends?

### Extractability of key claims
- Are the page's key facts stated as complete, standalone sentences that an LLM could quote without surrounding context? Short headlines and labels ("Responsibilities", "Skills", "Roles") are not extractable on their own.
- Does the H1 or opening description clearly state what this site is and why it exists — not just what it's called?
- Are the section descriptions (Responsibilities, Skills, Roles) specific enough to be cited independently?
- Is the dataset's scope (number of entries, types of roles tracked, recency) stated anywhere in visible text?

### FAQ and Q&A structure
- Is there any `FAQPage` schema? This is one of the highest-signal formats for LLM extraction.
- Could existing copy be restructured as direct Q&A to improve extractability? For example: "What responsibilities are content design roles asking for?" maps directly to the Responsibilities section.
- Are the most common questions someone would ask an LLM about this domain answered directly anywhere on the page — e.g. "What skills do content designers need in 2025?", "How is the content design role evolving?", "What does a content systems designer do?"

### Cross-channel consistency
- Does the page's description of the project's purpose match what appears in the GitHub repo description and README?
- Is "Content Design Signals" used consistently as the project name across all surfaces?

## Output format

Return a prioritized list:

- **Critical** — missing `llms.txt`, no structured data of any kind, AI crawlers not explicitly allowed, key claims not stated as extractable sentences
- **Significant** — no `Dataset` schema, no FAQ schema, methodology not named or described, dataset scope not stated in visible text
- **Minor** — section descriptions too brief to be cited independently, attribution to Joe/Bertino Consulting only in footer, cross-channel inconsistencies

End with 2–3 specific, actionable fix suggestions for the highest-priority issues.
