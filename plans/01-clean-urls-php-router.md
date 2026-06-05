# Plano 01: Clean URLs via PHP Front Controller

**Status:** Rascunho
**Branch:** `php-router`
**Autor:** Fernando Avena \<fernando.avena@gmail.com\>
**Criado em:** 2026-06-05

---

## Contexto

- **Site original:** SPIP CMS com URLs limpas (sem extensão), ex: `/Cananeia`
- **Conversão para estático:** 72 HTMLs em `site/`
- **Tentativa inicial (Plano A — falhou):** rewrite `.htaccess` para URLs limpas → 8/11 URLs em **loop infinito de 301** por `mod_dir` global do Dreamhost
- **Plano D (atual em produção):** aceita `.html` em URLs (commit `cad83b2`, deploy OK desde 2026-06-05)
- **Próxima tentativa (este plano):** PHP como front controller para contornar o `mod_dir` global

## Objetivo

Restaurar URLs limpas (estilo SPIP original) usando PHP como front controller, contornando o `mod_dir` global do Dreamhost. Atingir:

- `/Cananeia` → 200 (servido por `router.php`)
- `/Cananeia.html` → 200 direto (Variante B) **OU** 301 → `/Cananeia` (Variante A)
- `/NaoExiste` → 404 com página customizada
- `/sitemap.xml` → 200 (servido direto pelo Apache, bypassa router)

---

## Hipótese técnica

URLs **sem barra trailing** (`/Cananeia`, sem `/`) **NÃO ativam `mod_dir`**. O `mod_dir` do Dreamhost só dispara quando:

1. A URL termina em `/`
2. **E** não existe diretório físico correspondente
3. Aí ele gera um 301 extra (que causou o loop no Plano A)

PHP como front controller serve o `.html` correspondente quando recebe `/Cananeia`. Com `cgi.fix_pathinfo=0` no `.htaccess`, evita-se execução de código malicioso via PATH_INFO (que está `On` no servidor por padrão — ver `plans/02-`).

---

## Análise: prós e contras da abordagem

### ✅ Pontos fortes

**1. Resolve o problema raiz sem brigar com o Dreamhost**
O loop 301 do `mod_dir` global é uma decisão de arquitetura do provedor. Não há como sobrescrever config acima do `.htaccess` em shared hosting. PHP como front controller **contorna** o problema em vez de lutar contra ele. Limpo.

**2. PHP já está lá, e bem configurado**
- PHP 8.5.5 (recente, May 2026 build)
- CGI/FastCGI ativo
- OPcache habilitado (32MB, 3907 arquivos)
- A penalidade de performance é **mínima** porque o script será cacheado em bytecodes após a primeira execução

**3. Código pequeno, attack-surface pequeno**
~30 linhas de router, ~80 linhas de script de migração. Fácil de auditar, fácil de reverter. Comparado com Plano A (rewrite rules que tentam reescrever o filesystem), o router PHP é **mais legível e mais debugável**.

**4. Headers de cache preservados**
O `.htaccess` seta `max-age=600` para `.html` via FilesMatch, mas se o PHP serve via router, o Apache não aplica essa regra. **Solução:** o router seta manualmente. Bem documentado, sem mágica.

**5. Custom 404 sem gambiarra**
O `ErrorDocument 404` do `.htaccess` é limitado (não vê cookies, headers, etc). O router pode servir `404.html` com status correto e potencialmente fazer logging melhor no futuro.

**6. Extensibilidade futura**
Se um dia quiser adicionar analytics, compressão condicional, headers de segurança extras, A/B testing, geolocation... o router é o lugar natural. Sem isso, teria que mexer em 72 HTMLs.

### ⚠️ Pontos fracos

**1. PHP em todo request = overhead vs estático puro**
Mesmo com OPcache, o ciclo `getenv → readfile → exit` em PHP-FastCGI é da ordem de **1-3ms por request** vs **0.1ms** do Apache servindo estático. Para um site de museu/comunidade com centenas de visitas/dia, é **irrelevante**. Para 100k req/s, seria problema. Não é nosso caso.

**2. Dois caminhos para o mesmo recurso**
`Cananeia.html` (servido pelo Apache) e `Cananeia` (servido pelo router) — são **duas URLs para o mesmo conteúdo**. SEO vai consolidar (com canonical), mas é uma decisão arquitetural que precisa ser consciente. Por isso a decisão "Variante A vs B" é importante.

**3. Hardening obrigatório: `cgi.fix_pathinfo`**
O servidor tem `cgi.fix_pathinfo=On`. Isso é uma **porta aberta** para execução de código malicioso via PATH_INFO tipo `/router.php/etc/passwd`. Mitigação: `php_flag cgi.fix_pathinfo 0` no `.htaccess`. **Crítico, não pode esquecer.**

