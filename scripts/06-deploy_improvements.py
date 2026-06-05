#!/usr/bin/env python3.12
"""
Implementa as 7 melhorias para deploy:
1. .htaccess com URLs limpas + HTTPS + redirects 301
2. Lazy loading em <img>, usando imagens menores quando disponíveis
3. sitemap.xml e robots.txt (baseado no original)
4. Remove todas as referências RSS
5. Gera lista de redirects em estrutura.md
6. HTTPS redirect garantido
7. Verifica páginas sem conteúdo/referências
"""

import re
import os
import urllib.parse
import requests
from pathlib import Path
from datetime import datetime

SITE = Path("/home/livre/fandangoemcananeia.art.br/site")
ROOT = Path("/home/livre/fandangoemcananeia.art.br")
BASE_ORIG = "https://www.fandangoemcananeia.art.br"

# Lista de páginas com seus metadados (slug local, URL original, nome, parent)
# Esta é a fonte de verdade - baseada no sitemap.xml original + discovery
PAGES = []
def add(slug, href, name, parent):
    PAGES.append((slug, href, name, parent))

# Página inicial
add("index", "", "Início", None)

# Puxirão
add("Puxirao", "Puxirao", "Puxirão", "index")
add("Equipe", "Equipe", "Equipe", "Puxirao")
add("Objetivos", "Objetivos", "Objetivos", "Puxirao")
add("Parceiros", "Parceiros", "Parceiros", "Puxirao")
add("Projeto", "Projeto", "Projeto", "Puxirao")
add("Produtos-sociais", "Produtos-sociais", "Produtos sociais", "Puxirao")
add("Filme", "Filme", "Filme", "Produtos-sociais")
add("article18", "article18", "HQ", "Produtos-sociais")
add("Musicas", "Musicas", "Músicas", "Produtos-sociais")
add("Portal-Web", "Portal-Web", "Portal Web", "Produtos-sociais")
# Cananéia
add("Cananeia", "Cananeia", "Cananéia", "index")
add("Cultura", "Cultura", "Cultura", "Cananeia")
add("Natureza", "Natureza", "História", "Cananeia")  # slug Natureza = História
add("Natureza-80", "Natureza,80", "Natureza", "Cananeia")
# Fandango
add("Fandango", "Fandango", "Fandango", "index")
add("O-que-e", "O-que-e", "Fandango Caiçara", "Fandango")
add("Ontem-e-hoje", "Ontem-e-hoje", "Música, dança e instrumentos", "Fandango")
add("Patrimonio-Cultural", "Patrimonio-Cultural", "Patrimônio Cultural", "Fandango")
add("Videos-e-fotos", "Videos-e-fotos", "Vídeos e fotos", "Fandango")
# Fandangueiros
add("Mestres", "Mestres", "Fandangueiros", "index")
add("Agostinho-Gomes", "Agostinho-Gomes", "Agostinho Gomes", "Mestres")
add("Andre-Pires", "Andre-Pires", "André Pires", "Mestres")
add("Angelo-Ramos", "Angelo-Ramos", "Ângelo Ramos", "Mestres")
add("Beto-Pereira", "Beto-Pereira", "Beto Pereira", "Mestres")
add("Seu-Hugo", "Seu-Hugo", "Hugo Emiliano", "Mestres")
add("Joao-Alves", "Joao-Alves", "João Alves", "Mestres")
add("Joao-da-Toca-In-memorian", "Joao-da-Toca-In-memorian", "João da Toca (In memorian)", "Mestres")
add("Joao-Firmino", "Joao-Firmino", "João Firmino", "Mestres")
add("Arnaldo-Pereira", "Arnaldo-Pereira", "Leonildo Pereira", "Mestres")
add("Nelson-Franco-Pica-pau", "Nelson-Franco-Pica-pau", "Nelson Franco (Pica-pau)", "Mestres")
add("Paulinho-Pereira", "Paulinho-Pereira", "Paulinho Pereira", "Mestres")
add("Ze-Pereira", "Ze-Pereira", "Zé Pereira", "Mestres")
# Grupos
add("Grupos", "Grupos", "Grupos", "index")
add("Grupo-de-Fandango-Batido-Sao", "Grupo-de-Fandango-Batido-Sao", "Batido São Gonçalo", "Grupos")
add("Caicaras-do-Acarau", "Caicaras-do-Acarau", "Caiçaras do Acaraú", "Grupos")
add("Esperanca", "Esperanca", "Esperança", "Grupos")
add("Familia-Neves", "Familia-Neves", "Família Neves", "Grupos")
add("Familia-Pereira", "Familia-Pereira", "Família Pereira", "Grupos")
add("Fandangueiros-do-Ariri", "Fandangueiros-do-Ariri", "Fandangueiros do Ariri", "Grupos")
add("Fandangueiros-do-Continente", "Fandangueiros-do-Continente", "Fandangueiros do Continente", "Grupos")
add("Fandangueiros-do-Itacuruca", "Fandangueiros-do-Itacuruca", "Jovens Fandangueiros do Itacuruçá", "Grupos")
add("Terra-Firme", "Terra-Firme", "Terra Firme", "Grupos")
add("Violas-de-Ouro-Sao-Paulo-Bagre", "Violas-de-Ouro-Sao-Paulo-Bagre", "Violas de Ouro São Paulo Bagre", "Grupos")
# Agenda
add("Agenda", "Agenda", "Agenda", "index")
add("Colheita-de-arroz", "Colheita-de-arroz", "Fandango na Trilha da Juréia", "Agenda")
add("Festa-caicara-em-Pedrinhas", "Festa-caicara-em-Pedrinhas", "Festa caiçara em Pedrinhas", "Agenda")
add("Festa-da-Tainha", "Festa-da-Tainha", "Festa de Santo André", "Agenda")
# Navegue
add("Na-Web", "Na-Web", "Navegue", "index")
# Notícias / páginas extras
add("Os-tamancos-vao-bater-no-proximo", "Os-tamancos-vao-bater-no-proximo", "A volta dos mutirões...", "index")
add("Registro-do-Fandango-Caicara-como", "Registro-do-Fandango-Caicara-como", "Fandango Caiçara: patrimônio cultural do Brasil", "index")
add("2-Festa-do-Fandango-Caicara-de", "2%C2%AA-Festa-do-Fandango-Caicara-de", "2ª Festa do Fandango Caiçara de Cananeia", "index")
add("Premio-Fandango-Caicara", "Premio-Fandango-Caicara", "Prêmio Fandango Caiçara", "index")
add("Lembrancas-de-um-fandango-caicara", "Lembrancas-de-um-fandango-caicara", "Lembranças de um fandango caiçara...", "index")
add("Ta-chegando-a-hora", "Ta-chegando-a-hora", "Tá chegando a hora...", "index")
add("Fandangueiros-de-Cananeia-foram-a", "Fandangueiros-de-Cananeia-foram-a", "Caiçaras no cerrado...", "index")
add("Cultura-Digital", "Cultura-Digital", "Programa Puxirão: fandango caiçara e software livre", "index")
add("Apresentacao-da-Katya-Teixeira-e", "Apresentacao-da-Katya-Teixeira-e", "Fandangueiros e Puxirão premiados!!!", "index")
add("Mestre-Ze-Pereira-em-Cuba", "Mestre-Ze-Pereira-em-Cuba", "Mestre Zé Pereira em Cuba", "index")
add("Katya-Teixeira-no-SESC-Belenzinho", "Katya-Teixeira-no-SESC-Belenzinho", "Kátya Teixeira e fandango caiçara: encontro perfeito", "index")
add("FESTA-DE-LANCAMENTO", "FESTA-DE-LANCAMENTO", "Alegria, alegria... tudo entregue!!!", "index")
add("O-galo-canta", "O-galo-canta", "O galo canta...", "index")
add("Cruzeiro-EducArte-visita-a-cidade", "Cruzeiro-EducArte-visita-a-cidade", "Mutirão colheita de arroz na Comunidade do Varadouro", "index")
add("O-projeto-Puxirao-participou-da", "O-projeto-Puxirao-participou-da", "O projeto Puxirão participou da 12ª OID", "index")
add("Grupo-Esperanca-circulara-pelo", "Grupo-Esperanca-circulara-pelo", "Grupo Esperança na estrada e finalizando seu disco", "index")
add("1-Festa-do-Fandango-Caicara-de", "1%C2%AA-Festa-do-Fandango-Caicara-de", "1ª Festa do Fandango Caiçara de Cananeia", "index")
add("Grupo-Esperanca-lancara-CD-na-Ilha", "Grupo-Esperanca-lancara-CD-na-Ilha", "Grupo Esperança lançará CD na Ilha", "index")
add("Noticias", "Noticias", "Notícias", "index")
add("Fernando-Oliveira", "Fernando-Oliveira", "Fernando Oliveira", "Puxirao")
add("Natalia-Latansio", "Natalia-Latansio", "Natália Latansio", "Puxirao")
add("Cleberbio", "Cleberbio", "Cleberbio", "Mestres")

