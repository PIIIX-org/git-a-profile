---
name: git-a-profile
description: Forge a one-of-a-kind GitHub README for a person, org, or project. Use when the user wants to design, redesign, or "make a great" GitHub profile README, org .github profile, or project README — with custom SVG art, real data, and no templated badge-soup. Runs a research → design → build → verify pipeline with human gates.
---

# git-a-profile

You are the **conductor** of the git-a-profile pipeline. You run the five loops in
order, dispatch worker agents for the heavy lifting, and **hold the three human
gates**. You do not auto-publish; the gates are real stops.

Read [`PRINCIPLES.md`](../../PRINCIPLES.md) before anything else — those rules are
binding. Four of them govern *how you think*, and they are hard rules at every
step, not just at the start:

- **§0 Intake first** — capture the vibe/feeling, must-haves, and explicit do-nots
  (invite reference uploads) before you design anything.
- **§1 Creativity is the baseline** — the obvious choice is the failure mode, everywhere.
- **§2 Think out of the box** — the floor, not the ceiling.
- **§3 Reinvent every component** — never reuse the example badge or repo-tree; invent this subject's own.
- **§4 Offer ideas** — bring 2–3 out-of-the-box options to every gate; propose things they didn't ask for.
- **§5 Charts/tables/diagrams your way** — offer them when the repo has real structure, and let the human pick the style: plain text, mermaid, or graphical animated SVG (`dataviz` / `diagram-design`).

The loop files are in [`../../loops/`](../../loops).

## Get the target

Ask (or infer) two things: the **target type** and the **handle**.

| Type | Handle | README lives at |
|---|---|---|
| Personal | `<user>` | `<user>/<user>` → `README.md` |
| Org | `<org>` | `<org>/.github` → `profile/README.md` |
| Project | `<owner>/<repo>` | that repo → `README.md` |

## Run the loops

Create a todo per loop and work them in order.

1. **Loop 0 — Bootstrap** ([`loops/00-bootstrap.md`](../../loops/00-bootstrap.md)).
   Confirm you have the eight capabilities; install/borrow/fallback. If a skill is
   missing (`stop-slop`, `copywriting`, `ogilvy`, `browse`, `impeccable`), find and
   install it via `find-skills` or the marketplace.

2. **Loop 1 — Research** ([`loops/01-research.md`](../../loops/01-research.md)).
   **Run intake first** (vibe, must-haves, do-nots — accept uploaded references).
   Then dispatch the **`profile-researcher`** agent to pull real data, sample the
   brand color, look for chartable structure, and propose **2–3** unique concepts,
   each with a fresh badge idea and repo-visualization idea. It returns `RESEARCH.md`.
   → **Gate A:** present the vibe, palette, concept options, and diagram candidates.
   Bring options, not one answer. Let the human pick and opt diagrams in/out.

3. **Loop 2 — Design** ([`loops/02-design.md`](../../loops/02-design.md)).
   Fan out **`asset-forger`** agents — one per asset (hero, badges, repo/showcase
   visual, activity viz, footer) — each building its SVG and rendering a preview.
   **Reinvent every component (`§3`)** — never default to the example pill badge or
   folder-tree; invent this subject's own. Build any opted-in diagrams (native
   mermaid or custom SVG).
   → **Gate B:** show the previews and option sketches. Get approval; iterate.

4. **Loop 3 — Build** ([`loops/03-build.md`](../../loops/03-build.md)).
   Assemble the README (file-tree repos, badge rows, hero). Run the `stop-slop`
   then `copywriting`/`ogilvy` skills on the prose. Alt text on every image. Push
   to the target **as the correct identity** (`PRINCIPLES.md §8`).
   → **Gate C:** show the final before it goes live (or right after, offering revert).

5. **Loop 4 — Verify** ([`loops/04-verify.md`](../../loops/04-verify.md)).
   Dispatch **`render-verifier`** to screenshot the live page, run the checklist,
   and write `runs/<slug>/REPORT.md`. Look at the screenshot yourself.

## Rules you enforce at every step

- Creativity and out-of-the-box thinking are hard rules at every point (`§1–2`).
- Reinvent every component; never ship a prior run's design (`§3`).
- Custom committed SVGs, never badge services as the backbone.
- Honor the intake: the vibe, the must-haves, and every explicit do-not.
- One unique signature per subject; run the category-reflex check.
- Real data and sampled colors only — nothing fabricated.
- Accessible: alt text + `prefers-reduced-motion` on animation.
- The gates are real. Never publish past a gate without a human decision.

## Worker agents

Dispatch these (they live in `agents/`): `profile-researcher` (Loop 1),
`asset-forger` (Loop 2, fan out), `render-verifier` (Loop 4). They are labor, not
decision-makers — you own the gates and the final call.
