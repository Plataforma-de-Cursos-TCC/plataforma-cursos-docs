# Relatório Consolidado de Revisão Cruzada Final — Issue #135

**Data:** 2026-11-22  
**Escopo auditado:** Consolidação e verificação exaustiva dos 92 achados da revisão cruzada adversarial (Issue #135), confrontando os relatórios de quatro modelos (`Flash` com 24 achados, `Hydrogen` com 19 achados, `Argon` com 24 achados e `Neon` com 25 achados) diretamente contra a `main` atual do repositório Plataforma de Cursos (`especificacao/` Itens 1 a 15, diagramas `.drawio`, `docs/tdd.md`, `docs/testes/`, ADRs 0001 a 0018 e `entregas/ra2-relatorio-areas-abcd.md`).  
**Modo:** Somente Leitura (nenhum arquivo do repositório foi alterado).  
**Critério de reavaliação de gravidade:**
- **`bloqueia`**: O professor perceberia o erro ou contradição na entrega final do RA2 (inconsistência que quebra critérios formais C12 a C15, G.2 ou G.3 no DOCX/PDF gerado).
- **`corrigir`**: Inconsistência real menor, pontual entre camadas ou em artefatos de apoio que requer correção técnica sem invalidar o documento principal.
- **`sugestão`**: Melhoria editorial, preventiva ou de padronização estética/metadados.

---

## 1. Tabela-Resumo de Achados Consolidados (Confirmados e Parciais)

| Área / Escopo | `bloqueia` | `corrigir` | `sugestão` | Total |
|---|:---:|:---:|:---:|:---:|
| **Geral / Transversal** | 2 | 4 | 2 | **8** |
| **Área A (Acesso e conta)** | 0 | 4 | 3 | **7** |
| **Área B (Autoria do instrutor)** | 1 | 4 | 1 | **6** |
| **Área C (Aprendizagem do aluno)** | 0 | 1 | 1 | **2** |
| **Área D (Tutor de IA, analytics e administração)** | 0 | 7 | 0 | **7** |
| **TDD e Testes (`docs/tdd.md`, `docs/testes/`)** | 1 | 3 | 1 | **5** |
| **TOTAL GERAL** | **4** | **23** | **8** | **35** |

*(Total de 92 achados auditados: **35 itens consolidados** [32 CONFIRMADOS e 3 PARCIAIS] cobrindo 89 achados originais, e **3 achados FALSOS** [mais desconsiderações de regras intencionais]).*

---

## 2. Lista Consolidada de Achados Confirmados e Parciais (C1 a C35)

### C1
- **Gravidade:** `bloqueia`
- **Área:** TDD e Testes
- **Arquivo:Linha:** `docs/testes/cobertura.md:18, 19-21, 23-27, 31-33, 35-37, 39, 41`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R1, R2, R3, R4, R5), Hydrogen (R3), Argon (R3), Neon (R3)
- **Problema:** A matriz de rastreabilidade UC->TC em `docs/testes/cobertura.md` encontra-se severamente defasada frente aos arquivos vigentes de casos de teste em `especificacao/15-casos-de-teste/`:
  1. **Área D (l. 18, 24, 25, 33, 35):** UC001, UC007, UC008, UC016 e UC018 apontam para 13 identificadores legados do RA1 (`TC034–TC039`, `TC043–TC048`, `TC063`) que foram substituídos na entrega final, omitindo todos os 60 novos casos de teste vigentes da faixa `TC211` a `TC272`.
  2. **Área B (l. 21, 23, 31, 32):** Omissão dos 35 casos novos do RA2 (`TC091–TC110`, `TC112–TC114`, `TC116–TC124`) nos UCs 004, 006, 014 e 015.
  3. **Área C (l. 19, 20, 26, 27, 36, 37):** Omissão dos 26 casos novos da faixa `TC151–TC177` nos UCs 002, 003, 009, 010, 019 e 020; além disso, a linha do UC020 (l. 37) cita `TC057`, que foi renumerado para `TC175` em `area-c.md`.
  4. **UC001 e contagens (l. 18, 39, 41):** A linha do UC001 omite a estória `US022` e o requisito `RF020`; a nota da linha 39 declara que apenas a Área A migrou para o Item 15; e a linha 41 afirma *"as 21 estórias de usuário"* quando o projeto possui 22 estórias homologadas (`US001` a `US022`).
- **Correção:** Atualizar integralmente as linhas de todos os casos de uso em `docs/testes/cobertura.md` para refletir os 213 casos de teste vigentes de `especificacao/15-casos-de-teste/area-a.md` a `area-d.md`, remover os 14 IDs legados inexistentes, adicionar `US022` e `RF020` na linha do UC001 e retificar a nota para 22 estórias de usuário.

---

### C2
- **Gravidade:** `bloqueia`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/00-item.md:9-12`, `especificacao/13-diagrama-de-classes/00-item.md:10-12`, `especificacao/14-diagramas-de-sequencia/00-item.md:14-16`, `especificacao/15-casos-de-teste/00-item.md:14-16`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R12, R13, R14, R15), Hydrogen (R2), Argon (R2), Neon (R1)
- **Problema:** As tabelas-resumo dos quatro arquivos `00-item.md` do RA2 contêm texto provisório de placeholder `"a preencher"` (itens 12 e 13) e `"a definir"` (itens 14 e 15) para as Áreas B, C e D, embora todas as quatro áreas já tenham sido entregues. Adicionalmente, em `especificacao/12-modelo-de-dados/00-item.md:9`, as tabelas da Área A foram listadas em PascalCase de classes (`User, Address, InstructorProfile, PasswordResetToken, RefreshSession`) em vez de `snake_case` de banco. Como `scripts/build_doc.py:58-65` concatena os `00-item.md` diretamente no DOCX/PDF final entregue ao professor, esses placeholders vazam diretamente na entrega.
- **Correção:** Preencher as linhas das Áreas B, C e D nas quatro tabelas com as tabelas em `snake_case` (Item 12), classes principais (Item 13) e casos de uso entregues (Itens 14 e 15); na linha da Área A do Item 12, trocar os nomes em PascalCase por `users, addresses, instructor_profiles, password_reset_tokens, refresh_sessions`.

---

### C3
- **Gravidade:** `bloqueia`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/07-estorias-de-usuario/00-item.md:5-27`, `especificacao/09-diagrama-geral-de-casos-de-uso.md:13-33`, `especificacao/10-especificacoes-de-caso-de-uso/area-d.md:5`, `especificacao/07-estorias-de-usuario/area-d.md:71-85`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R9, R10, R11), Hydrogen (R1), Argon (R1), Neon (R2)
- **Problema:** O requisito `RF020` (*"Comprar pacote de créditos extras para o Tutor de IA"*) e a estória `US022` (*"Comprar créditos extras do Tutor de IA"*), criados na Área D, foram adicionados ao Item 6 mas quebraram a cadeia de rastreabilidade formal:
  1. `US022` foi omitida da tabela-índice de `especificacao/07-estorias-de-usuario/00-item.md:5-27` (que termina na `US016` / linha 21).
  2. `RF020` não consta na tabela de rastreabilidade `9.1` de `especificacao/09-diagrama-geral-de-casos-de-uso.md:13-33` (que termina em `RF019`).
  3. A descrição inicial do `UC001` (`especificacao/10-especificacoes-de-caso-de-uso/area-d.md:5`) referencia apenas `(US012, RF009)`, omitindo `US022` e `RF020` (que só aparecem adiante na regra R-2 e no fluxo A3).
  4. A `US022` (`area-d.md:79-84`) possui apenas 2 critérios positivos e nenhum cobrindo caminho alternativo ou de erro (recusa ou cancelamento do pagamento simulado), violando a ADR-0002.