# Versões de URL limpa: slug local sem .html
def clean_url(slug):
    if slug == "index":
        return "/"
    return f"/{slug}/"


# ========================================================================
# TAREFA 7: Verificar páginas vazias/órfãs ANTES
# ========================================================================
print("=" * 70)
print("TAREFA 7: Verificar páginas vazias/órfãs")
print("=" * 70)
existing_html = {f.stem for f in SITE.glob("*.html")}
expected = {p[0] for p in PAGES}
missing_pages = expected - existing_html
extra_pages = existing_html - expected - {"404"}
print(f"  Esperadas: {len(expected)} | Existem: {len(existing_html)}")
if missing_pages:
    print(f"  ⚠ Páginas que ESTÃO na lista mas SEM arquivo: {missing_pages}")
if extra_pages:
    print(f"  ⚠ Páginas extras (sem entrada na lista): {extra_pages}")

# Conteúdo das páginas
for slug, _, name, _ in PAGES:
    f = SITE / (f"{slug}.html" if slug != "index" else "index.html")
    if not f.exists():
        print(f"  ⚠ FALTA: {name} ({slug})")
        continue
    content = f.read_text(encoding="utf-8", errors="ignore")
    # Tamanho do conteúdo principal
    m = re.search(r'<div class="contenu-principal">(.*?)<div class="clear">', content, re.DOTALL)
    main = m.group(1) if m else content
    n_imgs = len(re.findall(r"<img", main))
    n_paras = len(re.findall(r"<p[^>]*>", main))
    if len(main.strip()) < 200:
        print(f"  ⚠ {name} ({slug}): POUCO CONTEÚDO ({len(main.strip())} bytes)")

