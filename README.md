# Fandango em Cananéia — site estático local

Versão estática (HTML + CSS + JS + imagens) do site
[https://www.fandangoemcananeia.art.br/](https://www.fandangoemcananeia.art.br/),
originalmente gerado pelo CMS **SPIP**.

Todo o conteúdo do site publicável está dentro de `site/`. Ao publicar, o
conteúdo de `site/` deve ir para a **raiz do servidor web** (DocumentRoot).

---

## 📁 Estrutura do repositório

```
.
├── site/                  ← Conteúdo publicável (vai para a raiz do servidor)
│   ├── index.html
│   ├── *.html             ← 71 páginas HTML
│   ├── 404.html           ← Página de erro customizada
│   ├── .htaccess          ← Configuração Apache (cache, gzip, 404)
│   ├── IMG/               ← Imagens originais dos artigos (217 MB)
│   ├── local/             ← Imagens em cache geradas pelo SPIP (26 MB)
│   ├── plugins/           ← Tema e extensões (theme_californiumite, fancybox, etc.)
│   ├── lib/               ← Bibliotecas JS (jQuery, fancybox)
│   ├── extensions/        ← Extensões SPIP
│   ├── squelettes-dist/   ← Templates base
│   └── prive/             ← Arquivos do painel admin (não usado em estático)
├── README.md              ← Este arquivo
└── estrutura.md           ← Listagem completa de todas as páginas e assets
```

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

Aponte o domínio para esse diretório. Acesse `https://seudominio/` — site funcionando.

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

---

## ✅ O que foi feito na conversão SPIP → HTML estático

| Categoria | Estado |
|---|---|
| Páginas HTML baixadas | 71 |
| Assets (CSS, JS, imagens, fontes) | 1076 únicos |
| Tamanho total do site | 240 MB |
| Links internos verificados | 8962 / 8962 OK |
| Referências externas a `fandangoemcananeia.art.br` | 0 |
| Referências a `spip.php` (backend dinâmico) | 0 |
| Formulários de contato/login | neutralizados |
| Menus, slideshow, fancybox, layout | preservados |

---

## 🔧 Adaptações realizadas

1. **URLs reescritas**: `SPIP` usa URLs limpas tipo `/Nome-da-Pagina` (sem extensão).
   Para funcionar como site estático, todos os links internos foram reescritos
   para `/Nome-da-Pagina.html`.

2. **Slug `Natureza,80`**: O artigo 80 (sobre Natureza) foi salvo como
   `Natureza-80.html` para não conflitar com a página `Natureza` (que é a
   seção História, slug original do SPIP).

3. **Caracteres especiais preservados**: arquivos como
   `1ª-Festa-do-Fandango-Caicara-de.html` mantêm a cedilha e o "ª" — funciona
   em qualquer servidor web moderno.

4. **Formulários neutralizados**: O form de contato e o link "Conectar-se"
   foram removidos/convertidos para `action="#"` pois dependem do backend PHP
   do SPIP.

5. **Scripts SPIP removidos**: `spip.php?page=main-loading.js`,
   `spip.php?action=cron`, `spip.php?page=login`, `spip.php?page=plan`,
   `spip.php?page=backend` (RSS) — todos removidos.

6. **Crédito SPIP removido**: Logo e link para spip.net no rodapé foram
   removidos (opcional — pode recolocar se quiser dar crédito).

7. **Páginas placeholder removidas**: `slider1`, `slider2`, `Nova-materia`,
   `icone` eram páginas vazias deixadas pelo SPIP — não servem o site estático.

8. **Paginação SPIP**: URLs tipo `Mestres?debut_articles=5#pagination_articles`
   foram convertidas para `Mestres.html` (página principal).

9. **Favicon**: O favicon original no servidor está corrompido (0 bytes);
   a tag `<link rel="icon">` foi removida para evitar erro 404 no browser.

10. **`.htaccess` criado**: Configuração Apache com cache de assets (1 ano
    para imagens, 1 mês para CSS/JS), compressão gzip, e página 404
    customizada.

---

## 🌐 URLs disponíveis após deploy

| URL | Página |
|---|---|
| `/` | Início |
| `/Puxirao.html` | Puxirão |
| `/Equipe.html` | Equipe |
| `/Objetivos.html` | Objetivos |
| `/Parceiros.html` | Parceiros |
| `/Projeto.html` | Projeto |
| `/Cananeia.html` | Cananéia |
| `/Fandango.html` | Fandango |
| `/Mestres.html` | Fandangueiros |
| `/Grupos.html` | Grupos |
| `/Agenda.html` | Agenda |
| `/Na-Web.html` | Navegue |
| `/Natureza.html` | História (página de Cananéia) |
| `/Natureza-80.html` | Natureza (artigo) |
| `/Ze-Pereira.html` | Mestre Zé Pereira |
| `/1ª-Festa-do-Fandango-Caicara-de.html` | 1ª Festa (com caractere especial) |
| `/Musicas.html`, `/Filme.html`, `/article18.html`, `/Portal-Web.html` | Produtos sociais |
| `/404.html` | Erro 404 customizado |

A lista completa com 71 páginas está em `estrutura.md`.

---

## 📂 Onde está cada asset

- **Imagens dos artigos** → `IMG/jpg/`, `IMG/png/`
- **Imagens em miniatura (cache SPIP)** → `local/cache-vignettes/`, `local/cache-gd2/`
- **CSS do tema** → `plugins/auto/theme_californiumite/squelette_californiumite/css/`
- **Bibliotecas JS** (jQuery, fancybox, jcarousellite) → `lib/`, `plugins/auto/fancybox/`
- **Ícones de redes sociais** → `plugins/auto/theme_californiumite/squelette_californiumite/`

---

## 📝 Licença do conteúdo

O site original usa ícone Creative Commons no rodapé. O conteúdo
(textos, fotos, etc.) é provavelmente CC-BY ou similar. Verifique com
os autores do projeto antes de republicar.

---

## 🔄 Regenerar o site estático a partir do SPIP original

Os scripts que geraram esta versão estão em `/tmp/` (na máquina onde foi feito):

- `build_static.py` — script principal
- `cleanup.py`, `fix_missing.py`, `final_fix.py` — passes de limpeza
- `prepare_deploy.py`, `final_cleanup.py` — preparação para deploy
- `gen_docs.py` — gera `README.md` e `estrutura.md`

Para refazer do zero:

```bash
# 1. Baixar todas as páginas
python3.12 /tmp/build_static.py

# 2. Limpar nomes, duplicações
python3.12 /tmp/cleanup.py
python3.12 /tmp/fix_missing.py
python3.12 /tmp/final_fix.py

# 3. Limpar referências SPIP/CMS
python3.12 /tmp/final_cleanup.py

# 4. Regenerar documentação
python3.12 /tmp/gen_docs.py
```

---

## 📞 Contato / origem

- Site original: [fandangoemcananeia.art.br](https://www.fandangoemcananeia.art.br/)
- Programa Puxirão: apoio ao Fandango Caiçara no Município de Cananéia
- SPIP CMS original: [spip.net](https://www.spip.net/)
