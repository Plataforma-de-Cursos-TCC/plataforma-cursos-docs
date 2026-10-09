---
titulo: "Propostas de Preenchimento de Lacunas e UCs Faltantes"
tipo: proposta
status: rascunho
atualizado: 2026-10-07
origem: v11.md + _lacunas.md
---

# Propostas de Preenchimento de Lacunas e UCs Faltantes

> **Nota sobre "v11":** as citações da v11 neste arquivo são registro histórico do rascunho anterior ao repositório (ver [ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md)). A fonte vigente é `especificacao/`.

> **Regra:** tudo aqui é **proposta** (marcado com `<!-- proposta: ... -->`). O grupo decide o que incorporar.
>
> **Atualização de 08/10/2026:** os IDs provisórios e a ideia de realocar RFs entre áreas foram superados pela [ADR-0001](../docs/adr/0001-minimo-por-integrante-e-numeracao-provisoria.md): fica a numeração da v11, com IDs novos no fim. A proposta RF-A4 (pagamento simulado) foi descartada por repetir o RF014. Ver [pendencias-revisao](pendencias-revisao.md).

---

## 1. Lacuna — Item 06, Área A: faltam 2 RFs (mínimo 4)

**Contexto:** Área A (Acesso e conta) tem RF-A1/RF001 e RF-A2/RF013. v11 cita RF012 (Gerenciar acesso por perfil) e RF014 (Pagamento simulado) como Must Have na Sprint 1, sem RF próprio na área A. US015/US016/US018 já existem.

### Candidato 1 — RF-A3 / RF012-An: Verificar permissão de acesso a rota (extensão de RF012)

| Campo | Valor |
|---|---|
| **ID provisório** | RF-A3 (próximo livre na área A) |
| **Texto do requisito** | Verificar permissão de acesso a rota protegida com base no perfil (aluno/instrutor/admin) e registrar tentativa negada em trilha de auditoria. |
| **Ator** | Aluno, Instrutor, Administrador (sistema executa automaticamente) |
| **Justificativa** | RF012 ("Gerenciar acesso de usuários por perfil") cobre criação/edição de perfis, mas a **verificação contínua em tempo de execução** (middleware de autorização) é implícita em UC005 (fluxo E2), UC016 (regras R-2/R-3) e RNF001/RNF016. Ainda não virou RF próprio. |
| **Citação da v11** | **UC005 (Realizar Login), Fluxo de exceção E2:** "E-2.1 O sistema identifica que o token JWT do usuário expirou. E-2.2 O sistema redireciona o usuário para a tela de login." — **UC016 (Acessar Área Protegida por Perfil), Regras de negócio:** "R-2 100% das rotas protegidas verificam o perfil (RNF001); R-3 toda negação de acesso é registrada na trilha de auditoria (RNF016)." — **UC016, Fluxo de exceção E2:** "E-2.2 O sistema nega o acesso, informa a restrição e registra a tentativa na trilha de auditoria." |

### Candidato 2 — RF-A4 / RF014-An: Processar pagamento simulado da matrícula (RF014 já listado, mas sem RF na área A)

| Campo | Valor |
|---|---|
| **ID provisório** | RF-A4 (próximo livre na área A) |
| **Texto do requisito** | Processar pagamento simulado (aprovado/recusado) na matrícula de curso pago, sem gateway externo, e condicionar a criação da matrícula ao resultado. |
| **Ator** | Aluno |
| **Justificativa** | RF014 aparece na tabela de RFs (Sprint 1, Must Have, UC003) mas não foi alocado a nenhuma área como RF próprio. O fluxo está em UC003 (passo 3, alternativas A2/E2) e US018. |
| **Citação da v11** | **RF014 na tabela de RFs:** "RF014 | Registrar pagamento simulado da matrícula | Aluno | Sprint 1 | UC003 | Must Have | Cobre o fluxo de curso pago sem gateway real." — **UC003 (Matricular-se em Curso), Fluxo básico passo 3:** "O sistema processa o pagamento simulado. (E-1) (E-2)" — **UC003, Alternativa A2 (curso gratuito):** "A-2.2 O sistema registra a matrícula sem executar o passo de pagamento." — **UC003, Exceção E2:** "E-2.1 O sistema identifica falha no processamento do pagamento simulado. E-2.2 O sistema informa o erro ao aluno e não registra a matrícula." — **US018 (RF014), Critérios 1-3.** |

