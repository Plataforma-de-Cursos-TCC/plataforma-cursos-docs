---
id: adr-0008
titulo: "ADR-0008 — Sessão com JWT em cookie HttpOnly e opção «manter conectado»"
tipo: decisao
decisao: D8
status: aceita
data: 2026-10-09
decisor: Grupo
itens_template: [5, 11]
areas: [A]
relacionados: [adr-0007, adr-0010]
---
# ADR-0008 — Sessão com JWT em cookie HttpOnly e opção «manter conectado»

- **Status:** aceita · **Data:** 09/10/2026 · **Decisor:** Grupo

## Contexto

- O RNF001 e o UC005 fixam a expiração do token de acesso em 1 hora. O UC005 também prevê a opção «manter conectado».
- O front-end é uma SPA em Next.js e a API é Laravel 13. Guardar o JWT em `localStorage` ou `sessionStorage` o deixa legível por qualquer script injetado (XSS).
- Uma sessão de 1 hora sem renovação obrigaria o aluno a reautenticar no meio de uma aula. A opção «manter conectado» precisa de um mecanismo de renovação que não amplie o tempo de vida do token de acesso.
- O logout e o bloqueio de conta (UC008, UC018) precisam invalidar o token antes da expiração. O ADR-0007 já prevê o Redis para a lista de tokens revogados.
- Detalhes, comparações e fontes estão em [sessao-e-listagens.md](../pesquisas/sessao-e-listagens.md).

## Opções consideradas

- **JWT em `localStorage`:** descartado. Exposto a XSS e contrário ao que o SDD e o TDD já descrevem.
- **Sessão com estado no servidor (cookie de sessão do Laravel):** descartado. Reintroduz estado no servidor web e não serve ao `ai-service` e ao `media-service`, que validam o token de forma independente com a chave pública.
- **JWT longo (dias) em cookie, sem refresh:** descartado. Amplia a janela de uso de um token roubado e contradiz o RNF001.
- **JWT de 1 hora em cookie `HttpOnly` mais refresh token opaco rotacionado:** escolhida.

## Decisão

1. O token de acesso é um JWT assinado com RS256 (chave privada só no core Laravel; os microsserviços validam com a chave pública), usando a biblioteca `php-open-source-saver/jwt-auth` (compatível com Laravel 13, ver pesquisa), com expiração de 1 hora, entregue em cookie `HttpOnly`, `Secure` e `SameSite=Strict` (nome `__Host-access`, `Path=/`). O front-end nunca lê nem grava o token.
2. O login recebe o campo booleano `rememberMe`. Com `rememberMe` verdadeiro, a API também emite um refresh token opaco, aleatório, guardado apenas como hash em tabela própria (`sessoes_refresh`), em cookie `HttpOnly` `__Host-refresh` com `Path=/api/v1/auth/refresh` e validade de 30 dias. Sem `rememberMe`, não há refresh token e o usuário reautentica ao expirar a hora.
3. `POST /api/v1/auth/refresh` troca o refresh token por um novo par de cookies e invalida o anterior (rotação). O uso de um refresh token já consumido revoga toda a família de tokens da sessão.
4. `GET /api/v1/auth/me` devolve o usuário autenticado para o front-end restaurar a sessão no carregamento da página.
5. O logout e o bloqueio ou exclusão de conta registram o `jti` do token de acesso em uma blocklist no Redis, com TTL igual ao tempo restante do token, e revogam a família de refresh tokens.
6. Proteção contra CSRF: `SameSite=Strict`, verificação do cabeçalho `Origin` nas rotas que alteram estado e, onde a pesquisa indicar, token de dupla submissão. O CORS usa `supports_credentials` com origem exata, nunca curinga.
7. A SPA e a API ficam no mesmo host: a Vercel encaminha `/api/*` ao Railway por `rewrite` ([ADR-0010](0010-hospedagem-e-armazenamento.md)), o que mantém `__Host-` e `SameSite=Strict`.

## Consequências

- **Mais seguro contra XSS:** o JavaScript da aplicação não alcança o token.
- **RNF001 preservado:** a expiração do token de acesso continua em 1 hora. «Manter conectado» é um complemento de sessão e não cria requisito novo.
- **Novo estado no servidor:** a tabela `sessoes_refresh` e a blocklist no Redis precisam existir; o Redis passa a ser dependência do logout imediato, e não apenas da Sprint 2.
- **Trabalho de implementação:** o front-end renova a sessão ao receber 401, repetindo a requisição uma vez; a configuração RS256 da biblioteca e o repasse de `Set-Cookie` pelo `rewrite` precisam de teste antes da implementação; a rotação de chaves não tem suporte documentado.
- **Pontos a confirmar na implementação:** domínio de hospedagem (pendente) e, se o grupo preferir, um TTL de acesso menor que 1 hora (exigiria alterar o RNF001).

---

## Ligações

- **Pesquisa:** [sessao-e-listagens.md](../pesquisas/sessao-e-listagens.md) · [hospedagem-e-jwt.md](../pesquisas/hospedagem-e-jwt.md)
- **TDD (autenticação):** [tdd.md](../tdd.md) · **SDD:** [sdd.md](../sdd.md)
- **Stack:** [ADR-0007](0007-stack-e-bancos.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
