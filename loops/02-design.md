# Loop 2 — Design

**Goal:** build the custom asset kit for the approved concept. Every asset is your
own committed SVG. No badge services (`PRINCIPLES.md §1`).

**Input:** approved `RESEARCH.md` (concept + palette).

**Output:** `assets/` full of SVGs, each previewed, ready for the README.

---

## The asset kit

Build these, in the approved palette, in a consistent type system (a monospace
family reads well and renders everywhere):

1. **Signature hero** — the unique concept as an animated SVG.
2. **Badge system** — role/affiliation badges and a tech-stack row, each a small
   pill SVG with the real logo embedded and the brand/tech color as background.
3. **Activity / showcase viz** — for a person, the real contribution data as a
   custom graphic; for an org/project, a real showcase.
4. **Footer** — a slim closing strip that echoes the hero.

## How to build each

- **Write SVG directly** (Python/JS/whatever). Keep viewBox tidy; use relative
  units so it scales to `width="100%"`.
- **Logos:** pull real marks from the subject's avatar (sample + embed as a
  clipped `<image>`) or from open icon sets (e.g. simple-icons) for tech logos —
  extract the `<path>` and fill it in your contrast color. Redraw a simple mark
  (e.g. a monogram) when no logo exists.
- **Animation — two ways, both render inside an `<img>` on GitHub:**
  - **SMIL** (`<animate>`, `<animateMotion>`) for orbits, twinkles, motion paths.
  - **CSS `<style>`** with `@keyframes` for pulses/loops — and this is the only
    way to honor reduced motion:
    ```
    @media (prefers-reduced-motion: reduce) { .anim { animation: none !important; } }
    ```
    Use CSS whenever the asset moves and a static fallback matters.
- **Contrast:** white text on saturated fills, dark text on light fills (yellow,
  cyan). Check body text ≥ 4.5:1.

## Preview every asset

Render each SVG to PNG and look at it before moving on:

```bash
qlmanage -t -s 900 -o . asset.svg      # macOS
rsvg-convert asset.svg -o asset.png    # librsvg
resvg asset.svg asset.png              # resvg
```

If you have no renderer, describe each asset precisely and rely on Gate B (a
human opens the SVGs). Fix anything that clips, misaligns, or reads wrong.

## Commit the assets

Put them under `assets/` (or `profile/assets/` for an org's `.github`). You'll
reference them by raw URL in Loop 3.

> ## Gate B — human decision
>
> Show the human the **preview images** of the hero, badges, and activity viz.
> Ask them to approve the visual direction (or call specific changes) before you
> assemble the README. Iterate here — it's cheap. Do not proceed without approval.