---

## 2. Lacuna — Item 06, Área D: falta 1 RF (mínimo 4)

**Contexto:** Área D tem RF-D1/RF009, RF-D2/RF010, RF-D3/RF012. v11 cita RF011 (Avaliar curso) e RF010 (Dashboard) como da área D (Sprint 3/4), mas só RF010 está coberto (UC-D2). RF011 não tem RF na área D.

### Candidato 1 — RF-D4 / RF011-An: Registrar avaliação do curso pelo aluno

| Campo | Valor |
|---|---|
| **ID provisório** | RF-D4 (próximo livre na área D) |
| **Texto do requisito** | Permitir que aluno matriculado avalie o curso com nota 1–5 e comentário opcional, substituindo avaliação anterior se houver, e recalcular nota média do curso. |
| **Ator** | Aluno |
| **Justificativa** | RF011 está na tabela (Sprint 3, Could Have, UC010) e UC010 existe, mas não há RF da área D para cobri-lo. US014 detalha os critérios. |
| **Citação da v11** | **RF011 na tabela de RFs:** "RF011 | Registrar avaliação do curso | Aluno | Sprint 3 | UC010 | Could Have | Gera feedback sobre os cursos." — **UC010 (Avaliar Curso), Descrição:** "o aluno avalia um curso em que está matriculado com nota de 1 a 5 e comentário opcional." — **UC010, Regras de negócio:** "só é possível 1 avaliação ativa por aluno por curso (nova avaliação substitui a anterior); nota é obrigatória, comentário é opcional." — **UC010, Fluxo alternativo A1:** "O sistema pré-preenche o formulário com a avaliação existente, pronta pra edição... atualizando a avaliação existente em vez de criar uma nova." — **US014 (RF011), Critérios 1-3.** |

---

## 3. Lacuna — Item 08, Área A: falta 1 RNF (mínimo 4)

**Contexto:** Área A tem RNF-A1/RNF001, RNF-A2/RNF007, RNF-A3/RNF008. v11 tem RNF016 (Trilha de auditoria) citada em UC016 (regra R-3) e UC008 (exclusão de usuário), mas não alocada à área A.

### Candidato 1 — RNF-A4 / RNF016-An: Trilha de auditoria das ações administrativas e de acesso negado

| Campo | Valor |
|---|---|
| **ID provisório** | RNF-A4 (próximo livre na área A) |
| **Texto do requisito** | Registrar automaticamente 100% das ações administrativas (bloqueio/exclusão de usuários, alteração de perfis) e toda negação de acesso a rotas protegidas, com retenção de 12 meses. |
| **Ator** | Administrador (sistema registra automaticamente) |
| **Justificativa** | RNF016 aparece na tabela de RNFs (Segurança) e é referenciada em UC016 (regra R-3) e UC008 (exclusão anonimizada mantém histórico). Área A (acesso/conta) é onde essas auditorias ocorrem. |
| **Citação da v11** | **RNF016 na tabela de RNFs:** "RNF016 | Trilha de auditoria das ações administrativas | Segurança | Registro de 100% das ações administrativas, retido por 12 meses." — **UC016 (Acessar Área Protegida por Perfil), Regras de negócio R-3:** "toda negação de acesso é registrada na trilha de auditoria (RNF016)." — **UC008 (Gerenciar Usuários), Fluxo básico passo 4:** "O sistema aplica a mudança de status... acesso do usuário é revogado ou restaurado imediatamente." — **UC008, Critério 3 (US016):** "ENTÃO seus dados pessoais são removidos mas o histórico de matrícula/pagamento permanece anonimizado." |

---

