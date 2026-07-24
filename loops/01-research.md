# Loop 1 — Research

**Goal:** understand the subject deeply enough to invent a design only they could
have. Then decide the one unique concept.

**Input:** the target — its type and handle.

| Target type | Handle | Where the README lives |
|---|---|---|
| Personal profile | `<user>` | `<user>/<user>` → `README.md` |
| Org profile | `<org>` | `<org>/.github` → `profile/README.md` |
| Project README | `<owner>/<repo>` | that repo → `README.md` |

**Output:** `RESEARCH.md` — identity, palette, real data, and the proposed concept.

---

## Step 1 — Pull the real data

```bash
# who they are
gh api users/<user> --jq '{login,name,bio,company,blog,followers,public_repos}'
# their repos (non-fork, by recent activity)
gh api "users/<user>/repos?per_page=100&sort=updated" \
  --jq '.[] | select(.fork==false) | {name,description,language,stars:.stargazers_count}'
# their real contribution graph (personal targets)
gh api graphql -f query='query{user(login:"<user>"){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}'
```

For an org, use `orgs/<org>` and `orgs/<org>/repos`. For a project, read the
repo's code, `package.json`/manifest, and existing README.

## Step 2 — Find the brand

- Read their bio, site (`blog` field), and any linked product.
- Get their avatar/logo: `gh api users/<user> --jq .avatar_url` (or `orgs/<org>`),
  download it, and **sample the dominant color** (see `PRINCIPLES.md §3`). If they
  have a real site, sample its accent too.
- If there's genuinely no brand, choose a color deliberately and record why.

## Step 3 — Find the throughline

What is the *one* true thing about this subject? Their name's origin, the problem
they solve, who they build for, the through-line across their repos. This is where
the concept comes from — not from their category.

## Step 4 — Decide the unique concept

Propose **one** signature hero concept, drawn from the throughline. Then run the
category-reflex check (`PRINCIPLES.md §2`): if it's guessable from the category
alone, or from category-plus-obvious-twist, redo it.

Also decide:
- **Palette** — accent (sampled) + background + ink, contrast-checked.
- **Activity/showcase viz** — for a person, a custom take on the real contribution
  data; for an org/project, a real showcase (products, architecture, stats).
- **Repo/section structure** — what the folder tree or sections will hold.

## Step 5 — Write `RESEARCH.md` and stop at Gate A

Record: identity summary, sampled palette (with hexes), real data pulled, the
proposed concept + why it's true to them, and the planned sections.

> ## Gate A — human decision
>
> Present to the human: **who this is, the sampled brand palette, and the one
> proposed concept.** Ask them to approve or adjust the concept and colors before
> any asset is built. Do not proceed to Loop 2 without it.
