# What this touches

git-a-profile runs on your machine, through your agent. Plainly, what it does:

- **Reads public GitHub data** about the subject (profile, repos, languages, the
  contribution graph) via the GitHub API, and reads their public site to sample a
  brand color.
- **Writes files locally** — SVGs and a README — and **pushes commits** to the one
  repo you point it at (`<user>/<user>`, `<org>/.github`, or a project repo).
- **Can act as another identity** *only if you tell it to* — forging someone else's
  profile means using their authenticated git login so the commits are theirs. It
  switches back to you afterward and never cross-contaminates accounts
  (`PRINCIPLES.md §12`).

What it does **not** do:

- No telemetry. It doesn't phone home. The only "counter" is a badge on *this*
  repo that tallies contributed run reports and profiles that kept the credit —
  it can't see private runs.
- No fabricated data — everything shown is sourced (`PRINCIPLES.md §8`).
- No hidden attribution — the "Forged with git-a-profile" credit is visible and
  removable by hand (`PRINCIPLES.md §14`).

The one hard requirement is git access to the target. Everything else is local.
