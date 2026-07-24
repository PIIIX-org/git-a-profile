<div align="center">

<img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/banner.svg" width="100%" alt="git-a-profile — forge a one-of-a-kind GitHub profile, org, or project README. Research, design, build, and verify with human gates, no templates." />

<br>

[![License: MIT](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/license.svg)](./LICENSE)
[![Loops 0 to 4](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/loops.svg)](./PIPELINE.md)
[![Human gates A B C](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/gates.svg)](./PRINCIPLES.md)
[![Any agent](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/agent.svg)](./INSTALL.md)
[![No templates](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/templates.svg)](./PRINCIPLES.md)

</div>

---

## What this is

Point a coding agent at this repo, give it a GitHub handle, and it forges a
one-of-a-kind README — for a **person**, an **org**, or a **project**. It
researches the real subject, invents a signature only they could have, builds
every asset by hand, writes prose a human would actually say, and verifies the
result renders on GitHub.

The default AI profile is a wall of `shields.io` badges, a typing-SVG, and a
stats card — the same on ten thousand accounts, half of them broken because a
free image host went down. That's templating. This is the opposite.

```text
  SET TARGET ─► RESEARCH ─► DESIGN ─► BUILD ─► VERIFY ─► runs/
   who/what     identity     assets   README   live shot   report on this repo
                + brand        kit     + push               on GitHub
                   ▲             ▲        ▲         ▲
                Gate A        Gate B   Gate C   (report is the deliverable)
```

## The five loops

| # | Loop | Output | Stops for |
|---|------|--------|-----------|
| **0** | [Bootstrap](./loops/00-bootstrap.md) | Capabilities ready — native, installed, or fallback | Machine ready |
| **1** | [Research](./loops/01-research.md) | Identity, brand color **sampled from their real logo**, real data | **Gate A** |
| **2** | [Design](./loops/02-design.md) | The custom asset kit: hero, badges, activity viz, footer (all your own SVG) | **Gate B** |
| **3** | [Build](./loops/03-build.md) | The assembled README, pushed to the target | **Gate C** |
| **4** | [Verify](./loops/04-verify.md) | Live screenshot + a run report under [`runs/`](./runs) | Report committed |

Full write-up: **[`PIPELINE.md`](./PIPELINE.md)** · The rules that keep it from
going generic: **[`PRINCIPLES.md`](./PRINCIPLES.md)**

## What makes it not generic

- **Custom SVGs, not badge services.** Every asset is your own committed file, so
  it never looks templated and never rots when a free host goes down.
- **One unique signature per subject, never reused.** If the concept is guessable
  from the category alone, the pipeline makes you redo it.
- **Brand color sampled from reality** — pulled from their actual logo or site.
- **Real data only** — contribution graphs from the GitHub GraphQL API; nothing
  fabricated.
- **Anti-slop prose**, **accessible by default** (alt text, `prefers-reduced-motion`),
  and **verified live** with a real screenshot.

## Install it

On **Claude Code**, install the full plugin — the conductor skill, three worker
agents, and the `/git-a-profile` command:

```
/plugin marketplace add PIIIX-org/git-a-profile
/plugin install git-a-profile
```

Then `/git-a-profile <handle>`. The skill runs the loops and holds the gates; the
worker agents (`profile-researcher`, `asset-forger`, `render-verifier`) do the
parallel labor between them — never the decisions.

## Works on any agent

The loops are plain instructions, and every platform gets a thin adapter that
points at them — nothing is duplicated. Codex (`AGENTS.md`), Cursor, Gemini CLI,
Copilot, Windsurf, Cline, OpenCode, Aider, and more are covered; the universal
entry is [`AGENTS.md`](./AGENTS.md). [Loop 0](./loops/00-bootstrap.md) makes your
agent find and install the tools it's missing, and fall back where it can't. Full
map: **[`PLATFORMS.md`](./PLATFORMS.md)** · tooling: [`INSTALL.md`](./INSTALL.md),
[`TOOLS.md`](./TOOLS.md).

## Run it

```
/loop [auto] /goal Forge a GitHub <profile|org|project> for <handle>.
Execute git-a-profile: run loops/00 → 04 in order, stop at Gates A, B, C, sample
the brand color from their real logo, build every asset as custom committed SVG,
keep it accessible, verify the live render, and commit a run report under runs/.
```

Not on Claude Code? Point your agent at this repo and have it read
[`loops/00-bootstrap.md`](./loops/00-bootstrap.md) first. Full instructions:
**[`HOW_TO_RUN.md`](./HOW_TO_RUN.md)**.

## Targets

| Type | Handle | Where the README lives |
|---|---|---|
| Personal profile | `<user>` | `<user>/<user>` → `README.md` |
| Org profile | `<org>` | `<org>/.github` → `profile/README.md` |
| Project README | `<owner>/<repo>` | that repo → `README.md` |

---

<sub>This README was forged by the pipeline it describes — banner, badges, and copy
built and verified through Loops 1–4. First run logged in [`runs/git-a-profile`](./runs/git-a-profile). Made by <a href="https://github.com/PIIIX-org">PIIIX</a>.</sub>
