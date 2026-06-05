# Fandango em Cananéia — site estático

Versão estática (HTML + CSS + JS + imagens) do site
[https://www.fandangoemcananeia.art.br/](https://www.fandangoemcananeia.art.br/),
originalmente gerado pelo CMS **SPIP**.

Todo o conteúdo do site publicável está dentro de `site/`. Ao publicar, o
conteúdo de `site/` deve ir para a **raiz do servidor web** (DocumentRoot).

---

## 🚦 Estado atual (junho/2026)

| Item | Status |
|------|--------|
| Servidor | Dreamhost (Apache 2.4 + PHP 8.5 via FastCGI) |
| URLs | `.html` (sem clean URLs — ver nota abaixo) |
| Loop 301 | ✅ Resolvido |
| PHP | 8.5.5 |
| HTTPS | ✅ Forçado |
| Páginas HTML | 72 (incluindo `404.html`) |
| Tamanho total do site | ~245 MB |
| `sitemap.xml` | 70 URLs com `.html` + 1 homepage = 71 total |
| `phpinfo.php` (debug) | No servidor (remover quando não precisar mais) |
| Último deploy | `8a96099` (Plano D) + `475df28` (fix sitemap `ª`) |

> **Por que `.html` nas URLs?** O servidor Dreamhost tem uma config global
> (acima do `.htaccess`) que força trailing-slash em diretórios. Regras de
> rewrite no `.htaccess` para gerar URLs limpas (`/Cananeia/` em vez de
> `/Cananeia.html`) entravam em **loop infinito de 301**. A solução foi
> aceitar URLs com `.html` e servir os arquivos diretamente, sem rewrite.
> O site está 100% funcional.

---

## 📁 Estrutura do repositório

```
.
├── site/                  ← Conteúdo publicável (vai para a raiz do servidor)
│   ├── index.html
│   ├── *.html             ← 71 páginas HTML + 404.html (servidas direto)
│   ├── 404.html           ← Página de erro customizada (ErrorDocument)
│   ├── .htaccess          ← Config Apache (HTTPS, PHP 8.5, SPIP 301s, cache, gzip)
│   ├── sitemap.xml        ← 70 URLs internas com .html
│   ├── robots.txt         ← Crawlers
│   ├── IMG/               ← Imagens originais dos artigos (217 MB)
│   ├── local/             ← Imagens em cache geradas pelo SPIP (26 MB)
│   ├── plugins/           ← Tema e extensões (theme_californiumite, fancybox, etc.)
│   ├── lib/               ← Bibliotecas JS (jQuery, fancybox)
│   ├── extensions/        ← Extensões SPIP
│   ├── squelettes-dist/   ← Templates base
│   └── prive/             ← Arquivos do painel admin (não usado em estático)
├── scripts/               ← Scripts Python que geram/atualizam o site
│   ├── run_all.py         ← Roda todos os scripts em ordem
│   ├── 01-build_static.py ← Baixa todas as páginas e assets
│   ├── 02-cleanup.py      ← Limpa arquivos com nomes inválidos
│   ├── 03-fix_missing.py  ← Baixa imagens faltantes
│   ├── 04-final_fix.py    ← Corrige links finais
│   ├── 05-final_cleanup.py← Remove SPIP/CMS references
│   ├── 06-deploy_improvements.py ← HTTPS, lazy loading, sitemap, robots
│   └── 07-gen_docs.py     ← Regenera README.md e estrutura.md
├── reports/               ← Relatórios de teste de deploy (gerados)
├── README.md              ← Este arquivo
└── estrutura.md           ← Listagem completa de todas as páginas e assets
```

---

## 🌐 Estrutura de URLs

### URLs canônicas (servidas direto do sistema de arquivos)

```
https://www.fandangoemcananeia.art.br/                         → index.html
https://www.fandangoemcananeia.art.br/Cananeia.html            → Cananeia.html
https://www.fandangoemcananeia.art.br/Ze-Pereira.html          → Ze-Pereira.html
https://www.fandangoemcananeia.art.br/1ª-Festa-do-Fandango-Caicara-de.html
https://www.fandangoemcananeia.art.br/404.html                 → página de erro
```

### URLs com caractere especial

O arquivo `1ª-Festa-do-Fandango-Caicara-de.html` contém o caractere
`ª` (U+00AA). Funciona em ambos formatos:
- Literal: `/1ª-Festa-do-Fandango-Caicara-de.html`
- URL-encoded: `/1%C2%AA-Festa-do-Fandango-Caicara-de.html`

### URLs que retornam 404 (esperado)

- `/Cananeia/` (sem `.html`) → 404 (não há rewrite)
- `/Cananeia` (sem `.html` e sem `/`) → 404
- `/NaoExiste.html` → 404 (arquivo não existe)

### Redirects 301 mantidos (compatibilidade com SPIP antigo)

- `/spip.php` → `/`
- `/spip.php?page=login` → `/`
- `/spip.php?page=backend` → `/` (RSS removido)
- `/spip.php?action=cron` → `/`

---

## 🔄 Regenerar/atualizar o site estático

Para refazer tudo do zero (do site SPIP original):

```bash
python3.12 scripts/run_all.py
```

Ou rodar passo a passo:

```bash
python3.12 scripts/01-build_static.py   # Baixa páginas
python3.12 scripts/02-cleanup.py        # Limpa nomes
python3.12 scripts/03-fix_missing.py     # Baixa imagens faltantes
python3.12 scripts/04-final_fix.py       # Corrige links duplicados
python3.12 scripts/05-final_cleanup.py   # Remove SPIP/CMS
python3.12 scripts/06-deploy_improvements.py  # HTTPS, sitemap, robots, etc
python3.12 scripts/07-gen_docs.py        # Regenera docs
```

**Requisitos:** Python 3.12+ com `requests` e `beautifulsoup4` instalados.

```bash
pip install --user --break-system-packages requests beautifulsoup4 lxml
```

**Configurar a URL base:** o script `01-build_static.py` tem
`BASE_URL = "https://www.fandangoemcananeia.art.br"` no topo. Edite essa
linha se o site original mudar de endereço.

---

## ✅ Status final da conversão

| Item | Valor |
|------|-------|
| Páginas HTML | 72 (incluindo `404.html`) |
| Assets (CSS, JS, imagens, fontes) | 1076 únicos |
| Tamanho total do site | ~245 MB |
| Links internos verificados | 8962 / 8962 OK |
| Referências externas a `fandangoemcananeia.art.br` | 0 |
| Referências a `spip.php` (backend dinâmico) | 0 |
| Atributos `loading="lazy"` adicionados | 1399 |
| Arquivos do site | ~1800 |
| `.htaccess` | 93 linhas (HTTPS + PHP 8.5 + SPIP 301s + cache + gzip) |
| `sitemap.xml` | 70 URLs `.html` + 1 homepage = 71 total |
| `robots.txt` | ✓ |
| `404.html` customizado | ✓ (acessível, ErrorDocument funcional) |
| Formulários de contato/login | neutralizados |
| Menus, slideshow, fancybox, layout | preservados |
| PHP no servidor | 8.5.5 (handler `php85.cgi`) |
| Loop 301 em URLs | ✅ Resolvido |

---

## 🚀 Como publicar (deploy)

### Opção 1: Servidor Apache / Nginx (recomendado)

Faça upload do **conteúdo de `site/`** para a raiz do seu servidor web:

```bash
# Exemplo com rsync
rsync -avz --delete site/ usuario@servidor:/var/www/html/

# Ou com scp
scp -r site/* usuario@servidor:/var/www/html/
```

Aponte o domínio para esse diretório. Acesse `https://seudominio/` — site
funcionando.

### Opção 2: GitHub Pages

1. Crie um repositório no GitHub
2. Mova o conteúdo de `site/` para a raiz do repo (ou copie `site/*` para a raiz)
3. Ative GitHub Pages nas settings
4. Pronto — site disponível em `https://usuario.github.io/repo/`

### Opção 3: Netlify / Vercel / Cloudflare Pages

1. Crie conta na plataforma
2. Conecte o repositório ou faça drag-and-drop da pasta `site/`
3. Deploy automático — sem configuração adicional

### Opção 4: Servidor local (apenas para visualizar)

```bash
cd site
python3 -m http.server 8000
# Abre http://localhost:8000/ no navegador
```

### Opção 5: Deploy via Git (Dreamhost)

O servidor Dreamhost tem o repo clonado em `~/staticpage/`. O DocumentRoot
é `~/staticpage/site/`. Para atualizar:

```bash
# No servidor
cd ~/staticpage
git fetch origin
git reset --hard origin/main
```

> **Nota:** O push local → GitHub está com timeout DNS intermitente. Se o
> `git push` travar, aguardar e tentar de novo, ou usar o GitHub CLI
> (`gh repo sync`).

---

## 🔧 Adaptações realizadas na conversão SPIP → HTML estático

1. **URLs com `.html`**: SPIP usava URLs limpas sem extensão. Para funcionar
   como site estático em Dreamhost (que tem config global interferindo com
   rewrite), todos os links internos foram mantidos com `.html`.

2. **Slug `Natureza,80`**: O artigo 80 (sobre Natureza) foi salvo como
   `Natureza-80.html` para não conflitar com a página `Natureza` (seção
   História).

3. **Caractere `ª` preservado**: O arquivo
   `1ª-Festa-do-Fandango-Caicara-de.html` mantém o "ª" — funciona em
   qualquer servidor web moderno.

4. **Formulários neutralizados**: Form de contato e link "Conectar-se"
   convertidos para `action="#"` (dependiam do backend PHP do SPIP).

5. **Scripts SPIP removidos**: `spip.php?page=main-loading.js`,
   `spip.php?action=cron`, `spip.php?page=login`, `spip.php?page=plan`,
   `spip.php?page=backend` (RSS) — todos removidos ou redirecionados 301
   para `/`.

6. **Crédito SPIP removido**: Logo e link para spip.net no rodapé foram
   removidos.

7. **Páginas placeholder removidas**: `slider1`, `slider2`, `Nova-materia`,
   `icone` eram páginas vazias deixadas pelo SPIP.

8. **Paginação SPIP**: URLs tipo `Mestres?debut_articles=5#pagination_articles`
   convertidas para `Mestres.html`.

9. **Favicon**: Tag `<link rel="icon">` removida (favicon original está
   corrompido, 0 bytes).

10. **`.htaccess`**: 93 linhas com HTTPS force, PHP 8.5 handler, redirects
    301 do SPIP (compatibilidade), cache de assets, compressão gzip, headers
    de segurança, e ErrorDocument 404 → `/404.html`.

11. **`<base href="/">`**: Adicionado aos 72 HTMLs para garantir resolução
    correta de links relativos quando arquivos são movidos.

12. **`loading="lazy"`**: Adicionado em 1399 tags `<img>` para performance.

13. **Sitemap.xml**: 70 URLs internas com `.html` + 1 homepage.

---

## 📞 Contato / origem

- Site: [fandangoemcananeia.art.br](https://www.fandangoemcananeia.art.br/)
- Programa Puxirão: apoio ao Fandango Caiçara no Município de Cananéia
- SPIP CMS original: [spip.net](https://www.spip.net/)
- Repositório: [github.com/avena/fandangoemcananeia.art.br](https://github.com/avena/fandangoemcananeia.art.br)

---

## 📋 Histórico recente de commits

```
475df28 fix(sitemap): add missing ª character to 1ª Festa URL
8a96099 fix(htaccess,sitemap): drop clean URLs, accept .html
342bd91 fix(htaccess): disable MultiViews and DirectorySlash to fix 301 loop
a14907c refactor(deploy): automate base href injection and update rewrite rules
4a694ab feat: add Python scripts for static site generation
0677811 Add static site export and update documentation
```

> **Nota:** Em junho/2026, todos os commits foram reescritos
> (`git filter-branch`) para corrigir o autor: agora todos estão
> atribuídos a `Fernando Avena <fernando.avena@gmail.com>`.
