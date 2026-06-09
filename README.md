# Skills Tracker

This is a lightweight research tool for tracking how content design skills and responsibilities are evolving with the help of AI. This is not intended to be an exhaustive study. It's just a curated list of jobs I find interesting.

## What's in this repo?

```
data/jobs.json     — Structured entries for each tracked role
docs/index.html    — Dashboard (hosted version coming soon)
```

## Data schema

Each entry in `jobs.json` includes:

- `company` / `title` / `domain` — basics
- `clusters` — which responsibility areas the role covers, based on stated responsibilities
- `signals` — observable characteristics of the JD (e.g. title uses systems language, JD prescribes LLM workflow)
- `compRange` — compensation data when stated in the JD
- `tag` — optional, factual classifier (e.g. `non-content-role`, `content-adjacent`)

## Adding job descriptions

See an interesting, forward-leaning job description? Add it by creating a PR. Open `data/jobs.json` and add a new object to the `entries` array. Copy an existing entry as a template. Update `meta.totalEntries` and `meta.lastUpdated` when done.

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
