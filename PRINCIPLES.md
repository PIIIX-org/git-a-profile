# Principles

These are the rules that separate a forged profile from a templated one. Every
loop enforces them. They are hard rules, not suggestions — if you break one, the
output looks like everyone else's.

The first four are about *intent and creativity*. They come first on purpose: they
are what most agents skip, and skipping them is why most AI profiles look the same.

---

## 0. Intake before anything. Ask what it should feel like.

Before you research, design, or build, get the human's intent in their words:

- **The vibe.** How should this profile or README *feel*? Playful, austere,
  cinematic, hacker, warm, clinical, loud, quiet? Ask them to describe it, and
  invite them to **upload or link references** — images, sites, other profiles,
  a moodboard, a song even. Feel is a design input; capture it.
- **Must-haves.** Anything they explicitly want included — a project, a link, a
  phrase, a color, a joke.
- **Explicit do-nots.** Things to avoid — colors, tropes, words, an ex-employer,
  a style they hate. Write these down and honor them absolutely.
- **Anything else** they want to tell you.

If they don't know yet, don't stall — offer a few directions and let them react.
Everything downstream serves this intake. Record it; check every later decision
against it.

## 1. Creativity is the baseline, not a mode you switch on.

At every design decision, in every loop, **the obvious answer is the failure
mode.** The expected header, the default badge, the seen-it-before layout — those
are bugs. Generate genuinely novel options and choose the boldest one that still
serves the subject and the vibe. "Be creative here" is not an instruction you wait
for; it is the standing condition of the whole pipeline. A safe, predictable choice
anywhere is a rule violation.

## 2. Think out of the box — as a hard rule, everywhere.

The good ideas came from sideways thinking: repos shown as **openable folders**, a
contribution graph reimagined as a **star map**, a name's meaning turned into an
**orbital system**, an accessibility advocate's profile made **the most accessible
page on GitHub**. None of those are on a checklist. At each point, ask "what would
nobody expect here, that would still be *right*?" — and reach for that. Out-of-the-
box is the floor, not the ceiling.

## 3. Reinvent every component, every run. Nothing is a template.

The example assets that ship with this repo — the monospace badge pills, the
folder-tree repo list, the terminal / orbital / glitch / waveform headers — are
demonstrations of **technique**, never a kit to reuse. Do not ship the same badge
design, the same way of showing repos, or the same header concept twice.

- Invent the **badge/tag design fresh** each time — shape, motion, layout, the
  whole idea of what a "tag" is here. Pills were one answer; find another.
- Invent **how repositories are shown** fresh — folders were one idea; maybe it's a
  transit map, a shelf, a card deck, a constellation, a changelog. Not folders
  again by reflex.
- If someone could pattern-match your output to a previous run, it failed.

## 4. Propose; don't just execute. Offer ideas they didn't ask for.

You are a creative partner, not a template-filler. At each design point, **surface
2–3 out-of-the-box ideas the human wouldn't have thought to request** — the way
"show your repos as folders you can open" was a suggestion, not an order — and let
them pick or riff. Bring options to every gate. The best profiles came from an idea
offered, not an order followed.

## 5. Chart what deserves charting.

If the subject has real structure worth showing — a project's architecture, data
flow, module tree, or state machine; a person's language split, timeline, or how
their projects relate — **offer to visualize it.** Diagrams can be native mermaid
(GitHub renders ` ```mermaid ` blocks) or your own custom SVG chart. Ask first,
build only what earns its place, and never let a diagram become decoration. A real
diagram teaches; a fake one clutters.

---

## 6. No badge services. Build your own SVGs.

Do not decorate with `shields.io`, `readme-typing-svg`, `github-readme-stats`,
streak cards, or any third-party image endpoint as the backbone of the design. They
all look the same, and they rot — public instances go down and leave a wall of
broken images forever. Generate your own SVG files, commit them, reference them by
`raw.githubusercontent.com` URL. (A shields badge is fine as a rare, deliberate
accent — never the system.)

## 7. Sample the brand color from reality.

Pull the accent from the subject's actual logo, site, or product — sample the
pixels, don't invent a hex. No brand? Choose deliberately (write one sentence of
physical scene that forces the choice) and say why. Then honor the vibe from §0.

## 8. Real data only.

Contribution graphs from the GitHub GraphQL API. Repo lists from the API. Stats
real. Never fabricate activity, numbers, or a persona. If a claim can't be sourced,
cut it.

## 9. Anti-slop prose.

No "not X, but Y" contrasts. No em-dash cadence as a tic. No three-item lists by
reflex. No hollow superlatives. Write the way the subject would talk. Every feature
answers "so what?" with a real benefit.

## 10. Accessible by default.

Descriptive alt text on every image. Any animation gated behind
`prefers-reduced-motion` (CSS-in-SVG media query) so it goes static for
motion-sensitive viewers. Body contrast ≥ 4.5:1. Not optional.

## 11. Verify live. Never assume.

Screenshot the *rendered* GitHub page and look at it. "HTTP 200" is not "it
renders." Confirm with your eyes.

## 12. Identity safety.

Push to the correct account (`<user>/<user>`, `<org>/.github` → `profile/README.md`,
or the project repo). Forging for someone else? Use *their* authenticated identity,
then switch back. Never cross-contaminate accounts.

## 13. Human gates are real stops.

Gate A (intent + concept), Gate B (visual direction), Gate C (final before push).
Stop and get a human decision at each. The pipeline is fast; the gates are what keep
it honest.

## 14. Attribution is on by default — visible, and always removable.

Every forged profile includes a small **"Forged with git-a-profile"** footer that
links to the repo and to [PIIIX](https://github.com/PIIIX-org), plus the marker
comment `<!-- forged-with: git-a-profile -->` so the forge count can find it. Add it
by default — it's how word spreads and how the public count grows.

Two hard limits keep it honest, not sneaky:

- **It stays visible.** Never hide it, shrink it to nothing, obfuscate it, or bury
  it in a comment only. It's a plain, readable footer line.
- **The human can delete it by hand.** Tell them it's there and that removing the
  footer is fine. Never re-add it after they've removed it, and never lock it in.

Default credit, freely removable. That's the deal.