- **Correção:** Inserir a linha 22 correspondente à `US022` no índice do Item 7; incluir a linha do `RF020` na tabela 9.1 do Item 9 apontando para `UC001 (fluxo A3)`; adicionar `US022, RF020` na descrição do `UC001` no Item 10; e acrescentar ao menos um critério de aceite de erro/recusa na `US022`.

---

### C4
- **Gravidade:** `bloqueia`
- **Área:** Área B
- **Arquivo:Linha:** `docs/adr/0010-hospedagem-e-armazenamento.md:34` vs `especificacao/08-requisitos-nao-funcionais/00-item.md:8`, `especificacao/10-especificacoes-de-caso-de-uso/area-b.md:278,285`, `especificacao/12-modelo-de-dados/area-b.md:19-20`, `docs/tdd.md:24,597,655`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R7), Neon (R5)
- **Problema:** Contradição direta entre uma ADR estruturante e os requisitos/especificação da Área B sobre upload de arquivos:
  - A `ADR-0010` (item 3) determina: *"O navegador **envia e baixa por URL assinada** gerada pela API, direto no domínio S3 do R2, sem passar pelo `rewrite`."*
  - Em oposição direta, o `RNF002` exige *"upload de vídeo e de material somente pela API, que grava no armazenamento; ... 0 acessos diretos ao armazenamento"*, e toda a modelagem da Área B (`UC015` R-3, passo 5 e A4, `MediaStorageInterface.uploadFile` e `docs/tdd.md:597`) adota upload binário `multipart/form-data` enviado diretamente à API do backend, repassando ao `media-service`. Esse fluxo passa pelo proxy/rewrite da Vercel, colidindo com limites rígidos de payload e contradizendo a ADR-0010.
- **Correção:** Harmonizar a arquitetura: registrar formalmente adendo na `ADR-0010` alinhando a decisão ao modelo implementado no `RNF002` e na Área B (ou ajustar o `RNF002`, `UC015`, diagramas da Área B e TDD para emissão de presigned URL com upload direto ao R2).

---

### C5
- **Gravidade:** `corrigir`
- **Área:** TDD e Testes
- **Arquivo:Linha:** `docs/tdd.md:35-555`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R6, R7), Hydrogen (R6), Argon (R7), Neon (R15)
- **Problema:** A Seção 2 de `docs/tdd.md` (diagrama ER Mermaid, Dicionário de Dados e Diagrama de Classes Mermaid) permaneceu na versão do RA1, violando as ADRs 0014, 0015 e 0017:
  1. Todas as colunas do `erDiagram` (linhas 67–230) e Dicionário (linhas 236–380) usam `camelCase` (`passwordHash`, `documentNumber`, `userId`, `courseId` etc.) em vez de `snake_case` (ADR-0015).
  2. Tipos de dados adotam dialeto genérico/MySQL (`VARCHAR`, `DATETIME`, `INT`, `TINYINT`, `ENUM`, `JSON`) em vez dos tipos nativos de PostgreSQL 16 (`uuid`, `timestamptz`, `text`, `integer`, `boolean`, `jsonb`, `text com CHECK`) (ADR-0017).
  3. Ausência da coluna `deleted_at: timestamptz` em todas as entidades de negócio (ADR-0014).
  4. Omissão das entidades criadas no RA2: `lesson_materials`, `tutor_credit_packs` e `audit_logs`, além das colunas `lessons.video_mime_type`, `lessons.video_size_bytes`, `lessons.index_status`, `quizzes.status`, `quizzes.allow_retake`, `quiz_attempts.status` e `payments.purpose`.
  5. No diagrama de classes Mermaid (linhas 481–483, 544), `Payment` expõe FKs como atributos primitivos (`-userId`, `-courseId`, `-enrollmentId`, violando C13.2) e define multiplicidade `Payment "0..*" --> "1" Enrollment`, incompatível com pagamentos avulsos de créditos do Tutor (`0..1`).
- **Correção:** Atualizar a Seção 2 de `docs/tdd.md` para alinhar as 21 tabelas com `snake_case`, tipos nativos do PostgreSQL 16, inclusão de `deleted_at`, adição das novas entidades do RA2 e correção das associações da classe `Payment`.

---

### C6
- **Gravidade:** `corrigir`
- **Área:** TDD e Testes
- **Arquivo:Linha:** `docs/tdd.md:613-623`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R8), Hydrogen (R11), Neon (R14)
- **Problema:** O JSON de exemplo do envelope de paginação na seção 3.2 de `docs/tdd.md` utiliza as propriedades `"totalItems"` e `"totalPages"`, divergindo da `ADR-0015` (item 2: *"O envelope de paginação também: meta.currentPage, meta.perPage, meta.total, meta.lastPage."*). Adicionalmente, os links de exemplo utilizam a rota `/api/v1/courses?...` em vez de `/api/v1/catalog/courses`.
- **Correção:** Renomear `"totalItems"` para `"total"` e `"totalPages"` para `"lastPage"` em `docs/tdd.md:616-617` e atualizar a rota nos links de exemplo.

---

### C7
- **Gravidade:** `corrigir`
- **Área:** TDD e Testes
- **Arquivo:Linha:** `docs/testes/casos-de-teste.md:10-15,71`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R5), Argon (R4)
- **Problema:** O cabeçalho de `docs/testes/casos-de-teste.md` declara *"66 casos de teste... estórias de usuário (US001–US021)"* e cita apenas as Áreas A e C como migradas para `especificacao/15-casos-de-teste/`, omitindo as Áreas B e D e a `US022`. Além disso, na linha 71, o `TC048` descreve remoção direta e anonimização de dados no momento da confirmação de exclusão no `UC008`, contrariando a `ADR-0014` (exclusão lógica reversível em `UC018`).
- **Correção:** Atualizar a nota de cabeçalho indicando que as quatro áreas e as 22 estórias residem em `especificacao/15-casos-de-teste/`, e marcar `TC048` como substituído pelos TCs do `UC018` (`TC257–TC272`).

---