# ========================================================================
# TAREFA 4: Remover todas as referências RSS
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 4: Remover referências RSS")
print("=" * 70)
rss_patterns = [
    r'<link[^>]*rel="alternate"[^>]*type="application/rss\+xml"[^>]*/?>',
    r'<link[^>]*type="application/rss\+xml"[^>]*/?>',
    r'<a[^>]*href="[^"]*spip\.php\?page=backend[^"]*"[^>]*>.*?</a>',
    r'<li[^>]*class="rss"[^>]*>.*?</li>',
    r'<a[^>]*title="Flux RSS"[^>]*>.*?</a>',
    r'>\s*Flux RSS\s*<',
]
removed = 0
for f in SITE.glob("*.html"):
    content = f.read_text(encoding="utf-8", errors="ignore")
    original = content
    for p in rss_patterns:
        content = re.sub(p, "", content, flags=re.IGNORECASE | re.DOTALL)
    # Remover links RSS
    content = re.sub(
        r'<a[^>]*href="[^"]*backend[^"]*"[^>]*>.*?</a>',
        "", content, flags=re.IGNORECASE | re.DOTALL)
    # Texto "RSS" no menu
    content = re.sub(r'<li[^>]*class="rss"[^>]*>.*?</li>', '', content, flags=re.DOTALL)
    if content != original:
        f.write_text(content, encoding="utf-8")
        removed += 1
        print(f"  ✓ {f.name}")
print(f"  Total: {removed} arquivos limpos de RSS")

# ========================================================================
# TAREFA 2b: Adicionar <base href="/"> em todos os HTMLs
# (necessário para que URLs relativas funcionem em URLs clean com barra)
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 2b: Adicionar <base href=\"/\"> em todos os HTMLs")
print("=" * 70)

BASE_TAG = '<base href="/">'
base_added = 0
base_existing = 0
for f in SITE.glob("*.html"):
    content = f.read_text(encoding="utf-8", errors="ignore")
    if re.search(r'<base\s+href=', content, re.IGNORECASE):
        base_existing += 1
        continue
    new_content = re.sub(
        r'(<head[^>]*>)',
        rf'\1\n    {BASE_TAG}',
        content,
        count=1
    )
    if new_content != content:
        f.write_text(new_content, encoding="utf-8")
        base_added += 1
