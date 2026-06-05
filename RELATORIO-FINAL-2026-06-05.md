# Relatório Final — Deploy Plano D (junho/2026)

**Data:** 2026-06-05  
**Projeto:** https://www.fandangoemcananeia.art.br/  
**Servidor:** Dreamhost (Apache 2.4 + PHP 8.5.5 via FastCGI)  
**Status final:** ✅ **Site 100% funcional em produção**

---

## 1. Resumo executivo

| Métrica | Valor |
|---------|-------|
| Páginas HTML publicadas | 72 (incluindo `404.html`) |
| Assets (CSS, JS, imagens, fontes) | 1076 únicos |
| Tamanho total do site | ~245 MB |
| Loop 301 | ✅ Resolvido |
| Tempo de resposta (homepage) | < 500ms |
| HTTPS | ✅ Forçado |
| `sitemap.xml` | 70 URLs + 1 homepage = 71 URLs |
| `robots.txt` | ✅ |
| `404.html` customizado | ✅ Acessível |
| PHP 8.5.5 (handler `FCGIWrapper "/dh/cgi-system/php85.cgi"`) | ✅ Ativo |
| `.htaccess` | 93 linhas (HTTPS, PHP 8.5, SPIP 301s, cache, gzip, security headers) |
| Total de commits (local) | 7 (todos reescritos com autor correto) |
| Total de commits (remote) | 6 (autor antigo `TODO <TODO>` — push da reescrita bloqueado por DNS) |

---

## 2. O que foi feito nesta sessão

### 2.1 Diagnóstico do loop 301 (Plano A — FALHOU)

**Hipótese inicial (Plano A):** Configurar `.htaccess` para reescrever URLs limpas → arquivo `.html`.

**Tentativa 1 (`Options -MultiViews -Indexes` + `DirectorySlash Off` + `RewriteBase /`):**
- 8/11 URLs testadas entraram em **loop infinito de 301** (`/Cananeia/`, `/Cananeia`, `/Ze-Pereira.html`, `/Ze-Pereira/`, etc.)
- Mesmo `/404.html` e `/NaoExiste.html` sofreram loop, quebrando o `ErrorDocument`
- Apenas 3 URLs funcionavam: `/`, `/sitemap.xml`, `/robots.txt`, `/phpinfo.php`
- **Causa raiz:** Dreamhost tem config global acima do `.htaccess` que força trailing-slash em diretórios, conflitando com rewrite rules

**Relatório:** `reports/deploy-test-20260605-084246.txt` (8 loops detectados)

### 2.2 Decisão: Plano D (sem clean URLs)

**Decisão:** Aceitar URLs com `.html` no caminho. Servir os arquivos diretamente, sem rewrite rules.

**Justificativa:** O ganho estético de URLs sem `.html` não compensa o custo de manter o site em produção com um loop que quebra navegação, sitemap, `ErrorDocument`, e SEO.

**Implementação (`commit 086ba3c` → `080369e`):**
- Removido "Bloco 2" (clean URL rewrites) do `.htaccess`
- Mantidos: PHP 8.5 handler, HTTPS force, SPIP 301s, cache, gzip, security headers
- URLs passam a ser servidas diretamente do filesystem: `Cananeia.html`, `Ze-Pereira.html`, etc.
- Sitemap atualizado para incluir `.html` em todas as 70 URLs internas

**Teste completo (Plano D) — TODOS OK:**

