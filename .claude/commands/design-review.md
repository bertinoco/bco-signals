Review the current state of `docs/index.html` and `docs/css/styles.css` against the design system defined in `CLAUDE.md` and documented in `styles.css`'s own header comment. Evaluate the following areas and report findings as a prioritized list of issues (Critical → Minor):

## What to check

**Layout & proportion**
- The hero (`.site-header`) and sticky nav (`.nav-bar`) are deliberately left-aligned, not centered — that's an intentional departure from `body`'s global `text-align: center`, not an inconsistency to flag. The pull-quote band, tab content, and card grids stay centered/left-aligned per their own existing rules. Check that each area matches its *own* intended alignment, not that everything matches each other.
- Do cluster and signal card grids feel balanced at 3-column desktop / 2-column tablet / 1-column mobile?
- Is the Roles tab ("All roles") list readable and well-proportioned at all breakpoints?
- Is vertical rhythm consistent? Sections should breathe but not feel disconnected. (This has needed real, iterated tuning around `.nav-bar` specifically — check it isn't drifting back toward feeling too tight against the pull-quote above or too disconnected from the cards below.)

**Typography**
- Are `--font-sans` (Inter, for prose/headings) and `--font-mono` (IBM Plex Mono, for metadata, stats, labels, dates, comp figures) applied to the right content — mono never for body prose, sans never for tabular/label data?
- Is the type hierarchy clear (H1 → card headings → card stat → body → labels)?
- Are font sizes from the type scale (`--font-xs` through `--font-3xl`) applied consistently — no ad-hoc values? (One known exception: `.flip-card-back-title` at `1.625rem`, predates the current scale and hasn't yet met the project's own bar for tokenizing — a single usage. Don't re-flag it unless a second element now shares that size.)

**Color & contrast**
- Are CSS custom properties used — no hardcoded hex values except in `:root`?
- Does all readable text meet WCAG AA (4.5:1 normal text, 3:1 large text) against the background it actually renders on? `--muted-foreground` and `--secondary-foreground` are real, legible text colors in this system, not decorative-only — check their computed contrast, don't assume either is exempt.
- The palette is achromatic throughout by design. `--destructive` (red) is the only hue in the system, reserved exclusively for failure/error states (see `.state--error .state-title`) — flag any use of color for emphasis, brand, or decoration, since that would break a rule the project has stated explicitly, not just a convention.

**Spacing**
- Is the 8px spacing scale (`--space-1` through `--space-12`) respected? Flag ad-hoc pixel values that aren't clearly derived (icon sizing, hit-area math with its reasoning documented inline, or breakpoint values) — not every raw px is a violation, but an unexplained one is.
- Are section padding values consistent with their role (e.g. `--space-12` for large section gaps, `--space-3`/`--space-4` for component-internal padding)?

**Component consistency**
- Do cluster cards and signal cards look identical in structure and feel (title top-left, stat bottom-right, same back-panel layout)?
- Do tab styles (default, hover, active) feel intentional and consistent? (Active state is plain text — color + weight change — not a filled pill; don't flag the absence of a pill as missing affordance.)
- Does the expandable title row in the Roles tab (reveals the quote and signal chips) work cleanly — click-anywhere-on-the-row to expand, not just the icon, with a real ≥24px hit area?

**Responsive behavior**
- Breakpoints in actual use: `480px` (nav wrap to a second row), `599px` (card overlay switches to a full-screen mobile sheet), `600px`/`900px` (grid column counts), `768px`/`1024px` (`.container` padding steps — not grid columns). Confirm these are complete and don't conflict.
- Does anything clip, overlap, or force horizontal scroll at **320px** viewport width — the actual WCAG reflow checkpoint, not just 375px. (375px alone previously missed a real nav-overflow bug that only appeared at 320-340px; always include 320px explicitly.)

**Semantic HTML & accessibility**
- Are landmark elements (`<header>`, `<nav>`, `<main>`, `<footer>`) used correctly, and does the nav carry `role="tablist"`/`role="tab"` correctly?
- Do `aria-labelledby`, `aria-selected`, `aria-controls`, `aria-expanded`, and `role` attributes point to valid ids and values?
- Do interactive elements (tabs, expand buttons, cards) have visible focus states, and does each card's accessible name (`aria-label`) reflect everything meaningful shown on its face — including the front-facing percentage stat, not just the title?

**Design system adherence**
- Are `--radius`/`--radius-sm` (small controls), `--radius-lg` (panel-scale surfaces, e.g. the card overlay), `--max-width`, and the spacing scale applied consistently? A new panel-scale rounded surface should reuse `--radius-lg`, not introduce a raw value.
- Does any element use inline styles or non-system values where a token already exists for that purpose? (Inline `style="display:none"` on the three show-more wrapper divs is an established, consistent pattern — not a violation to re-flag each time.)

## Output format

Return a prioritized list:

- **Critical** — broken layout, missing content, accessibility failures
- **Significant** — noticeable visual inconsistency or proportion problem
- **Minor** — small polish items, spacing tweaks, code cleanliness

End with 2–3 specific, actionable fix suggestions for the highest-priority issues.
