#!/usr/bin/env python3.12
"""Cleanup pass: fix filenames with ? and #, remove duplicates, fix bad URLs."""

import os
import re
import shutil
from pathlib import Path

SITE = Path("/home/livre/fandangoemcananeia.art.br/site")

# 1. Remove broken files (with ? or # in name)
broken_patterns = ["?debut_articles=", "}"]
removed = []
for f in SITE.iterdir():
    if not f.is_file():
        continue
    if any(p in f.name for p in broken_patterns):
        # These are SPIP pagination/malformed URLs - delete them
        removed.append(f.name)
        f.unlink()

print(f"Removed {len(removed)} broken files:")
for n in removed:
    print(f"  - {n}")

# 2. Remove duplicates: keep 2-Festa-do-Fandango-Caicara-de.html (decoded) and
#    remove the URL-encoded version 2ª-Festa-do-Fandango-Caicara-de.html
duplicate_names = ["2ª-Festa-do-Fandango-Caicara-de.html"]
for n in duplicate_names:
    p = SITE / n
    if p.exists():
        print(f"Removing duplicate: {n}")
        p.unlink()

# 3. Inside all HTML files, fix any internal links that point to bad slugs
#    Map of old_slug -> new_slug
slug_fixes = {
    "Mestres?debut_articles=10#pagination_articles": "Mestres.html",
    "Mestres?debut_articles=5#pagination_articles": "Mestres.html",
    "Grupos?debut_articles=5#pagination_articles": "Grupos.html",
    "2ª-Festa-do-Fandango-Caicara-de": "2-Festa-do-Fandango-Caicara-de.html",
    "1ª-Festa-do-Fandango-Caicara-de": "1-Festa-do-Fandango-Caicara-de.html",
    "oficinainclusaodigital.org.br}": "#",
    # Non-content placeholder pages that don't add value
    "slider1": "index.html",
    "slider2": "index.html",
    "icone": "Filme.html",
    "Cleberbio": "Ze-Pereira.html",  # He is a collaborator
}

html_files = list(SITE.glob("*.html"))
fixes_applied = 0
for f in html_files:
    content = f.read_text(encoding="utf-8", errors="ignore")
    original = content
    for old, new in slug_fixes.items():
        # Match href="<old>" or href="<old>.html"
        content = re.sub(
            rf'href="{re.escape(old)}(?:\.html)?"',
            f'href="{new}"',
            content
        )
        # Also in src if used as link
        content = re.sub(
            rf'src="{re.escape(old)}(?:\.html)?"',
            f'src="{new}"',
            content
        )
    if content != original:
        f.write_text(content, encoding="utf-8")
        fixes_applied += 1

print(f"Applied link fixes in {fixes_applied} HTML files")

# 4. Remove the placeholder non-content pages (slider1, slider2, Nova-materia, etc.)
#    These don't add real value - they were auto-discovered broken links
placeholders = ["slider1.html", "slider2.html", "Nova-materia.html"]
for n in placeholders:
    p = SITE / n
    if p.exists():
        print(f"Removing placeholder: {n}")
        p.unlink()

print("\nDone.")
