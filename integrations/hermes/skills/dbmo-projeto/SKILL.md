---
name: dbmo-projeto
description: "Acompanha o projeto d-BMO: estado, roadmap, issues e PRs dos repos resende-g/d-BMO e resende-g/d-BMO-body, e a lista de compras do hardware. Só leitura por padrão."
version: 0.1.0
author: Gabriel Almeida Resende
license: Apache-2.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [d-BMO, GitHub, Projeto]
---

# d-BMO: acompanhamento do projeto

## Quando usar

Perguntas sobre o andamento do d-BMO ou do d-BMO-body: "como está o d-BMO", "o que falta no hardware", "tem PR aberto", "o que vem no roadmap", "o que falta comprar".

## Onde está cada coisa

| O quê | Onde |
|---|---|
| Assistente (docs, arquitetura, roadmap) | clone em `/Users/BMO`; `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md` |
| Hardware (firmware, BOM, carcaça) | clone em `~/d-BMO-body` |
| Arquivos fora do git (compras, imagens) | `/Users/BMO/_local/` |
| Issues e PRs | `gh issue list -R resende-g/d-BMO`, `gh pr list -R resende-g/d-BMO-body` |

## Procedimento

1. Atualize sem alterar nada: `git -C /Users/BMO fetch --quiet` e `git -C ~/d-BMO-body fetch --quiet`. Compare com `git status -sb`.
2. Leia só o necessário para a pergunta: o trecho relevante de `STATUS.md` ou `ROADMAP.md`, os últimos commits (`git log --oneline -10`) e as issues e PRs abertos.
3. Responda em poucas linhas: estado, próximo passo e o que depende do usuário. Cite arquivo ou número de issue/PR.

## Limites

- Só leitura. Criar issue, comentar, abrir PR, fazer commit ou push exige pedido explícito do usuário na conversa.
- `training_docs/` e `_local/` têm contexto pessoal: nunca copie esse conteúdo para issue, PR ou commit.
- Não reintroduza elementos visuais do BMO de *Hora de Aventura*; o personagem é próprio (ver `docs/brand/`).

## Verificação

Toda afirmação sobre estado aponta para um arquivo, commit, issue ou PR que você leu nesta sessão.
