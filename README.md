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

- `company` / `domain` — basics
- `title` — stored verbatim. Em dash and pipe separators are normalized to commas at render, so the site and `jobs.json` differ on some entries by design. A forward slash joining two titles for one role is preserved. Never edit a title to match what the site shows — see "Title field" in `CLAUDE.md`
- `clusters` — responsibility areas the role covers
- `signals` — skills and observable patterns
- `compRange` — stated range, plus `covers` (`base` / `total` / `null` when the JD does not say), `scope` (location the range is tied to), and `extras` (what sits on top, recorded but not displayed)
- `quote` — optional verbatim excerpt from the JD that anchors the cluster and signal assignments
- `note` — optional factual note about the role or posting
- `tag` — optional, factual classifier (e.g. `non-content-role`, `content-adjacent`)

---

## Design

The site runs an achromatic palette, informed by **[Midday](https://midday.ai)**
([midday-ai/midday](https://github.com/midday-ai/midday), AGPL-3.0). The naming convention
it uses — HSL channel triplets, and a surface/`-foreground` pairing so every
ground carries its own text colour — originates with
[shadcn/ui](https://ui.shadcn.com) (MIT).

Every text token clears WCAG AA on its own ground.

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
