---
id: adr-indice
titulo: "Decisões do projeto (ADRs)"
tipo: decisao-indice
status: vigente
atualizado: 2026-11-20
relacionados: [adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006, adr-0007, adr-0008, adr-0009, adr-0010, adr-0011, adr-0012, adr-0013, adr-0014, adr-0015, adr-0016, adr-0017, adr-0018, adr-0019]
---
# Decisões do projeto (ADRs)

> Uma decisão por arquivo. **As decisões prevalecem** sobre a pesquisa (`pesquisa/`) e sobre rascunhos antigos, inclusive as versões `.docx`. Decisão nova: próximo número, mesmo formato (contexto, opções, decisão, consequências, ligações), status "aceita" e data. Decisão que muda outra: a antiga passa a "substituída por ADR-NNNN".

| ADR | Origem | Decisão | Itens afetados |
|---|---|---|---|
| [0001](0001-minimo-por-integrante-e-numeracao-provisoria.md) | D1 | Meta interna de 4 por integrante; numeração final definida na ADR-0001, com IDs novos no fim | 6, 7, 8, 9, 10 |
| [0002](0002-formato-de-estoria-e-criterios.md) | D2 | Estória em Como / Posso / Para, com pelo menos 2 critérios DADO QUE / QUANDO / ENTÃO | 7 |
| [0003](0003-extend-no-sentido-do-te3-3.md) | D3 | «extend» do caso opcional para o base (TE3_3 e UML) | 9, 10 |
| [0004](0004-diagramas-como-codigo.md) | D4 | Substituída pela ADR-0012. Diagramas como código: BPMN 2.0 no item 4, PlantUML nos itens 9 e 11 | 4, 9, 11 |
| [0005](0005-tutor-de-ia-como-ator-sistemico.md) | D5 | Tutor de IA como ator sistêmico | 2, 5, 6, 9, 10 |
| [0006](0006-divisao-por-areas.md) | D6 | Divisão do trabalho em áreas A a D, uma por integrante | 6, 7, 8, 10 |
| [0007](0007-stack-e-bancos.md) | D7 | Banco do core substituído pela ADR-0017 (PostgreSQL). Stack (Next.js SPA, API Laravel 13, MySQL 8) e ai-service físico com PostgreSQL 16 + pgvector | 5, 11 |
| [0008](0008-sessao-jwt-em-cookie.md) | D8 | Sessão com JWT de 1 h em cookie HttpOnly, refresh rotacionado e «manter conectado» | 5, 11 |
| [0009](0009-listagens-na-url-e-paginacao.md) | D9 | Nome `per_page` substituído pela ADR-0015 (`perPage`). Filtros, ordenação e página na URL; paginação obrigatória; resposta mínima da API | 5, 11 |
| [0010](0010-hospedagem-e-armazenamento.md) | D10 | Front na Vercel, back no Railway, mídia no Cloudflare R2; domínio pendente | 5, 11 |
| [0011](0011-diagramas-do-ra2-em-plantuml.md) | D11 | Substituída pela ADR-0013. Diagramas do RA2 (modelo de dados, classes e sequência) em PlantUML, PNG gerado da fonte | 12, 13, 14 |
| [0012](0012-diagramas-do-ra1-em-drawio.md) | D4 | Diagramas do RA1 em draw.io: fonte `.drawio` e PNG exportado da fonte; substitui a ADR-0004 | 4, 9, 11 |
| [0013](0013-diagramas-do-ra2-em-drawio.md) | D4 | Diagramas do RA2 (itens 12 a 14) em draw.io: fonte `.drawio` e PNG exportado da fonte; substitui a ADR-0011 | 12, 13, 14 |
| [0014](0014-exclusao-logica-e-anonimizacao.md) | D14 | Exclusão lógica (`deleted_at`) em todo o sistema; exclusão de usuário reversível e anonimização como passo separado | 10, 12, 13, 14, 15 |
| [0015](0015-convencao-de-nomes-por-camada.md) | D15 | Banco em snake_case, API e código em camelCase (`perPage`); substitui o nome do item 4 da ADR-0009 | 12, 13, 14, 15 |
| [0016](0016-retencao-de-logs-e-auditoria.md) | D16 | Auditoria 12 meses no PostgreSQL e 5 anos arquivada no R2; logs da aplicação por 90 dias | 8, 12, 14 |
| [0017](0017-core-em-postgresql.md) | D17 | Core em PostgreSQL 16, mesma instância do `ai-service`, databases `core` e `ai` separados; substitui o MySQL da ADR-0007 | 5, 11, 12 |
| [0018](0018-core-como-monolito-modular.md) | D18 | Core como monólito modular (Auth, Authoring, Learning, Admin e Analytics); só três serviços | 11, 13 |
| [0019](0019-upload-pela-api.md) | D19 | Upload de arquivos pela API, chave no banco e leitura por URL assinada; substitui o item 3 da ADR-0010 | 8, 10, 12, 13, 14 |

---

## Ligações

- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
- **Plano do RA1:** [ra1-tarefas.md](../../entregas/ra1-tarefas.md)