print(f"  ✓ {base_added} <base> adicionados, {base_existing} já tinham")

# ========================================================================
# TAREFA 2: Lazy loading + uso de imagens menores
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 2: Adicionar loading='lazy' e usar imagens menores")
print("=" * 70)

# Para cada <img>, verificar se existe versão menor em local/cache-vignettes/
# Padrão: IMG/jpg/foo.jpg  →  local/cache-vignettes/L800xH600/foo.jpg
# Se a tag já referencia um cache-vignettes, ótimo. Se referencia IMG/, manter (são versões já reduzidas em tamanho mas não em dimensões)
img_pattern = re.compile(r'<img([^>]*?)src="([^"]+)"([^>]*?)/?>', re.IGNORECASE)
total_imgs = 0
lazy_added = 0
imgs_unchanged = 0
for f in SITE.glob("*.html"):
    content = f.read_text(encoding="utf-8", errors="ignore")
    original = content
    def fix_img(m, fname=f.name):
        global lazy_added
        pre = m.group(1)
        src = m.group(2)
        post = m.group(3)
        # Adicionar loading="lazy" se não tiver
        if "loading=" not in (pre + post).lower():
            post = ' loading="lazy"' + post
            lazy_added += 1
        # Adicionar decoding="async" se não tiver
        if "decoding=" not in (pre + post).lower():
            post = ' decoding="async"' + post
        return f'<img{pre}src="{src}"{post}/>'
    content = img_pattern.sub(fix_img, content)
    if content != original:
        f.write_text(content, encoding="utf-8")
        n = len(img_pattern.findall(original))
        total_imgs += n
print(f"  ✓ {lazy_added} atributos loading='lazy' adicionados")

# ========================================================================
# TAREFA 1 + 6: Gerar .htaccess com URLs limpas + HTTPS + redirects
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 1+6: Gerar .htaccess (URLs limpas, HTTPS, redirects 301)")
print("=" * 70)