| URL | Status | Tamanho | Observação |
|-----|--------|---------|------------|
| `/` | 200 | 25127 B | Homepage |
| `/Cananeia.html` | 200 | 22984 B | Página principal |
| `/Ze-Pereira.html` | 200 | 20224 B | Perfil mestre |
| `/Natureza-80.html` | 200 | 26049 B | Slug com sufixo `-80` |
| `/Puxirao.html` | 200 | — | Seção Puxirão |
| `/Equipe.html` | 200 | — | Equipe |
| `/1ª-Festa-do-Fandango-Caicara-de.html` | 200 | — | Caractere `ª` preservado |
| `/Objetivos.html` | 200 | — | Objetivos Puxirão |
| `/Parceiros.html` | 200 | — | Parceiros |
| `/Projeto.html` | 200 | — | Projeto |
| `/Produtos-sociais.html` | 200 | — | Produtos sociais |
| `/Filme.html` | 200 | — | Filme |
| `/sitemap.xml` | 200 | 9534 B | 70 URLs + homepage |
| `/robots.txt` | 200 | — | Sitemap + Disallow |
| `/phpinfo.php` | 200 | 92570 B | PHP 8.5.5 confirmado |
| `/Cananeia/` | 404 | — | Sem `.html`, sem rewrite — esperado |
| `/NaoExiste.html` | 404 | 701 B | ErrorDocument funcional |
| `/PaginaInexistente.html` | 404 | — | ErrorDocument funcional |

**Relatório:** `reports/deploy-test-2-20260605-091957.txt` (todos os 18 endpoints OK)

### 2.3 Bug fix: caractere `ª` no sitemap

**Bug:** O sitemap gerado automaticamente pelo script `06-deploy_improvements.py` tinha URL-encoded `1%C2%AA` no `1ª-Festa-do-Fandango-Caicara-de.html`. O caractere literal `ª` é igualmente válido em ambos formatos, mas para legibilidade do XML e SEO, mantemos literal.

**Fix (`commit caf1fa8`):**
- Script `06-deploy_improvements.py` agora gera URL com `ª` literal (não URL-encode)
- Sitemap regenerado e deployado
- Teste confirma: `1ª-Festa-do-Fandango-Caicara-de.html` retorna 200 (25 KB) com `ª` literal

### 2.4 Reescrita do histórico Git (autor)

**Problema:** Os 6 commits originais tinham autor `TODO <TODO>` (placeholder do script de migração do SPIP).

**Solicitação do usuário:** "edita todos commit com meu username e email do git. os commits nao estao registrado que é o author from commit. edit past commits"

**Execução:**
```bash
git filter-branch -f --env-filter "
  export GIT_AUTHOR_NAME='Fernando Avena'
  export GIT_AUTHOR_EMAIL='fernando.avena@gmail.com'
  export GIT_COMMITTER_NAME='Fernando Avena'
  export GIT_COMMITTER_EMAIL='fernando.avena@gmail.com'
" -- --all
```

**Resultado local:** Todos os 6 commits agora têm autor `Fernando Avena <fernando.avena@gmail.com>`

**Resultado remote:** ❌ **Push bloqueado por timeout DNS** (ver seção 4)

### 2.5 Atualização da documentação

**`README.md` atualizado** (commit `093e151`):
- Removida menção a "Plano A" e clean URLs como tentativa principal
- Adicionada seção "Estado atual (junho/2026)" com Plano D
- Tabela de URLs canônicas com `.html`
- Lista de "URLs que retornam 404 (esperado)" para URLs sem `.html`
- Atualizado deploy guide para refletir `.htaccess` de 93 linhas (sem bloco 2)
- Adicionadas notas sobre o `phpinfo.php` (remover quando não precisar mais)
- Histórico de commits reescritos

**`estrutura.md` atualizado** (commit `093e151`):
- Header com data, total de páginas (72, incluindo `404.html`), servidor
- Tabela "Estado atual (junho/2026)" com Plano D
- Nova seção "URLs servidas pelo servidor" com mapeamento URL → arquivo
- Total de páginas atualizado: 71 → 72
- Mantida a árvore de páginas e o detalhamento por página

---

## 3. Histórico de commits (local)

```
093e151 docs: update README and estrutura for Plano D (.html URLs, PHP 8.5, no loop)  [Fernando Avena]
caf1fa8 fix(sitemap): add missing ª character to 1ª Festa URL                          [Fernando Avena]
080369e fix(htaccess,sitemap): drop clean URLs, accept .html                            [Fernando Avena]
086ba3c fix(htaccess): disable MultiViews and DirectorySlash to fix 301 loop            [Fernando Avena]
3d4f4a1 refactor(deploy): automate base href injection and update rewrite rules         [Fernando Avena]
596564b feat: add Python scripts for static site generation                             [Fernando Avena]
3b781e6 Add static site export and update documentation                                [Fernando Avena]
```

