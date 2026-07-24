# How to run it

## On Claude Code

Point Claude Code at this repo and drive it with `/loop` + a `/goal`, running the
loop files in order. One reliable pattern:

```
/loop [auto] /goal Forge a GitHub <profile|org|project> for <handle>.
Execute git-a-profile: run loops/00 → 04 in order, stop at Gates A, B, C for my
approval, sample the brand color from their real logo/site, build every asset as
custom committed SVG (no badge services), keep it accessible, verify the live
render with a screenshot, and commit a run report under runs/.
```

Claude Code will use its skills where it has them (`impeccable`, `stop-slop`,
`copywriting`, `ogilvy`, `browse`) and install/borrow equivalents where it
doesn't — Loop 0 handles that.

## On any other capable agent

The loop files are plain instructions. Codex CLI, Cursor, Aider, Gemini CLI, and
similar agents can run them the same way — read `loops/00-bootstrap.md` first; it
finds and installs the equivalents of the capabilities the pipeline needs on your
platform, and falls back gracefully when it can't. See [`INSTALL.md`](./INSTALL.md).

## Manually

Not driving an agent? You can follow the loops yourself. The SVG generators are
ordinary scripts; the gates are just moments to look at the work and decide. It's
slower, but the method is the same.

## The one hard requirement

Git access to the target: a `gh` login (or a token with `repo` scope) that can push
to the target repo. Everything else has a fallback in Loop 0.