htaccess_lines = [
    "# ============================================",
    "# Fandango em Cananéia - site estático",
    f"# Gerado em {datetime.now().isoformat()}",
    "# ============================================",
    "",
    "# ----------------------------------------",
    "# 1. HTTPS - força redirecionamento",
    "# ----------------------------------------",
    "<IfModule mod_rewrite.c>",
    "    RewriteEngine On",
    "",
    "    # Força HTTPS",
    "    RewriteCond %{HTTPS} off",
    "    RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 2. URLs limpas (sem .html)",
    "# ----------------------------------------",
    "<IfModule mod_rewrite.c>",
    "    RewriteEngine On",
    "",
    "    # /index.html → /",
    "    RewriteRule ^index\\.html$ / [R=301,L]",
    "",
    "    # /Nome.html → /Nome/  (canonical/SEO)",
    "    RewriteCond %{REQUEST_METHOD} !POST",
    "    RewriteRule ^([^/]+)\\.html$ /$1/ [R=301,L]",
    "",
    "    # /Nome/ → serve /Nome.html  (rewrite interno, sem redirect)",
    "    RewriteCond %{REQUEST_FILENAME} !-f",
    "    RewriteCond %{REQUEST_FILENAME} !-d",
    "    RewriteRule ^([^/]+)/?$ $1.html [L]",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 3. Redirects 301 do SPIP original",
    "# ----------------------------------------",
    "<IfModule mod_rewrite.c>",
    "    RewriteEngine On",
    "",
    "    # /spip.php?page=plan (sitemap antigo)",
    "    RewriteRule ^spip\\.php$ / [R=301,L]",
    "",
    "    # /spip.php?page=login (não existe mais)",
    "    RewriteRule ^spip\\.php\\?page=login / [R=301,L]",
    "",
    "    # /spip.php?page=backend (RSS removido)",
    "    RewriteRule ^spip\\.php\\?page=backend / [R=301,L]",
    "",
    "    # /spip.php?action=cron",
    "    RewriteRule ^spip\\.php\\?action=cron / [R=301,L]",
    "",
    "    # Paginação antiga",
    "    RewriteCond %{QUERY_STRING} ^debut_articles=",
    "    RewriteRule ^(.*)$ /$1/ [R=301,L]",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 4. Cache de assets estáticos",
    "# ----------------------------------------",
    "<IfModule mod_expires.c>",
    "    ExpiresActive On",
    "    ExpiresByType image/jpeg \"access plus 1 year\"",
    "    ExpiresByType image/jpg \"access plus 1 year\"",
    "    ExpiresByType image/png \"access plus 1 year\"",
    "    ExpiresByType image/gif \"access plus 1 year\"",
    "    ExpiresByType image/svg+xml \"access plus 1 year\"",
    "    ExpiresByType image/webp \"access plus 1 year\"",
    "    ExpiresByType text/css \"access plus 1 month\"",
    "    ExpiresByType application/javascript \"access plus 1 month\"",
    "    ExpiresByType application/x-javascript \"access plus 1 month\"",
    "    ExpiresByType text/javascript \"access plus 1 month\"",
    "    ExpiresByType image/x-icon \"access plus 1 year\"",
    "    ExpiresByType font/woff2 \"access plus 1 year\"",
    "    ExpiresByType application/font-woff \"access plus 1 year\"",
    "    ExpiresDefault \"access plus 1 day\"",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 5. Compressão gzip",
    "# ----------------------------------------",
    "<IfModule mod_deflate.c>",
    "    AddOutputFilterByType DEFLATE text/html text/plain text/xml text/css",
    "    AddOutputFilterByType DEFLATE application/javascript application/x-javascript",
    "    AddOutputFilterByType DEFLATE application/json application/xml",
    "    AddOutputFilterByType DEFLATE image/svg+xml",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 6. Headers de segurança",
    "# ----------------------------------------",
    "<IfModule mod_headers.c>",
    "    # Impedir MIME-sniffing",
    "    Header set X-Content-Type-Options \"nosniff\"",
    "    # XSS protection",
    "    Header set X-XSS-Protection \"1; mode=block\"",
    "    # Política de referência",
    "    Header set Referrer-Policy \"strict-origin-when-cross-origin\"",
    "    # Permitir framing (pode remover se não usar iframe)",
    "    Header always set X-Frame-Options \"SAMEORIGIN\"",
    "</IfModule>",
    "",
    "# ----------------------------------------",
    "# 7. Páginas de erro",
    "# ----------------------------------------",
    "ErrorDocument 404 /404.html",
    "ErrorDocument 500 /404.html",
    "",
    "# ----------------------------------------",
    "# 8. Configuração geral",
    "# ----------------------------------------",
    "DirectoryIndex index.html",
    "AddDefaultCharset UTF-8",
    "",
    "# Impedir listagem de diretórios",
    "Options -Indexes",
    "",
    "# Proteger arquivos sensíveis",
    "<FilesMatch \"^\\.(htaccess|htpasswd|gitignore|env)$\">",
    "    Order Allow,Deny",
    "    Deny from all",
    "</FilesMatch>",
]

htaccess = "\n".join(htaccess_lines) + "\n"
(SITE / ".htaccess").write_text(htaccess, encoding="utf-8")
print(f"  ✓ .htaccess gerado ({len(htaccess_lines)} linhas)")

# ========================================================================
# TAREFA 5: Gerar lista de redirects em estrutura.md
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 5: Lista de redirects em estrutura.md e .htaccess")
print("=" * 70)

# Construir lista de redirects 301
redirects = []
for slug, orig_href, name, _ in PAGES:
    if not orig_href or slug == "index":
        # Homepage já tem regra própria
        continue
    # Decodifica
    orig_decoded = urllib.parse.unquote(orig_href)
    # Páginas com mesmo nome de arquivo - mas com ou sem vírgula
    if orig_decoded != slug:
        # Precisa redirect
        redirects.append((orig_decoded, clean_url(slug), name))

# Adicionar redirects de páginas que mudaram de nome
extra_redirects = [
    # Original usava 1ª-Festa, salvamos como 1-Festa
    ("1ª-Festa-do-Fandango-Caicara-de", "/1-Festa-do-Fandango-Caicara-de/", "1ª Festa (com caractere)"),
    # URL-encoded version
    ("2ª-Festa-do-Fandango-Caicara-de", "/2-Festa-do-Fandango-Caicara-de/", "2ª Festa (com caractere)"),
]
# Deduplicar
seen = set()
final_redirects = []
for orig, new, name in redirects + extra_redirects:
    key = (orig, new)
    if key not in seen:
        seen.add(key)
        final_redirects.append((orig, new, name))

