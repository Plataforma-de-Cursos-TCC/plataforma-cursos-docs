---
id: adr-0007
titulo: "ADR-0007 — Definição da stack tecnológica e bancos de dados"
tipo: decisao
decisao: D7
status: aceita
data: 2026-10-08
decisor: Grupo
itens_template: [5, 11]
areas: [A, B, C, D]
relacionados: [adr-0005, adr-0006]
---
# ADR-0007 — Definição da stack tecnológica e bancos de dados

- **Status:** aceita · **Data:** 08/10/2026 · **Decisor:** Grupo

## Contexto

- A especificação de requisitos e o Documento de Design de Software (SDD) necessitavam de definições concretas da arquitetura física e lógica, componentes, linguagens e sistemas gerenciadores de banco de dados (SGBDs).
- O sistema é composto por:
  1. Uma aplicação web voltada aos usuários finais (alunos, instrutores e administradores);
  2. Uma API central responsável pelas regras de negócio dos domínios principais (autenticação, catálogo, aprendizagem, pagamentos e métricas);
  3. Um serviço de inteligência artificial (`ai-service`) responsável pelo Tutor de IA com arquitetura RAG (busca semântica em transcrições e geração de respostas contextualizadas com timestamps);
  4. Um serviço de mídia (`media-service`) para upload e streaming de vídeos via Cloudflare R2 (já estabelecido no SDD).
- Para o `ai-service`, era necessário escolher a engine de banco de dados para armazenamento de vetores e busca por similaridade restrita ao curso (`course_id`), considerando que a infraestrutura prevista era uma VPS única rodando containers Docker Compose para uma equipe de 4 desenvolvedores (hospedagem posteriormente alterada pela [ADR-0010](0010-hospedagem-e-armazenamento.md)).

## Opções consideradas (ai-service)

- **PostgreSQL 16 com extensão pgvector:** Suporte nativo e oficial no ecossistema Laravel/PHP através do método `whereVectorSimilarTo()` do Query Builder e SDK de IA, além de índice HNSW maduro e filtragem relacional combinada com índices B-tree.
- **MySQL 9 (Community):** [Documentação Oficial](https://dev.mysql.com/doc/refman/9.0/en/vector-data-type.html) — Descartado: A edição comunitária introduziu o tipo `VECTOR`, mas não possui índices vetoriais (nem HNSW nem IVF), exigindo varredura linear exaustiva ($O(n)$) ou o serviço comercial proprietário [MySQL HeatWave na OCI](https://docs.oracle.com/en-us/iaas/mysql-database/doc/heatwave-genai.html), além de não possuir driver vetorial no Laravel AI SDK.
- **MariaDB 11.7+ (Vector):** [Documentação Oficial](https://mariadb.com/kb/en/vector-overview/) — Descartado: Embora tenha suporte no Laravel e índice HNSW próprio, a funcionalidade é muito recente (fim de 2024 / 2025) com pouca maturidade em produção, e exigiria um container separado de qualquer forma, pois o core utiliza MySQL.
- **Qdrant:** [Documentação Oficial](https://qdrant.tech/documentation/) — Descartado: Banco vetorial dedicado de alto desempenho, porém sem suporte nativo no Laravel AI SDK (requer chamadas REST/gRPC manuais via `qdrant/qdrant-php`) e exigiria manter dois bancos no microsserviço (um relacional para metadados/sessões e o Qdrant para vetores), adicionando complexidade operacional desnecessária.
- **SQLite + sqlite-vec:** [Documentação Oficial](https://github.com/asg017/sqlite-vec) — Descartado: Não possui integração no Laravel AI SDK, requer compilação manual de extensões binárias C em runtime e apresenta concorrência limitada (locks de escrita) durante a ingestão assíncrona de transcrições e embeddings.

## Decisão

O grupo decidiu pela seguinte arquitetura de stack e bancos:

1. **Front-end:** Next.js com TypeScript arquitetado estritamente como SPA (Single Page Application, sem uso de Server Components ou Server Actions), consumindo a API central e o `ai-service` via REST/streaming SSE.
2. **API (Core):** Laravel 13 com PHP 8.3 estruturado como monólito modular, contendo os módulos de auth, catalog, learning e analytics.
3. **Banco de dados do Core:** MySQL 8 como SGBD relacional transacional primário para todas as entidades do sistema.
4. **Serviço do Tutor de IA (`ai-service`):** Microsserviço físico independente implementado em Laravel 13 / PHP 8.3, utilizando **PostgreSQL 16 com a extensão `pgvector`** como seu banco de dados exclusivo, executando buscas vetoriais com índice HNSW e filtragem obrigatória por `course_id`.
5. **Serviço de Mídia (`media-service`):** Microsserviço separado para manipulação de mídia com armazenamento de arquivos de vídeo no Cloudflare R2 (mantendo o que já está definido no `docs/sdd.md`).

## Consequências

- **Dois SGBDs:** A infraestrutura exigirá duas instâncias de banco de dados (uma para o MySQL 8 do core e uma dedicada ao PostgreSQL 16 + pgvector do `ai-service`). Em produção rodam no Railway ([ADR-0010](0010-hospedagem-e-armazenamento.md)).
- **Composição no Docker Compose (desenvolvimento local):** Mais um container de banco adicionado à orquestração (`pgvector/pgvector:pg16`), consumindo aproximadamente 100 MB adicionais de memória RAM. Em produção, o `pgvector` no Railway exige imagem própria (a confirmar).
- **Isolamento de dados e dependências:** O core da aplicação permanece simples e focado no MySQL 8 relacional, enquanto a carga pesada de vetores e processamento de RAG fica isolada no `ai-service` sem afetar a performance transacional do core.
- **Produtividade do time:** O uso do Laravel 13 em ambas as partes (API central e `ai-service`) unifica o ferramental de desenvolvimento, migrations, Eloquent e testes, aproveitando a integração de primeira classe com `pgvector`.

---

## Ligações

- **Documento de Design de Software:** [docs/sdd.md](../sdd.md)
- **Tutor como ator sistêmico:** [ADR-0005](0005-tutor-de-ia-como-ator-sistemico.md)
- **Divisão por áreas:** [ADR-0006](0006-divisao-por-areas.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
