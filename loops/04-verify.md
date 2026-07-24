# Loop 4 — Verify & report

**Goal:** confirm the profile actually renders on GitHub, check accessibility, and
write a run report. "HTTP 200" is not "it renders" (`PRINCIPLES.md §7`).

**Input:** the pushed README.

**Output:** `runs/<slug>/REPORT.md` committed to *this* pipeline repo.

---

## Step 1 — Screenshot the rendered page

Open the live page and screenshot the README region:

- Personal/org: `https://github.com/<user-or-org>`
- Project: `https://github.com/<owner>/<repo>`

Use browser automation (Claude `browse`, Playwright, Puppeteer, headless Chrome).
No automation? Open it yourself and/or ask the human to confirm. **Look at it.**

## Step 2 — The render checklist

- **Every image loads.** GitHub serves same-origin `raw.githubusercontent.com`
  SVGs directly and proxies external images through `camo` — if a custom SVG is
  blank, check it's committed and served as `image/svg+xml`.
- **Animation moves** (and stops under reduced motion if you enable that setting).
- **`<details>` expand/collapse** works; links resolve; private repos aren't
  linked.
- **Contrast** is readable in both GitHub light and dark themes.
- **Alt text** is present on every image (view source or your build notes).

## Step 3 — Fix and re-verify

Anything wrong, fix in Loop 2/3 and screenshot again. Don't sign off on a
description — sign off on a picture.

## Step 4 — Write the run report

Copy `runs/_template/` to `runs/<slug>/` (slug = the subject, e.g. `octocat` or
`acme-org`) and fill in `REPORT.md`:

- Target (type + handle), date, agent/platform used.
- The concept chosen and why.
- Palette (hexes) and where each color came from.
- Assets built (list) and the render/a11y checklist result.
- Link to the live profile + the verification screenshot.
- Anything deferred or using a fallback.

Commit it. The run log is how the pipeline proves it works and how the next person
learns from yours.

> **Gate:** none — but the report is the deliverable. A run isn't done until its
> `REPORT.md` is committed and the live profile is confirmed by screenshot.
