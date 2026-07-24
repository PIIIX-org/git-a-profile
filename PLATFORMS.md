# Platforms

`git-a-profile` ships one pipeline and a thin adapter for each agent. The loop
files in [`loops/`](./loops) are the single source of truth; every adapter below
points at them, so nothing is duplicated or drifts.

| Platform | How it finds the pipeline | Install / run |
|---|---|---|
| **Claude Code** | Full plugin: skill + 3 worker agents + `/git-a-profile` command | `claude plugin marketplace add PIIIX-org/git-a-profile` then `claude plugin install git-a-profile` — or just `/git-a-profile <handle>` in this repo. Also reads `CLAUDE.md`. |
| **Codex CLI** | `AGENTS.md` (+ `.codex-plugin/plugin.json`) | Open the repo; Codex reads `AGENTS.md`. Ask it to run git-a-profile for `<handle>`. |
| **Cursor** | `.cursor/rules/git-a-profile.mdc` | Open the repo in Cursor; the rule loads. Ask it to forge a profile. |
| **Gemini CLI** | `gemini-extension.json` → `AGENTS.md` | Reads `AGENTS.md` as the context file. |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Copilot picks it up in-repo. |
| **Windsurf** | `.windsurfrules` | Loaded automatically in-repo. |
| **Cline / Roo** | `.clinerules` | Loaded automatically in-repo. |
| **OpenCode** | `opencode.json` → instructions | Reads `AGENTS.md`, `PRINCIPLES.md`, Loop 0. |
| **Aider / Zed / anything else** | `AGENTS.md` | Add it as a read/context file (`aider --read AGENTS.md`), or paste the "How to run it" section. |

## The universal path

Any agent that can read markdown, run a shell, and write files can run this. Point
it at [`AGENTS.md`](./AGENTS.md) — that's the portable entry. It calls the loops,
and Loop 0 makes the agent find and install the tools it's missing on its own
platform (or fall back). No platform-specific magic is required beyond git access.

## Adding a platform

New agent format? Add one small adapter file that says "read `AGENTS.md` and run
the loops," and add a row here. Don't copy the loops — point at them.
