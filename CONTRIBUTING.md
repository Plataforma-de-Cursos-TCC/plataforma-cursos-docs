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
