---
description: Forge a one-of-a-kind GitHub README for a person, org, or project (research → design → build → verify, with human gates).
argument-hint: "<user | org | owner/repo>"
---

Invoke the **git-a-profile** skill and run the pipeline for the target: `$ARGUMENTS`.

Determine the target type (personal `<user>` / org `<org>` / project `<owner>/<repo>`),
then run loops 0→4 in order. Dispatch the worker agents (`profile-researcher`,
`asset-forger`, `render-verifier`) for the heavy loops, and stop at Gates A, B, and
C for the human. Enforce PRINCIPLES.md throughout: custom committed SVGs (no badge
services), one unique signature, sampled brand color, real data, accessibility,
and live verification by screenshot.
