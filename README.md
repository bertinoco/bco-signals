# Content Design Signals

Content design is evolving. Teams are shrinking. Roles and responsibilities are expanding. The skills needed to succeed in the future are starting to appear.

To monitor this shift, and content design's unique position in the "context is king" era, I've started to track interesting, ambitious, or forward leaning job postings. These are mostly senior-level IC roles where the description is signaling change.

I began parsing this data using a curated schema (json) and rendering content in html. The output is a living map of core responsibilities, grouped by focus area, as well as a number of required skills — which reflect emerging patterns in the content design hiring process.

## Structure

```
docs/data/jobs.json   — Structured entries for each tracked role
docs/index.html       — Dashboard at signals.bertino.co
```

## Data schema

Each entry in `jobs.json` includes:

- `company` / `title` / `domain` — basics
- `clusters` — responsibility areas the role covers, based on stated responsibilities
- `signals` — skills and observable patterns explicit in the JD
- `compRange` — compensation data when stated in the JD
- `quote` — optional verbatim excerpt from the JD that anchors the cluster and signal assignments
- `note` — optional factual note about the role or posting
- `tag` — optional, factual classifier (e.g. `non-content-role`, `content-adjacent`)

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
