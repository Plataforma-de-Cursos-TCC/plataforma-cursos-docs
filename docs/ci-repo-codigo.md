# CI do repositório de código (proposta)

Pipeline planejado para o futuro repositório de código. Este documento não cria workflow; o arquivo real será escrito quando o repositório existir.

## Stack

- Backend: Laravel 13, PHP 8.3, Pest para testes e Pint para formatação.
- Frontend: Next.js com TypeScript, ESLint, Vitest e Playwright.
- Banco: MySQL 8, como service container no job de testes.

## Jobs

| Job | Conteúdo |
| --- | --- |
| `lint` | `vendor/bin/pint --test` e `npx eslint .` |
| `test` | `php artisan test --coverage --min=75` (Pest, com PCOV) e `npx vitest run` |
| `build` | `npm run build` do Next.js e `php artisan optimize` |
| `conventions` | Mesmo job do repositório de docs: título do PR via `amannn/action-semantic-pull-request@v5` e mensagens de commit por regex |

## Gatilho e serviços

- `pull_request` para `main`: roda os quatro jobs.
- `test` sobe `mysql:8` como service, com porta 3306 e banco efêmero.
- Nenhum segredo é necessário nos jobs de PR.

## Versões

- Actions fixadas por SHA de commit, com o tag em comentário.
- `setup-php` com `php-version: "8.3"` e extensão `pcov`.
- `setup-node` na versão LTS que o Next.js suportar.

## Pendências

- Definir o limite de cobertura de 75% com a equipe depois da primeira medição.
