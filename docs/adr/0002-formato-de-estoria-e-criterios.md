---
id: adr-0002
titulo: "ADR-0002 — Estória em Como / Posso / Para, com pelo menos 2 critérios"
tipo: decisao
decisao: D2
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [7]
areas: [A, B, C, D]
relacionados: [adr-0001]
---
# ADR-0002 — Estória em Como / Posso / Para, com pelo menos 2 critérios

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- O item 7 pede uma estória por RF, com critérios de aceite verificáveis.
- Cada integrante escreve as suas estórias; sem um formato fixo, o documento final sai com quatro estilos diferentes.

## Opções consideradas

- **(a)** Formato livre.
- **(b)** "Como / Quero / Para que" (Connextra).
- **(c)** **"Como / Posso / Para"**, o formato usado nas versões anteriores do documento, com critérios em **DADO QUE / QUANDO / ENTÃO**.

## Decisão

**(c)**. Modelo:

```
US-<área><n> — <título curto>   (RF-<área><n>)
Como <ator>, posso <ação>, para <benefício>.

Critérios de aceite
1. DADO QUE <contexto>, QUANDO <ação>, ENTÃO <resultado observável>.
2. DADO QUE <contexto>, QUANDO <ação alternativa ou de erro>, ENTÃO <resultado observável>.
```

- **Pelo menos 2 critérios** por estória; um deles cobre um caminho alternativo ou de erro.
- O ator é um dos nomes exatos do [CONTEXT.md](../../CONTEXT.md).

## Consequências

- Os critérios viram insumo direto dos casos de teste ([docs/testes/casos-de-teste.md](../testes/casos-de-teste.md)).
- Uma estória sem critério de erro volta na revisão cruzada.

---

## Ligações

- **Itens da especificação:** item 7 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D1](0001-minimo-por-integrante-e-numeracao-provisoria.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
