# Contributing

Three ways to help — the first is the one that makes this repo grow.

## 1. Share your forge

Made a profile with git-a-profile? Add it to the gallery and the count:

1. Copy `runs/_template/` to `runs/<your-handle>/` and fill in `REPORT.md`
   (target, live URL, the concept, palette + sources, verification).
2. Drop a small screenshot at `assets/gallery/<your-handle>.png` (a ~600px-wide
   crop of the hero region).
3. Open a PR. On merge, the **profiles forged** badge recounts automatically and
   your forge can appear in the gallery.

Keeping the "Forged with git-a-profile" credit is appreciated but never required —
you can remove it by hand any time (`PRINCIPLES.md §14`).

## 2. Add a platform

New agent format (a `.something/rules` file, a manifest)? Add **one small adapter**
that says "read `AGENTS.md` and run the loops," and a row in `PLATFORMS.md`. Don't
copy the loops — point at them. The loop files are the single source of truth.

## 3. Improve the pipeline

Sharper loop instructions, a better default, a real bug in a script. Keep
[`PRINCIPLES.md`](./PRINCIPLES.md) intact — those are the guardrails, not
suggestions. Run `python3 scripts/preflight.py <a-README>` before proposing
changes that touch output quality.

## Ground rules

- Real data only; no fabricated stats or personas.
- Accessible by default (alt text, reduced-motion).
- Don't turn the examples into a template library — reinvention is the point.
