# Install

The pipeline needs eight capabilities (see `loops/00-bootstrap.md`). Here's where
to get each, per platform, with fallbacks. **Nothing here is a hard blocker except
git access.**

## Claude Code

Skills (install via the plugin marketplace or the `find-skills` skill):

| Capability | Skill |
|---|---|
| Design system / anti-slop UI | `impeccable` |
| Remove AI writing tells | `stop-slop` |
| Marketing copy | `copywriting`, `copy-editing`, `ogilvy` |
| Screenshots / live QA | `browse` (or the claude-in-chrome tools) |
| Charts / graphs | `dataviz` |
| Diagrams | `diagram-design`, `diagram` |
| Find & install more skills | `find-skills` |

Built-in tools cover web research (`WebFetch`/`WebSearch`), shell, and file I/O.
`gh` and Python are typically already present.

## Any other agent

Search your platform's extension / MCP / package registry for equivalents, and
install with `npm`/`pip`/your package manager:

| Capability | Get it via |
|---|---|
| GitHub read/write | `gh` CLI, or `git` + a `repo`-scoped token |
| Web research | your built-in web tool, or `curl` + a search API |
| GitHub GraphQL | `gh api graphql`, or `curl` to `api.github.com/graphql` |
| Write SVG | any language you already have (examples here use Python) |
| Render SVG → PNG | `rsvg-convert` (librsvg) · `resvg` · `cairosvg` · `inkscape` · headless Chrome · macOS `qlmanage` |
| Sample colors | Python `Pillow` · `imagemagick` |
| Screenshot pages | `playwright` · `puppeteer` · headless Chrome |
| Anti-slop writing | the checklist in `loops/03-build.md` |
| Charts / diagrams | native **mermaid** + markdown tables (no install) · `mermaid-cli` · custom SVG · Claude `dataviz` (charts) + `diagram-design` (diagrams) |

## Self-discovery

Loop 0 tells your agent to actively search its own registry for these and install
what it can. If your platform has any skill/plugin/MCP search, use it with queries
like "svg render", "screenshot web page", "github stats", "web research". Prefer
official/verified sources; read what a tool does before installing it.