### C8
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `docs/adr/0014-exclusao-logica-e-anonimizacao.md:35`, `especificacao/07-estorias-de-usuario/area-d.md:69`, `especificacao/10-especificacoes-de-caso-de-uso/area-d.md:290,296,327-331`, `docs/tdd.md:682` vs `especificacao/diagramas/13-classes-area-d-implementacao-administracao.drawio:251`, `13-classes-area-b-implementacao-cursos-modulos.drawio:71`, `especificacao/diagramas/14-sequencia-uc018.drawio:680-687`, `especificacao/15-casos-de-teste/area-d.md:90,94`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R9), Argon (R13), Neon (R6)
- **Problema:** A `ADR-0014` (item 5), a `US016` (critério 8), o `UC018` (R-5 e fluxo alternativo A4) e `docs/tdd.md:682` determinam que, ao excluir um Instrutor com cursos publicados, o Administrador escolhe entre: (1) despublicar os cursos (`status = archived`); **ou** (2) aplicar exclusão lógica em cascata nos cursos, módulos, aulas e quizzes (`deleted_at`). Porém, nos diagramas de classes de implementação das Áreas B e D (`CourseService`), no diagrama de sequência `14-sequencia-uc018.drawio:680` e nos testes (`TC266` e `TC272`), apenas o método `archiveAllByInstructor` foi modelado e testado, sem ramo nem método para a cascata lógica.
- **Correção:** Adicionar o método `softDeleteAllByInstructor(instructorId: UUID): void` em `CourseService` (Áreas B e D), modelar o ramo alternativo em bloco `alt` em `14-sequencia-uc018.drawio` e adicionar caso de teste correspondente no Item 15 (ou documentar na ADR-0014/UC018 a consolidação de arquivar cursos caso haja histórico de alunos).

---

### C9
- **Gravidade:** `corrigir`
- **Área:** Área A
- **Arquivo:Linha:** `docs/adr/0014-exclusao-logica-e-anonimizacao.md:36`, `especificacao/10-especificacoes-de-caso-de-uso/area-a.md:32-63` (`UC005`), `especificacao/diagramas/14-sequencia-uc005.drawio:530-575`, `especificacao/15-casos-de-teste/area-a.md:11-16`, `docs/tdd.md:635`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R10), Argon (R14), Neon (R16 part 3)
- **Problema:** A `ADR-0014` (item 6) determina que tentativa de login em conta excluída (`status = deleted`) ou anonimizada devolve `401 UNAUTHENTICATED` genérico, igual a senha errada (testado em `TC262` na Área D). Entretanto, o `UC005` (`area-a.md`), o diagrama `14-sequencia-uc005.drawio` e os casos de teste da Área A tratam apenas credenciais incorretas (`E1`) e conta bloqueada (`E3`), sem mencionar conta excluída ou anonimizada.
- **Correção:** Registrar no fluxo `E1` de `especificacao/10-especificacoes-de-caso-de-uso/area-a.md`, em `14-sequencia-uc005.drawio:533,548` e em `docs/tdd.md:635` que conta com `status = deleted` ou `anonymized_at IS NOT NULL` recebe o mesmo retorno `401 UNAUTHENTICATED` genérico de E1.

---

### C10
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `especificacao/10-especificacoes-de-caso-de-uso/area-d.md:301-303,325`, `especificacao/diagramas/14-sequencia-uc018.drawio:674,749,794`, `especificacao/15-casos-de-teste/area-d.md:81,93`
- **Classificação:** PARCIAL
- **Modelos que acharam:** Argon (R12, R15, R16), Hydrogen (R19 part 1), Neon (R8)
- **Problema:** Inconsistências na modelagem da exclusão lógica e anonimização do UC018:
  1. Em `14-sequencia-uc018.drawio:794`, a query de anonimização usa colunas em português (`UPDATE users SET nome, e-mail, documento, anonymized_at=NOW()`), omitindo `phone`, `birth_date`, `photo` e a limpeza de `addresses`.
  2. Em `14-sequencia-uc018.drawio:674,749` e no teste `TC257`, as queries atualizam apenas `deleted_at`, omitindo a alteração de `status` (`status = 'deleted'` e `status = 'active'`).
  3. No texto do UC018 (`area-d.md:325`), o passo A-3.2 omite data de nascimento e endereços da lista de campos PII anonimizados (ADR-0014 item 4).
  4. A legenda do protótipo no fluxo básico (`area-d.md:301-303`) descreve *"modal de confirmação com aviso de anonimização irreversível"*, texto defasado da época pré-ADR-0014. *(Nota: a numeração "Figura 0" é intencional e não constitui defeito).*
- **Correção:** Atualizar o SQL em `14-sequencia-uc018.drawio` para colunas em inglês com atualização de `status`, incluir data de nascimento e endereços no passo A-3.2 de `area-d.md:325` e no `TC271`, e retificar a legenda do protótipo básico para *"aviso de exclusão lógica"*.

---

### C11
- **Gravidade:** `corrigir`
- **Área:** Área B
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/area-b.md:48,59,70` e `12-modelo-de-dados-area-b.drawio` vs `especificacao/diagramas/13-classes-area-b-implementacao-cursos-modulos.drawio:47,98`, `13-classes-area-b-implementacao-aulas.drawio:29,35`, `especificacao/diagramas/14-sequencia-uc014.drawio:467,485`, `especificacao/15-casos-de-teste/area-b.md:30` (`TC099`), `docs/tdd.md:141,150,305,313,438`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R9), Neon (R10)
- **Problema:** O atributo de ordenação de módulos, aulas e materiais chama-se `position` no modelo relacional do Item 12 e nas classes negociais (`Module.position`, `Lesson.position`), mas chama-se `order` nos DTOs de implementação (`ModuleDTO.order`, `LessonDTO.order`), nos métodos de repositório (`isOrderTaken`), no retorno de validação de `14-sequencia-uc014.drawio:485` (`fields.order`, onde a query executa `WHERE course_id e position`), no teste `TC099` (`fields.order`) e na seção 2 do TDD (`order`).
- **Correção:** Padronizar para `position` em todas as camadas (evitando palavra reservada SQL `ORDER`): atualizar DTOs, renomear `isOrderTaken` para `isPositionTaken`, e retificar `fields.order` para `fields.position` no `14-sequencia-uc014.drawio` e no `TC099`.

---

### C12
- **Gravidade:** `corrigir`
- **Área:** Área B
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/area-b.md:16` vs `especificacao/10-especificacoes-de-caso-de-uso/area-b.md:97` (`UC006 R-2`), `especificacao/diagramas/13-classes-area-b-negocial.drawio:41`, `13-classes-area-b-implementacao-cursos-modulos.drawio:71`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R9)
- **Problema:** Em `especificacao/12-modelo-de-dados/area-b.md:16`, afirma-se que o bloqueio de exclusão de curso com matrículas permite *"a alteração de status para despublicado / rascunho (`draft`) ou arquivado (`archived`)"*, mas a regra de negócio `UC006 R-2` proíbe expressamente o retorno de curso com alunos matriculados para `draft` (permitindo exclusivamente o arquivamento `archived` para não cortar o acesso dos alunos matriculados). Além disso, `Course` em `13-classes-area-b-negocial.drawio:41` declara `+unpublish(): void` mas omite `+archive(): void`, e `InstructorCourseController`/`CourseService` declaram `unpublish()`, operação sem rota correspondente no TDD nem fluxo no UC006.
- **Correção:** Remover a permissão de retorno a `draft` quando há matriculados em `12-modelo-de-dados/area-b.md:16`, substituir `unpublish()` por `archive()` em `Course` no diagrama negocial e alinhar `CourseService`.

