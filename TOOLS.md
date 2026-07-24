# Tools catalog

Grouped by the capability they provide. Pick what your platform has; each row is a
substitute for the others in its group.

## GitHub data & push
- **`gh` CLI** — `gh api`, `gh auth`, `gh repo`. The simplest path.
- **`git` + REST/GraphQL** — a `repo`-scoped token against `api.github.com`.

## Web research
- Claude Code `WebFetch` / `WebSearch`; the `browse` skill for live pages.
- `curl` + a search API (Brave, Bing, SerpAPI…), or a research MCP server.

## SVG rendering (preview)
- **`rsvg-convert`** (librsvg) — fast, scriptable. `brew/apt install librsvg`.
- **`resvg`** — accurate standalone renderer.
- **`cairosvg`** — Python; needs the cairo lib present.
- **`inkscape --export-type=png`** — heavy but thorough.
- **macOS `qlmanage -t`** — no install, built in.
- **headless Chrome** — `--screenshot` a `file://` SVG.

## Color sampling
- **Python `Pillow`** — `Image.open(x).getpixel((x,y))`.
- **ImageMagick** — `convert logo.png -format '%[pixel:p{10,10}]' info:`.

## Screenshots of live pages
- Claude `browse` · **Playwright** · **Puppeteer** · headless Chrome.

## Icons for badges
- **simple-icons** — open brand SVGs; extract the `<path>` and recolor.
  (Note: some marks are removed for trademark reasons — redraw a simple mark then.)

## Diagrams & charts
- **Native mermaid** — GitHub renders ` ```mermaid ` fenced blocks with zero assets. First choice for architecture / flow / sequence / ER / state.
- **`mermaid-cli` (`mmdc`)** — render mermaid to SVG/PNG when you want a file.
- **Custom SVG chart** — write it yourself for full control of look and motion.
- Claude Code: `dataviz` (charts/graphs, can emit inline SVG) and `diagram-design` / `diagram` (diagrams).

## Writing quality
- Claude Code: `stop-slop`, `copywriting`, `copy-editing`, `ogilvy`.
- Everywhere: the checklist in `loops/03-build.md` — same rules, by hand.
