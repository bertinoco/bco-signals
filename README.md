# Signals

Content design is evolving. Teams are shrinking. Roles and responsibilities are expanding. The skills needed to succeed in the future are starting to appear.

To monitor this shift, and content design's unique position in the "context is king" era, I've started to track interesting, ambitious, or forward leaning job postings. These are mostly senior-level IC roles where the description is signaling change.

I began parsing this data using a curated schema (json) and rendering content in html. The output is a living map of core responsibilities, grouped by focus area, as well as a number of required skills — which reflect emerging patterns in the content design hiring process.

## Structure

```
docs/data/jobs.json   — Structured entries for each tracked role

jd-source/            — Verbatim JD text archive
                          - One md file per entry
                          - Includes included and excludes JDs
  README.md           — A good place to read more about exclusion rules

jd-insights/            — What this dataset means (none of this content is published) 
  stats.md              — Interesting stats (generated)
  quotes.md             — Interesting quotes (generated verbatim)
  patterns.md           — Notes and commentary on how postings are written
  findings.md           — Notes on what Claude and I find interesting (this is editorialized) 
  refresh.py            — How we generate stats.md and quotes.md from jobs.json + jd-source/
  README.md             — What each file is for and the editorial boundary
```

## Data schema

Each entry in `jobs.json` includes:

- `company` / `domain` — basics
- `title` — normalized at render
- `clusters` — responsibility areas the role covers
- `signals` — skills and observable patterns
- `compRange` — stated range, plus extras
- `quote` — optional verbatim excerpt
- `note` — optional factual note
- `tag` — optional, factual classifier

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