---

### C13
- **Gravidade:** `corrigir`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/13-diagrama-de-classes/area-a.md:21`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R7)
- **Problema:** O texto descreve `PhotoStorage` como *"armazenamento de imagem no Cloudflare R2 com **URL pública** e CDN"*, o que contradiz a `ADR-0010` (item 3: *"Vídeos, **imagens** e arquivos ficam em **bucket privado** do Cloudflare R2... CORS libera somente a origem do front-end"*) e o `RNF002` (*"0 acessos diretos ao armazenamento"*).
- **Correção:** Ajustar `PhotoStorage` para gerar URL assinada a partir do bucket privado do Cloudflare R2 (em consonância com a ADR-0010 e RNF002) ou registrar exceção explícita na ADR-0010 para fotos de perfil em bucket público separado.

---

### C14
- **Gravidade:** `corrigir`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/diagramas/12-modelo-de-dados-area-a.drawio:28,31,34,110` vs `especificacao/12-modelo-de-dados/area-a.md:11,26-28,42`, `12-modelo-de-dados-area-b.md:26-89`, `12-modelo-de-dados-area-d.md:34-68`, `12-modelo-de-dados-area-d.drawio:11-214`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R8), Neon (R11)
- **Problema:** Divergências na representação dos tipos PostgreSQL 16 (ADR-0017):
  1. No diagrama `12-modelo-de-dados-area-a.drawio`, as colunas enumeradas `users.role`, `users.status`, `users.theme` e `addresses.type` estão tipadas como `varchar(20)`, divergindo do dicionário da Área A e dos diagramas das Áreas B e C (que usam `text CHECK`).
  2. No dicionário da Área B (`area-b.md`), a coluna DOMÍNIO usa rótulos genéricos em português (`UUID`, `Texto`, `Inteiro`, `Data e hora`) sem os tipos nativos do PostgreSQL 16.
  3. No diagrama da Área D (`12-modelo-de-dados-area-d.drawio`), os tipos estão em caixa alta (`UUID`, `TEXT`, `TIMESTAMPTZ`) e os enums anotados como `TEXT [user, assistant]` em vez de `text CHECK (...)`.
- **Correção:** Alterar `varchar(20)` para `text CHECK (...)` nas colunas de `12-modelo-de-dados-area-a.drawio` e padronizar os domínios do Item 12 com a nomenclatura em minúsculas do PostgreSQL 16.

---

### C15
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `especificacao/13-diagrama-de-classes/area-d.md:3,8`, `especificacao/diagramas/13-classes-area-d-negocial.drawio:41,53,89,119,263`, `especificacao/diagramas/13-classes-area-d-implementacao-administracao.drawio:143`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R14), Argon (R18, R19 part 1), Neon (R13)
- **Problema:** Desvios de notação e completude no Item 13 da Área D:
  1. O enumerador `AuditAction` no texto (`area-d.md:3`) e no diagrama negocial (`13-classes-area-d-negocial.drawio:119`) lista apenas 6 valores, omitindo `USER_ANONYMIZE` (usado nos Itens 10, 12, 14 e 15).
  2. A entidade `AuditLog` em `13-classes-area-d-implementacao-administracao.drawio:143` declara `-userId: UUID` como atributo primitivo, violando a regra de não expor FKs como atributos no diagrama de classes (critério C13.2 / TE5_1).
  3. A classe `Conversation` (`13-classes-area-d-negocial.drawio:53`) exibe a restrição relacional `UNIQUE(userId, lessonId)` na lista de atributos, e `DashboardFilter` (linha 263) traz `+courseId?: UUID` como atributo primitivo.
  4. Stubs negociais em `13-classes-area-d-negocial.drawio` usam `string` fraca para `Course.status`, `Payment.purpose` e `DashboardFilter.groupBy` em vez dos enums correspondentes.
  5. Em `area-d.md:8`, o texto grafa `messages_used` em `snake_case` ao referenciar a propriedade de objeto no código (em vez de `messagesUsed`).
- **Correção:** Incluir `USER_ANONYMIZE` em `AuditAction`; remover `-userId: UUID` de `AuditLog`; mover a anotação de unicidade de `Conversation` para nota externa; aplicar tipos enumerados em `Course.status`, `Payment.purpose` e `DashboardFilter.groupBy`; e grafar `messagesUsed` em `area-d.md:8`.

---

### C16
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `especificacao/diagramas/13-classes-area-d-implementacao-administracao.drawio:53,113,245`, `especificacao/diagramas/14-sequencia-uc018.drawio:785`, `docs/tdd.md:684`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R21), Hydrogen (R12 part 2, R15 part 2), Neon (R17)
- **Problema:** A classe `UserController` em `13-classes-area-d-implementacao-administracao.drawio:53` declara apenas os métodos `index`, `updateStatus`, `updateRole`, `destroy` e `restore`, omitindo o método `+anonymize(id: UUID): JsonResponse` (que é acionado expressamente em `14-sequencia-uc018.drawio:785` e corresponde à rota `POST /api/v1/admin/users/{id}/anonymize` em `docs/tdd.md:684`). Adicionalmente, as assinaturas dos stubs da Área A em `administracao.drawio` divergem: `UserRepository.save` aparece retornando `: void` (vs `: User` na Área A) e `InstructorProfileRepository.createEmpty` aparece retornando `: void` (vs `: InstructorProfile` em `perfil.drawio:116`).
- **Correção:** Adicionar `+anonymize(id: UUID): JsonResponse` em `UserController` e alinhar os tipos de retorno dos métodos de `UserRepository` e `InstructorProfileRepository` no diagrama de implementação da Área D.

---

### C17
- **Gravidade:** `corrigir`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/diagramas/13-classes-area-d-implementacao-administracao.drawio:74,287`, `especificacao/diagramas/13-classes-area-a-implementacao-login.drawio:95,250`, `perfil.drawio:101,229`, `recuperacao.drawio:71,74`, `13-classes-area-d-implementacao-tutor-analytics.drawio:431`, `13-classes-area-c-implementacao-aprendizagem.drawio:302,335`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R19 part 2, R20), Hydrogen (R15 part 1, 3), Neon (R19 part 1, R20 part 1)
- **Problema:** Ícones de tipo UML (círculos C/A/I/E) e estereótipos incorretos nos diagramas de classes:
  1. `JwtGuard (Área A)` aparece como `<<Service>>`, cor verde `#D5E8D4` e ícone `(C)` em `13-classes-area-d-implementacao-administracao.drawio:74,287`, quando na Área A é uma interface (`<<interface>>`, cor `#F8CECC`, ícone `(I)`).
  2. A classe abstrata `User` aparece com ícone `(C)` (classe concreta) e nome sem itálico nos 3 diagramas de implementação da Área A e no diagrama de implementação do Tutor da Área D, divergindo dos diagramas negociais e de administração (onde está corretamente com ícone `(A)` e nome em itálico).
  3. A enumeração `GroupBy` em `13-classes-area-c-implementacao-aprendizagem.drawio:302` está preenchida com a cor roxa `#E1D5E7` (reservada para DTO/Request) e sem o estereótipo `<<enumeration>>`.
