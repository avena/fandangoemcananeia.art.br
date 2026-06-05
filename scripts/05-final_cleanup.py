#!/usr/bin/env python3.12
"""
Limpeza FINAL para deploy:
- Remove TODAS as referências a SPIP/CMS
- Remove links de login
- Remove forms (não funcionam sem backend)
- Remove scripts SPIP
- Remove URLs externas ao site original
- Mantém apenas o conteúdo real do site
"""

import re
import urllib.parse
from pathlib import Path

SITE = Path("/home/livre/fandangoemcananeia.art.br/site")
BASE = "https://www.fandangoemcananeia.art.br"


def clean_url(url):
    """Retorna None se a URL deve ser removida, ou a URL limpa/reescrita."""
    if not url:
        return None
    url = url.strip()

    # URLs externas ao site original - manter apenas spip.net (crédito)
    if url.startswith(("http://", "https://")):
        if "fandangoemcananeia.art.br" in url:
            # Páginas do site - reescrever para local
            parsed = urllib.parse.urlparse(url)
            path = urllib.parse.unquote(parsed.path.lstrip("/"))
            if not path or path == "/":
                return "index.html"
            if "," in path:
                path = path.replace(",", "-")
            path = path.rstrip("/")
            target = SITE / f"{path}.html"
            if target.exists():
                return f"{path}.html"
            # Tenta como slug direto
            if (SITE / path).exists():
                return path
            return None
        if "spip.net" in url:
            return None  # Remove o crédito SPIP
        if "oficinainclusaodigital" in url:
            return None
        # Qualquer outra URL externa - remove
        return None

    # Já é local
    return url


# ========================================================================
# 1. PROCESSAR TODOS OS HTMLs
# ========================================================================
print("=" * 60)
print("LIMPEZA FINAL PARA DEPLOY")
print("=" * 60)

files_processed = 0
total_changes = 0

for f in SITE.glob("*.html"):
    content = f.read_text(encoding="utf-8", errors="ignore")
    original = content
    changes = [0]  # use list for mutability in nested function

    # 1a. Remover comentários HTML com SPIP
    content, n = re.subn(r'<!--[^>]*SPIP[^>]*-->', '', content, flags=re.IGNORECASE)
    content, n2 = re.subn(r'<!--[^>]*insert_head[^>]*-->', '', content, flags=re.IGNORECASE)
    changes[0] += n + n2

    # 1b. Reescrever/remover hrefs externas
    def fix_href(m, ch=changes):
        attr = m.group(1)
        url = m.group(2)
        new = clean_url(url)
        if new is None:
            ch[0] += 1
            return ""  # remove o atributo inteiro
        if new != url:
            ch[0] += 1
        return f'{attr}="{new}"'
    content = re.sub(r'(href|src|action|cite|longdesc|usemap)="(https?://[^"]+)"',
                     fix_href, content, flags=re.IGNORECASE)

    # 1c. Remover TODOS os links de login
    content = re.sub(
        r'<a[^>]*href="[^"]*spip\.php\?page=login[^"]*"[^>]*>.*?</a>',
        '', content, flags=re.IGNORECASE | re.DOTALL)

    # 1d. Remover divs/bgs com spip.php
    content = re.sub(
        r'<div[^>]*background[^>]*spip\.php[^>]*>.*?</div>',
        '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(
        r'<div[^>]*style="[^"]*spip\.php[^"]*"[^>]*>.*?</div>',
        '', content, flags=re.IGNORECASE | re.DOTALL)

    # 1e. Remover tags <link> e <script> que apontam para spip.php
    content = re.sub(
        r'<link[^>]*href="[^"]*spip\.php[^"]*"[^>]*/?>',
        '', content, flags=re.IGNORECASE)
    content = re.sub(
        r'<script[^>]*src="[^"]*spip\.php[^"]*"[^>]*>.*?</script>',
        '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(
        r'<script[^>]*src="[^"]*fancybox\.js"[^>]*>.*?</script>',
        '', content, flags=re.IGNORECASE | re.DOTALL)  # já tratado pelo rewrite, mas garante

    # 1f. Remover bloco <!-- SPIP-CRON -->
    content = re.sub(
        r'<!--\s*SPIP-CRON\s*-->.*?</div>',
        '', content, flags=re.IGNORECASE | re.DOTALL)

    # 1g. Remover divs com spip.php?action=cron
    content = re.sub(
        r'<div[^>]*url\([\'"]?http[^)]*spip\.php\?action=cron[^)]*\)[\'"]?[^>]*>.*?</div>',
        '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(
        r'<div[^>]*style="[^"]*spip\.php\?action=cron[^"]*"[^>]*>\s*</div>',
        '', content, flags=re.IGNORECASE)
    content = re.sub(
        r'<div[^>]*background-image:\s*url\([\'"]?http[^)]*cron[^)]*\)[\'"]?[^>]*>\s*</div>',
        '', content, flags=re.IGNORECASE)
    content = re.sub(
        r"<div[^>]*style=['\"][^'\"]*spip\.php\?action=cron[^'\"]*['\"][^>]*>\s*</div>",
        '', content, flags=re.IGNORECASE)

    # 1h. Remover imagem SPIP (logo do SPIP no rodapé)
    content = re.sub(
        r'<a[^>]*href="https?://www\.spip\.net/?"[^>]*>\s*<img[^>]*alt="SPIP"[^>]*/?>\s*</a>',
        '', content, flags=re.IGNORECASE)
    # Texto "SPIP" solto no rodapé
    content = re.sub(
        r'<a[^>]*href="https?://www\.spip\.net/?"[^>]*>\s*</a>\s*\|\s*',
        '', content, flags=re.IGNORECASE)

    # 1i. Remover qualquer form (não funcionam sem backend)
    # Manter a estrutura visual mas neutralizar
    def neutralize_form(m):
        form_html = m.group(0)
        # Trocar action por #
        form_html = re.sub(r'action="[^"]*"', 'action="#" onsubmit="return false;"', form_html)
        return form_html
    content = re.sub(r'<form[^>]*>.*?</form>', neutralize_form, content, flags=re.IGNORECASE | re.DOTALL)

    # 1j. Remover tags com spip_out (rel="external")
    content = re.sub(
        r'<a([^>]*)rel="external"([^>]*)>',
        r'<a\1\2>', content, flags=re.IGNORECASE)

    # 1k. Remover meta generator SPIP
    content = re.sub(
        r'<meta[^>]*name="generator"[^>]*content="SPIP[^"]*"[^>]*/?>',
        '', content, flags=re.IGNORECASE)

    # 1l. Remover link RSS do SPIP
    content = re.sub(
        r'<link[^>]*rel="alternate"[^>]*type="application/rss\+xml"[^>]*/?>',
        '', content, flags=re.IGNORECASE)

    # 1m. Limpar classes spip_* que não fazem mais sentido (opcional)
    # Manter pois o CSS ainda pode depender delas

    if content != original:
        f.write_text(content, encoding="utf-8")
        files_processed += 1
        total_changes += changes[0]
        print(f"  ✓ {f.name}: {changes[0]} alterações")

