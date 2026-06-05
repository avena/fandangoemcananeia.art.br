#!/usr/bin/env python3.12
"""Download all missing images referenced in HTML files and fix broken links."""

import re
import os
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

SITE = Path("/home/livre/fandangoemcananeia.art.br/site")
BASE_URL = "https://www.fandangoemcananeia.art.br"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"

session = requests.Session()
session.headers.update({"User-Agent": UA})


def find_all_asset_urls():
    """Find all asset URLs referenced in HTML files (including images in IMG/)."""
    urls = set()
    href_re = re.compile(r'(?:href|src)="([^"]+)"')
    bg_re = re.compile(r'url\([\'"]?([^\'")]+)[\'"]?\)')
    for f in SITE.glob("*.html"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        for m in href_re.finditer(content):
            u = m.group(1).strip()
            if u.startswith(("http://", "https://", "data:", "javascript:", "#")):
                continue
            u = u.split("?")[0].split("#")[0]
            u = urllib.parse.unquote(u)
            if u and not u.startswith("//"):
                urls.add(u)
        for m in bg_re.finditer(content):
            u = m.group(1).strip()
            if u.startswith(("http://", "https://", "data:")):
                continue
            u = u.split("?")[0].split("#")[0]
            u = urllib.parse.unquote(u)
            if u and not u.startswith("//"):
                urls.add(u)
    return urls


def download_one(rel_url):
    """Download a single asset. Returns (rel_url, ok)."""
    # Build target path
    target = SITE / rel_url
    if target.exists() and target.stat().st_size > 0:
        return (rel_url, True)
    target.parent.mkdir(parents=True, exist_ok=True)
    url = f"{BASE_URL}/{rel_url}"
    try:
        r = session.get(url, timeout=30, allow_redirects=True)
        if r.status_code == 200 and len(r.content) > 0:
            target.write_bytes(r.content)
            return (rel_url, True)
        else:
            return (rel_url, False)
    except Exception as e:
        return (rel_url, False)


def main():
    print("Finding all asset URLs...")
    all_urls = find_all_asset_urls()
    print(f"Found {len(all_urls)} unique asset URLs")

    # Find which ones are missing
    missing = [u for u in all_urls if not (SITE / u).exists()]
    print(f"Missing: {len(missing)}")

    # Download missing in parallel
    if missing:
        print(f"Downloading {len(missing)} missing files...")
        with ThreadPoolExecutor(max_workers=15) as ex:
            futures = {ex.submit(download_one, u): u for u in missing}
            ok = 0
            fail = 0
            for fut in as_completed(futures):
                url, success = fut.result()
                if success:
                    ok += 1
                else:
                    fail += 1
            print(f"  Downloaded: {ok}, Failed: {fail}")

    # Now fix the few remaining issues:
    # 1. 1-Festa vs 1ª-Festa filename
    # 2. SPIP pagination links
    print("\nFixing remaining broken links in HTML files...")
    fix_old_to_new = {
        "1-Festa-do-Fandango-Caicara-de": "1ª-Festa-do-Fandango-Caicara-de",
        "2-Festa-do-Fandango-Caicara-de": "2-Festa-do-Fandango-Caicara-de",  # identity
    }
    pagination_to_clean = re.compile(r'^(?P<page>[^"?#]+)\?debut_articles=\d+#?pagination_articles?$')

    fixes = 0
    for f in SITE.glob("*.html"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        original = content
        # Fix href links that are pagination URLs
        def fix_pagination(m):
            url = m.group(1)
            if "debut_articles=" in url:
                # Strip the pagination, keep just the page slug
                clean = url.split("?")[0]
                return f'href="{clean}.html"'
            return m.group(0)
        content = re.sub(r'href="([^"]+debut_articles=[^"]+)"', fix_pagination, content)
        if content != original:
            f.write_text(content, encoding="utf-8")
            fixes += 1
    print(f"  Applied pagination fixes in {fixes} files")

    # 1-Festa is referenced - check the actual file
    if (SITE / "1-Festa-do-Fandango-Caicara-de.html").exists() and not (SITE / "1ª-Festa-do-Fandango-Caicara-de.html").exists():
        (SITE / "1-Festa-do-Fandango-Caicara-de.html").rename(SITE / "1ª-Festa-do-Fandango-Caicara-de.html")
        print("Renamed 1-Festa-... to 1ª-Festa-...")
    elif (SITE / "1-Festa-do-Fandango-Caicara-de.html").exists() and (SITE / "1ª-Festa-do-Fandango-Caicara-de.html").exists():
        # Duplicate - remove the encoded one, keep the literal
        (SITE / "1-Festa-do-Fandango-Caicara-de.html").unlink()
        print("Removed duplicate 1-Festa-... keeping 1ª-...")
    elif not (SITE / "1ª-Festa-do-Fandango-Caicara-de.html").exists():
        # Make a symlink so both work
        if (SITE / "1-Festa-do-Fandango-Caicara-de.html").exists():
            (SITE / "1-Festa-do-Fandango-Caicara-de.html").rename(SITE / "1ª-Festa-do-Fandango-Caicara-de.html")
            print("Renamed 1-Festa-... to 1ª-Festa-...")

    # Update links: 1-Festa-do-Fandango-Caicara-de -> 1ª-Festa-do-Fandango-Caicara-de
    fix_count = 0
    for f in SITE.glob("*.html"):
        content = f.read_text(encoding="utf-8", errors="ignore")
        new_content = content.replace(
            'href="1-Festa-do-Fandango-Caicara-de"',
            'href="1ª-Festa-do-Fandango-Caicara-de.html"'
        ).replace(
            'href="1-Festa-do-Fandango-Caicara-de.html"',
            'href="1ª-Festa-do-Fandango-Caicara-de.html"'
        )
        if new_content != content:
            f.write_text(new_content, encoding="utf-8")
            fix_count += 1
    print(f"Updated 1-Festa links in {fix_count} files")

    print("Done.")


if __name__ == "__main__":
    main()