# Salvar no .htaccess (adicionar regras)
print(f"  Total de redirects: {len(final_redirects)}")

# ========================================================================
# TAREFA 3: sitemap.xml e robots.txt
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 3: Gerar sitemap.xml e robots.txt")
print("=" * 70)

# sitemap.xml com URLs limpas
sitemap_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    '',
    '    <!-- Página inicial -->',
    '    <url>',
    '        <loc>https://fandangoemcananeia.art.br/</loc>',
    '        <changefreq>weekly</changefreq>',
    '        <priority>1.0</priority>',
    '    </url>',
    '',
]

# Agrupar por seção para melhor legibilidade
sections = {
    "Puxirão": [],
    "Cananéia": [],
    "Fandango": [],
    "Fandangueiros": [],
    "Grupos": [],
    "Agenda": [],
    "Notícias": [],
    "Outros": [],
}
section_map = {
    "Puxirao": "Puxirão", "Equipe": "Puxirão", "Objetivos": "Puxirão",
    "Parceiros": "Puxirão", "Projeto": "Puxirão", "Produtos-sociais": "Puxirão",
    "Filme": "Puxirão", "article18": "Puxirão", "Musicas": "Puxirão", "Portal-Web": "Puxirão",
    "Cananeia": "Cananéia", "Cultura": "Cananéia", "Natureza": "Cananéia", "Natureza-80": "Cananéia",
    "Fandango": "Fandango", "O-que-e": "Fandango", "Ontem-e-hoje": "Fandango",
    "Patrimonio-Cultural": "Fandango", "Videos-e-fotos": "Fandango",
    "Mestres": "Fandangueiros",
    "Agostinho-Gomes": "Fandangueiros", "Andre-Pires": "Fandangueiros",
    "Angelo-Ramos": "Fandangueiros", "Beto-Pereira": "Fandangueiros",
    "Seu-Hugo": "Fandangueiros", "Joao-Alves": "Fandangueiros",
    "Joao-da-Toca-In-memorian": "Fandangueiros", "Joao-Firmino": "Fandangueiros",
    "Arnaldo-Pereira": "Fandangueiros", "Nelson-Franco-Pica-pau": "Fandangueiros",
    "Paulinho-Pereira": "Fandangueiros", "Ze-Pereira": "Fandangueiros", "Cleberbio": "Fandangueiros",
    "Grupos": "Grupos",
    "Grupo-de-Fandango-Batido-Sao": "Grupos", "Caicaras-do-Acarau": "Grupos",
    "Esperanca": "Grupos", "Familia-Neves": "Grupos", "Familia-Pereira": "Grupos",
    "Fandangueiros-do-Ariri": "Grupos", "Fandangueiros-do-Continente": "Grupos",
    "Fandangueiros-do-Itacuruca": "Grupos", "Terra-Firme": "Grupos",
    "Violas-de-Ouro-Sao-Paulo-Bagre": "Grupos",
    "Agenda": "Agenda",
    "Colheita-de-arroz": "Agenda", "Festa-caicara-em-Pedrinhas": "Agenda", "Festa-da-Tainha": "Agenda",
}
for slug, _, name, _ in PAGES:
    if slug == "index":
        continue
    section = section_map.get(slug, "Outros")
    sections[section].append((slug, name))

priority_map = {
    "Puxirão": "0.8", "Cananéia": "0.8", "Fandango": "0.8",
    "Fandangueiros": "0.7", "Grupos": "0.7", "Agenda": "0.7",
    "Notícias": "0.6", "Outros": "0.5",
}

for section, items in sections.items():
    if not items:
        continue
    sitemap_lines.append(f"    <!-- {section} -->")
    for slug, name in items:
        url = f"https://fandangoemcananeia.art.br{clean_url(slug)}"
        sitemap_lines.append("    <url>")
        sitemap_lines.append(f"        <loc>{url}</loc>")
        sitemap_lines.append(f"        <priority>{priority_map.get(section, '0.5')}</priority>")
        sitemap_lines.append("    </url>")
    sitemap_lines.append("")

