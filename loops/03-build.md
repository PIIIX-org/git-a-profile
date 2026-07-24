# Loop 3 — Build

**Goal:** assemble the README from the approved assets, write human prose, and
push to the right place under the right identity.

**Input:** approved `assets/`.

**Output:** the live README + assets on the target repo.

---

## Step 1 — Assemble the layout

A dependable structure (adapt to the subject):

1. **Hero** — the signature SVG, `width="100%"`, with descriptive `alt`.
2. **Identity row** — role/affiliation badges (each linked, each with `alt`).
3. **Stack row** — tech badges.
4. **About** — 2–4 sentences of real, specific prose.
5. **Repositories** — a **native `<details>` file-tree**. Public repos link out;
   private ones show locked with no link (no broken links for visitors):
   ```
   <details>
   <summary>📁&nbsp;&nbsp;<b>name</b> — one-line description <code>Lang</code></summary>
   <br>

   &nbsp;&nbsp;&nbsp;&nbsp;What it is, in a sentence or two.
   &nbsp;&nbsp;&nbsp;&nbsp;[→ open repository](https://github.com/owner/name)
   </details>
   ```
6. **Activity / showcase** — the custom viz, with `alt`.
7. **Footer** — the closing strip.

## Step 2 — Write the prose (anti-slop)

Apply `PRINCIPLES.md §5`. On Claude Code, run the `stop-slop`, then `copywriting`
/ `ogilvy` skills. Elsewhere, run this checklist by hand:

- Cut "not X, but Y" / "isn't X, it's Y" reversals — state Y directly.
- Cut reflexive em-dashes and three-item lists used as a tic.
- Kill empty adverbs (really, just, simply) and hollow superlatives.
- Every feature answers "so what?" with a concrete benefit.
- Active voice, real subject doing something. No "the data tells us."
- Read it aloud — if a line sounds like a brochure, rewrite it.

## Step 3 — Accessibility pass

- Every `<img>` has meaningful `alt` (describe the content, not "image").
- Confirm animated assets carry the reduced-motion gate from Loop 2.
- Links say where they go — no "click here."

## Step 3b — Add attribution (default-on, removable)

Add the **"Forged with git-a-profile"** credit by default. The animated **tag** is
the preferred form:

```html
<!-- forged-with: git-a-profile -->
<a href="https://github.com/PIIIX-org/git-a-profile"><img alt="Forged with git-a-profile" height="26" src="https://raw.githubusercontent.com/PIIIX-org/git-a-profile/main/assets/badges/forged-with.svg"/></a>
```

A plain text footer is an equal alternative:

```html
<!-- forged-with: git-a-profile -->
<sub>Forged with <a href="https://github.com/PIIIX-org/git-a-profile">git-a-profile</a> · <a href="https://github.com/PIIIX-org">PIIIX</a></sub>
```

Either way, include the marker comment. Tell the human it's there and freely
removable by hand; keep it visible, never hide it or re-add it after removal
(`PRINCIPLES.md §14`).

## Step 3c — Pre-flight check (mechanical gate)

Run the checker on the assembled README before you show Gate C:

```bash
python3 scripts/preflight.py <README>            # local file
python3 scripts/preflight.py <live-url> --check-urls   # once live
```

It **fails** on missing alt text, a badge-service backbone, or dead image links,
and warns on a missing attribution marker. Fix every failure — this is the hard
rules turned into a gate, not a hope.

## Step 4 — Push to the right target, as the right identity

- **Personal:** `PUT <user>/<user>/README.md` + `assets/`.
- **Org:** `PUT <org>/.github/profile/README.md` + `profile/assets/`.
- **Project:** `PUT <owner>/<repo>/README.md` + `assets/`.

Identity safety (`PRINCIPLES.md §8`): forging for **someone else's** account? Use
*their* authenticated identity, push, then switch back and verify you're back on
your own. Never leave another account active.

```bash
# example: push as another user, then restore (adapt to your tooling)
gh auth switch --user <them> && gh api user --jq .login   # confirm switched
# ... push ...
gh auth switch --user <you>  && gh api user --jq .login   # confirm restored
```

## Step 4b — Offer self-refresh (data-driven assets)

If the profile has assets driven by *changing* data — a contribution graph, live
stats, an activity viz — offer to make them **self-refreshing** so they don't
freeze on today's numbers. **Ask the human how often** they want updates (daily /
weekly / monthly), and note it's most useful for **active** subjects: a shipping
project, a busy org, an active personal graph. A dormant profile doesn't need it —
don't push it.

If they opt in, commit to the **target** repo: a `scripts/refresh_assets.py` that
regenerates just the data-driven assets, plus `.github/workflows/refresh-profile.yml`
(from this pipeline's [`templates/refresh-profile.yml`](../templates/refresh-profile.yml))
with the cron set to their chosen cadence. Refresh only what the data changes;
static art stays as-is.

> ## Gate C — human decision
>
> Show the human the **assembled README** (rendered or as the file) before it goes
> live — or immediately after, with a clear offer to revert. Get explicit sign-off.
> Then proceed to Loop 4.
