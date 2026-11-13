---
description: Revisa a parte de um integrante (PRs, código, issues) contra as regras do projeto. Somente leitura.
argument-hint: "[integrante|todos] [prs|codigo|issues|tudo]"
---

Revise o trabalho no repositório `Plataforma-de-Cursos-TCC/plataforma-cursos-docs`. Argumentos: `$ARGUMENTS`.

## Interpretação dos argumentos

- 1º argumento (integrante): nome, primeiro nome ou login. Sem argumento ou `todos`: os quatro.
- 2º argumento (escopo): `prs`, `codigo`, `issues` ou `tudo` (padrão: `tudo`).
- Ordem livre: se o 1º argumento for um escopo, o integrante é `todos`.

| Integrante | Login | Área |
|---|---|---|
| Lucas Stopinski | LucasStop | A, acesso e conta |
| Adrian | adrian69-droid | B, autoria do instrutor |
| Lucas Bruno | Luc-Bruno | C, aprendizagem do aluno |
| Vinicius Teider | Teider011 | D, Tutor de IA, analytics e administração |

Neste repositório "código" é o documento: os arquivos da área em `especificacao/` (itens 6 a 15), os `.drawio` e PNGs em `especificacao/diagramas/` e os protótipos.

## Regras

- Somente leitura. Não edite arquivo, não comente, não aprove, não peça mudanças e não faça merge. Só relate.
- Leia antes: `CONTEXT.md`, `AGENTS.md`, `entregas/ra2-tarefas.md`, `entregas/ra2-analise-do-professor.md`, `entregas/ra2-criterios-de-aceite.md` e a ADR-0013.
- Decisões (`docs/adr/`) vencem pesquisa e rascunhos. Contradição com ADR é achado, nunca motivo para mudar a ADR.
- Cada achado leva `arquivo:linha` (ou `#issue`/`PR`), o que está errado, a regra violada e a correção sugerida. Sem achado, diga que conferiu e o que conferiu.

## Escopo `issues`

`gh issue list --assignee <login> --state all --limit 100` e `gh issue view N` em cada uma. Conferir: critérios de aceite claros, bloco "Atualização do fluxo" presente nas issues dos itens 12 a 15, branch `N-slug`, issue aberta com PR ligado ou fechada por PR, labels e projeto coerentes, pendências entre áreas registradas na issue `pendencia-cruzada` em vez de inventadas.

## Escopo `prs`

`gh pr list --author <login> --state all` e, para cada PR aberto, `gh pr view N`, `gh pr diff N` e `gh pr checks N`. Conferir: `Closes #N`, linha em `CHANGELOG.md` `[Não lançado]` com o número do PR (ou label `sem-changelog` justificado), CI (`checks`, `conventions`, `issue-link`, `changelog`), título e commits em Conventional Commits com escopo e corpo, diff restrito ao escopo da issue, status de revisão pendente.

## Escopo `codigo`

Arquivos da área do integrante, por item:

- Itens 6 a 8, 10: IDs finais (RF, US, RNF, UC), estória Como/Posso/Para com pelo menos 2 critérios DADO QUE/QUANDO/ENTÃO (D2), meta de 4 especificações por integrante (D1).
- Item 9 e 11: `extend` no sentido da UML (D3), Tutor de IA como ator sistêmico (D5), diagramas com fonte `.drawio` e PNG exportado (D4).
- Item 12: entidades e relações cobrem o que as funções da área persistem, ligadas às entidades da Área A (por exemplo `User`).
- Item 13: tipo do elemento em círculo (C, A, I, E) e estereótipo de papel, classes integradas às da Área A.
- Item 14: mensagens são métodos do item 13; cancelar e confirmar em `alt`, com o cancelamento encerrando o diagrama; padrão do `scripts/drawio-seqgen/`.
- Item 15: um cenário negativo por regra de negócio, estado anterior verificado como inalterado, IDs a partir de TC091 (Área A até TC090), sem ID repetido.
- Em todos: nomes exatos de atores e glossário, fonte citada por número de `pesquisa/fontes.md` ao usar dado de concorrente, [Fato] e [Inferência] separados, links relativos válidos, o PNG corresponde ao `.drawio`.
- Os pontos da análise do professor para os itens 12 a 15 não podem se repetir na área.

## Saída

1. Uma linha por integrante revisado: contagem de achados por gravidade (bloqueia, corrigir, sugestão).
2. Lista de achados agrupada por integrante e escopo.
3. Pendências cruzadas: o que uma área supõe de outra sem ter registrado.
4. Para `todos`: inconsistências entre áreas (nomes, IDs, regras, classes ou entidades duplicadas ou divergentes). A revisão cruzada final do projeto está na issue #135.