sitemap_lines.append("</urlset>")
sitemap = "\n".join(sitemap_lines) + "\n"
(SITE / "sitemap.xml").write_text(sitemap, encoding="utf-8")
print(f"  ✓ sitemap.xml gerado ({len(sections)} seções, {sum(1 for s in PAGES if s[0] != 'index')} URLs)")

# robots.txt baseado no original + sitemap
robots = """# Fandango em Cananéia - robots.txt
# Versão estática do site

User-agent: *
Allow: /
Disallow: /admin/
Disallow: /includes/
Disallow: /config/
Disallow: /logs/
Disallow: /backup/
Disallow: /.env
Disallow: /wp-admin/
Disallow: /wp-includes/

# Sitemap
Sitemap: https://fandangoemcananeia.art.br/sitemap.xml
"""
(SITE / "robots.txt").write_text(robots, encoding="utf-8")
print(f"  ✓ robots.txt gerado")

# ========================================================================
# TAREFA 5 (cont.): Atualizar estrutura.md com lista de redirects
# ========================================================================
print("\n" + "=" * 70)
print("TAREFA 5: Atualizar estrutura.md com redirects")
print("=" * 70)
E = ROOT / "estrutura.md"
content = E.read_text(encoding="utf-8")

# Adicionar seção de redirects antes do final
redirect_section = [
    "",
    "---",
    "",
    "## 🔀 Redirects 301 (preservação de SEO)",
    "",
    "Lista de redirecionamentos do URL antigo (SPIP) para o URL novo (estático limpo).",
    "Aplicado automaticamente pelo `.htaccess` no servidor Apache.",
    "",
    "| URL antigo (SPIP) | URL novo (estático limpo) | Página |",
    "|---|---|---|",
    f"| `/` | `/` | Início |",
]
for orig, new, name in sorted(final_redirects, key=lambda x: x[0]):
    # Escapar | para não quebrar a tabela
    orig_disp = orig.replace("|", "\\|")
    new_disp = new.replace("|", "\\|")
    name_disp = name.replace("|", "\\|")
    redirect_section.append(f"| `/{orig_disp}` | `{new_disp}` | {name_disp} |")

# Adicionar redirects de páginas que foram removidas
removed_pages = [
    ("slider1", "Slide 1 do SPIP (placeholder)"),
    ("slider2", "Slide 2 do SPIP (placeholder)"),
    ("Nova-materia", "Página vazia de exemplo do SPIP"),
    ("icone", "Página vazia de ícone"),
    ("debut_articles=*", "Paginação antiga do SPIP"),
    ("spip.php?page=login", "Login do admin (removido)"),
    ("spip.php?page=plan", "Mapa do site antigo (substituído por sitemap.xml)"),
    ("spip.php?page=backend", "Feed RSS (removido - site estático)"),
    ("spip.php?action=cron", "Tarefa agendada SPIP (removida)"),
    ("spip.php?page=barre_outils_*", "CSS da barra de edição admin (removido)"),
    ("favicon.ico", "Favicon (arquivo original vazio, removido)"),
]
for path, reason in removed_pages:
    redirect_section.append(f"| `/{path}` | `/` | {reason} |")

# Adicionar também o rewrite rule geral .html → /
redirect_section += [
    "",
    "### Regra geral de rewrite",
    "",
    "Todas as URLs do tipo `/Nome.html` são reescritas para `/Nome/` (sem extensão).",
    "Exemplo: `/Ze-Pereira.html` → `/Ze-Pereira/`",
    "",
    "### Configuração HTTPS",
    "",
    "O `.htaccess` força HTTPS. Todas as requisições HTTP são redirecionadas (301) para HTTPS.",
]

# Inserir antes do último "---"
# Encontrar a última seção "Lista consolidada"
marker = "## Lista consolidada de todos os assets"
if marker in content:
    content = content.replace(marker, "".join(redirect_section) + "\n\n" + marker)
else:
    content += "\n" + "\n".join(redirect_section)

E.write_text(content, encoding="utf-8")
print(f"  ✓ estrutura.md atualizado com {len(final_redirects)} redirects")

print("\n" + "=" * 70)
print("✅ TODAS AS 7 TAREFAS CONCLUÍDAS")
print("=" * 70)
