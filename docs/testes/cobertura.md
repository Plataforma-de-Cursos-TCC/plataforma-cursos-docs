---
id: testes-cobertura
titulo: "Cobertura de testes"
tipo: documento-projeto
status: vigente
atualizado: 2026-11-22
---
# Cobertura de testes

As medições de cobertura de código serão coletadas automaticamente e registradas a cada execução do pipeline de integração contínua (CI) no repositório de implementação, tendo como meta mínima 75% de cobertura no backend e no frontend conforme estabelecido no RNF006 e no RNF021 e na [Estratégia de testes](estrategia.md).

## 1. Rastreabilidade de Casos de Uso e Estórias de Usuário

A tabela a seguir apresenta a matriz de rastreabilidade entre os requisitos funcionais, estórias de usuário, casos de uso e os respectivos casos de teste documentados no item 15 da especificação ([casos de teste](../../especificacao/15-casos-de-teste/00-item.md)). A tabela do RA1 em [casos-de-teste.md](casos-de-teste.md) fica como histórico. Os IDs TC054, TC111, TC115, TC237 e TC267 foram descartados durante a revisão e não são reaproveitados; a numeração não foi refeita para não quebrar referências:

| Caso de Uso (UC) | Estória de Usuário (US) | Requisito Funcional (RF) | Casos de Teste Associados | Status de Cobertura |
|---|---|---|---|---|
| UC001 – Conversar com Tutor de IA | US012, US022 | RF009, RF020 | TC211, TC212, TC213, TC214, TC215, TC216, TC217, TC218, TC219, TC220, TC270, TC278 | Coberto |
| UC002 – Responder Quiz | US011 | RF008 | TC031, TC032, TC033, TC164, TC165, TC166, TC167, TC168, TC179, TC180, TC181, TC182, TC183, TC190, TC191, TC192, TC193 | Coberto |
| UC003 – Matricular-se em Curso | US007 | RF005 | TC019, TC020, TC021, TC151, TC152, TC153, TC154, TC184, TC185, TC186 | Coberto |
| UC004 – Cadastrar Quiz com Gabarito | US010 | RF007 | TC028, TC029, TC030, TC112, TC113, TC114, TC116, TC117 | Coberto |
| UC005 – Realizar Login | US001 | RF017 | TC001, TC002, TC003, TC065, TC066, TC067, TC068, TC069, TC070, TC071 | Coberto |
| UC006 – Cadastrar Curso | US004 | RF002 | TC010, TC011, TC012, TC091, TC092, TC093, TC094, TC095, TC123, TC124 | Coberto |
| UC007 – Ver Dashboard com Filtro | US013 | RF010 | TC221, TC222, TC223, TC224, TC225, TC226, TC227, TC228, TC229, TC230 | Coberto |
| UC008 – Gerenciar Usuários | US016 | RF012 | TC231, TC232, TC233, TC234, TC235, TC236, TC238, TC239, TC240, TC241, TC242, TC243, TC244, TC245, TC246 | Coberto |
| UC009 – Assistir Aula | US008, US009 | RF006 | TC022, TC023, TC024, TC025, TC026, TC027, TC159, TC160, TC161, TC162, TC163 | Coberto |
| UC010 – Avaliar Curso | US014 | RF011 | TC040, TC041, TC042, TC169, TC170, TC171, TC172, TC173 | Coberto |
| UC011 – Recuperar Senha | US017 | RF013 | TC049, TC050, TC051, TC072, TC073, TC074, TC075, TC076, TC090 | Coberto |
| UC012 – Cadastrar-se na Plataforma | US002 | RF001 | TC004, TC005, TC006, TC077, TC078, TC079 | Coberto |
| UC013 – Editar Dados do Perfil | US003, US020 | RF001, RF016 | TC007, TC009, TC058, TC059, TC060, TC080, TC081, TC082, TC083, TC084, TC085, TC086, TC087 | Coberto |
| UC014 – Gerenciar Módulos do Curso | US005 | RF003 | TC013, TC014, TC015, TC096, TC097, TC098, TC099, TC100, TC101, TC102 | Coberto |
| UC015 – Gerenciar Aulas do Curso | US006 | RF004 | TC016, TC017, TC018, TC103, TC104, TC105, TC106, TC107, TC108, TC109, TC110, TC118, TC119, TC120, TC121, TC122 | Coberto |
| UC016 – Acessar Área Protegida por Perfil | US015 | RF018 | TC247, TC248, TC249, TC250, TC251, TC252, TC253, TC254, TC255, TC256 | Coberto |
| UC017 – Alterar Senha | US021 | RF019 | TC061, TC062, TC064, TC088, TC089 | Coberto |
| UC018 – Excluir e Anonimizar Usuário | US016 | RF012 | TC257, TC258, TC259, TC260, TC261, TC262, TC263, TC264, TC265, TC266, TC268, TC269, TC271, TC272, TC273 | Coberto |
| UC019 – Processar Pagamento Simulado | US018 | RF014 | TC052, TC053, TC155, TC156, TC157, TC158, TC187, TC188, TC189 | Coberto |
| UC020 – Consultar Catálogo de Cursos | US019 | RF015 | TC055, TC056, TC174, TC175, TC176, TC177, TC178, TC194, TC195, TC196, TC197 | Coberto |

*Os casos de UC005, UC011, UC012, UC013 e UC017 vêm do [item 15](../../especificacao/15-casos-de-teste/area-a.md), que é a fonte desses casos; o TC008 foi descartado porque o UC013 não permite editar o e-mail.*

*Todos os 20 casos de uso e as 21 estórias de usuário possuem casos de teste especificados.*

## 2. Histórico de Medições do CI

As linhas desta tabela serão preenchidas automaticamente pelo pipeline de CI a cada execução da suíte de testes automatizados na branch principal do repositório de código, aferindo a conformidade com a meta de 75% estabelecida no RNF006 (backend) e no RNF021 (frontend):

| Data | Módulo | Cobertura | Meta | Observação |
|---|---|---|---|---|
| *Aguardando início do desenvolvimento do código* | Backend (Core API) | — | 75% | Medição a ser gerada via Pest coverage no CI |
| *Aguardando início do desenvolvimento do código* | Backend (ai-service) | — | 75% | Medição a ser gerada via Pest coverage no CI |
| *Aguardando início do desenvolvimento do código* | Frontend (Web SPA) | — | 75% | Medição a ser gerada via Vitest coverage no CI (RNF021) |
