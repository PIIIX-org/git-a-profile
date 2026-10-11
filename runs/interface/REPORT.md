# Run report — inter.face

- **Target:** project · `PIIIX-org/inter.face`
- **Live at:** https://github.com/PIIIX-org/inter.face
- **Date:** 2026-10-11
- **Agent / platform:** omp (Claude)

## Concept
The handoff packet. The README is shaped like what the pipeline produces: a DIRECTION.md page as hero where adjectives are struck through and replaced by the values they became in the one real run; DTCG token chips as tags; the router's phase routing table drawn as the structure map; the run as a signed gate block that names what is missing.

## Palette
| Role | Hex | Source |
|---|---|---|
| Ground | `#f5f9fb` | PIIIX avatar paper white |
| Ink | `#272625` | PIIIX avatar ink |
| Gate accent | `#b35b00` | piiix.org `--primary-light` (AA on paper) |
| Strike / missing | `#c63f28` | the run's own `color.diazo.redline` token |

## Assets built
- Hero: `assets/hero.svg` — adjective → value, six real rows from `runs/taha-portfolio/tokens.json`
- Tags: `assets/tokens/*.svg` — 8 token chips
- Structure: `assets/routing.svg` — what each phase reads
- Showcase: `assets/run.svg` — the first real run, signed
- Footer: `assets/footer.svg`

## Verification
- [x] Live page renders; preflight `--check-urls` passed
- [x] Animation moves in Chromium; static under reduced motion
- [x] `<details>` hold the long sections; anchors kept
- [x] Alt text on every image

## Notes
Prose kept verbatim and restructured; reference files untouched.
