# Loop 2 — Design

**Goal:** build the custom asset kit for the approved concept — reinvented for this
subject, not reused from any prior run. Every asset is your own committed SVG (or
native mermaid for diagrams). No badge services (`PRINCIPLES.md §6`).

**Input:** approved `RESEARCH.md` (vibe + concept + palette + diagram opt-ins).

**Output:** `assets/` full of SVGs (+ any mermaid), each previewed, ready for the README.

---

## The rule that governs this whole loop

**Reinvent every component (`PRINCIPLES.md §3`).** The reference assets in this repo
are technique, not a template. Do not reach for the monospace pill badge or the
folder-tree repo list by reflex. Invent *this subject's* badge idea and *this
subject's* way of showing repositories. If it looks like a previous run, redo it.
Creativity is the floor here, not a bonus (`§1–2`).

## The asset kit

Build these in the approved palette and vibe, in a consistent type system:

1. **Signature hero** — the approved unique concept, as an animated SVG.
2. **Badge / tag system** — reinvented for this subject. Maybe it's not pills at
   all. Whatever it is, it carries real logos and the right colors, and it's *this
   profile's* idea of a tag.
3. **Repository / showcase visual** — reinvented. Folders were one past idea; find
   the one that fits this subject (a map, a shelf, a deck, a timeline, a
   constellation…).
4. **Activity / showcase viz** — real data (person) or real showcase (org/project),
   reimagined per the concept.
5. **Structure view (file-heavy projects)** — if the repo has many files/folders,
   build a *curated* map that groups files by purpose, nests related ones, hides
   noise, and annotates each group. Render it per the chosen style (`§5`): an
   annotated tree in a code block, a set of `<details>` groups, or a diagram. Show
   the *logical* shape. **Never move or rename the real files (`§16`)** — this is
   documentation, not refactoring.
6. **Diagrams / charts / tables the human opted into**, in the style they chose (`§5`):
   - **Plain text / code** — ASCII, fenced blocks, markdown tables. No assets.
   - **Code-rendered** — native mermaid (` ```mermaid `) and markdown tables. No assets.
   - **Graphical** — your own committed SVG, animated where it helps. Use the
     `dataviz` skill for chart design and `diagram-design` for diagrams; render the
     final as an SVG through the asset step. Alt text required.
   Only build ones that earn their place.
7. **Footer** — a closing note that echoes the hero.

## Before you build each — offer options (`PRINCIPLES.md §4`)

For the components with real design freedom (badges, repo visual), it's fair to
sketch 2 quick directions and let the human pick at Gate B, rather than committing
to the first. Bring ideas, not one default.

## How to build

- **Write SVG directly.** Tidy viewBox, relative units, `width="100%"` friendly.
- **Logos:** embed the subject's real mark (sample + clip an `<image>`), or pull a
  tech logo's `<path>` from an open icon set and recolor it; redraw a simple mark
  when none exists.
- **Animation** renders inside an `<img>` on GitHub: SMIL for motion paths; CSS
  `<style>` `@keyframes` when you need the reduced-motion gate:
  `@media (prefers-reduced-motion: reduce){ .anim{ animation:none !important } }`.
- **Mermaid diagrams** go straight in the README as fenced blocks — theme them to
  the palette where the renderer allows.
- **Contrast:** white text on saturated fills, dark on light; body ≥ 4.5:1.
- **RTL / non-Latin (`§15`):** set `direction="rtl"` and right-align RTL text; use a font that renders the script; never mangle a name to fit.

## Preview every asset

Render each SVG to PNG and look at it:

```bash
qlmanage -t -s 900 -o . asset.svg      # macOS
rsvg-convert asset.svg -o asset.png    # librsvg
resvg asset.svg asset.png              # resvg
```

For mermaid, preview in any markdown viewer that renders it (or `mmdc`). No
renderer? Describe each asset precisely and rely on Gate B. Fix anything that
clips, misaligns, or reads wrong.

## Commit the assets

Under `assets/` (or `profile/assets/` for an org `.github`).

> ## Gate B — human decision
>
> Show the **preview images** (and any option sketches). Confirm the visual
> direction reads as intended — and that it doesn't look like a prior run. Iterate
> here; it's cheap. Do not assemble the README without approval.
