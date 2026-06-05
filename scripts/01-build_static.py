#!/usr/bin/env python3.12
"""
Fandango em Cananeia - Static site generator
Downloads the entire site (HTML, CSS, JS, images) and creates a static version
with estrutura.md listing all pages and their assets.
"""

import os
import re
import sys
import json
import shutil
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.fandangoemcananeia.art.br"
ROOT = Path("/home/livre/fandangoemcananeia.art.br")
SITE_DIR = ROOT / "site"
TMP_DIR = Path("/tmp/fandango_downloads")
TMP_DIR.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

# Pages identified from the homepage navigation
# Format: (slug, original_href, friendly_name, parent_slug)
SEED_PAGES = [
    # Top-level menu
    ("index", "", "Início", None),
    ("Puxirao", "Puxirao", "Puxirão", "index"),
    ("Equipe", "Equipe", "Equipe", "Puxirao"),
    ("Objetivos", "Objetivos", "Objetivos", "Puxirao"),
    ("Parceiros", "Parceiros", "Parceiros", "Puxirao"),
    ("Projeto", "Projeto", "Projeto", "Puxirao"),
    ("Produtos-sociais", "Produtos-sociais", "Produtos sociais", "Puxirao"),
    ("Filme", "Filme", "Filme", "Produtos-sociais"),
    ("article18", "article18", "HQ", "Produtos-sociais"),
    ("Musicas", "Musicas", "Músicas", "Produtos-sociais"),
    ("Portal-Web", "Portal-Web", "Portal Web", "Produtos-sociais"),
    ("Cananeia", "Cananeia", "Cananéia", "index"),
    ("Cultura", "Cultura", "Cultura", "Cananeia"),
    ("Natureza", "Natureza", "História", "Cananeia"),  # slug Natureza = História
    ("Natureza-80", "Natureza,80", "Natureza", "Cananeia"),  # article 80 = Natureza
    ("Fandango", "Fandango", "Fandango", "index"),
    ("O-que-e", "O-que-e", "Fandango Caiçara", "Fandango"),
    ("Ontem-e-hoje", "Ontem-e-hoje", "Música, dança e instrumentos", "Fandango"),
    ("Patrimonio-Cultural", "Patrimonio-Cultural", "Patrimônio Cultural", "Fandango"),
    ("Videos-e-fotos", "Videos-e-fotos", "Vídeos e fotos", "Fandango"),
    ("Mestres", "Mestres", "Fandangueiros", "index"),
    ("Agostinho-Gomes", "Agostinho-Gomes", "Agostinho Gomes", "Mestres"),
    ("Andre-Pires", "Andre-Pires", "André Pires", "Mestres"),
    ("Angelo-Ramos", "Angelo-Ramos", "Ângelo Ramos", "Mestres"),
    ("Beto-Pereira", "Beto-Pereira", "Beto Pereira", "Mestres"),
    ("Seu-Hugo", "Seu-Hugo", "Hugo Emiliano", "Mestres"),
    ("Joao-Alves", "Joao-Alves", "João Alves", "Mestres"),
    ("Joao-da-Toca-In-memorian", "Joao-da-Toca-In-memorian", "João da Toca (In memorian)", "Mestres"),
    ("Joao-Firmino", "Joao-Firmino", "João Firmino", "Mestres"),
    ("Arnaldo-Pereira", "Arnaldo-Pereira", "Leonildo Pereira", "Mestres"),
    ("Nelson-Franco-Pica-pau", "Nelson-Franco-Pica-pau", "Nelson Franco (Pica-pau)", "Mestres"),
    ("Paulinho-Pereira", "Paulinho-Pereira", "Paulinho Pereira", "Mestres"),
    ("Ze-Pereira", "Ze-Pereira", "Zé Pereira", "Mestres"),
    ("Grupos", "Grupos", "Grupos", "index"),
    ("Grupo-de-Fandango-Batido-Sao", "Grupo-de-Fandango-Batido-Sao", "Batido São Gonçalo", "Grupos"),
    ("Caicaras-do-Acarau", "Caicaras-do-Acarau", "Caiçaras do Acaraú", "Grupos"),
    ("Esperanca", "Esperanca", "Esperança", "Grupos"),
    ("Familia-Neves", "Familia-Neves", "Família Neves", "Grupos"),
    ("Familia-Pereira", "Familia-Pereira", "Família Pereira", "Grupos"),
    ("Fandangueiros-do-Ariri", "Fandangueiros-do-Ariri", "Fandangueiros do Ariri", "Grupos"),
    ("Fandangueiros-do-Continente", "Fandangueiros-do-Continente", "Fandangueiros do Continente", "Grupos"),
    ("Fandangueiros-do-Itacuruca", "Fandangueiros-do-Itacuruca", "Jovens Fandangueiros do Itacuruçá", "Grupos"),
    ("Terra-Firme", "Terra-Firme", "Terra Firme", "Grupos"),
    ("Violas-de-Ouro-Sao-Paulo-Bagre", "Violas-de-Ouro-Sao-Paulo-Bagre", "Violas de Ouro São Paulo Bagre", "Grupos"),
    ("Agenda", "Agenda", "Agenda", "index"),
    ("Colheita-de-arroz", "Colheita-de-arroz", "Fandango na Trilha da Juréia", "Agenda"),
    ("Festa-caicara-em-Pedrinhas", "Festa-caicara-em-Pedrinhas", "Festa caiçara em Pedrinhas", "Agenda"),
    ("Festa-da-Tainha", "Festa-da-Tainha", "Festa de Santo André", "Agenda"),
    ("Na-Web", "Na-Web", "Navegue", "index"),
    # Homepage news articles
    ("Os-tamancos-vao-bater-no-proximo", "Os-tamancos-vao-bater-no-proximo", "A volta dos mutirões...", "index"),
    ("Registro-do-Fandango-Caicara-como", "Registro-do-Fandango-Caicara-como", "Fandango Caiçara: patrimônio cultural do Brasil", "index"),
    ("2-Festa-do-Fandango-Caicara-de", "2%C2%AA-Festa-do-Fandango-Caicara-de", "2ª Festa do Fandango Caiçara de Cananeia", "index"),
    ("Premio-Fandango-Caicara", "Premio-Fandango-Caicara", "Prêmio Fandango Caiçara", "index"),
    ("Lembrancas-de-um-fandango-caicara", "Lembrancas-de-um-fandango-caicara", "Lembranças de um fandango caiçara...", "index"),
    ("Ta-chegando-a-hora", "Ta-chegando-a-hora", "Tá chegando a hora...", "index"),
    ("Fandangueiros-de-Cananeia-foram-a", "Fandangueiros-de-Cananeia-foram-a", "Caiçaras no cerrado...", "index"),
    ("Cultura-Digital", "Cultura-Digital", "Programa Puxirão: fandango caiçara e software livre", "index"),
    ("Apresentacao-da-Katya-Teixeira-e", "Apresentacao-da-Katya-Teixeira-e", "Fandangueiros e Puxirão premiados!!!", "index"),
    ("Mestre-Ze-Pereira-em-Cuba", "Mestre-Ze-Pereira-em-Cuba", "Mestre Zé Pereira em Cuba", "index"),
    ("Katya-Teixeira-no-SESC-Belenzinho", "Katya-Teixeira-no-SESC-Belenzinho", "Kátya Teixeira e fandango caiçara: encontro perfeito", "index"),
    ("FESTA-DE-LANCAMENTO", "FESTA-DE-LANCAMENTO", "Alegria, alegria... tudo entregue!!!", "index"),
    ("O-galo-canta", "O-galo-canta", "O galo canta...", "index"),
    ("Cruzeiro-EducArte-visita-a-cidade", "Cruzeiro-EducArte-visita-a-cidade", "Mutirão colheita de arroz na Comunidade do Varadouro", "index"),
    ("O-projeto-Puxirao-participou-da", "O-projeto-Puxirao-participou-da", "O projeto Puxirão participou da 12ª OID", "index"),
    ("Grupo-Esperanca-circulara-pelo", "Grupo-Esperanca-circulara-pelo", "Grupo Esperança na estrada e finalizando seu disco", "index"),
]

