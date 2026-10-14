# Methodology talk

A short, speaker-led talk on BCO Signals in three parts: the idea, how it is
set up (a walkthrough of the README: structure, data schema, taxonomy, archive,
the weekly scout, the audit command, and the checks that close the loop), and
what it found. Findings are the bulk of the deck.

**Editorial, not data reporting.** Like `jd-insights/findings.md`, this is
opinion and interpretation built on the dataset. It does not follow the data
integrity rules, the voice rules, or the no-"I" rule that govern the rest of
the repo. Every count in it is recomputed and dated ("as of Oct 2026, 78
postings") rather than quoted from `findings.md`, whose own figures go stale.

**Status: draft, public.** Published on the branch `presentation/methodology-talk`
so it can be edited from any device or session. Not merged to `main`. The
repository is public, so the deck is visible to anyone, and it is unfinished.

## Files

- `methodology-talk.html` is the built deck. It is a single file and opens
  in any browser. Arrow keys navigate, `N` shows speaker notes, `V` outlines
  the space reserved for visuals, `E` edits text (saved to that browser only).
- `source/slides_data.py` holds every slide's copy. Edit here.
- `source/template.html` holds the design, ported from `docs/css/styles.css`.
- `source/make_deck.py` builds the deck from the two files above.

Rebuild after editing the source:

    python3 presentations/methodology-talk/source/make_deck.py presentations/methodology-talk/methodology-talk.html

Page numbers are computed from the slide count, so adding a slide needs no
renumbering.

## Still to do

- Confirm the cold open (slide 1): that "automate the frontend" is the phrase as
  said, and that attributing it to Legora by name is intended. This branch is
  public.
- Decide the judgment-and-taste count (slide 16). The finding says eight; a
  recount at 78 entries suggests ten (Glean and Ethos qualify on the finding's
  own criteria). Not changed yet.
- Quotes on the slides were verified against the archived source texts in
  October 2026. Counts are as of Oct 2026 (78 postings).
