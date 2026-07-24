# Run report — website-pitch-pipeline

- **Target:** project · `PIIIX-org/website-pitch-pipeline`
- **Live at:** https://github.com/PIIIX-org/website-pitch-pipeline
- **Date:** 2026-07-24
- **Agent / platform:** Claude Code (Fable 5 conductor; profile-researcher + 5× asset-forger + render-verifier workers)

## Concept

**"The Drawing Set, filed clean"** — the README is the crew's numbered blueprint drawing set inside their job file. The human's intake asked for "a heist crew with blueprints, ready for the heist"; the repo's own docs supplied the two truths that shaped it: the human is the lock on every door (gates A/B/C are non-negotiable), and the crew works clean (the legal rules are load-bearing, so the heist reads as professional planning, never deception). The pipeline's loops became numbered sheets (00a Takeoff → 04 The File), the gates became carbon triplicate slips, repo tags became manila evidence tags, and the cost estimator became the takeoff sheet that prices the job before the crew takes it.

A blend of two Gate A options (the blueprint "Drawing Set" structure + the "Clean Crew" job-file furniture). Rejected for range: an Ocean's-style crew lineup — first image the category conjures, so it failed the reflex check.

## Palette

| Role | Hex | Source |
|---|---|---|
| Brand anchor (dark) | `#272625` | Sampled from the PIIIX-org avatar with Pillow (81.5% coverage) |
| Brand anchor (light) | `#f5f9fb` | Sampled from the same avatar (ring + monogram, 16.7%) |
| Vibe layer (blueprint) | `#0E2A3F` / `#2E5C8A` / `#9CC3E0` | Chosen deliberately: cyanotype drafting tradition for the sheets |
| Decision accent | `#B3402F` | Stamp red, reserved exclusively for human/gate moments |
| Paper tones | `#E3D9BE` / `#E9CFC9` / `#EBDFB4` | Manila + carbon-copy file furniture, desaturated |

Intake do-not honored: no PIIIX logo invented or redrawn anywhere; the mark's hex silhouette is echoed only as layout rhythm, and PIIIX appears as typed text (`FIRM: PIIIX.org`).

## Assets built

All committed SVGs under `assets/` on the target repo — 9 files, no badge services:

- Hero: `hero-banner.svg` — overhead planning-table scene; cyanotype storefront elevation flagged NO CTA / MENU IS A JPG / MOBILE BROKEN, pinned city map, torn takeoff slip ($0.06–$32.25 / SAME JOB), GATE A carbon slip, red CHECKED: HUMAN stamp; linework draws itself, stamp lands at ~4s
- Tags: `tag-metabar.svg` (title-block cells replacing any badge row) · `tag-lifecycle.svg` (manila evidence tags: pending-beta → in-progress → ready-for-review → ready-for-outreach) · `section-tab.svg` (folder-tab divider)
- Gates: `gate-slips.svg` — carbon triplicates with the real gate checklists; Gate A signed with a landed GO stamp
- Flow: `sheet-register.svg` — the 6-loop / 3-gate state machine as a drawing set's index, with the scale-only-after-the-sample-passes return arrow
- Chart: `takeoff-chart.svg` — cost-vs-quality scatter of all 12 models in `utils/cost-estimator.js`, hand-derived from its constants (script never executed; target repo is modify-only), log cost axis, $0.06–$32.25 spread
- Footer: `footer-strip.svg` — closing title block with the real org motto and the FORGED WITH: GIT-A-PROFILE credit cell

## Verification

- [x] Every image renders on the live page ([screenshot](./verification-screenshot.png)) — all 8 README images `naturalWidth > 0`, served as `image/svg+xml`
- [x] Animation moves; static under reduced motion (one-shot CSS/SMIL, `.anim` + `prefers-reduced-motion` gate, base state = final state)
- [x] No `<details>` used; spot-checked links resolve (`loops/00a-cost-estimate.md`, `utils/README.md`, `PIPELINE.md`, `runs/_template/`)
- [x] Readable in light and dark themes — assets carry their own charcoal stage; light mode confirmed visually, dark covered by construction
- [x] Alt text on every image (preflight: 0 warnings, live URL check green)

## Notes / deferred

- **Fallbacks:** SVG previews rendered with `qlmanage` (frame-0 only), so end states were verified from animation-stripped copies; dark-theme chrome not separately screenshotted.
- **Deferred:** no cron self-refresh for the takeoff chart — it derives from static constants in the target repo, so it only changes when someone edits the PRICING table. Flagged for the maintainer: Loop 0a's prose claims "$50–200" for the quality strategy while the estimator's own formula tops out at ~$32 for a 5/5/5 campaign; the chart shows the formula's numbers.
- **Process note:** the first attempt (pre-pipeline) shipped shields-style badges and an invented gradient-circle logo, and was fully reverted — both moves are named do-nots in this run's intake. The forged run replaced it end to end: intake → research → Gate A (3 concepts) → asset fan-out → Gate B → build → Gate C → live screenshot verify.
