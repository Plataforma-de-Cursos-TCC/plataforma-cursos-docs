---
id: adr-0003
titulo: "ADR-0003 — «extend» no sentido do material da disciplina (TE3_3)"
tipo: decisao
decisao: D3
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [9, 10]
areas: [A, B, C, D]
relacionados: [adr-0004]
---
# ADR-0003 — «extend» no sentido do material da disciplina (TE3_3)

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- Na UML 2.5, a seta de «extend» sai do caso de uso **estendido** (o opcional) e aponta para o caso de uso **base**.
- O material da disciplina (TE3_3) desenha a seta no sentido oposto: do caso de uso base para o estendido. A correção do RA1 segue o material da disciplina.
- Diagramas com sentidos misturados confundem a leitura e custam ponto.

## Opções consideradas

- **(a)** Sentido da UML 2.5 (estendido → base).
- **(b)** **Sentido do TE3_3** (base → estendido).

## Decisão

**(b)**. Em todos os diagramas de caso de uso do projeto, a seta de «extend» sai do caso de uso base e aponta para o estendido. «include» segue o sentido usual (base → incluído).

## Consequências

- O diagrama geral (item 9) e os diagramas por caso de uso (item 10) usam o mesmo sentido.
- Quem consultar fonte externa (livro, UML 2.5) não corrige o sentido no repositório; se houver dúvida, registra para o grupo.

---

## Ligações

- **Itens da especificação:** itens 9 e 10 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D4](0004-diagramas-como-codigo.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
