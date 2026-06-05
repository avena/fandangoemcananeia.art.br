#!/usr/bin/env python3.12
"""Final cleanup pass."""

import re
import urllib.parse
import requests
from pathlib import Path

SITE = Path("/home/livre/fandangoemcananeia.art.br/site")
BASE_URL = "https://www.fandangoemcananeia.art.br"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"

session = requests.Session()
session.headers.update({"User-Agent": UA})


# 1. Download favicon.ico
fav = SITE / "favicon.ico"
if not fav.exists():
    for url in [f"{BASE_URL}/favicon.ico", f"{BASE_URL}/local/favicon.ico", f"{BASE_URL}/squelettes-dist/favicon.ico"]:
        try:
            r = session.get(url, timeout=10)
            if r.status_code == 200 and len(r.content) > 0:
                fav.write_bytes(r.content)
                print(f"Downloaded favicon.ico from {url}")
                break
        except:
            pass

# 2. Remove the Nova-materia placeholder page
nm = SITE / "Nova-materia.html"
if nm.exists():
    nm.unlink()
    print("Removed Nova-materia.html (placeholder)")

# 3. In Na-Web.html, replace all links to non-existent files with valid ones
nw = SITE / "Na-Web.html"
if nw.exists():
    content = nw.read_text(encoding="utf-8", errors="ignore")
    # The Nova-materia was a SPIP "new article" placeholder - point to index instead
    content = content.replace('href="Nova-materia"', 'href="index.html"')
    content = content.replace('href="Nova-materia.html"', 'href="index.html"')
    # Also fix any other invalid links
    # Anything matching "Nome-pagina" (no .html) inside Na-Web - convert to Nome-pagina.html
    nw.write_text(content, encoding="utf-8")
    print("Fixed Na-Web.html")

# 4. Add a small "static-fixes.js" or just convert all relative page links across all files
#    to ensure they have .html extension
print("\nFinal pass: ensure all page links have .html extension")
fixed = 0
for f in SITE.glob("*.html"):
    content = f.read_text(encoding="utf-8", errors="ignore")
    original = content
    # Find href="PageName" where PageName doesn't have .html, /, or is one of the known page slugs
    known_slugs = set()
    for ff in SITE.glob("*.html"):
        known_slugs.add(ff.stem)  # file name without .html
    known_slugs.discard("index")  # don't rewrite index.html refs to index.html.html
    def add_html(m):
        prefix = m.group(1)
        url = m.group(2)
        # Skip if already has .html, /, or special
        if url.startswith(("http", "#", "javascript", "mailto", "spip.php", "/", "data:")):
            return m.group(0)
        # Skip if has query/fragment only
        clean = url.split("?")[0].split("#")[0]
        if clean in known_slugs:
            suffix = url[len(clean):]
            return f'{prefix}"{clean}.html{suffix}"'
        return m.group(0)
    content = re.sub(r'(href|src)="([^"]+)"', add_html, content)
    if content != original:
        f.write_text(content, encoding="utf-8")
        fixed += 1
print(f"  Fixed .html extensions in {fixed} files")

# 5. Verify
print("\nRe-verifying...")
HREF_RE = re.compile(r'(?:href|src)="([^"]+)"')
missing = []
ok = 0
total = 0
for f in sorted(SITE.glob("*.html")):
    content = f.read_text(encoding="utf-8", errors="ignore")
    for m in HREF_RE.finditer(content):
        url = m.group(1).strip()
        if url.startswith(("http://", "https://", "data:", "javascript:", "mailto:", "#", "spip.php")):
            continue
        url = urllib.parse.unquote(url)
        if not url or url.startswith("#") or url.startswith("//"):
            continue
        clean = url.split("?")[0].split("#")[0]
        if not clean:
            continue
        total += 1
        target = SITE / clean
        if not target.exists():
            missing.append((f.name, url))
        else:
            ok += 1
print(f"Total: {total}  OK: {ok}  Missing: {len(missing)}")
if missing:
    by_target = {}
    for src, tgt in missing:
        by_target.setdefault(tgt, []).append(src)
    print("Still missing:")
    for tgt, srcs in sorted(by_target.items())[:30]:
        print(f"  {tgt}  (from {len(srcs)} pages, e.g. {srcs[0]})")