## 4. Lacuna — Item 08, Área B: falta 1 RNF (mínimo 4)

**Contexto:** Área B tem RNF-B1/RNF002, RNF-B2/RNF006, RNF-B3/RNF015. v11 tem RNF004 (Cache de transcrição/embeddings) citada em UC015 (regra R-4) e no Mapeamento de Negócios, mas não alocada à área B (conteúdo/aulas).

### Candidato 1 — RNF-B4 / RNF004-An: Cache de transcrição e embeddings por aula (sem reprocessamento)

| Campo | Valor |
|---|---|
| **ID provisório** | RNF-B4 (próximo livre na área B) |
| **Texto do requisito** | Garantir que a transcrição e os embeddings de cada aula sejam gerados uma única vez no upload/edição do vídeo, armazenados em cache, e reutilizados em todos os acessos subsequentes do tutor de IA, sem reprocessamento. |
| **Ator** | Sistema (processamento assíncrono) |
| **Justificativa** | RNF004 está na tabela (Eficiência de Desempenho) e é regra explícita em UC015 (R-4) e no Mapeamento de Negócios. Área B (conteúdo/curso) é onde o upload e processamento de vídeo ocorrem. |
| **Citação da v11** | **RNF004 na tabela de RNFs:** "RNF004 | Transcrição e embeddings gerados uma única vez por aula (cache), sem reprocessar a cada acesso | Eficiência de Desempenho | 0 reprocessamentos em acessos repetidos à mesma aula." — **UC015 (Gerenciar Aulas do Curso), Regras de negócio R-4:** "a transcrição e os embeddings são gerados uma única vez por aula (RNF004)." — **Mapeamento de Negócios, raia Plataforma e Tutor de IA:** "a plataforma... armazena, transcreve e indexa as aulas... o tutor de IA busca trechos do curso e responde com citação de origem". — **UC001 (Conversar com Tutor de IA), Pré-condições:** "aula já transcrita e indexada (embeddings gerados)." |

---

## 5. UC Faltante — RF015 (Consultar catálogo e buscar cursos por categoria)

**Contexto:** RF015 está na tabela de RFs (Sprint 2, Should Have) com "Sem UC (lacuna)". US019 existe com 3 critérios de aceite. Área sugerida: B (conteúdo/catálogo).

### Esqueleto de UC — UC-B5 (UC017): Consultar Catálogo e Buscar Cursos

<!-- proposta: UC para RF015 baseado em US019; área B (conteúdo); IDs livres UC-B5/UC017 -->

| Campo | Valor |
|---|---|
| **Nome do caso de uso** | Consultar Catálogo e Buscar Cursos |
| **Ator(es)** | Visitante, Aluno |
| **Descrição** | O visitante ou aluno acessa o catálogo público, visualiza cursos publicados com título, instrutor e preço, filtra por categoria e busca por termo, obtendo lista filtrada ou mensagem de vazio. |
| **Pré-condições** | Catálogo contém ao menos um curso com status publicado. |
| **Pós-condições** | Lista de cursos exibida conforme filtros/termo; nenhum estado de erro para busca sem resultado (mensagem amigável). |
| **Regras de negócio** | R-1 Somente cursos com status "publicado" aparecem no catálogo. R-2 Filtro por categoria restringe a lista aos cursos daquela categoria. R-3 Busca por termo aplica-se a título, descrição e nome do instrutor. R-4 Visitante não autenticado vê preço e instrutor, mas não acessa aulas sem matrícula (exceto prévias). |
| **Protótipo(s) de tela** | Página de catálogo com grade de cards (título, instrutor, preço, categoria), barra de busca, filtros laterais por categoria/nível/preço. Imagem do protótipo pendente. |
| **Fluxo básico** | 1. O ator acessa a página do catálogo. (A-1) 2. O sistema exibe cards dos cursos publicados com título, instrutor e preço. 3. O ator opcionalmente seleciona uma categoria no filtro. (A-2) 4. O ator opcionalmente digita termo na busca e aciona enter. (A-3) 5. O sistema filtra a lista e exibe resultados. 6. Este caso de uso é finalizado. |
| **Fluxos alternativos** | **A1 – Filtro por categoria**<br>A-1.1 O ator seleciona uma categoria.<br>A-1.2 O sistema restringe a lista aos cursos da categoria.<br>A-1.3 Retorna ao fluxo básico (passo 5).<br><br>**A2 – Busca por termo**<br>A-2.1 O ator digita termo e aciona busca.<br>A-2.2 O sistema aplica busca em título, descrição e instrutor.<br>A-2.3 Retorna ao fluxo básico (passo 5). |
| **Fluxos de exceção** | **E1 – Nenhum curso publicado**<br>E-1.1 O sistema identifica catálogo vazio (sem cursos publicados).<br>E-1.2 Exibe mensagem "Nenhum curso disponível no momento" com CTA para voltar depois.<br>E-1.3 Caso de uso finalizado.<br><br>**E2 – Busca sem resultado**<br>E-2.1 O sistema identifica zero resultados para o termo/filtr<br>E-2.2 Exibe mensagem "Nenhum curso encontrado para '<termo>'" com sugestão de limpar filtros.<br>E-2.3 Caso de uso finalizado (não é erro). |
| **Origem da proposta** | US019 (RF015): "Como visitante ou aluno, quero consultar o catálogo e buscar cursos por categoria..." — Critérios 1, 2, 3. |

