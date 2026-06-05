#!/usr/bin/env python3.12
"""Regenerate estrutura.md with final, accurate data."""

import os
import re
import json
import urllib.parse
from pathlib import Path
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

ROOT = Path("/home/livre/fandangoemcananeia.art.br")
SITE = ROOT / "site"
BASE_URL = "https://www.fandangoemcananeia.art.br"

# Page metadata - clean authoritative list
PAGES = [
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
    ("Natureza", "Natureza", "História", "Cananeia"),
    ("Natureza-80", "Natureza,80", "Natureza", "Cananeia"),
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
    ("1ª-Festa-do-Fandango-Caicara-de", "1ª-Festa-do-Fandango-Caicara-de", "1ª Festa do Fandango Caiçara de Cananeia", "index"),
    ("Grupo-Esperanca-lancara-CD-na-Ilha", "Grupo-Esperanca-lancara-CD-na-Ilha", "Grupo Esperança lançará CD na Ilha", "index"),
    ("Noticias", "Noticias", "Notícias", "index"),
    ("Fernando-Oliveira", "Fernando-Oliveira", "Fernando Oliveira (autor)", "Puxirao"),
    ("Natalia-Latansio", "Natalia-Latansio", "Natália Latansio (autora)", "Puxirao"),
    ("Cleberbio", "Cleberbio", "Cleberbio", "Mestres"),
]


def get_page_assets(slug):
    """Extract all assets (images, CSS, JS) referenced in a page."""
    if slug == "index":
        f = SITE / "index.html"
    else:
        f = SITE / f"{slug}.html"
    if not f.exists():
        return [], []
    content = f.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(content, "lxml")
    assets = set()
    # CSS
    for tag in soup.find_all("link", rel="stylesheet"):
        h = tag.get("href", "")
        if h and not h.startswith(("http://", "https://")):
            assets.add(h)
    # JS
    for tag in soup.find_all("script", src=True):
        s = tag.get("src", "")
        if s and not s.startswith(("http://", "https://")):
            assets.add(s)
    # Images
    for tag in soup.find_all("img"):
        s = tag.get("src", "")
        if s and not s.startswith(("http://", "https://", "data:")):
            assets.add(s)
    # Background images
    for tag in soup.find_all(style=True):
        s = tag.get("style", "")
        for m in re.finditer(r'url\([\'"]?([^\'")]+)[\'"]?\)', s):
            u = m.group(1)
            if not u.startswith(("http://", "https://", "data:")):
                assets.add(u)
    return content, sorted(assets)


