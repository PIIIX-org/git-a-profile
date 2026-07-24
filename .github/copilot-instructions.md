# git-a-profile

This repository is the **git-a-profile** pipeline — it forges one-of-a-kind GitHub
READMEs for a person, org, or project.

When the user wants to design/redesign a GitHub profile or README, follow the
pipeline: read `AGENTS.md` and `PRINCIPLES.md`, then run the loop files
`loops/00-bootstrap.md` through `loops/04-verify.md` in order, stopping at the
three human gates. Build every visual as a custom committed SVG (never badge
services), invent one unique signature per subject, sample the brand color from
their real logo, use only real data, keep it accessible (alt text +
`prefers-reduced-motion`), and verify the live render with a screenshot.
