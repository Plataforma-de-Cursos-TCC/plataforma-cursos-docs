---
id: adr-indice
titulo: "Decisões do projeto (ADRs)"
tipo: decisao-indice
status: vigente
atualizado: 2026-10-08
relacionados: [adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006, adr-0007]
---
# Decisões do projeto (ADRs)

> Uma decisão por arquivo. **As decisões prevalecem** sobre a pesquisa (`pesquisa/`) e sobre rascunhos antigos, inclusive as versões `.docx`. Decisão nova: próximo número, mesmo formato (contexto, opções, decisão, consequências, ligações), status "aceita" e data. Decisão que muda outra: a antiga passa a "substituída por ADR-NNNN".

| ADR | Origem | Decisão | Itens afetados |
|---|---|---|---|
| [0001](0001-minimo-por-integrante-e-numeracao-provisoria.md) | D1 | Meta interna de 4 por integrante; numeração final da v11, com IDs novos no fim | 6, 7, 8, 9, 10 |
| [0002](0002-formato-de-estoria-e-criterios.md) | D2 | Estória em Como / Posso / Para, com pelo menos 2 critérios DADO QUE / QUANDO / ENTÃO | 7 |
| [0003](0003-extend-no-sentido-do-te3-3.md) | D3 | «extend» do caso opcional para o base (TE3_3 e UML) | 9, 10 |
| [0004](0004-diagramas-como-codigo.md) | D4 | Diagramas como código: BPMN 2.0 no item 4, PlantUML nos itens 9 e 11 | 4, 9, 11 |
| [0005](0005-tutor-de-ia-como-ator-sistemico.md) | D5 | Tutor de IA como ator sistêmico | 2, 5, 6, 9, 10 |
| [0006](0006-divisao-por-areas.md) | D6 | Divisão do trabalho em áreas A a D, uma por integrante | 6, 7, 8, 10 |
| [0007](0007-stack-e-bancos.md) | D7 | Stack (Next.js SPA, API Laravel 13, MySQL 8) e ai-service físico com PostgreSQL 16 + pgvector | 5, 11 |
| [0008](0008-sessao-jwt-em-cookie.md) | D8 | Sessão com JWT de 1 h em cookie HttpOnly, refresh rotacionado e «manter conectado» | 5, 11 |
| [0009](0009-listagens-na-url-e-paginacao.md) | D9 | Filtros, ordenação e página na URL; paginação obrigatória; resposta mínima da API | 5, 11 |
| [0010](0010-hospedagem-e-armazenamento.md) | D10 | Front na Vercel, back no Railway, mídia no Cloudflare R2; domínio pendente | 5, 11 |

---

## Ligações

- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
- **Plano do RA1:** [ra1-tarefas.md](../../entregas/ra1-tarefas.md)