print(f"\n[HTML] {files_processed} arquivos modificados, {total_changes} mudanças")


# ========================================================================
# 2. PROCESSAR CSS/JS (remover referências externas)
# ========================================================================
print("\n" + "=" * 60)
print("Limpando CSS/JS...")
print("=" * 60)

url_re = re.compile(r'url\([\'"]?(https?://[^\'")]+)[\'"]?\)')
for f in list(SITE.rglob("*.css")) + list(SITE.rglob("*.js")):
    try:
        content = f.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    original = content
    def repl(m):
        url = m.group(1)
        new = clean_url(url)
        if new is None:
            return ""  # remove
        if new != url:
            return f'url({new})'
        return m.group(0)
    content = url_re.sub(repl, content)
    if content != original:
        f.write_text(content, encoding="utf-8")
        print(f"  ✓ {f.relative_to(SITE)}")


# ========================================================================
# 3. Verificação final
# ========================================================================
print("\n" + "=" * 60)
print("VERIFICAÇÃO FINAL")
print("=" * 60)

# 3a. Nenhuma referência externa a SPIP
spip_refs = []
href_re = re.compile(r'(?:href|src|action)="([^"]+)"', re.IGNORECASE)
for f in SITE.rglob("*.html"):
    try:
        content = f.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    for m in href_re.finditer(content):
        url = m.group(1)
        if "spip" in url.lower() or "spip.php" in url.lower():
            spip_refs.append((f.relative_to(SITE), url))
print(f"  Referências a SPIP/spip.php: {len(spip_refs)}")
for f, u in spip_refs[:5]:
    print(f"    {f}: {u}")

# 3b. Nenhuma referência a fandangoemcananeia.art.br (exceto RSS que aponta pro original)
fandango_refs = []
for f in SITE.rglob("*.html"):
    try:
        content = f.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    for m in href_re.finditer(content):
        url = m.group(1)
        if "fandangoemcananeia.art.br" in url:
            fandango_refs.append((f.relative_to(SITE), url))
print(f"  Referências a fandangoemcananeia.art.br: {len(fandango_refs)}")
for f, u in fandango_refs[:5]:
    print(f"    {f}: {u}")

# 3c. Contar links locais OK
ok = 0
total = 0
for f in SITE.rglob("*.html"):
    try:
        content = f.read_text(encoding="utf-8", errors="ignore")
    except:
        continue
    for m in href_re.finditer(content):
        url = m.group(1)
        if url.startswith(("http://", "https://", "data:", "javascript:", "mailto:", "#")):
            continue
        url = urllib.parse.unquote(url).split("?")[0].split("#")[0]
        if not url or url.startswith("//"):
            continue
        total += 1
        if (SITE / url).exists():
            ok += 1
print(f"  Links locais: {ok}/{total} OK")

# 3d. Tamanho total
size_mb = sum(f.stat().st_size for f in SITE.rglob('*') if f.is_file()) / (1024*1024)
print(f"  Tamanho total: {size_mb:.1f} MB")
print(f"  Arquivos: {sum(1 for _ in SITE.rglob('*') if _.is_file())}")

print("\n" + "=" * 60)
print("✅ Pronto para deploy!")
print("=" * 60)
print("""
Para publicar:
  1. Faça upload do conteúdo de `site/` para a raiz do seu servidor web
  2. Pronto! Acesse https://seudominio/ para ver o site

URLs disponíveis:
  /                      → página inicial
  /Puxirao.html          → Puxirão
  /Ze-Pereira.html       → página do Mestre Zé Pereira
  /Natureza-80.html      → artigo sobre Natureza
  /404.html              → página de erro customizada
  /local/                → imagens em cache
  /IMG/                  → imagens dos artigos
  /plugins/              → CSS/JS do tema
""")
