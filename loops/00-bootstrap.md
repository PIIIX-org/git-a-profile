# Loop 0 — Bootstrap

**Goal:** get your agent and machine ready, whatever platform you're on. Detect
what you have, install or find equivalents for what you're missing, fall back
gracefully when you can't.

**Output:** a short bootstrap report listing each capability as `native`,
`installed`, or `fallback`. Nothing is a hard blocker except git access.

---

## Step 1 — Identify your platform

You might be Claude Code, Codex CLI, Cursor, Aider, Gemini CLI, Copilot, or
something else. The pipeline is plain markdown instructions; any capable coding
agent can run it. Note which you are — it changes *how* you get each capability,
not *what* you need.

## Step 2 — The capability checklist

You need these capabilities (the first eight always; the ninth when the subject
has structure worth charting). For each: check if you already have it, else
install it, else use the fallback.

| # | Capability | What it's for |
|---|---|---|
| 1 | **Shell + git + GitHub API** | Read profile/repo data, push results |
| 2 | **Web fetch + search** | Research the subject, find their brand |
| 3 | **GitHub GraphQL** | Pull the real contribution graph |
| 4 | **Write SVG files** | Generate custom assets (any language) |
| 5 | **Render SVG → PNG** | Preview assets before committing |
| 6 | **Sample colors from an image** | Pull brand color from a logo/screenshot |
| 7 | **Screenshot a live web page** | Verify the rendered GitHub page |
| 8 | **Anti-slop writing guidance** | Keep the prose human (see `PRINCIPLES.md`) |
| 9 | **Charts / diagrams (optional)** | Native mermaid + markdown tables need nothing; graphical output uses chart/diagram skills (`dataviz`, `diagram-design`) + an SVG renderer |

## Step 3 — Self-discovery: find and install what you're missing

**Do this actively — don't just note gaps.** For each missing capability, search
your own platform's registry for an equivalent and install it. This is what makes
the pipeline portable.

- **Claude Code:** use the `find-skills` skill (or the plugin marketplace) to
  search for and install skills. The ones this pipeline was built with:
  `impeccable` (design), `stop-slop` + `copywriting` + `ogilvy` (prose),
  `browse` (screenshots), `dataviz` (charts), `diagram-design` / `diagram`
  (diagrams). Also check the MCP registry for servers you need.
- **Codex / Cursor / Aider / other:** search your extension/tool marketplace,
  MCP server registry, or npm/pip for equivalents:
  - screenshots → `playwright`, `puppeteer`, or headless Chrome
  - SVG render → `rsvg-convert` (librsvg), `resvg`, `cairosvg`, `inkscape`
  - color sampling → Python `Pillow`, or `imagemagick` (`convert ... -format '%[pixel:...]'`)
  - research → your built-in web tool, or `curl` + a search API
- **Any agent:** if your platform has a skill/tool/plugin search, run it now with
  queries like "svg render", "screenshot web page", "github stats", "web
  research", "chart / data visualization", "diagram", and install the best matches. Prefer official/verified sources;
  read what a tool does before installing it.

## Step 4 — Fallbacks (when you can't install)

Nothing here is a hard stop except git.

| Capability | Fallback |
|---|---|
| Render SVG → PNG | If no renderer: skip visual preview, describe the asset in words, and rely on Gate B (a human opens the SVG). |
| Screenshot live page | If no browser automation: open the URL yourself / ask the human to confirm it renders. |
| Sample colors | If no image lib: read the brand's published hex from their site/brand page, or pick deliberately per `PRINCIPLES.md §3`. |
| GraphQL | If no token scope: use REST (`/users/<u>/events`) or render a simpler viz; never fabricate data. |
| Anti-slop skills | Inline the checklist in `loops/03-build.md`; it's the same rules. |

## Step 5 — Verify git access (the one hard requirement)

Confirm you can read the target and push:

```bash
gh auth status            # or: git remote -v && a token with repo scope
gh api user --jq .login   # who am I authenticated as?
```

If you'll forge for an org, confirm you can write to `<org>/.github`. If for
another person, confirm you have *their* authenticated identity (see
`PRINCIPLES.md §8`).

## Step 6 — Write the bootstrap report

List each capability as `native` / `installed` / `fallback`, note your platform,
and note which identity you're authenticated as. Then proceed to Loop 1.

> **Gate:** none. Bootstrap is machine setup. The first human gate is in Loop 1.