**4. Ponto único de falha**
Se o `router.php` tiver um erro de sintaxe ou permissão negada, **todas as URLs limpas quebram de uma vez**. Com Plano D, isso não acontece (cada `.html` é independente). Mitigação: testes rigorosos antes de merge + logs no servidor.

**5. Mod_dir pode voltar a morder**
O `.htaccess` precisa ser **cirúrgico**: garantir que `/Cananeia/` (com barra) também não dispare mod_dir. Vai precisar de uma regra explícita para canonalizar sem trailing slash.

**6. Fuzzing necessário**
Bots, scanners, browser pre-fetchers podem enviar paths estranhos. O sanitize com `mb_ereg_replace` + `realpath` + `str_starts_with` mitiga, mas vale teste de fuzzing com payloads tipo `../`, `%2e%2e`, null bytes.

### 🎯 Quando essa ideia é **ideal**

- ✅ Sites estáticos pequenos/médios (até 100 páginas)
- ✅ Shared hosting com restrições (nosso caso)
- ✅ Quando o usuário não pode mudar config do Apache
- ✅ Quando clean URLs são importantes para SEO/UX
- ✅ Quando o time aceita manter 1 arquivo PHP simples

### ❌ Quando **NÃO** fazer

- Sites com 10k+ páginas (router vira gargalo)
- Quando tem controle total do Apache (use rewrite puro)
- Quando pode usar Cloudflare/CDN que reescreve URLs na borda
- Quando quer serverless puro (substituir por Hugo + GitHub Pages)

### 📊 Comparação rápida com Plano D (status quo)

| Aspecto | Plano D (atual) | Plano E (router PHP) |
|---------|-----------------|----------------------|
| URLs | `/Cananeia.html` | `/Cananeia` |
| Round-trips por clique | 1 | 1 (Variante B) ou 2 (Variante A) |
| Performance | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ (com OPcache) |
| Complexidade | Baixa | Média (router + hardening) |
| Risco de loop 301 | Zero | Baixo (com testes) |
| Risco de segurança | N/A | Médio (precisa hardening) |
| Compatibilidade com HTML5 | ✅ | ✅ |
| SEO | Bom | Bom (Variante B) ou Neutro (Variante A) |
| Rollback | Trivial | Trivial (git revert) |
| **Recomendação** | Já em produção | Vale tentar em branch |

---

## Arquitetura proposta

### Fluxo de cada request

| URL | Atendido por | Status |
|-----|--------------|--------|
| `/` | `index.html` (DirectoryIndex) | 200 |
| `/Cananeia` | `router.php` serve `Cananeia.html` | 200 |
| `/Cananeia.html` | Apache serve direto (VARIANTE B) | 200 |
| `/NaoExiste` | `router.php` serve `404.html` | 404 |
| `/sitemap.xml` | Apache serve direto | 200 |
| `/robots.txt` | Apache serve direto | 200 |
| `/phpinfo.php` | Apache serve direto | 200 (debug) |
| `/Cananeia/` (com barra) | Rewrite canonaliza → `/Cananeia` | 301 → 200 |

---

## Componentes

### 1. `site/router.php` (NOVO, ~35 linhas)

PHP front controller com:
- Hardening contra `cgi.fix_pathinfo=On`
- Validação de método HTTP (só GET/HEAD)
- Sanitização com `mb_ereg_replace` (UTF-8-safe)
- Path resolution com `realpath` + prefix check (anti directory traversal)
- Cache headers preservados

```php
<?php
declare(strict_types=1);

// 1. Hardening para cgi.fix_pathinfo=On no servidor
if (isset($_SERVER['PATH_INFO']) && $_SERVER['PATH_INFO'] !== '') {
    http_response_code(404);
    exit;
}

// 2. Validar método HTTP (apenas GET/HEAD)
if (!in_array($_SERVER['REQUEST_METHOD'], ['GET', 'HEAD'], true)) {
    http_response_code(405);
    header('Allow: GET, HEAD');
    exit;
}

// 3. Pegar parâmetro page
$page = $_GET['page'] ?? '';

// 4. Sanitização usando mbstring (mais seguro que preg_replace puro)
$page = mb_ereg_replace('[^a-zA-Z0-9\-_ªº]', '', $page);
$page = mb_substr($page, 0, 200);

if (empty($page)) {
    http_response_code(404);
    readfile(__DIR__ . '/404.html');
    exit;
}

// 5. Path resolution com realpath (prevenir directory traversal)
$file = realpath(__DIR__ . '/' . $page . '.html');

if ($file === false || !str_starts_with($file, __DIR__ . '/') || !is_file($file)) {
    http_response_code(404);
    readfile(__DIR__ . '/404.html');
    exit;
}

// 6. Servir o arquivo com headers corretos
$stat = stat($file);
header('Content-Type: text/html; charset=UTF-8');
header('Cache-Control: max-age=600, public');
header('Content-Length: ' . $stat['size']);
header('X-Content-Type-Options: nosniff');
http_response_code(200);

if ($_SERVER['REQUEST_METHOD'] === 'HEAD') {
    exit;
}
readfile($file);
exit;
```

