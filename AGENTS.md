# git-a-profile — agent instructions

This file is the universal entry point. It works for any agent that reads an
`AGENTS.md` (Codex, Cursor, Aider, Zed, OpenCode, and others). Claude Code has a
richer path — a skill + worker agents — described in `CLAUDE.md`; everything below
still applies to it.

## What you are doing

Forge a **one-of-a-kind** GitHub README for a subject — a person, an org, or a
project. Not from a template: you research the real subject, invent a signature
only they could have, build every asset by hand, write human prose, and verify it
renders. Read [`PRINCIPLES.md`](./PRINCIPLES.md) first; those rules are binding.

## How to run it

Execute the five loops in order. Each is a file under `loops/`. Stop at the human
gates — they are real stops, not formalities.

1. **`loops/00-bootstrap.md`** — ready your capabilities (install/borrow/fallback). Actively search your own platform's registry for tools you lack.
2. **`loops/01-research.md`** — pull real data, sample the brand color, propose the one unique concept. → **Gate A** (human approves concept + palette).
3. **`loops/02-design.md`** — build the custom asset kit as your own committed SVGs. → **Gate B** (human approves the visuals).
4. **`loops/03-build.md`** — assemble the README, write anti-slop prose, push to the target under the right identity. → **Gate C** (human approves before/at go-live).
5. **`loops/04-verify.md`** — screenshot the live page, run the checklist, commit a report under `runs/`.

## The non-negotiables (full list in `PRINCIPLES.md`)

- Custom SVGs you commit — never badge services as the visual backbone.
- One unique signature per subject; if it's guessable from the category, redo it.
- Brand color sampled from their real logo/site; real data only.
- Anti-slop prose; accessible by default (alt text + `prefers-reduced-motion`).
- Verify the live render with a screenshot; never assume "HTTP 200" means "renders."
- Push as the correct identity; never cross-contaminate accounts.
- The three human gates are real stops.

## Targets

| Type | Handle | README location |
|---|---|---|
| Personal | `<user>` | `<user>/<user>` → `README.md` |
| Org | `<org>` | `<org>/.github` → `profile/README.md` |
| Project | `<owner>/<repo>` | that repo → `README.md` |

## Worker agents (optional, if your platform supports subagents)

The loops are parallelizable in places. If you can spawn subagents, use them as
**workers, never as decision-makers** — the gates stay with the human:

- a **researcher** worker for Loop 1 (→ Gate A),
- **asset-forger** workers for Loop 2, one per asset (→ Gate B),
- a **verifier** worker for Loop 4.

Claude Code ships these as `agents/*.md`. On other platforms, run the loops inline
or fan out with your own subagent mechanism. Full method: [`PIPELINE.md`](./PIPELINE.md).
