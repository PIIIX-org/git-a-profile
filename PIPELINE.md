# The pipeline

`git-a-profile` turns any GitHub subject — a person, an org, or a project — into a
one-of-a-kind README, by running five loops with human gates between them. It is
an agent operating system: markdown instructions a capable coding agent executes,
not a program you install.

```text
  SET TARGET ─► RESEARCH ─► DESIGN ─► BUILD ─► VERIFY ─► runs/
   who/what     identity     assets   README   live shot   report on this repo
                + brand       kit      + push                on GitHub
                   ▲            ▲         ▲          ▲
                Gate A       Gate B    Gate C   (report is the deliverable)
```

## Why it exists

The default AI profile is a wall of `shields.io` badges, a typing-SVG, and a stats
card — the same on ten thousand accounts, and half of them broken because a free
image host went down. That is templating, not design.

This pipeline forces the opposite: research the real subject, invent a signature
only they could have, build every asset by hand, write prose a human would say,
and verify it renders. The result looks like *them*, and it doesn't rot.

## The five loops

| # | Loop | File | Output | Gate |
|---|------|------|--------|------|
| **0** | Bootstrap | [`loops/00-bootstrap.md`](./loops/00-bootstrap.md) | Capabilities ready (native / installed / fallback) | — |
| **1** | Research | [`loops/01-research.md`](./loops/01-research.md) | `RESEARCH.md`: identity, sampled palette, real data, concept | **A** |
| **2** | Design | [`loops/02-design.md`](./loops/02-design.md) | `assets/`: hero, badges, activity viz, footer (all custom SVG) | **B** |
| **3** | Build | [`loops/03-build.md`](./loops/03-build.md) | Live README + assets pushed to the target | **C** |
| **4** | Verify | [`loops/04-verify.md`](./loops/04-verify.md) | Live screenshot + `runs/<slug>/REPORT.md` | — |

The non-negotiable rules that run through every loop are in
[`PRINCIPLES.md`](./PRINCIPLES.md). Read them first.

## Targets

| Type | Handle | README location |
|---|---|---|
| Personal profile | `<user>` | `<user>/<user>` → `README.md` |
| Org profile | `<org>` | `<org>/.github` → `profile/README.md` |
| Project README | `<owner>/<repo>` | that repo → `README.md` |

## Running it

See [`HOW_TO_RUN.md`](./HOW_TO_RUN.md) for the exact invocation on Claude Code and
on other agents. In short: point your agent at this repo, give it the target, and
have it execute the loops in order, stopping at each gate for your decision.