- **Correção:** Ajustar `JwtGuard` para `<<interface>>` com ícone `(I)` na Área D; trocar o ícone de `User` para `(A)` com nome em itálico nos diagramas de implementação afetados; e aplicar estereótipo `<<enumeration>>` e fundo neutro em `GroupBy`.

---

### C18
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `docs/tdd.md:679`, `especificacao/diagramas/13-classes-area-d-implementacao-administracao.drawio:11`, `especificacao/15-casos-de-teste/area-d.md:42,50,54,84`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R12 part 1, 3), Neon (R4 part 3)
- **Problema:** Parâmetro de busca textual e placeholders de rota inconsistentes:
  1. `docs/tdd.md:679` documenta o parâmetro de busca de usuários como `search`, enquanto `ListUsersRequest` (`administracao.drawio:11`) define `+query?: string` (e omite `status`), e o teste `TC231` (`area-d.md:42`) envia `?query=João&page=1&perPage=15`.
  2. Os casos de teste `TC240`, `TC244` e `TC260` (`area-d.md:50,54,84`) utilizam placeholders de rota informais em `snake_case` (`{seu_id}`, `{seu_proprio_id}`) em vez do padrão de rota `{id}`.
- **Correção:** Unificar o parâmetro de busca para `search` (ou `query`) e adicionar `status?: UserStatus` em `ListUsersRequest` e `TC231`; substituir `{seu_id}` e `{seu_proprio_id}` por `{id}` nas rotas de teste.

---

### C19
- **Gravidade:** `corrigir`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/02-e-nao-e-faz-nao-faz.md:10`, `especificacao/05-atores-usuarios.md:12`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R17), Argon (R22), Neon (R23)
- **Problema:** Violações ao vocabulário estrito de atores e produto:
  1. Em `especificacao/02-e-nao-e-faz-nao-faz.md:10`, a tabela descreve *"quiz e gabarito do **professor**"*, utilizando termo fora do glossário em vez do ator oficial **Instrutor** (AGENTS.md regra 5, CONTEXT.md seção 2).
  2. Em `especificacao/05-atores-usuarios.md:12`, o texto cita que o sistema aparece *"como raia **'Plataforma'** no mapeamento de negócios (item 4)"*, mas no texto e no diagrama BPMN do Item 4 o nome oficial da raia é **"Plataforma de Cursos"**.
- **Correção:** Substituir `"do professor"` por `"do Instrutor"` no Item 2 e alterar `'Plataforma'` para `'Plataforma de Cursos'` no Item 5.

---

### C20
- **Gravidade:** `corrigir`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/10-especificacoes-de-caso-de-uso/area-d.md:147,238,287,290`, `especificacao/12-modelo-de-dados/area-b.md:19-21`, `area-c.md:12,37`, `area-d.md:3,12,15,17,48,51`, `especificacao/13-diagrama-de-classes/area-c.md:3,5,8,9`, `area-d.md:3,7,8`, `especificacao/14-diagramas-de-sequencia/area-b.md:23`, `area-c.md:15,23,47`, `area-d.md:3,11,19,27,35,48`, `especificacao/15-casos-de-teste/area-b.md:12,48`, `area-c.md:103`, `area-d.md:8,12,17,25,29,34,42,43,47,53-56,72,81,82,86,89-91`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R18), Argon (R5), Neon (R22)
- **Problema:** Códigos e rótulos de controle interno de trabalho (`D-TC243`–`D-TC268`, `D-cota`, `D-cota-extra`, `decisão #51`, `decisões B2/B3/B4`, `C3/C5/C10`, `D1/D3/D5/D6/D7/D8/D9`) permaneceram no texto da especificação compilada no DOCX/PDF entregue ao professor. Vários desses rótulos colidem com a numeração oficial de decisões de `CONTEXT.md` seção 4 (ex.: no UC016, `(D7)` é usado para blocklist do Redis, mas no CONTEXT.md `D7` é a ADR-0007; no Item 14, `(D3)` é usado para parâmetros de dashboard, mas `D3` oficial é a ADR-0003 sobre setas de extend).
- **Correção:** Remover os prefixos internos `D-` dos TCs e substituir todos os rótulos de controle interno pelas citações formais às decisões (`ADR-0008`, `ADR-0014`, `ADR-0015`, `ADR-0016`) ou requisitos (`RF020`, `RNF022`).

---