### 2. `site/.htaccess` Bloco 2 (EDITAR)

Adicionar antes do `<IfModule mod_rewrite.c>`:

```apache
# Desabilitar cgi.fix_pathinfo (segurança contra PATH_INFO attack)
<IfModule mod_php.c>
    php_flag cgi.fix_pathinfo 0
</IfModule>
```

Substituir Bloco 2 (Clean URLs) por:

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /

    # /index.html → /  (canonical homepage)
    RewriteRule ^index\.html$ / [R=301,L]

    # Servir arquivos reais diretamente (xml, txt, php, css, js, imagens, .html)
    RewriteCond %{REQUEST_FILENAME} -f [OR]
    RewriteCond %{REQUEST_FILENAME} -d
    RewriteRule ^ - [L]

    # /Nome/ (com barra trailing) → /Nome (canonalizar para evitar mod_dir)
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule ^(.*)/$ /$1 [R=301,L]

    # /Nome (sem extensão) → router.php serve o .html
    RewriteCond %{REQUEST_URI} !\.
    RewriteRule ^([^/]+)/?$ /router.php?page=$1 [L,QSA]
</IfModule>
```

**Nota:** Não há redirect 301 de `.html` → limpa na Variante B. Os arquivos `.html` são servidos diretamente. A Variante B assume que os links internos dos HTMLs foram atualizados.

### 3. `site/sitemap.xml` (REGENERAR)

URLs **sem `.html`**:

```xml
<url>
  <loc>https://www.fandangoemcananeia.art.br/Cananeia</loc>
  ...
</url>
```

Total: 71 URLs (70 internas + 1 homepage). Caractere `ª` mantido literal (não URL-encode).

### 4. `scripts/08-update_internal_links.py` (NOVO, ~80 linhas)

```python
#!/usr/bin/env python3
"""
Atualiza todos os links internos nos HTMLs de X.html para X.
Preserva links externos (http://, https://, //cdn...).
Aplica apenas em <a href="...">, não em <link>, <script>, <img>.
"""
import re
from pathlib import Path

SITE_DIR = Path(__file__).parent.parent / "site"

# Regex: captura href="..." onde conteúdo NÃO começa com http://, https://, //
# e termina com .html
INTERNAL_HTML_LINK = re.compile(
    r'href="((?!https?://|//|mailto:|tel:|#|data:)[^"]*?)\.html"',
    re.IGNORECASE
)

def update_html(path: Path) -> int:
    """Retorna número de links atualizados."""
    content = path.read_text(encoding='utf-8')
    new_content, n = INTERNAL_HTML_LINK.subn(r'href="\1"', content)
    if n > 0:
        path.write_text(new_content, encoding='utf-8')
    return n

def main():
    total = 0
    for html in SITE_DIR.glob('*.html'):
        n = update_html(html)
        if n > 0:
            print(f"  {html.name}: {n} links")
            total += n
    print(f"\nTotal: {total} links atualizados em {len(list(SITE_DIR.glob('*.html')))} arquivos")

if __name__ == '__main__':
    main()
