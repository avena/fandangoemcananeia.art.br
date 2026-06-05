# Planos do projeto Fandango em Cananéia — site estático

Este diretório contém planos de feature, snapshots de ambiente e decisões
técnicas do projeto.

## Índice

| # | Arquivo | Status | Descrição |
|---|---------|--------|-----------|
| 01 | [01-clean-urls-php-router.md](01-clean-urls-php-router.md) | Rascunho | Plano para restaurar URLs limpas via PHP front controller |
| 02 | [02-php-8.5.5-environment.md](02-php-8.5.5-environment.md) | Completo (snapshot) | Ambiente PHP 8.5.5 do Dreamhost anotado |

## Convenção de nomenclatura

- `NN-titulo-curto.md` — onde `NN` é o número sequencial do plano
- Status possíveis: `Rascunho` / `Aprovado` / `Em execução` / `Concluído` / `Cancelado`

## Última atualização

2026-06-05 — Estrutura inicial criada na branch `php-router`.

## Como usar estes planos

1. Cada plano vive na **branch** onde a feature está sendo desenvolvida
2. São commitados junto com (ou antes de) o código da feature
3. Quando a feature é mergeada em `main`, o plano permanece no repo como histórico
4. Snapshots de ambiente (tipo `02-`) podem ser regenerados a qualquer momento (ver instruções no próprio arquivo)
