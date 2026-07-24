<div align="center">

<img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/banner.svg" width="100%" alt="git-a-profile — forge a one-of-a-kind GitHub profile, org, or project README. Research, design, build, and verify with human gates, no templates." />

<br>

[![Profiles forged](https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/forges.svg)](./runs)
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

<sub>The **profiles forged** badge is self-updating: a GitHub Action recounts the
[`runs/`](./runs) reports and regenerates the badge — no external service. It's an
honest lower bound: documented forges, plus profiles that keep the default "Forged
with git-a-profile" footer. Running the pipeline locally leaves no trace to count,
and the footer is freely removable, so the real number runs higher.</sub>

Full write-up: **[`PIPELINE.md`](./PIPELINE.md)** · The rules that keep it from
going generic: **[`PRINCIPLES.md`](./PRINCIPLES.md)**

## What makes it not generic

- **It asks how you want it to *feel* first.** Before any design, it captures your
  vibe, your must-haves, your explicit do-nots — and takes reference images you
  upload. Feel is an input, not an afterthought.
- **Creativity and out-of-the-box thinking are hard rules at every step.** The
  obvious choice is treated as the failure mode. It reaches for the idea you
  wouldn't have asked for — the way your repos became openable folders, a
  contribution graph became a star map, a name's meaning became an orbital system.
- **It reinvents every component every run.** The badge design, the way repos are
  shown, the header — none are reused. If the output could be pattern-matched to a
  previous profile, the pipeline makes it redo it.
- **It proposes, doesn't just execute.** Options at every gate; ideas you didn't
  request.
- **It charts what deserves charting — your way.** Offers diagrams, tables, and
  charts when the repo has real structure, and lets you choose the style: plain
  text, code-rendered mermaid, or graphical animated SVG (via `dataviz` /
  `diagram-design`).
- **It checks its own work.** A pre-flight gate (`scripts/preflight.py`) fails the
  build on missing alt text, a badge-service backbone, or dead image links —
  before it reaches you.
- **It can stay current.** Opt in and your data-driven assets (contribution graph,
  stats) self-refresh on a schedule you pick — no badge-service profile does that.
- **Custom SVGs, not badge services** — never rots, never templated. **Brand color
  sampled from reality.** **Real data only.** **Anti-slop prose**, **accessible by
  default** (alt text, `prefers-reduced-motion`), **verified live** with a real
  screenshot.

## Gallery

Real profiles forged with this pipeline. **[Add yours →](./CONTRIBUTING.md)**

<table>
<tr>
<td width="50%"><a href="https://github.com/PIIIX-org"><img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/gallery/piiix.png" alt="PIIIX org profile — an animated orbital system where the products orbit the PIIIX star"/></a><br><sub><b>PIIIX</b> · org · orbital system</sub></td>
<td width="50%"><a href="https://github.com/CyborgTech-co"><img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/gallery/cyborg.png" alt="Cyborg Tech org profile — a glitch / cyberpunk header with chromatic aberration"/></a><br><sub><b>Cyborg Tech</b> · org · glitch / cyberpunk</sub></td>
</tr>
<tr>
<td><a href="https://github.com/Taha-Mahmoodi"><img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/gallery/taha.png" alt="Taha-Mahmoodi personal profile — a terminal header and a contribution star-timeline"/></a><br><sub><b>Taha-Mahmoodi</b> · personal · terminal + star-timeline</sub></td>
<td><a href="https://github.com/sadeqisaidmohaddes-star"><img src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/gallery/sadeq.png" alt="Said Mohaddes Sadeqi personal profile — an accessibility-first voice waveform"/></a><br><sub><b>Said Mohaddes Sadeqi</b> · personal · accessibility-first</sub></td>
</tr>
</table>

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

## How this repo is laid out

Curated by purpose, not dumped as a file list — the same move the pipeline makes for
any file-heavy repo (`PRINCIPLES.md §16`). Nothing here was renamed to look tidy;
this is the *story* of the tree, not the tree.

```text
git-a-profile/
├─ the method ─────────── what the agent actually runs
│  ├─ loops/00–04         bootstrap → research → design → build → verify
│  ├─ PIPELINE.md         full write-up
│  └─ PRINCIPLES.md       the hard rules (intake, creativity, a11y, §16…)
├─ run it ─────────────── entry points, one per platform
│  ├─ README · HOW_TO_RUN · AGENTS.md · CLAUDE.md
│  └─ PLATFORMS.md        Codex · Cursor · Gemini · Copilot · Windsurf · Cline · OpenCode
├─ the Claude plugin ─── skill + worker agents + command
│  ├─ skills/ · agents/ · commands/
│  └─ .claude-plugin/     manifest + marketplace
├─ automation ─────────── scripts and the self-updating badge
│  ├─ scripts/            preflight.py · forge_badge.py
│  ├─ templates/          self-refresh workflow you drop into your repo
│  └─ .github/workflows/  the forge counter
├─ the forge log ──────── proof it works, and social proof
│  ├─ runs/               one report per forge
│  └─ assets/             banner · badges · gallery
└─ meta ───────────────── CONTRIBUTING · TRANSPARENCY · TOOLS · INSTALL · LICENSE
```

## Trust & contributing

What it touches — and what it doesn't — is spelled out in
**[`TRANSPARENCY.md`](./TRANSPARENCY.md)** (no telemetry, real data only, credit
removable). Made a profile with it? **[Share your forge](./CONTRIBUTING.md)** — it
joins the gallery and the count.

## Targets

| Type | Handle | Where the README lives |
|---|---|---|
| Personal profile | `<user>` | `<user>/<user>` → `README.md` |
| Org profile | `<org>` | `<org>/.github` → `profile/README.md` |
| Project README | `<owner>/<repo>` | that repo → `README.md` |

---

<!-- forged-with: git-a-profile -->
<a href="https://github.com/PIIIX-org/git-a-profile"><img alt="Forged with git-a-profile" height="26" src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/forged-with.svg"/></a>

<sub>This README was forged by the pipeline it describes — banner, badges, and copy built and verified through Loops 1–4. First run in [`runs/git-a-profile`](./runs/git-a-profile). Made by <a href="https://github.com/PIIIX-org">PIIIX</a>.</sub>
