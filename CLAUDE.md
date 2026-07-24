# git-a-profile (Claude Code)

This repo is an installable plugin **and** a universal, agent-agnostic pipeline.

**To run it here:** use `/git-a-profile <handle>`, or invoke the `git-a-profile`
skill. The skill is the conductor: it runs the five loops, dispatches the worker
agents, and holds the three human gates.

- Skill: `skills/git-a-profile/SKILL.md`
- Worker agents: `agents/profile-researcher.md`, `agents/asset-forger.md`, `agents/render-verifier.md`
- Pipeline + rules: `PIPELINE.md`, `PRINCIPLES.md`, `loops/00`–`04`
- Other platforms: `AGENTS.md` (universal), `PLATFORMS.md` (per-tool)

The loops in `loops/` are the single source of truth. The skill, agents, and every
platform adapter point at them — nothing is duplicated.
