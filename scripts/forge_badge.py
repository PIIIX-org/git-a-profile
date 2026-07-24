#!/usr/bin/env python3
"""Count documented forges (runs/*/ minus _template) and write assets/badges/forges.svg.
Self-hosted, no external service. Run by .github/workflows/forge-count.yml."""
import os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
runs = [d for d in glob.glob(os.path.join(ROOT, "runs", "*"))
        if os.path.isdir(d) and os.path.basename(d) != "_template"]
n = len(runs)

# optional wild-adoption augmentation: if FORGE_SEARCH_COUNT is set (by the Action's
# best-effort code search for the attribution marker), take the larger, honest number.
try:
    n = max(n, int(os.environ.get("FORGE_SEARCH_COUNT", "0")))
except ValueError:
    pass

label, value = "profiles forged", str(n)
FONT = "SFMono-Regular, Menlo, Consolas, monospace"
H, FS, CW, PAD = 30, 12.5, 7.5, 10
text = f"{label} · {value}"
W = round(PAD + len(text) * CW + PAD)
ty = H / 2 + FS * 0.35
svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{text}">
<title>{text}</title>
<rect width="{W}" height="{H}" rx="7" fill="#8B7BFF"/>
<circle cx="{PAD+4}" cy="{H/2}" r="3.2" fill="#F5A623"/>
<text x="{PAD+13}" y="{ty:.1f}" font-family="{FONT}" font-size="{FS}" font-weight="600" fill="#ffffff">{text}</text>
</svg>'''
# nudge text right to clear the spark dot
svg = svg.replace(f'x="{PAD+13}"', f'x="{PAD+16}"')
W2 = W + 6
svg = svg.replace(f'width="{W}"', f'width="{W2}"', 1).replace(f'viewBox="0 0 {W} {H}"', f'viewBox="0 0 {W2} {H}"').replace(f'<rect width="{W}"', f'<rect width="{W2}"')

out = os.path.join(ROOT, "assets", "badges", "forges.svg")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    f.write(svg)
print(f"forges = {n}  ->  {out}")
