# Run report — piiix-org (second forge)

- **Target:** org · `PIIIX-org`
- **Live at:** https://github.com/PIIIX-org
- **Date:** 2026-10-11
- **Agent / platform:** omp (Claude)
- **Previous forge:** 2026-07, orbital system in `#6C63FF`

## Concept
The real system. The star stays PIIIX; every body is drawn as what it is: Elara the big inner planet with Yildizim as its moon, three smaller planets sized by commit count, Vectory a comet parked at aphelion. Distance from the star is distance from shipped. Tags are ephemeris rows, not pills; activity is a light curve so paused work goes visibly flat.

## Palette
| Role | Hex | Source |
|---|---|---|
| Accent (star) | `#fd9f13` / `#ffc048` | piiix.org `tokens.color.css` `--accent` / `--accent-lift` |
| Ground | `#0b0a09` | between the site's `--n900` and the avatar's `#272625` |
| Ink / stars | `#f5f9fb` / `#d8d4cf` | avatar's paper white (16.7 %), site `--stars` |
| Muted | `#a8a29b` | site `--muted` |
| Warn (Vectory) | `#e62706` | site `--red` |

The avatar has no purple (81.5 % `#272625`, 16.7 % `#f5f9fb`); the old accent was dropped.

## Assets built
- Hero: `profile/assets/system.svg` — CSS-animated orbits (nested rotate / counter-rotate under a `scale(1,.38)` plane, so bodies stay round and labels upright)
- Tags: `profile/assets/almanac.svg` + `profile/assets/ephemeris/*.svg` (one row per body, orbiting dot)
- Activity: `profile/assets/lightcurve.svg` — commits per week per body from `repos/*/commits`
- Footer: `profile/assets/footer.svg`
- Generator: `profile/forge.py` writes `profile/data.json` from the API and regenerates every data-driven asset

## Verification
- [x] Every image renders on the live page (`verification-screenshot.png`; preflight `--check-urls` passed)
- [x] Animation moves in Chromium; static under `prefers-reduced-motion`
- [x] `<details>` works; private Yildizim unlinked
- [x] Alt text on all 20 images

## Notes / deferred
- Labels can overlap briefly when two planets pass; clears in seconds.
- Status words are hand-set in `BODIES` inside `forge.py`; everything else is API data.
- Self-refresh workflow offered, not yet installed.