### C21
- **Gravidade:** `corrigir`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/15-casos-de-teste/area-b.md:54,66,68,70`, `especificacao/15-casos-de-teste/area-d.md:47,48,90,91,90-94`, `especificacao/15-casos-de-teste/area-c.md:26,97`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R16, R17, R18), Hydrogen (R4), Argon (R6), Neon (R4 part 1, 2)
- **Problema:** Buracos internos e inconsistências numéricas nas tabelas de casos de teste sem nota explicativa:
  1. Na Área B: ausência de `TC111` (salto de `TC110` para `TC112`) e `TC115` (salto de `TC114` para `TC116`).
  2. Na Área D: ausência de `TC237` (salto de `TC236` para `TC238`) e `TC267` (salto de `TC266` para `TC268`); duplicidade de numeração de cenários no UC018 (`TC266` e `TC272` ambos numerados como `9 –`; `TC269` e `TC271` ambos numerados como `11 –`).
  3. Na Área C / RA1: ausência de `TC054` entre `TC053` e `TC055`.
  *(Ressalva: conforme regra do projeto, o uso de `TC271`/`TC272` na Área D é intencional e não constitui defeito).*
- **Correção:** Inserir nota explicativa de descarte para os IDs intermediários não utilizados (`TC111`, `TC115`, `TC237`, `TC267`, `TC054`), análoga à nota existente para o `TC008` em `docs/testes/cobertura.md:39`, e ajustar a numeração dos cenários duplicados no UC018.

---

### C22
- **Gravidade:** `corrigir`
- **Área:** Área C
- **Arquivo:Linha:** `especificacao/diagramas/12-modelo-de-dados-area-c.drawio:59`, `especificacao/diagramas/14-sequencia-uc020.drawio:488,524`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R13 part 1), Argon (R11, R23 part 1), Neon (R12)
- **Problema:** Inconsistências de schema da Área B reproduzidas na Área C:
  1. No diagrama relacional da Área C (`12-modelo-de-dados-area-c.drawio:59`), a tabela de referência `courses [Área B]` declara `status: text CHECK (draft, published)`, omitindo o valor `archived` estabelecido pela Área B e pela ADR-0014.
  2. Na sequência do UC020 (`14-sequencia-uc020.drawio:488`), a query faz `SELECT courses WHERE status='published' AND category='Programacao'`, mas a coluna `category` inexiste na tabela `courses` (a chave estrangeira é `category_id`). Na linha 524, a query usa a tabela no singular (`SELECT course, modules, lessons WHERE id`) em vez de `courses`.
- **Correção:** Incluir `archived` no `CHECK` de `courses.status` em `12-modelo-de-dados-area-c.drawio:59`; ajustar o SQL da linha 488 de `14-sequencia-uc020.drawio` para filtrar via `categories.name` (ou `category_id`) e corrigir `course` para `courses` na linha 524.

---

### C23
- **Gravidade:** `corrigir`
- **Área:** Área B
- **Arquivo:Linha:** `especificacao/07-estorias-de-usuario/area-b.md:31` vs `especificacao/10-especificacoes-de-caso-de-uso/area-b.md:193,225-230,262-265` (`UC014 R-4`, `E4`)
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R17)
- **Problema:** Na `US005` (*"Gerenciar módulos do curso"*, critério de aceite 3), o texto afirma que ao tentar excluir um módulo com aulas cadastradas o usuário apenas recebe aviso de que as aulas também serão removidas. Contudo, após os ajustes do RA2 motivados pela análise do professor, o `UC014 R-4` e a exceção `E4` passaram a **bloquear com HTTP 409 `CONFLICT`** a exclusão de módulo que contenha histórico de alunos (`lesson_progress` ou `quiz_attempts`), permitindo a exclusão em cascata somente quando não houver histórico. A `US005` não foi atualizada com essa regra de bloqueio.
- **Correção:** Atualizar o critério 3 da `US005` ressalvando que a exclusão em cascata aplica-se apenas a módulos sem histórico de alunos, e adicionar critério cobrindo o bloqueio por histórico acadêmico.

---

### C24
- **Gravidade:** `corrigir`
- **Área:** Área B
- **Arquivo:Linha:** `especificacao/diagramas/14-sequencia-uc006-2.drawio:326`, `especificacao/14-diagramas-de-sequencia/area-b.md:23`, `especificacao/15-casos-de-teste/area-b.md:15,70` (`TC094`, `TC116`)
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R21)
- **Problema:** Erros pontuais de referência e rótulos na Área B:
  1. Em `14-sequencia-uc006-2.drawio:326`, a guarda do fluxo de cancelamento de exclusão está rotulada como `[A3 - o Instrutor cancela a exclusão]`, mas no `UC006` o fluxo `A3` é o cancelamento do formulário de criação de curso (a exclusão e seu cancelamento estão modelados em `A2`, passo `A-2.3`).
  2. No texto explicativo `14-diagramas-de-sequencia/area-b.md:23`, a variável de camada de serviço/aplicação é grafada como `video_key` em `snake_case`.
  3. No caso de teste `TC094` (`area-b.md:15`), a resposta cita `(R-1)` para permissão de não proprietário, mas a regra R-1 do UC006 é status inicial rascunho; em `TC116` (`area-b.md:70`), cita `(R-1)` para UC004, cuja regra R-1 trata do mínimo de duas alternativas com uma correta.
- **Correção:** Ajustar o rótulo do fragmento em `14-sequencia-uc006-2.drawio:326` para `[A2 - o Instrutor cancela a exclusão]`; grafar `videoKey` em `14-diagramas-de-sequencia/area-b.md:23`; e corrigir a citação da regra em `TC094` e `TC116` para a respectiva exceção de autorização `(E3)`.

---

### C25
- **Gravidade:** `corrigir`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/13-diagrama-de-classes/area-a.md:28-29`, `especificacao/diagramas/14-sequencia-uc013-1.drawio:341`, `especificacao/diagramas/13-classes-area-a-implementacao-login.drawio:92`, `especificacao/diagramas/13-classes-area-a-negocial.drawio:23,65`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R16 part 1, 2; R20 part 2, 3)
- **Problema:** Lacunas e erros de formatação na Área A:
  1. Em `especificacao/13-diagrama-de-classes/area-a.md:28-29`, o método `- anonymize(id: UUID): void` está indentado como subitem de `RefreshSessionRepository` em vez de `UserRepository`, e cita `(UC018 R-2)` (proibição de autoexclusão) em vez de `(UC018 R-3, A3)`.
  2. Em `14-sequencia-uc013-1.drawio:341`, a instrução SQL grafa `INSERT ou UPDATE address` no singular em vez do nome da tabela `addresses`.
  3. `UserRepository` nos diagramas de implementação da Área A não declara `findById(id: UUID): ?User`, invocado pela Área D em `14-sequencia-uc018.drawio:836`.
  4. As entidades `Address` e `InstructorProfile` em `13-classes-area-a-negocial.drawio:23,65` não exibem o atributo `-deletedAt: ?DateTime`, apesar de possuírem `deleted_at: timestamptz` no modelo relacional do Item 12.
- **Correção:** Mover `anonymize` para o bloco de `UserRepository` em `area-a.md` e corrigir a regra citada; corrigir `address` para `addresses` em `14-sequencia-uc013-1.drawio:341`; declarar `+findById(id: UUID): ?User` em `UserRepository`; e incluir `-deletedAt: ?DateTime` nas entidades do diagrama negocial.

---

### C26
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `especificacao/15-casos-de-teste/area-d.md:70,71,84`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R22)
- **Problema:** Uso do termo abreviado `"Admin"` em vez do nome padronizado `"Administrador"` no Item 15 da Área D:
  - Linha 70 (`TC253`): `CT1 Aluno tenta acessar rota de Admin`
  - Linha 71 (`TC254`): `CT2 Instrutor tenta acessar rota de Admin`
  - Linha 84 (`TC260`): `3 – E1 Autoexclusão de Admin`
  Isso viola a regra 5 do `AGENTS.md` e a seção 2 do `CONTEXT.md` (uso estrito dos nomes exatos dos atores).
- **Correção:** Substituir `"Admin"` por `"Administrador"` nos títulos dos casos de teste e cenários em `especificacao/15-casos-de-teste/area-d.md`.

---