def main():
    print("Regenerating estrutura.md...")
    pages_meta = {p[0]: {"name": p[2], "parent": p[3], "href": p[1]} for p in PAGES}

    # Collect data per page
    pages_data = {}
    total_assets = set()
    for slug, _, name, parent in PAGES:
        content, assets = get_page_assets(slug)
        pages_data[slug] = {"name": name, "parent": parent, "assets": assets, "content": content}
        total_assets.update(assets)

    # Build the markdown
    L = []
    L.append("# Estrutura do site Fandango em Cananéia (versão estática)\n")
    L.append(f"**Origem:** <{BASE_URL}/>  ")
    L.append(f"**Gerado em:** {os.popen('date -Iseconds').read().strip()}  ")
    L.append(f"**Total de páginas:** {len(PAGES)}  ")
    L.append(f"**Total de assets únicos referenciados:** {len(total_assets)}  ")
    L.append(f"**Tamanho total do site local:** {sum(f.stat().st_size for f in SITE.rglob('*') if f.is_file()) / (1024*1024):.1f} MB")
    L.append("")
    L.append("Site estático local pronto para abrir no navegador (HTML + CSS + JS + imagens).")
    L.append("")
    L.append("---")
    L.append("")

    # Tree
    L.append("## Árvore de páginas")
    L.append("")
    children = defaultdict(list)
    for slug, meta in pages_meta.items():
        children[meta["parent"]].append((slug, meta))

    def render_tree(parent_slug, level=0):
        out = []
        items = sorted(children.get(parent_slug, []), key=lambda x: x[1]["name"])
        for slug, meta in items:
            local = "index.html" if slug == "index" else f"{slug}.html"
            indent = "  " * level
            out.append(f"{indent}- [{meta['name']}](site/{local}) (`{slug}`)")
            out.extend(render_tree(slug, level + 1))
        return out

    L.extend(render_tree(None))
    L.append("")
    L.append("---")
    L.append("")

    # Per-page details
    L.append("## Detalhamento por página")
    L.append("")
    L.append("Para cada página, lista dos assets (imagens, CSS, JS) referenciados e confirmados como baixados em `site/`.")
    L.append("")

    for slug, _, name, parent in sorted(PAGES, key=lambda x: x[2]):
        data = pages_data[slug]
        local_file = "site/index.html" if slug == "index" else f"site/{slug}.html"
        path = SITE / ("index.html" if slug == "index" else f"{slug}.html")
        status = "OK" if path.exists() else "FALTA"
        size_kb = path.stat().st_size / 1024 if path.exists() else 0
        url_original = f"{BASE_URL}/{data['parent']}" if data.get("href") == "" else f"{BASE_URL}/{pages_meta[slug]['href']}"

        L.append(f"### {name}")
        L.append("")
        L.append(f"- **Slug:** `{slug}`")
        L.append(f"- **URL original:** <{url_original}>")
        L.append(f"- **Arquivo local:** `{local_file}` ({size_kb:.0f} KB)")
        L.append(f"- **Status:** **{status}**")
        if data.get("parent"):
            L.append(f"- **Página pai:** `{data['parent']}`")
        n_assets = len(data["assets"])
        L.append(f"- **Assets referenciados:** {n_assets}")
        L.append("")

        if data["assets"]:
            images = [a for a in data["assets"] if a.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".svg"))]
            css = [a for a in data["assets"] if a.lower().endswith(".css")]
            js = [a for a in data["assets"] if a.lower().endswith(".js")]
            other = [a for a in data["assets"] if a not in images and a not in css and a not in js]

            def emit(items, label, kind):
                if not items:
                    return
                L.append(f"  **{label} ({len(items)}):**")
                L.append("")
                for a in items:
                    target = SITE / a
                    if target.exists():
                        size = target.stat().st_size
                        kb = size / 1024
                        sz = f" ({kb:.0f} KB)" if kb < 1024 else f" ({kb/1024:.1f} MB)"
                    else:
                        sz = " ❌ FALTA"
                    L.append(f"  - `{a}`{sz}")
                L.append("")

            emit(images, "Imagens", "img")
            emit(css, "CSS", "css")
            emit(js, "JavaScript", "js")
            emit(other, "Outros", "other")
        L.append("")

    L.append("---")
    L.append("")
    L.append("## Lista consolidada de todos os assets")
    L.append("")
    L.append(f"Total de assets únicos: **{len(total_assets)}**")
    L.append("")

    # Group by top-level folder
    by_folder = defaultdict(list)
    for a in sorted(total_assets):
        if a.startswith(("local/", "plugins/", "lib/", "prive/", "squelettes-dist/", "extensions/", "IMG/")):
            top = a.split("/")[0]
            by_folder[top].append(a)
        else:
            by_folder["_outros"].append(a)

    for folder in sorted(by_folder.keys()):
        items = by_folder[folder]
        L.append(f"### `{folder}/` ({len(items)} arquivos)")
        L.append("")
        for a in items:
            target = SITE / a
            if target.exists():
                size = target.stat().st_size
                kb = size / 1024
                sz = f" ({kb:.0f} KB)" if kb < 1024 else f" ({kb/1024:.1f} MB)"
            else:
                sz = " ❌ FALTA"
            L.append(f"- `{a}`{sz}")
        L.append("")

    (ROOT / "estrutura.md").write_text("\n".join(L), encoding="utf-8")
    print(f"Saved estrutura.md ({len(L)} lines)")

    # Regenerate README
    rd = [
        "# Fandango em Cananéia — site estático local",
        "",
        "Versão estática (HTML + CSS + JS + imagens) do site ",
        "[https://www.fandangoemcananeia.art.br/](https://www.fandangoemcananeia.art.br/).",
        "",
        "## Como abrir",
        "Abra `site/index.html` em qualquer navegador moderno. O site é totalmente offline.",
        "",
        "## Como servir localmente (opcional)",
        "Se preferir usar um servidor local para evitar problemas com caminhos relativos:",
        "```",
        "cd site && python3 -m http.server 8000",
        "# depois abra http://localhost:8000/",
        "```",
        "",
        "## Estrutura",
        "- `site/` — todas as páginas HTML e assets (CSS, JS, imagens)",
        "- `site/local/` — imagens em cache geradas pelo SPIP original",
        "- `site/IMG/` — imagens originais dos artigos",
        "- `site/plugins/`, `site/lib/`, `site/prive/`, `site/extensions/`, `site/squelettes-dist/` — assets do tema e bibliotecas JS",
        "- `estrutura.md` — listagem completa de todas as páginas com seus assets",
        "- `README.md` — este arquivo",
        "- `build_static.py` — script que gerou o site (em `/tmp/`)",
        "",
        "## Estatísticas",
        f"- **{len(PAGES)}** páginas HTML",
        f"- **{len(total_assets)}** assets únicos (CSS, JS, imagens, fontes, etc.)",
        f"- **{sum(f.stat().st_size for f in SITE.rglob('*') if f.is_file()) / (1024*1024):.1f} MB** total no disco",
        f"- Origem: {BASE_URL}",
        "",
        "## Notas técnicas",
        "",
        "O site original é gerado pelo CMS **SPIP** e usa URLs limpas (sem extensão), tipo `/Nome-da-Pagina`.",
        "Para funcionar como site estático, cada página foi salva como `<slug>.html` e todos os",
        "links internos foram reescritos para apontar para os arquivos `.html` correspondentes.",
        "",
        "**Adaptações feitas:**",
        "- URLs internas reescritas de `/Nome` para `/Nome.html`",
        "- Slug `Natureza,80` (artigo 80) salvo como `Natureza-80.html` para evitar conflitos com a página `Natureza` (que é a seção História)",
        "- Caracteres especiais preservados (ex: `1ª-Festa-do-Fandango-Caicara-de.html`)",
        "- Formulários (contato, login) neutralizados — não há backend PHP",
        "- Scripts `spip.php?page=*` e `spip.php?action=cron` removidos",
        "- `<link rel=\"icon\" href=\"favicon.ico\">` removido (o favicon original está vazio)",
        "- Páginas placeholder vazias (`slider1`, `slider2`, `Nova-materia`, `icone`) removidas",
        "- Paginação SPIP (`?debut_articles=N`) redirecionada para a página principal",
        "",
        "Os menus, layout, CSS, JS, fancybox, slideshow e todas as interações client-side foram preservados.",
    ]
    (ROOT / "README.md").write_text("\n".join(rd), encoding="utf-8")
    print(f"Saved README.md")


if __name__ == "__main__":
    main()
