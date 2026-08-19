# Signals

Content design is evolving. Teams are shrinking. Roles and responsibilities are expanding. The skills needed to succeed in the future are starting to appear.

To monitor this shift, and content design's unique position in the "context is king" era, I've started to track interesting, ambitious, or forward leaning job postings. These are mostly senior-level IC roles where the description is signaling change.

I began parsing this data using a curated schema (json) and rendering content in html. The output is a living map of core responsibilities, grouped by focus area, as well as a number of required skills — which reflect emerging patterns in the content design hiring process.

## Structure

```
docs/data/jobs.json   — Structured entries for each tracked role

CLAUDE.md             - This is the good stuff. Start here to learn about our criteria and audit process.

jd-source/            — Verbatim JD text archive
                          - One md file per entry
                          - Both included and excluded JDs
  README.md           — Read more about exclusion rules

jd-insights/          — Big picture archive
  stats.md            — Interesting stats
  quotes.md           — Interesting quotes (verbatim)
  patterns.md         — Notes on how postings are formatted and written
  findings.md         — Notes on what Claude and I find interesting (based on dictation, then editorialized) 
  refresh.py          — How we generate stats.md and quotes.md from jobs.json + jd-source/
  README.md           — What each file is for and our editorial boundaries
```

## Data schema

Each entry in `jobs.json` includes:

- `company` / `domain` — basics
- `title` — normalized at render
- `clusters` — responsibility areas the role covers
- `signals` — skills and observable patterns
- `compRange` — stated range, plus extras
- `quote` — optional verbatim excerpt
- `note` — optional note
- `tag` — optional classifier

---

## Design

The site runs an achromatic palette, informed by **[Midday](https://midday.ai)**
([midday-ai/midday](https://github.com/midday-ai/midday), AGPL-3.0). The naming convention
it uses — HSL channel triplets, and a surface/`-foreground` pairing so every
ground carries its own text colour — originates with
[shadcn/ui](https://ui.shadcn.com) (MIT).

Every text token clears WCAG AA on its own ground.

---

## Contributing

Come across a posting that fits? See `CONTRIBUTING.md`.

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