### C27
- **Gravidade:** `corrigir`
- **Área:** Área D
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/area-d.md:19,54`, `especificacao/diagramas/13-classes-area-d-implementacao-tutor-analytics.drawio:35,95,101,143`, `especificacao/diagramas/14-sequencia-uc001.drawio:533-554`
- **Classificação:** PARCIAL
- **Modelos que acharam:** Hydrogen (R8), Neon (R19 part 3)
- **Problema:** No `UC001 A3`, a compra de créditos de tutor exige pagamento simulado com `Payment.purpose = 'tutor_credits'`, gerando um `payment_id NOT NULL` na tabela `tutor_credit_packs`. Porém, `TutorService.buyCreditPack` não aciona `PaymentService` (Área C) e `TutorCreditPackRepository.create` omite o parâmetro `paymentId`. Além disso, a classe `BuyCreditPackRequest` (`tutor-analytics.drawio:35`) declara `+paymentMethod: string`, divergindo do padrão de pagamento simulado da Área C (`PaymentDTO` usa `+confirmPayment: boolean`), e na sequência `14-sequencia-uc001.drawio:533-554` `TutorService` valida matrícula e indexação gerando 403 e 409 sem explicitar as chamadas aos Services das Áreas B e C. *(Nota: a alegação de violação modular por consulta via Repositories é improcedente, pois a decisão entre áreas em `ra2-relatorio-areas-abcd.md` permite expressamente leitura via Repositories).*
- **Correção:** Integrar `TutorService` com `PaymentService` (Área C) na compra de créditos, adicionar `paymentId: UUID` em `TutorCreditPackRepository.create`, substituir `paymentMethod` por `confirmPayment: boolean` em `BuyCreditPackRequest` e explicitar chamadas aos Services de Authoring/Learning em `14-sequencia-uc001.drawio`.

---

### C28
- **Gravidade:** `sugestão`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/14-diagramas-de-sequencia/00-item.md:5` vs `especificacao/diagramas/14-sequencia-uc005.drawio:8,41,44,482`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Argon (R24), Neon (R20 part 4)
- **Problema:** O texto de abertura do Item 14 (`00-item.md:5`) estipula que *"cada fluxo de exceção vira uma região de um fragmento `alt`; cada fluxo alternativo também é um `alt`... sem `opt` seguido de continuação"*. Entretanto, em `14-sequencia-uc005.drawio`, o fluxo alternativo A2 (`frame_2`), a exceção E2 (`frame_10`) e o alternativo A1 (`frame_11`) foram representados com fragmentos `opt` em vez de `alt`.
- **Correção:** Converter os fragmentos `opt` em regiões de fragmentos `alt` em `14-sequencia-uc005.drawio` (ou documentar no `00-item.md` que desvios independentes e opcionais de tela podem usar `opt`).

---

### C29
- **Gravidade:** `sugestão`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/13-diagrama-de-classes/area-a.md:24`, `especificacao/13-diagrama-de-classes/area-d.md:7`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Hydrogen (R16)
- **Problema:** O tipo `UserFiltersDTO` é referenciado nas assinaturas de `UserRepository.paginate(filters: UserFiltersDTO)` e `UserAdminService.paginateUsers(...)`, mas não possui caixa de classe ou DTO modelada em nenhum dos diagramas do Item 13 (a Área D modela apenas a classe `ListUsersRequest`).
- **Correção:** Modelar a classe `UserFiltersDTO` no diagrama da Área A ou explicitar que `UserRepository.paginate` consome diretamente os filtros validados da camada de apresentação.

---

### C30
- **Gravidade:** `sugestão`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/14-diagramas-de-sequencia/area-{b,c,d}.md`, `especificacao/15-casos-de-teste/area-{b,c,d}.md`, `especificacao/12-modelo-de-dados/area-d.md:25-32`, `especificacao/14-diagramas-de-sequencia/area-d.md:41-48`, `docs/adr/0013-diagramas-do-ra2-em-drawio.md:36`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R24), Hydrogen (R19 part 2)
- **Problema:** Pequenos desvios de padronização editorial no documento compilado:
  1. Nos itens 14 e 15, os arquivos das Áreas B, C e D reiniciam a numeração em `## 1.`, gerando títulos duplicados no DOCX/PDF unificado.
  2. As subseções de encerramento de pendências internas do GitHub (`### Resolução das pendências cruzadas da Área A (Issue #122)` e `#123`) em `12-modelo-de-dados/area-d.md` e `14-diagramas-de-sequencia/area-d.md` entram no documento final.
  3. A `ADR-0013:36` ainda prescreve diagramas de classes em *"preto e branco"*, enquanto os 14 diagramas entregues adotaram com sucesso preenchimento pastel por papel arquitetural.
  4. Casos de teste das Áreas A e C omitem o prefixo `/api/v1` em parte das rotas.
- **Correção:** Harmonizar a hierarquia de títulos nos itens 14 e 15; mover o histórico de issues para a pasta `entregas/`; atualizar a ADR-0013 para formalizar as cores pastéis por papel; e padronizar o prefixo `/api/v1` nos TCs.

---

### C31
- **Gravidade:** `sugestão`
- **Área:** Área A
- **Arquivo:Linha:** `especificacao/10-especificacoes-de-caso-de-uso/area-a.md:259-261`, `especificacao/diagramas/13-classes-area-a-negocial.drawio:56`, `13-classes-area-d-negocial.drawio:257`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Neon (R25), Argon (R19 part 3)
- **Problema:**
  1. A legenda e alt-text do protótipo `UC013-E3-1.png` (`area-a.md:259-261`) dizem *"acesso negado à edição de perfil de **outro Instrutor**"*, enquanto o fluxo `E3` descreve tentativa de edição por **Aluno ou Administrador**.
  2. O enumerador `Locale` exibe apenas o valor ativo `pt-BR` no diagrama da Área A (com nota explicativa), enquanto o diagrama da Área D exibe `pt-BR`, `en` e `es`.
- **Correção:** Ajustar a legenda do protótipo para *"acesso negado à edição de perfil de Instrutor por Aluno ou Administrador"* e padronizar os valores exibidos do enum `Locale`.

---

