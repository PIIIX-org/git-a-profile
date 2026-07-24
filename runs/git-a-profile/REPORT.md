# Run report — git-a-profile (self / dogfood)

- **Target:** project · `PIIIX-org/git-a-profile` (this repo's own README)
- **Live at:** https://github.com/PIIIX-org/git-a-profile
- **Date:** 2026-07-21
- **Agent / platform:** Claude Code (Opus)

## Concept
A "forge" terminal banner: `git · a · profile` with the separators rendered as
glowing orbs (a nod to PIIIX's orbital brand), a blinking cursor, and an animated
spark sweeping the underline — the pipeline forging elements into place. True to
the subject because the subject *is* a forge for profiles.

## Palette
| Role | Hex | Source |
|---|---|---|
| Accent | `#8B7BFF` | PIIIX brand purple (parent org) |
| Spark | `#F5A623` | forge accent, chosen to pair with the purple |
| Background | `#05060d` | PIIIX space-dark, consistent across the family |
| Ink | `#f2f2f4` | near-white for AA contrast on dark |

## Assets built
- Hero: `assets/banner.svg` — animated forge banner (SMIL: blinking cursor, spark sweep, twinkle)
- Badges: 5 (`license`, `loops`, `gates`, `agent`, `templates`) — custom monospace pills
- Activity / showcase: n/a for a meta-repo; the loop table + flow diagram carry it
- Footer: n/a (compact repo README)

## Verification
- [x] Every image renders on the live page (screenshot taken)
- [x] Animation moves (blinking cursor + spark sweep); static assets fine
- [x] Links resolve to the loop files and docs
- [x] Readable in light and dark themes (dark banner, theme-neutral body)
- [x] Alt text on the banner and every badge

## Notes / deferred
Dogfood run: this repo's README was produced by the pipeline it documents, as the
first entry in the run log. Tooling used: `gh` (data + push), Python (SVG
generation), macOS `qlmanage` (preview), `browse` (live screenshot), PIL (color
sampling). All eight capabilities were native on this platform; no fallbacks
needed.
