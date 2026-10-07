---
id: adr-0005
titulo: "ADR-0005 — Tutor de IA como ator sistêmico"
tipo: decisao
decisao: D5
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [2, 5, 6, 9, 10]
areas: [D]
relacionados: [adr-0006]
---
# ADR-0005 — Tutor de IA como ator sistêmico

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- O Tutor de IA responde dúvidas do Aluno no contexto da aula. A resposta vem de um modelo de linguagem externo à plataforma.
- Era preciso decidir se o Tutor aparece nos diagramas como ator, como parte do sistema ou não aparece.

## Opções consideradas

- **(a)** Tutor como funcionalidade interna, sem ator.
- **(b)** Tutor como **ator sistêmico** (secundário), que participa dos casos de uso iniciados pelo Aluno.
- **(c)** Modelo de linguagem externo como ator, e o Tutor como funcionalidade.

## Decisão

**(b)**. O Tutor de IA é um ator sistêmico: não inicia casos de uso por conta própria; participa de "Conversar com Tutor de IA", que o Aluno inicia. O provedor do modelo de linguagem fica atrás do Tutor e não aparece como ator.

## Consequências

- O diagrama geral (item 9) mostra o Tutor de IA como ator secundário ligado a "Conversar com Tutor de IA".
- RNFs de tempo de resposta, disponibilidade e privacidade do Tutor ficam na área D.
- A especificação do caso de uso trata a indisponibilidade do Tutor como fluxo alternativo.

---

## Ligações

- **Itens da especificação:** itens 2, 5, 6, 9 e 10 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D6](0006-divisao-por-areas.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
