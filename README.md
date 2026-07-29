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
- `clusters` — responsibility areas the role covers
- `signals` — skills and observable patterns
- `compRange` — compensation data
- `quote` — optional verbatim excerpt from the JD that anchors the cluster and signal assignments
- `note` — optional factual note about the role or posting
- `tag` — optional, factual classifier (e.g. `non-content-role`, `content-adjacent`)

---

## Design

The site runs an achromatic palette: an off-white and a soft black carry the
whole interface, and red is the only chromatic value in the system — reserved
for failure and flagged status, never for emphasis. Inter carries prose; a
monospace face carries all metadata — domains, dates, comp ranges, counts — so
data reads as data.

Light and dark follow `prefers-color-scheme`, and there is no in-page toggle.
The OS setting is a deliberate preference the reader has already expressed
once, for everything they use; asking again per-site adds a control, a stored
value, and a way for the two answers to disagree. Both themes get the same
care — each has its own foreground values rather than being an inversion of
the other.

The token layer is modelled on **[Midday](https://midday.ai)**
([midday-ai/midday](https://github.com/midday-ai/midday), AGPL-3.0), whose
`globals.css` is a good argument for restraint: their dark theme is 0%
saturation on every token, and their charts separate series by value and
pattern rather than by hue. A finance product running almost entirely on
greyscale is a more convincing case than any style guide. The naming convention
it uses — HSL channel triplets, and a surface/`-foreground` pairing so every
ground carries its own text colour — originates with
[shadcn/ui](https://ui.shadcn.com) (MIT).

The values here are not Midday's. Their light mode is warm-tinted and their
muted foreground is shared across both themes, which drops it to 3.14:1 on
their dark background. This palette is achromatic in both directions and every
text token clears WCAG AA on its own ground.

**[Nothing](https://nothing.tech)** informed the type treatment — their pairing
of NType 82 with NType 82 Mono, and the habit of setting metadata as uppercase
letter-spaced monospace so labels read as machine output.

---

## License

© 2026 Bertino Consulting AB. All rights reserved.

---

## Contact

Joe Bertino — [joe@bertino.co](mailto:joe@bertino.co)