**Verificação do autor:**
```bash
$ git log -1 --format='%an <%ae>'
Fernando Avena <fernando.avena@gmail.com>
```

---

## 4. Pendência: push do histórico reescrito

### 4.1 Diagnóstico

A reescrita via `git filter-branch` mudou todos os SHAs dos 6 commits originais, criando **divergência** entre local e remote:

```
$ git status -sb
## main...origin/main [ahead 7, behind 6]
?? reports/
```

- **Local (ahead 7):** 7 commits que o remote não tem (6 reescritos + 1 novo de docs)
- **Remote (behind 6):** 6 commits originais com autor `TODO <TODO>` que o local não tem (porque filter-branch mudou os SHAs)

### 4.2 Tentativas de push executadas

| Tentativa | Método | Resultado |
|-----------|--------|-----------|
| 1 | `git push origin main` (regular) | ❌ Rejeitado: `non-fast-forward` (divergência) |
| 2 | `git push --force origin main` | ⏱️ Timeout (60s, 90s, 120s, 180s) |
| 3 | `GIT_PROXY_COMMAND` com `nc` para IP 140.82.121.4 | ⏱️ Timeout (60s, 90s) |
| 4 | `HOSTALIASES=/tmp/hosts-hack` com IP fixo | ✅ `git ls-remote` funciona, ❌ `git push` trava |
| 5 | `gh repo sync` | ❌ "error connecting to api.github.com" |
| 6 | DNS direto para github.com | ⏱️ Timeout (4 tentativas, 20s cada) |

### 4.3 Causa raiz

DNS para `github.com` está **com timeout consistente** neste ambiente (4+ tentativas em 5 minutos). DNS para `raw.githubusercontent.com` (que tem AAAA IPv6) funciona parcialmente, mas `github.com` e `api.github.com` (que dependem de IPv4) falham.

**Workaround parcial:** `curl --resolve "github.com:443:IP"` funciona (confirma que GitHub está acessível via IP), mas o libcurl do `git push` (que faz `git send-pack`) trava na negociação HTTPS, mesmo com `GIT_PROXY_COMMAND`.

### 4.4 Comando para push manual (quando rede normalizar)

```bash
cd /home/livre/fandangoemcananeia.art.br
git push --force origin main
```

OU, se o DNS continuar instável:

```bash
# Adicionar github.com ao /etc/hosts (precisa sudo)
echo "140.82.121.4 github.com" | sudo tee -a /etc/hosts
git push --force origin main
```

OU via `gh` CLI:

```bash
gh auth login  # se não autenticado
gh repo sync --force
```

### 4.5 Impacto

- ✅ **Site em produção**: 100% funcional (independe do push)
- ✅ **Repo local**: tem todos os commits com autor correto
- ⚠️ **Repo remote (GitHub)**: ainda mostra 6 commits com autor `TODO <TODO>`
- ⚠️ **Pull no servidor Dreamhost**: precisa de `git pull --ff-only` após o push manual

---

## 5. Status no servidor Dreamhost

O servidor já tem o Plano D deployado. Verificação ao vivo (via IP direto 67.205.7.12):

```bash
$ curl -s -o /dev/null -w "Status: %{http_code} | Size: %{size_download}\n" \
    --resolve "www.fandangoemcananeia.art.br:443:67.205.7.12" \
    "https://www.fandangoemcananeia.art.br/Cananeia.html"
Status: 200 | Size: 22984

$ curl -s -o /dev/null -w "Status: %{http_code} | Size: %{size_download}\n" \
    --resolve "www.fandangoemcananeia.art.br:443:67.205.7.12" \
    "https://www.fandangoemcananeia.art.br/NaoExiste.html"
Status: 404 | Size: 701
```

**Response headers observados:**
- `server: Apache`
- `x-frame-options: SAMEORIGIN`
- `x-content-type-options: nosniff`
- `cache-control: max-age=600`
- `content-type: text/html; charset=UTF-8`
- `date: Fri, 05 Jun 2026 14:04:43 GMT` (servidor respondendo)

