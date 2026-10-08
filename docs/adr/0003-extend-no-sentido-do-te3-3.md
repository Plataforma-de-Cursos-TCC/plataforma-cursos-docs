---
id: adr-0003
titulo: "ADR-0003 — «extend» no sentido do material da disciplina (TE3_3) e da UML"
tipo: decisao
decisao: D3
status: aceita
data: 2026-10-08
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [9, 10]
areas: [A, B, C, D]
relacionados: [adr-0004]
---
# ADR-0003 — «extend» no sentido do material da disciplina (TE3_3) e da UML

- **Status:** aceita · **Data:** 08/10/2026 (revisão da versão de 07/10/2026) · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- A versão de 07/10/2026 desta decisão afirmava que o TE3_3 desenha a seta de «extend» do caso de uso base para o estendido. A releitura do material (TE3_3, p. 13 e p. 23 a 25) mostra o contrário: a seta sai do caso de uso **opcional** (o que estende) e aponta para o caso de uso **base**, o mesmo sentido da UML 2.5.
- O diagrama geral (item 9) foi desenhado com o sentido invertido, o que custa ponto na correção do RA1.

## Opções consideradas

- **(a)** Manter o sentido base → opcional, que não tem apoio no material nem na UML.
- **(b)** **Sentido do TE3_3 e da UML 2.5:** a seta de «extend» sai do caso de uso opcional e aponta para o caso de uso base.

## Decisão

**(b)**. Em todos os diagramas de caso de uso do projeto:

- **«extend»:** seta tracejada do caso de uso opcional para o caso de uso base (ex.: "Recuperar senha" → "Realizar login").
- **«include»:** seta tracejada do caso de uso base para o incluído, sempre executado.

## Consequências

- O diagrama geral (item 9) e as especificações de caso de uso (item 10) são corrigidos para o sentido acima.
- O critério C09.5 de [ra1-criterios-de-aceite](../../entregas/ra1-criterios-de-aceite.md) passa a conferir este sentido.

---

## Ligações

- **Itens da especificação:** itens 9 e 10 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D4](0004-diagramas-como-codigo.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
