# Loop 1 — Research

**Goal:** capture what the human wants it to *feel* like, understand the subject
deeply, and propose a unique concept only they could have — with creative options,
not one default.

**Input:** the target — its type and handle.

| Target type | Handle | Where the README lives |
|---|---|---|
| Personal profile | `<user>` | `<user>/<user>` → `README.md` |
| Org profile | `<org>` | `<org>/.github` → `profile/README.md` |
| Project README | `<owner>/<repo>` | that repo → `README.md` |

**Output:** `RESEARCH.md` — intent, identity, palette, real data, diagram options,
and 2–3 proposed concepts.

---

## Step 0 — Intake (do this first; `PRINCIPLES.md §0`)

Ask the human, before you look at anything:

- **Vibe / feeling** — how should it feel? Invite them to describe it and to
  **upload or link references** (images, sites, profiles, a moodboard). Feel is an
  input, not an afterthought.
- **Must-haves** — anything they explicitly want in it.
- **Explicit do-nots** — anything to avoid (colors, tropes, words, styles). Honor
  these absolutely.
- **Anything else** they want you to know.

If they're unsure, offer directions and let them react. Record all of it — every
later decision is checked against it.

## Step 1 — Pull the real data

```bash
gh api users/<user> --jq '{login,name,bio,company,blog,followers,public_repos}'
gh api "users/<user>/repos?per_page=100&sort=updated" \
  --jq '.[] | select(.fork==false) | {name,description,language,stars:.stargazers_count}'
gh api graphql -f query='query{user(login:"<user>"){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}'
```

Org → `orgs/<org>`. Project → read the code, manifest, and existing README.

## Step 2 — Find the brand

Read bio and site; download the avatar/logo and **sample the dominant color**
(`PRINCIPLES.md §7`). Sample the site's accent too. Reconcile the sampled palette
with the vibe from Step 0.

## Step 3 — Look for what can be charted (`PRINCIPLES.md §5`)

Scan for real structure worth a diagram, and note candidates:

- **Project:** architecture, data flow, module/dependency tree, state machine, API
  or request flow, ER/data model.
- **Person / org:** language distribution, contribution timeline, how projects
  relate, a tech-stack map.

For each candidate, note what it would show and whether it's native **mermaid** or a
custom SVG chart. You'll *offer* these at Gate A — never force one in.

## Step 4 — Find the throughline, then invent concepts

The one true thing about this subject (name's meaning, problem solved, who they
build for, the pattern across repos). From it, generate **2–3 distinct signature
concepts** — and for each, a fresh idea for the components too:

- a different **badge/tag idea** (not the pill by default — `PRINCIPLES.md §3`),
- a different **way to show repositories** (folders were one idea; find others),
- how the **activity/showcase** is reimagined.

Run the category-reflex check on each (`PRINCIPLES.md §1–2`): if a concept is
guessable from the category alone, or category-plus-obvious-twist, throw it out. Bring
the boldest survivors. Note one you rejected and why, so the human sees the range.

## Step 5 — Write `RESEARCH.md` and stop at Gate A

Record: the intake (vibe, must-haves, do-nots); identity summary; sampled palette
with hexes and sources; real data pulled; diagram candidates; and the 2–3 proposed
concepts with their component ideas.

> ## Gate A — human decision
>
> Present: **the vibe you captured, the palette, 2–3 concept options (each with a
> fresh badge idea and repo-visualization idea), and the diagram candidates.** Let
> the human choose a concept, opt diagrams in or out, and adjust. Bring options,
> not one answer (`PRINCIPLES.md §4`). Do not proceed without their pick.