# Asset extensions to download
ASSET_EXT = (".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico",
             ".woff", ".woff2", ".ttf", ".eot", ".otf")

session = requests.Session()
session.headers.update({"User-Agent": UA})

def fetch(url, timeout=30):
    try:
        r = session.get(url, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        return r
    except Exception as e:
        print(f"  [ERR] {url}: {e}", file=sys.stderr)
        return None

def download_html(slug, href):
    """Download a page's HTML. Returns the raw HTML content or None."""
    if slug == "index":
        url = f"{BASE_URL}/"
    else:
        url = f"{BASE_URL}/{href}"
    print(f"  GET {url}")
    r = fetch(url)
    if r is None:
        return None
    return r.text

def download_binary(url, local_path):
    """Download a binary file. Returns the local path or None."""
    if local_path.exists() and local_path.stat().st_size > 0:
        return local_path
    r = fetch(url, timeout=60)
    if r is None:
        return None
    local_path.parent.mkdir(parents=True, exist_ok=True)
    with open(local_path, "wb") as f:
        f.write(r.content)
    return local_path

def extract_asset_urls(html):
    """Extract all asset URLs (CSS, JS, images) from HTML."""
    soup = BeautifulSoup(html, "lxml")
    urls = set()
    # CSS
    for tag in soup.find_all("link", rel="stylesheet"):
        href = tag.get("href")
        if href and not href.startswith(("http://", "https://", "data:", "javascript:")):
            urls.add(href)
    # JS
    for tag in soup.find_all("script", src=True):
        src = tag.get("src")
        if src and not src.startswith(("http://", "https://", "data:", "javascript:")):
            urls.add(src)
    # Images
    for tag in soup.find_all("img"):
        src = tag.get("src")
        if src and not src.startswith(("http://", "https://", "data:")):
            urls.add(src)
    # Background images in inline style
    for style in soup.find_all(style=True):
        bg = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', style.string or "")
        for u in bg:
            if not u.startswith(("http://", "https://", "data:")):
                urls.add(u)
    # Background in style attribute
    for tag in soup.find_all(style=True):
        s = tag.get("style", "")
        bg = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', s)
        for u in bg:
            if not u.startswith(("http://", "https://", "data:")):
                urls.add(u)
    return urls

def is_asset_url(url):
    """Check if URL is an asset we should download."""
    if "?" in url and not url.endswith(ASSET_EXT):
        return False
    return url.lower().endswith(ASSET_EXT) or "/IMG/" in url or "/local/" in url

def extract_page_links(html, current_slug):
    """Extract internal page links from HTML. Returns set of (slug, href) tuples."""
    soup = BeautifulSoup(html, "lxml")
    found = set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        # Skip external
        if href.startswith(("http://", "https://", "#", "javascript:", "mailto:")):
            continue
        # Skip spip.php pages (dynamic)
        if "spip.php" in href:
            continue
        # Skip already absolute paths
        if href.startswith("/"):
            href = href.lstrip("/")
        # Normalize
        # Handle Natureza,80
        if "," in href:
            href = href.replace(",", "-")
        # URL decode
        href = urllib.parse.unquote(href)
        # Skip empty
        if not href or href in ("#", ""):
            continue
        # Skip assets
        if is_asset_url(href):
            continue
        # Map to slug (filename)
        slug = href.split("/")[-1]
        if slug:
            found.add((slug, href))
    return found

def main():
    print("=" * 60)
    print("Fandango em Cananéia - Static Site Generator")
    print("=" * 60)
    SITE_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Download all seed pages
    print("\n[1/5] Downloading HTML pages...")
    pages_html = {}     # slug -> raw html
    pages_meta = {}     # slug -> dict with name, parent, href
    for slug, href, name, parent in SEED_PAGES:
        html = download_html(slug, href)
        if html:
            pages_html[slug] = html
        pages_meta[slug] = {"name": name, "parent": parent, "href": href}

    # 2. Discover additional internal links from each page
    print("\n[2/5] Discovering additional links...")
    all_page_slugs = set(pages_meta.keys())
    all_page_slugs_by_href = {p[1]: p[0] for p in SEED_PAGES}  # href -> slug
    for slug, html in list(pages_html.items()):
        links = extract_page_links(html, slug)
        for lslug, lhref in links:
            if lslug not in pages_meta:
                # Add as a new page
                if lslug not in all_page_slugs_by_href.values():
                    # Try to find a name from the link
                    pages_meta[lslug] = {"name": lslug.replace("-", " "), "parent": slug, "href": lhref}
                    all_page_slugs_by_href[lhref] = lslug

    # Try to download additional discovered pages
    for slug, meta in list(pages_meta.items()):
        if slug not in pages_html and meta.get("href"):
            html = download_html(slug, meta["href"])
            if html:
                pages_html[slug] = html

    print(f"  Total pages downloaded: {len(pages_html)}")
    print(f"  Total pages in catalog: {len(pages_meta)}")

    # 3. Collect and download all assets
    print("\n[3/5] Downloading assets...")
    asset_map = {}  # url -> local_path
    pages_assets = {}  # slug -> list of (url, local_path)

    # First, collect assets from all pages
    all_assets = set()
    for slug, html in pages_html.items():
        urls = extract_asset_urls(html)
        pages_assets[slug] = []
        for u in urls:
            if is_asset_url(u) or u.startswith(("local/", "plugins/", "lib/", "prive/", "squelettes-dist/", "extensions/", "IMG/", "images/")):
                all_assets.add(u)
                pages_assets[slug].append(u)

    print(f"  Total unique assets: {len(all_assets)}")

    # Download assets in parallel
    def dl_asset(u):
        # Normalize URL - it can be relative like "local/foo.png" or absolute like "https://.../local/foo.png"
        if u.startswith(("http://", "https://")):
            # Already absolute - extract path portion
            parsed = urllib.parse.urlparse(u)
            path = parsed.path.lstrip("/")
        else:
            path = u.lstrip("/")
        # Skip spip.php assets that need to be generated
        if "spip.php" in path:
            return None
        # Determine URL
        if u.startswith(("http://", "https://")):
            url = u
        else:
            url = f"{BASE_URL}/{u}"
        local_path = SITE_DIR / path
        result = download_binary(url, local_path)
        return (u, result)

    with ThreadPoolExecutor(max_workers=10) as ex:
        futures = {ex.submit(dl_asset, u): u for u in all_assets}
        for fut in as_completed(futures):
            res = fut.result()
            if res:
                asset_map[res[0]] = str(res[1])

    # 4. Process each page: rewrite URLs, save as static HTML
    print("\n[4/5] Processing and saving pages...")
    for slug, html in pages_html.items():
        save_page(slug, html, pages_meta, asset_map)

    # 5. Generate documentation
    print("\n[5/5] Generating documentation...")
    generate_docs(pages_html, pages_meta, pages_assets, asset_map)

    print("\nDone!")

def rewrite_url(href, current_slug, asset_map, pages_meta):
    """Rewrite a relative URL so it works as a static site link."""
    if not href:
        return href
    href = href.strip()
    if href.startswith(("http://", "https://", "data:", "javascript:", "mailto:", "#")):
        return href
    if "spip.php" in href:
        return "#"
    # Decode
    href_decoded = urllib.parse.unquote(href)
    # Handle Natureza,80
    if "," in href_decoded:
        href_decoded = href_decoded.replace(",", "-")
    # Skip leading slash
    href_decoded = href_decoded.lstrip("/")
    # If it's an asset path, return as-is (relative)
    if is_asset_url(href_decoded) or href_decoded.startswith(("local/", "plugins/", "lib/", "prive/", "squelettes-dist/", "extensions/", "IMG/")):
        return href_decoded
    # It's a page link
    # Map href to slug
    target_slug = None
    # Check if href matches one of our known pages
    if href_decoded in [m["href"] for m in pages_meta.values()]:
        # Find matching slug
        for s, m in pages_meta.items():
            if m["href"] == href_decoded:
                target_slug = s
                break
    else:
        # Treat as a slug
        target_slug = href_decoded.split("/")[-1]
    if target_slug and target_slug in pages_meta:
        return f"{target_slug}.html"
    # Unknown - keep as-is
    return href_decoded

def save_page(slug, html, pages_meta, asset_map):
    """Save a page as static HTML with rewritten URLs."""
    if slug == "index":
        out = SITE_DIR / "index.html"
    else:
        out = SITE_DIR / f"{slug}.html"
    soup = BeautifulSoup(html, "lxml")

    # Rewrite all hrefs
    for a in soup.find_all("a", href=True):
        new = rewrite_url(a["href"], slug, asset_map, pages_meta)
        a["href"] = new

    # Rewrite link[rel=stylesheet] href
    for tag in soup.find_all("link", href=True):
        new = rewrite_url(tag["href"], slug, asset_map, pages_meta)
        tag["href"] = new

    # Rewrite script src
    for tag in soup.find_all("script", src=True):
        src = tag.get("src", "")
        if "spip.php" in src or "main-loading.js" in src:
            # Remove the loading script and the spip-specific scripts
            tag.decompose()
            continue
        new = rewrite_url(src, slug, asset_map, pages_meta)
        tag["src"] = new

    # Rewrite img src
    for tag in soup.find_all("img"):
        src = tag.get("src", "")
        if src:
            new = rewrite_url(src, slug, asset_map, pages_meta)
            tag["src"] = new

    # Rewrite background images in style
    for tag in soup.find_all(style=True):
        s = tag.get("style", "")
        s = re.sub(r'url\([\'"]?([^\'")]+)[\'"]?\)',
                   lambda m: f'url({rewrite_url(m.group(1), slug, asset_map, pages_meta)})', s)
        tag["style"] = s

    # Remove SPIP-CRON div
    for div in soup.find_all("div", style=re.compile(r"spip\.php\?action=cron")):
        div.decompose()

    # Remove any forms that need backend (contact form etc.) - keep them visually but disable
    for form in soup.find_all("form"):
        # Remove the action
        form["action"] = "#"
        form["onsubmit"] = "return false;"

    # Save
    out.write_text(str(soup), encoding="utf-8")
    print(f"  Saved {out.relative_to(ROOT)}")

def generate_docs(pages_html, pages_meta, pages_assets, asset_map):
    """Generate README.md and estrutura.md with all pages and assets."""

    # estrutura.md - listing of all pages and their assets
    lines = ["# Estrutura do site Fandango em Cananéia (versão estática)\n"]
    lines.append(f"Total de páginas: **{len(pages_html)}**\n")
    lines.append(f"Total de assets baixados: **{len(asset_map)}**\n")
    lines.append(f"Origem: <https://www.fandangoemcananeia.art.br/>\n")
    lines.append(f"Gerado em: {os.popen('date -Iseconds').read().strip()}\n")
    lines.append("\n---\n")

    # Group by parent
    def build_tree():
        children = {}
        for slug, meta in pages_meta.items():
            p = meta.get("parent")
            children.setdefault(p, []).append((slug, meta))
        return children

    tree = build_tree()

    def render_node(parent_slug, level=0):
        items = sorted(tree.get(parent_slug, []), key=lambda x: x[1]["name"])
        out = []
        for slug, meta in items:
            indent = "  " * level
            local = "index.html" if slug == "index" else f"{slug}.html"
            downloaded = "OK" if slug in pages_html else "FALTA"
            name = meta["name"]
            out.append(f"{indent}- [{name}](site/{local}) — `{slug}` — {downloaded}")
            out.extend(render_node(slug, level + 1))
        return out

    lines.append("\n## Árvore de páginas\n")
    lines.extend(render_node(None))

    # Per-page detail with images
    lines.append("\n\n---\n## Detalhamento por página\n")
    lines.append("Para cada página, lista dos assets (imagens, CSS, JS) baixados em `site/`.\n")

    for slug, meta in sorted(pages_meta.items(), key=lambda x: x[1]["name"]):
        local = "site/index.html" if slug == "index" else f"site/{slug}.html"
        name = meta["name"]
        status = "OK" if slug in pages_html else "NÃO BAIXADA"
        lines.append(f"\n### {name}\n")
        lines.append(f"- Slug: `{slug}`  ")
        lines.append(f"- URL original: `{BASE_URL}/{meta['href']}`  ")
        lines.append(f"- Arquivo local: `{local}`  ")
        lines.append(f"- Status: **{status}**  ")
        if meta.get("parent"):
            lines.append(f"- Página pai: `{meta['parent']}`  ")
        assets = pages_assets.get(slug, [])
        if assets:
            lines.append(f"\n**Assets ({len(assets)}):**\n")
            # Group by type
            images = [a for a in assets if a.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg"))]
            css = [a for a in assets if a.lower().endswith(".css")]
            js = [a for a in assets if a.lower().endswith(".js")]
            other = [a for a in assets if a not in images and a not in css and a not in js]
            if images:
                lines.append(f"\n  Imagens ({len(images)}):\n")
                for img in sorted(set(images)):
                    local_p = asset_map.get(img, "—")
                    lines.append(f"    - `{img}` → `{local_p}`")
            if css:
                lines.append(f"\n  CSS ({len(css)}):\n")
                for c in sorted(set(css)):
                    local_p = asset_map.get(c, "—")
                    lines.append(f"    - `{c}` → `{local_p}`")
            if js:
                lines.append(f"\n  JS ({len(js)}):\n")
                for j in sorted(set(js)):
                    local_p = asset_map.get(j, "—")
                    lines.append(f"    - `{j}` → `{local_p}`")
            if other:
                lines.append(f"\n  Outros ({len(other)}):\n")
                for o in sorted(set(other)):
                    lines.append(f"    - `{o}`")
        else:
            lines.append("\n  *(nenhum asset listado)*")

    # Global assets
    lines.append("\n\n---\n## Todos os assets baixados\n")
    lines.append(f"Total: **{len(asset_map)}** arquivos únicos.\n")
    by_type = {}
    for url, local in asset_map.items():
        ext = Path(url).suffix.lower()
        by_type.setdefault(ext, []).append((url, local))
    for ext in sorted(by_type.keys()):
        lines.append(f"\n### {ext} ({len(by_type[ext])})\n")
        for url, local in sorted(by_type[ext]):
            lines.append(f"- `{url}` → `{local}`")

    (ROOT / "estrutura.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"  Saved estrutura.md")

    # README.md
    rd = [
        "# Fandango em Cananéia — site estático\n",
        "Versão estática (HTML + CSS + JS + imagens) do site ",
        "<https://www.fandangoemcananeia.art.br/>.\n",
        "\n## Como abrir localmente\n",
        "Abra `site/index.html` em qualquer navegador moderno.\n",
        "\n## Estrutura\n",
        "- `site/` — páginas HTML e todos os assets (CSS, JS, imagens, plugins, etc.)",
        "- `estrutura.md` — lista completa de páginas e assets baixados",
        "- `README.md` — este arquivo\n",
        "\n## Detalhes\n",
        f"- {len(pages_html)} páginas baixadas",
        f"- {len(asset_map)} assets baixados",
        f"- Origem: {BASE_URL}\n",
        "\n## Notas técnicas\n",
        "O site original é gerado pelo CMS SPIP e usa URLs do tipo `/Nome-da-Pagina` (sem `.html`). ",
        "Para funcionar como site estático, cada página foi salva como `<slug>.html` e todos os ",
        "links internos foram reescritos para apontar para os arquivos `.html` correspondentes.\n",
        "\nOs scripts e elementos dinâmicos do SPIP (formulários de contato, login, RSS, etc.) ",
        "foram removidos ou neutralizados pois requerem backend PHP.\n",
    ]
    (ROOT / "README.md").write_text("\n".join(rd), encoding="utf-8")
    print(f"  Saved README.md")

if __name__ == "__main__":
    main()