### C32
- **Gravidade:** `sugestão`
- **Área:** Área B
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/area-b.md:28-84`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R20)
- **Problema:** As tabelas da Área B no dicionário de dados do Item 12 (`categories`, `courses`, `modules`, `lessons`, `lesson_materials`, `quizzes`, `questions`, `question_options`) omitem as colunas de auditoria temporal `created_at` e `updated_at: timestamptz`, que constam nas tabelas das demais áreas e são geradas por padrão pelo ORM.
- **Correção:** Acrescentar `created_at: timestamptz` e `updated_at: timestamptz` nas tabelas de negócio do dicionário e diagrama da Área B.

---

### C33
- **Gravidade:** `sugestão`
- **Área:** Área C
- **Arquivo:Linha:** `especificacao/12-modelo-de-dados/area-c.md:32-42`, `especificacao/diagramas/12-modelo-de-dados-area-c.drawio:77,104,107,116,125`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R21), Hydrogen (R13 part 2), Argon (R23 part 2)
- **Problema:**
  1. A tabela `payments` possui `paid_at: timestamptz` (preenchido apenas quando o status é `approved`), mas não define a coluna `created_at: timestamptz`. Em transações com status recusado (`declined`), a tentativa de pagamento fica sem registro de data e hora no banco de dados.
  2. No diagrama `12-modelo-de-dados-area-c.drawio`, a notação de obrigatoriedade está invertida: as colunas anuláveis `course_id: uuid (NULL)`, `enrollment_id: uuid (NULL)` e `paid_at: timestamptz` em `payments` estão em negrito (indicando `NOT NULL`), enquanto colunas obrigatórias como `payments.amount_cents`, `payments.currency`, `enrollments.price_paid_cents` e `enrollments.currency` estão sem negrito.
- **Correção:** Adicionar `created_at: timestamptz NOT NULL` na tabela `payments` e corrigir o negrito das colunas em `12-modelo-de-dados-area-c.drawio`.

---

### C34
- **Gravidade:** `sugestão`
- **Área:** Geral
- **Arquivo:Linha:** `especificacao/README.md:3`
- **Classificação:** CONFIRMADO
- **Modelos que acharam:** Flash (R24)
- **Problema:** O texto introdutório de `especificacao/README.md:3` afirma *"Esqueleto dos 11 itens do template da disciplina"*, enquanto a tabela imediatamente abaixo e a entrega consolidada abrangem os 15 itens do projeto.
- **Correção:** Atualizar o texto para *"Esqueleto dos 15 itens do template da disciplina"*.

---

### C35
- **Gravidade:** `sugestão`
- **Área:** TDD e Testes
- **Arquivo:Linha:** `docs/tdd.md:5-6,687`
- **Classificação:** PARCIAL
- **Modelos que acharam:** Neon (R18)
- **Problema:** O cabeçalho YAML de `docs/tdd.md:5-6` mantém `status: rascunho` e `atualizado: 2026-10-08`, data anterior à incorporação das decisões do RA2. *(Ressalva: a alegação de haver um 'hífen solto' na linha 687 é improcedente; trata-se de um divisor temático padrão Markdown `---` entre seções).*
- **Correção:** Atualizar os metadados de status e data no frontmatter de `docs/tdd.md`.

---

## 3. Lista de Achados Falsos (Falsos Positivos)

1. **F1 · `flash-R19`** (`especificacao/15-casos-de-teste/`): **FALSO** — A alegação de descontinuidade acidental entre as faixas reservadas por integrante (TC125 a TC150 entre B e C, TC198 a TC210 entre C e D) é improcedente; a partição de blocos numéricos por área (Área B: 091–124, Área C: 151–197, Área D: 211–272) foi uma decisão deliberada de planejamento da equipe para evitar colisões entre os integrantes no RA2.
2. **F2 · `flash-R23`** (`especificacao/diagramas/14-sequencia-uc008.drawio:1`, `14-sequencia-uc018.drawio:1`): **FALSO** — A alegação de que `UserAdminService` violou a ADR-0018 por acessar repositórios da Área A contradiz frontalmente a decisão expressa e homologada entre as áreas em `entregas/ra2-relatorio-areas-abcd.md:3`, que estabelece categoricamente: *"leitura entre módulos só por Services ou Repositories"*.
3. **F3 · `argon-R10`** (`docs/adr/0018-core-como-monolito-modular.md:30`): **FALSO** — A alegação de violação modular pelo acesso de Admin aos repositórios de Auth contradiz a decisão conjunta das quatro áreas em `entregas/ra2-relatorio-areas-abcd.md:3` (*"leitura entre módulos só por Services ou Repositories"*), sendo o acesso aos repositórios de Auth deliberado e autorizado entre as áreas.
4. **F4 · Saltos numéricos `TC271`/`TC272`** (apontamentos diversos): **FALSO** — A instrução geral explicita expressamente que *"a faixa D usa TC271/TC272 de propósito"* para os cenários finais de anonimização e cascata de arquivamento (`area-d.md:93-94`), sendo numeração intencional e válida.
5. **F5 · Numeração `"Figura 0"`** (apontamentos diversos): **FALSO** — A instrução geral explicita que *"legendas 'Figura 0' são intencionais (build renumera)"*, pois o compilador `scripts/build_doc.py:91-105` renumera automaticamente todas as figuras sequencialmente no documento final DOCX/PDF.

---

## 4. Correções aplicadas

Todas as correções foram aprovadas pelo grupo antes de começar, foram feitas por área (cada commit tem o autor da área) e conferidas pelo coordenador.

- [x] C1: matriz de `docs/testes/cobertura.md` refeita a partir dos itens 15, com UC001 em TC211 a TC221.
- [x] C2: índices dos itens 12 a 15 preenchidos para as Áreas B, C e D.
- [x] C3: US022 no índice do item 7, RF020 na tabela do item 9 e na descrição do UC001.
- [x] C4: [ADR-0019](../docs/adr/0019-upload-pela-api.md) (upload pela API, chave no banco, leitura por URL assinada) substitui o item 3 da ADR-0010.
- [x] C5: seção 2 do `docs/tdd.md` reescrita a partir dos itens 12 e 13 (23 tabelas).
- [x] C6: envelope de paginação do TDD com `total` e `lastPage`.
- [x] C7: tabela do RA1 em `docs/testes/casos-de-teste.md` marcada como histórico; TC048 substituído pelos casos do UC018.
- [x] C8: `CourseService.softDeleteAllByInstructor`, `alt` de arquivar ou excluir em cascata no UC018 e TC273.
- [x] C9: conta excluída ou anonimizada recebe o mesmo 401 genérico no UC005, na sequência, nos casos de teste e no TDD.
- [x] C10: SQL e dados pessoais da anonimização no UC018; endereços sobrescritos com `deleted_at`, sem `DELETE` físico.
- [x] C11: `position` em todas as camadas da Área B e no TDD.
- [x] C12: sem volta a rascunho com matriculados; `Course.archive()` no lugar de `unpublish()`.
- [x] C13: `PhotoStorage` sem URL pública.
- [x] C14: tipos PostgreSQL em minúsculas nos dicionários e nos diagramas das quatro áreas.
- [x] C15 e C16: classes e retornos da Área D alinhados com a Área A.
- [x] C17: tipo do elemento corrigido (`User` abstrata, `JwtGuard` interface, `GroupBy` enumeração).
- [x] C18: parâmetro `search`, filtro `status` e `{id}` nas rotas de usuários.
- [x] C19 e C34: nomes do glossário nos itens 2 e 5; README com 15 itens.
- [x] C20: rótulos internos de trabalho trocados por ADR, RF ou RNF.
- [x] C21: cenários duplicados do UC018 corrigidos; IDs descartados registrados sem renumerar.
- [x] C22, C24, C25, C32 e C33: modelos de dados das Áreas A, B e C (colunas, CHECK, `created_at` e `updated_at`).
- [x] C23: critérios da US005.
- [x] C26: "Administrador" nos casos de teste da Área D.
- [x] C27: compra de créditos via `PaymentService` da Área C.
- [x] C28: fluxos do UC005 em `alt`; os `opt` que restam são passos condicionais.
- [x] C29: `UserFiltersDTO` no diagrama de perfil da Área A.
- [x] C30: ADR-0013 aceita cor por papel no item 13; títulos dos itens 14 e 15 e prefixo `/api/v1` padronizados; seções das issues #122 e #123 retiradas.
- [x] C31: legenda do protótipo UC013-E3-1 e `Locale` igual nas Áreas A e D.
- [x] C35: TDD com status vigente.

Conferência mecânica: 0 links relativos quebrados, todo `.drawio` com PNG, nenhum PNG cortado e nenhum ID de caso de teste repetido.
