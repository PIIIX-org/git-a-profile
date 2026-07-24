#!/usr/bin/env python3
"""Pre-flight check for a forged README, before Gate C.

Turns the hard rules into a mechanical gate: every image has alt text, the design
isn't propped up on badge services, the attribution marker is present, and (with
--check-urls) every image actually resolves.

Usage:
    python3 scripts/preflight.py path/to/README.md
    python3 scripts/preflight.py path/to/README.md --check-urls
    python3 scripts/preflight.py https://raw.githubusercontent.com/u/u/main/README.md

Exit code 0 = no failures (warnings allowed), 1 = at least one failure.
"""
import sys, re, os

BADGE_SERVICES = [
    "img.shields.io", "readme-typing-svg", "github-readme-stats",
    "github-readme-streak-stats", "komarev.com", "profile-counter",
]

def load(src):
    if src.startswith("http"):
        from urllib.request import urlopen
        return urlopen(src, timeout=20).read().decode("utf-8", "replace")
    with open(src, encoding="utf-8") as f:
        return f.read()

def find_images(md):
    """Return list of (src, alt) for markdown and html images."""
    imgs = []
    for m in re.finditer(r'!\[(?P<alt>.*?)\]\((?P<src>[^)\s]+)', md):
        imgs.append((m.group("src"), m.group("alt")))
    for m in re.finditer(r'<img\b[^>]*>', md, re.I):
        tag = m.group(0)
        src = (re.search(r'src\s*=\s*"([^"]*)"', tag, re.I) or [None, ""])[1]
        alt_m = re.search(r'alt\s*=\s*"([^"]*)"', tag, re.I)
        alt = alt_m.group(1) if alt_m else None   # None = attribute absent
        imgs.append((src, alt))
    return imgs

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    src = sys.argv[1]
    check_urls = "--check-urls" in sys.argv[2:]
    md = load(src)
    imgs = find_images(md)
    fails, warns, oks = [], [], []

    # 1. alt text on every image
    missing = [s for (s, a) in imgs if a is None or a.strip() == ""]
    if missing:
        fails.append(f"{len(missing)} image(s) missing alt text: " +
                     ", ".join(os.path.basename(s) for s in missing[:5]))
    else:
        oks.append(f"alt text present on all {len(imgs)} images")

    # 2. badge services as the backbone
    hits = [(s, svc) for (s, _) in imgs for svc in BADGE_SERVICES if svc in s]
    if len(hits) >= 3:
        fails.append(f"{len(hits)} badge-service images — the design leans on "
                     f"third-party endpoints (they look generic and rot). Build own SVGs.")
    elif hits:
        warns.append(f"{len(hits)} badge-service image(s) — fine as a rare accent, "
                     f"not as the system: " + ", ".join(sorted({h[1] for h in hits})))
    else:
        oks.append("no badge-service backbone — assets are self-hosted")

    # 3. attribution marker (info; removable by design)
    if "forged-with: git-a-profile" in md:
        oks.append("attribution marker present")
    else:
        warns.append("no 'forged-with: git-a-profile' marker (fine if the human "
                     "removed the credit by hand)")

    # 4. optional: images resolve
    if check_urls:
        from urllib.request import Request, urlopen
        bad = []
        for (s, _) in imgs:
            if s.startswith("http"):
                try:
                    urlopen(Request(s, method="HEAD"), timeout=15)
                except Exception:
                    bad.append(s)
        if bad:
            fails.append(f"{len(bad)} image URL(s) did not resolve: " +
                         ", ".join(os.path.basename(s) for s in bad[:5]))
        else:
            oks.append("all image URLs resolve")

    for o in oks:   print(f"  ok    {o}")
    for w in warns: print(f"  warn  {w}")
    for fl in fails: print(f"  FAIL  {fl}")
    print()
    if fails:
        print(f"pre-flight: {len(fails)} failure(s). Fix before Gate C.")
        sys.exit(1)
    print(f"pre-flight: passed ({len(warns)} warning(s)).")

if __name__ == "__main__":
    main()
