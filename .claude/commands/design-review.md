Review the current state of `docs/index.html` and `docs/css/styles.css` against the design system defined in `CLAUDE.md`. Evaluate the following areas and report findings as a prioritized list of issues (Critical → Minor):

## What to check

**Layout & proportion**
- Is the centered layout consistent throughout (header, tabs, section intros, grids, footer)?
- Do cluster and signal card grids feel balanced at 3-column desktop / 2-column tablet / 1-column mobile?
- Is the All Job Descriptions list readable and well-proportioned at all breakpoints?
- Is vertical rhythm consistent? Sections should breathe but not feel disconnected.

**Typography**
- Are `--font-serif` (Playfair Display) and `--font-sans` (Inter) applied correctly across the hierarchy?
- Is the type hierarchy clear (H1 → card headings → body → labels)?
- Are font sizes from the type scale applied consistently — no ad-hoc values?

**Color & contrast**
- Are CSS custom properties used — no hardcoded hex values except in `:root`?
- Does all readable text meet WCAG AA (4.5:1) against its background? `--color-text-muted` is decorative only.
- Is the coral accent (`--color-accent`) used sparingly and consistently?

**Spacing**
- Is the 8px spacing scale respected? Flag any ad-hoc pixel values outside the scale.
- Are section padding values (`--space-12`) consistent?

**Component consistency**
- Do cluster cards and signal cards look identical in structure and feel?
- Do tab styles (default, hover, active) feel intentional and consistent?
- Does the expandable quote row in All Job Descriptions work cleanly?

**Responsive behavior**
- Are breakpoints at 600px and 768px and 900px complete and correct?
- Does anything break or overflow at 375px viewport width?

**Semantic HTML & accessibility**
- Are landmark elements (`<nav>`, `<main>`, `<section>`, `<footer>`) used correctly?
- Do `aria-labelledby`, `aria-selected`, `aria-expanded`, and `role` attributes point to valid ids and values?
- Do interactive elements (tabs, expand buttons) have visible focus states?

**Design system adherence**
- Are `--radius`, `--max-width`, and the spacing scale applied consistently?
- Does any element use inline styles or non-system values?

## Output format

Return a prioritized list:

- **Critical** — broken layout, missing content, accessibility failures
- **Significant** — noticeable visual inconsistency or proportion problem
- **Minor** — small polish items, spacing tweaks, code cleanliness

End with 2–3 specific, actionable fix suggestions for the highest-priority issues.