```

---

## Variante A vs B (decisão recomendada: **B**)

| Aspecto | Variante A (com 301) | Variante B (sem 301) ⭐ |
|---------|----------------------|--------------------------|
| `/Cananeia.html` → | 301 → `/Cananeia` → 200 | 200 (direto) |
| `/Cananeia` → | 200 (router) | 200 (router) |
| Performance | 2 round-trips para `.html` | 1 round-trip |
| Trabalho extra | Só .htaccess + router | + atualizar 8962 links |
| Risco SEO | Neutro (301 preserva PageRank) | Ligeiramente melhor |
| Risco de bug | Baixo (padrão web) | Médio (regex precisa cobrir tudo) |

**Recomendação:** Variante B — script `08-update_internal_links.py` faz a atualização 1 vez. Site mais rápido e limpo.

---

## Riscos identificados e mitigações

| Risco | Mitigação |
|-------|-----------|
| Sanitização incompleta (caracteres faltando) | `mb_ereg_replace` cobre multibyte UTF-8 |
| Directory traversal | `realpath()` + `str_starts_with($file, __DIR__)` |
| `cgi.fix_pathinfo=On` no servidor | `php_flag cgi.fix_pathinfo 0` no `.htaccess` |
| `mod_dir` interferir com `/Nome/` | Rewrite canonaliza para `/Nome` (sem barra) |
| Cache headers sumirem | `router.php` seta `Cache-Control: max-age=600` |
| ErrorDocument 404 não disparar | `router.php` serve `404.html` diretamente |
| OPcache cachear versão antiga | OK, `revalidate_freq=2` no servidor detecta |
| Bot faz fuzzing | Sanitização + realpath + método HTTP restrito |

---

## Caracteres especiais nos filenames

Após análise, o único caractere especial conhecido é `ª` em `1ª-Festa-do-Fandango-Caicara-de.html`. Regex `[^a-zA-Z0-9\-_ªº]` cobre.

**Verificação pendente:** listar todos os `.html` em `site/` antes de implementar para confirmar.

---

## Plano de teste (no servidor, não local)

| # | Request | Esperado | Verificar |
|---|---------|----------|-----------|
| 1 | `GET /` | 200 | `index.html` servido |
| 2 | `GET /Cananeia` | 200 | router serve `Cananeia.html` |
| 3 | `GET /Cananeia.html` | 200 | Apache serve direto (Variante B) |
| 4 | `GET /Ze-Pereira` | 200 | router serve `Ze-Pereira.html` |
| 5 | `GET /1ª-Festa-do-Fandango-Caicara-de` | 200 | router serve `1ª-Festa-...html` (caractere `ª`) |
| 6 | `GET /1ª-Festa-do-Fandango-Caicara-de.html` | 200 | Apache serve direto |
| 7 | `GET /Natureza-80` | 200 | router serve `Natureza-80.html` |
| 8 | `GET /NaoExiste` | 404 | router serve `404.html` |
| 9 | `GET /NaoExiste.html` | 404 | Apache serve direto (arquivo não existe) |
| 10 | `GET /sitemap.xml` | 200 | Apache serve direto |
| 11 | `GET /robots.txt` | 200 | Apache serve direto |
| 12 | `GET /phpinfo.php` | 200 | Apache serve direto (debug) |
| 13 | `GET /Cananeia/` (com barra) | 301 → `/Cananeia` | Rewrite canonaliza |
| 14 | `GET /CANANEIA` (uppercase) | 404 | Linux é case-sensitive |
| 15 | `HEAD /Cananeia` | 200 | Sem body, com headers |
| 16 | `POST /Cananeia` | 405 | Método não permitido |
| 17 | `GET /router.php/etc/passwd` | 404 | PATH_INFO bloqueado |
| 18 | `GET /../etc/passwd` | 404 | Directory traversal bloqueado |
| 19 | `GET /Cananeia?foo=bar` | 200 | Query string preservada |

**Critério de aceite:**
- 0 loops 301
- 0 erros PHP (warnings, notices)
- 0 status inesperado
- Cache headers idênticos ao Plano D

---

## Critérios de pronto

- [ ] Branch `php-router` criada ✅ (já criada)
- [ ] `router.php` criado e commitado
- [ ] `.htaccess` Bloco 2 revisado e commitado
- [ ] `cgi.fix_pathinfo=0` setado no `.htaccess`
- [ ] `scripts/08-update_internal_links.py` criado e executado (8962 links)
- [ ] Sitemap regenerado (URLs sem `.html`)
- [ ] 19 endpoints testados em produção (0 falhas)
- [ ] Caractere `ª` testado
- [ ] Fuzzing básico testado (PATH_INFO, directory traversal)
- [ ] Branch mergeada em `main` com force-push
- [ ] Servidor Dreamhost com Plano E deployed
- [ ] `README.md` e `RELATORIO-FINAL-2026-06-05.md` atualizados

---

## Fallback (rollback)

Se Plano E falhar em qualquer teste:

```bash
git checkout main
git branch -D php-router
# Site continua com Plano D (.html nas URLs) - commit cad83b2
```

**Rollback é trivial** porque Plano D já está em produção e estável.

---

## Próximos passos (sequência)

1. ✅ Criar branch `php-router` (FEITO)
2. ✅ Criar pasta `plans/` e documentação (FEITO — este arquivo)
3. Listar todos os filenames `.html` para validar regex
4. Criar `site/router.php`
5. Editar `site/.htaccess` Bloco 2
6. Criar e executar `scripts/08-update_internal_links.py`
7. Regenerar `site/sitemap.xml`
8. Deploy no servidor (push + SSH pull OU rsync)
9. Testar 19 endpoints via `curl --resolve`
10. Se OK: merge em `main` + force-push
11. Se falhar: rollback (Plano D continua)
