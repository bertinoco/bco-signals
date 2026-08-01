# jd-insights

What the dataset adds up to. Consult this before writing anything that cites
the data — a post, a pitch, a talk — so the figures and caveats are current
rather than remembered.

Lives outside `docs/`, like `jd-source/`, so it is not served by GitHub Pages.
Some of it is working material — noting that a named company's posting has a
grammar error is a fine research note and a poor thing to publish.

## The four files

| File | Written by | Refreshed |
|---|---|---|
| `stats.md` | **Generated** — never hand-edit | Every entry, by script |
| `quotes.md` | **Generated** — never hand-edit | Every entry, by script |
| `patterns.md` | Hand-written | When a posting does something notable in how it is written |
| `findings.md` | Hand-written | Rarely — a new instance updates a count, it does not make a finding |

`stats.md` and `quotes.md` are rewritten in full on every run. Anything typed
into them is lost.

## Refreshing

    python3 jd-insights/refresh.py

Reads `docs/data/jobs.json` and the `jd-source/` front matter. Writes
`stats.md` and `quotes.md`. Never touches the hand-written files.

This runs as part of Step 6 of the entry audit process in `CLAUDE.md`, in the
same pass as the other sync points — so the generated files cannot silently
fall behind the dataset.

## The editorial boundary

`findings.md` is the only place in this repository where interpretation is
allowed. It is where a claim can go beyond what a posting literally says.

Two rules keep that from leaking:

**Findings separate what the data shows from what it is taken to mean.** The
first is defensible by citation. The second is opinion, and marked as such.

**This directory reads from the dataset and never into it.** Nothing here is
evidence for a cluster or signal assignment — those derive from JD text alone.
If a finding appears to justify an assignment, the finding has drifted from its
evidence and needs revisiting, not the entry.

Everything outside `findings.md` — including `patterns.md` — stays
reportorial. `patterns.md` describes what postings do; it does not argue about
what that means.

## Figures go stale

Every number here is a snapshot of a growing dataset. `stats.md` states the
entry count and date it was generated from, and `findings.md` dates its
figures, because a percentage quoted without its n reads as a standing claim
about the field rather than a count of 29 postings.

Anything already published cannot be corrected retroactively. That is an
argument for citing the count alongside the figure, not for avoiding the
figure.
