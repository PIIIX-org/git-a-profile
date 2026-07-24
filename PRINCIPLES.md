# Principles

These are the rules that separate a forged profile from a templated one. Every
loop enforces them. If you break one, the output looks like everyone else's.

## 1. No badge services. Build your own SVGs.

Do not decorate with `shields.io`, `readme-typing-svg`, `github-readme-stats`,
streak cards, or any third-party image endpoint as the backbone of the design.
They all look the same, and they rot — public instances go down (a 503 or a
dead domain leaves a wall of broken images on someone's profile forever).

Generate your own SVG files, commit them to the repo, and reference them by
`raw.githubusercontent.com` URL. Self-hosted assets never break and never look
generic. (A shields badge is acceptable as a rare, deliberate accent — never as
the whole visual system.)

## 2. One unique signature per subject. Never reused.

Every profile gets a hero concept invented for *that* subject. Terminal window,
orbital system, glitch wordmark, audio waveform — these were four real ones, and
none was used twice.

Run the category-reflex check before you commit to a concept:

- **First-order:** could someone guess the concept from the subject's category
  alone? ("It's a design agency, so… a glitch header.") If yes, it's the first
  training-data reflex. Redo it.
- **Second-order:** could someone guess it from category-plus-obvious-twist?
  Redo until neither is obvious.

The concept should come from something *true* about the subject — their name's
meaning, what they build, their brand's origin — not from a genre.

## 3. Sample the brand color from reality.

Pull the accent color from the subject's actual logo, site, or product — sample
the pixels, don't invent a hex. If they have no brand, choose deliberately (write
one sentence of physical scene that forces the choice) and say why.

## 4. Real data only.

Contribution graphs come from the GitHub GraphQL API for that account. Repo lists
come from the API. Stats are real. Never fabricate activity, numbers, or a
persona. If a claim can't be sourced, cut it.

## 5. Anti-slop prose.

No "not X, but Y" contrasts. No em-dash-joined AI cadence as a tic. No three-item
lists by reflex. No hollow superlatives. Write the way the subject would talk.
Every feature answers "so what?" with a real benefit. (On Claude Code, the
`stop-slop`, `copywriting`, and `ogilvy` skills do this; elsewhere, apply the
checklist in `loops/03-build.md`.)

## 6. Accessible by default.

Every image gets descriptive alt text. Any animation is gated behind
`prefers-reduced-motion` (CSS-in-SVG media query) so it goes static for
motion-sensitive viewers. Body contrast clears 4.5:1. This is not optional — a
profile that fails here fails.

## 7. Verify live. Never assume.

Screenshot the *rendered* GitHub page and look at it. GitHub proxies external
images through `camo` and serves same-origin SVGs directly — behavior differs,
and "it returned HTTP 200" is not "it renders." Confirm with your eyes.

## 8. Identity safety.

Push to the correct account. A personal profile lives at
`<user>/<user>`; an org profile lives at `<org>/.github` under `profile/README.md`;
a project README lives in that repo. If forging for someone else's account, use
*their* authenticated identity so the commits are theirs, and switch back after.
Never cross-contaminate accounts.

## 9. Human gates are real stops.

Gate A (identity + concept), Gate B (visual direction), Gate C (final before
push). Stop and get a human decision at each. This pipeline is fast; the gates
are what keep it honest.
