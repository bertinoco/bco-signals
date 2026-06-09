# BCO Skills Tracker

A lightweight research tool for tracking how content design, content systems, and language infrastructure skills are evolving across industries.

## What's in here

- `data/jobs.json` — the source of truth. Each entry is a job description, tagged with skill clusters and signals.
- `docs/` — a simple HTML dashboard that reads the JSON and surfaces patterns across entries.

## Data structure

Each entry in `jobs.json` includes a company, title, domain, and two types of tags:

- **Clusters** — skill areas the role covers (e.g. `terminology-governance`, `ai-tooling`, `enablement`)
- **Signals** — patterns worth noting (e.g. `ai-native-expectation`, `governance-as-value-prop`, `title-dilution`)

## Adding entries

Open `data/jobs.json` and add a new object to the `entries` array. Copy an existing entry as a template. Update `meta.totalEntries` and `meta.lastUpdated` when done.

## Viewing the dashboard

Open `docs/index.html` in a browser. No build step required.

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