---

## 6. Arquivos modificados nesta sessão

| Arquivo | Mudança | Commit |
|---------|---------|--------|
| `site/.htaccess` | Removido bloco 2 (clean URL rewrites) | `086ba3c` → `080369e` |
| `site/sitemap.xml` | URLs com `.html` + fix `ª` literal | `080369e` → `caf1fa8` |
| `scripts/06-deploy_improvements.py` | Gera sitemap com `.html` e `ª` literal | `caf1fa8` |
| `README.md` | Reescrito para refletir Plano D | `093e151` |
| `estrutura.md` | Header atualizado com Plano D, URLs | `093e151` |
| `reports/deploy-test-20260605-084246.txt` | Relatório de teste Plano A (8 loops) | novo |
| `reports/deploy-test-2-20260605-091957.txt` | Relatório de teste Plano D (18 OK) | novo |
| `RELATORIO-FINAL-2026-06-05.md` | Este relatório | novo |

**Histórico Git reescrito (autor):** 6 commits anteriores (de `TODO <TODO>` para `Fernando Avena <fernando.avena@gmail.com>`).

---

## 7. Próximas ações (para o usuário)

1. **Quando a rede normalizar**, fazer push manual:
   ```bash
   cd /home/livre/fandangoemcananeia.art.br
   git push --force origin main
   ```

2. **No servidor Dreamhost**, fazer pull:
   ```bash
   cd ~/staticpage
   git fetch origin
   git reset --hard origin/main
   ```

3. **Remover `phpinfo.php` do servidor** (deixar de commit ou adicionar ao `.gitignore`):
   ```bash
   rm -f ~/staticpage/site/phpinfo.php
   ```

4. **Opcional:** Adicionar `phpinfo.php` ao `.gitignore` para evitar commit acidental:
   ```bash
   echo "site/phpinfo.php" >> .gitignore
   echo "reports/" >> .gitignore
   git add .gitignore
   git commit -m "chore: ignore debug phpinfo and reports"
   ```

5. **Verificação final no navegador:**
   - https://www.fandangoemcananeia.art.br/ (homepage)
   - https://www.fandangoemcananeia.art.br/Cananeia.html (navegação interna)
   - https://www.fandangoemcananeia.art.br/sitemap.xml (sitemap)
   - https://www.fandangoemcananeia.art.br/NaoExiste.html (404 customizado)

---

## 8. Lições aprendidas

1. **Plano D (`.html` em URLs) foi a decisão certa**: tentar manter URLs limpas em ambiente shared hosting com config global é uma batalha perdida. `.html` é feio mas funciona.

2. **Diagnosticar antes de otimizar**: o teste com Plano A mostrou exatamente onde estava o loop (8 endpoints, incluindo `/404.html`), o que confirmou a causa raiz e justificou o Plano D.

3. **Teste em produção, não local**: o loop 301 só se manifestou no servidor real (Dreamhost), nunca em teste local. Por isso o usuário foi enfático em **parar de testar localmente**.

4. **DNS intermitente é esperado em ambientes compartilhados**: ter `git ls-remote` funcionando não garante que `git push` funcione. O send-pack do git usa libcurl que tem comportamento diferente do `getent`/resolver.

5. **`git filter-branch` para reescrever autor funciona localmente**, mas empurra o remote para um estado divergente que exige `--force`. O push fica bloqueado se a rede cair nesse momento crítico.

6. **Sites estáticos são resilientes**: uma vez deployado, não há banco de dados, não há PHP em runtime (exceto o `phpinfo.php` debug), não há cron jobs. O site é apenas HTML+CSS+JS+imagens, servido pelo Apache.

---

**Conclusão:** O site Fandango em Cananéia está **100% funcional** com a versão estática em produção. A única pendência é o push do histórico reescrito (autor correto) ao GitHub, que está bloqueado por problemas de DNS neste ambiente. O usuário pode fazer o push manual quando a rede normalizar.
