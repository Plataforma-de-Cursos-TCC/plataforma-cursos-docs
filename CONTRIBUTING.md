# Como contribuir

## Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
<tipo>(<escopo>): <assunto no imperativo>

<corpo explicando o porquê>
```

Tipos aceitos: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`. O escopo é opcional.

- Escreva a mensagem em inglês, no imperativo (`add`, não `added`).
- O corpo explica o porquê da mudança, não o que o diff já mostra.

## Branches

Nome no formato `<tipo>/<assunto>`, por exemplo `docs/uc020-catalog` ou `ci/commit-conventions`.

## Fluxo de uma tarefa

1. Na issue, use **Create a branch** (barra lateral, "Development"). A branch nasce da `main`, fica ligada à issue e o cartão vai para **In progress**.
2. Commit no padrão acima, sempre em branch; a `main` não aceita push direto.
3. Abra o PR pela branch com `Closes #<issue>` no corpo (o CI `issue-link` exige; PR sem issue usa o label `sem-issue`). Os outros integrantes entram como revisores pelo `CODEOWNERS` e o cartão vai para **In review**.
4. O CI (`checks`, `conventions` e `issue-link`) precisa passar e **outro integrante** precisa aprovar; o autor não aprova o próprio PR.
5. Merge por merge commit (único método liberado). A branch é apagada, a issue fecha e o cartão vai para **Done**.
6. Issue não fecha à mão: fechada como "completed" sem PR, ela é reaberta (vale a partir da #90; issue `tarefa-mae` e "not planned" ficam de fora).

## Pull requests

- O título segue o mesmo padrão dos commits (`docs: split overloaded use cases`).
- O corpo é escrito em português brasileiro.
- O CI valida o título do PR e a mensagem de cada commit. Se falhar, corrija antes de pedir revisão.

## Verificação local

Antes de abrir o PR, rode na raiz do repositório:

```
python3 scripts/build_doc.py --check
python3 scripts/render_prototypes.py --check
```

O primeiro valida a lista de itens do documento; o segundo valida a lista de capturas dos protótipos. Os dois só checam a configuração, não geram arquivos.