---

## 6. UC Faltante — RF016 (Gerenciar perfil do instrutor)

**Contexto:** RF016 está na tabela de RFs (Sprint 2, Could Have) com "Sem UC (lacuna)". US020 existe com 3 critérios de aceite. Área sugerida: A (acesso/conta) ou C (instrutor/curso) — aqui colocada em A por ser perfil de usuário.

### Esqueleto de UC — UC-A5 (UC018): Gerenciar Perfil do Instrutor

<!-- proposta: UC para RF016 baseado em US020; área A (acesso/conta); IDs livres UC-A5/UC018 -->

| Campo | Valor |
|---|---|
| **Nome do caso de uso** | Gerenciar Perfil do Instrutor |
| **Ator(es)** | Instrutor |
| **Descrição** | O instrutor autenticado edita seu perfil público (minibiografia, headline, links de redes sociais) que é exibido na página de seus cursos. |
| **Pré-condições** | Usuário autenticado com perfil instrutor (role=instrutor). |
| **Pós-condições** | Perfil do instrutor atualizado e refletido nas páginas de cursos onde ele aparece. |
| **Regras de negócio** | R-1 Só o próprio instrutor edita seu perfil (outro instrutor/admin recebe acesso negado). R-2 Links de redes sociais devem ser URLs válidas (formato https://...). R-3 Campos: bio (texto livre, máx. 500 chars), headline (máx. 150 chars), socialLinks (JSON com label+URL). R-4 Perfil não publicado se instrutor não tiver cursos publicados (regra de exibição). |
| **Protótipo(s) de tela** | Tela "Meu perfil de instrutor" com campos: minibiografia (textarea), headline (input), lista de links sociais (adicionar/remover), botão "Salvar". Imagem do protótipo pendente. |
| **Fluxo básico** | 1. O instrutor acessa "Meu perfil de instrutor" no menu da área do instrutor. 2. O instrutor preenche/altera minibiografia, headline e links sociais. (A-1) 3. O instrutor aciona "Salvar". 4. O sistema valida formato dos links (URLs válidas). (E-1) 5. O sistema salva o perfil e confirma a atualização. 6. Este caso de uso é finalizado. |
| **Fluxos alternativos** | **A1 – O instrutor adiciona/remove link social**<br>A-1.1 O instrutor clica "Adicionar link" e informa label + URL.<br>A-1.2 O sistema valida URL e adiciona à lista.<br>A-1.3 Retorna ao fluxo básico (passo 2).<br><br>**A2 – O instrutor limpa o perfil**<br>A-2.1 O instrutor apaga todos os campos e salva.<br>A-2.2 O sistema salva perfil vazio (não exibido em cursos).<br>A-2.3 Retorna ao fluxo básico (passo 5). |
| **Fluxos de exceção** | **E1 – Link em formato inválido**<br>E-1.1 O sistema identifica URL malformada ou sem https://.<br>E-1.2 Bloqueia o salvamento e indica o campo com erro.<br>E-1.3 Retorna ao fluxo básico (passo 2).<br><br>**E2 – Acesso indevido**<br>E-2.1 Aluno ou administrador tenta acessar a URL de edição de perfil de instrutor.<br>E-2.2 O sistema nega acesso (RNF001/RNF016) e redireciona à área do usuário.<br>E-2.3 Caso de uso finalizado. |
| **Origem da proposta** | US020 (RF016): "Como instrutor, quero gerenciar meu perfil de instrutor, para que eu possa apresentar minha formação e minhas redes aos alunos." — Critérios 1, 2, 3. |

---

## Resumo das Propostas

| Lacuna / Item | Proposta | ID Provisório | Status |
|---|---|---|---|
| 06-A (falta 2 RFs) | Verificar permissão de acesso a rota (middleware) | RF-A3 / RF012-An | Proposta |
| 06-A (falta 2 RFs) | Processar pagamento simulado na matrícula | RF-A4 / RF014-An | Proposta |
| 06-D (falta 1 RF) | Registrar avaliação do curso | RF-D4 / RF011-An | Proposta |
| 08-A (falta 1 RNF) | Trilha de auditoria de ações admin/acesso | RNF-A4 / RNF016-An | Proposta |
| 08-B (falta 1 RNF) | Cache de transcrição/embeddings por aula | RNF-B4 / RNF004-An | Proposta |
| RF015 (sem UC) | UC Consultar Catálogo e Buscar Cursos | UC-B5 / UC017 | Proposta |
| RF016 (sem UC) | UC Gerenciar Perfil do Instrutor | UC-A5 / UC018 | Proposta |

**Total:** 7 propostas (5 RFs/RNFs + 2 UCs). Todas apoiadas em citações literais da v11.
---

## Correção da revisão (orquestrador)

Quatro das cinco propostas de lacuna repetem requisitos que já estão alocados em outra área. Se fossem incorporadas como estão, o mesmo requisito da v11 apareceria duas vezes:

| Proposta | Já existe como |
|---|---|
| RF-A4 (RF014, pagamento simulado) | RF-C5 |
| RF-D4 (RF011, avaliação do curso) | RF-C4 |
| RNF-A4 (RNF016, trilha de auditoria) | RNF-D6 |
| RNF-B4 (RNF004, cache de transcrição e embeddings) | RNF-D2 |

Por isso essas quatro devem ser lidas como **propostas de realocação**, não como requisitos novos. As áreas C (6 RFs) e D (6 RNFs) têm sobra e continuariam com o mínimo de 4 depois de ceder um ou dois itens. A única proposta que acrescenta um requisito novo é a RF-A3 (verificação de permissão por rota, derivada do UC016).

Uma alternativa de realocação que respeita melhor o escopo de cada área:
- RF-D3 (RF012, gerenciar acesso por perfil) passa para a área A, que é "Acesso e conta".
- RF-C4 (RF011, avaliação do curso) passa para a área D, que é "analytics".
- A área D ainda ficaria com 3 RFs. O grupo precisaria escolher entre aceitar a RF-A3 nova, mover outro RF ou escrever um RF novo para a D.

Isso é decisão do grupo.

Os IDs dos UCs propostos também precisam seguir a área do RF que cobrem:
- RF015 é RF-C6, então o UC proposto seria **UC-C5** (e não UC-B5).
- RF016 é RF-B5, então o UC proposto seria **UC-B5** (e não UC-A5).

Os detalhes que não estão na v11 são invenção do proponente e precisam de validação do grupo:
- os limites de caracteres e o formato `socialLinks` no UC de perfil;
- os filtros por nível e preço no UC de catálogo.
