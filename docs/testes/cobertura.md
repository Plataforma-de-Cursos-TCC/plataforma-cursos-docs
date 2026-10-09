---
id: testes-cobertura
titulo: "Cobertura de testes"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-08
---
# Cobertura de testes

As medições de cobertura de código serão coletadas automaticamente e registradas a cada execução do pipeline de integração contínua (CI) no repositório de implementação, tendo como meta mínima 75% de cobertura no backend e no frontend conforme estabelecido no RNF006 e no RNF021 e na [Estratégia de testes](estrategia.md).

## 1. Rastreabilidade de Casos de Uso e Estórias de Usuário

A tabela a seguir apresenta a matriz de rastreabilidade entre os requisitos funcionais, estórias de usuário, casos de uso e os respectivos casos de teste documentados em [Casos de teste](casos-de-teste.md):

| Caso de Uso (UC) | Estória de Usuário (US) | Requisito Funcional (RF) | Casos de Teste Associados | Status de Cobertura |
|---|---|---|---|---|
| UC001 – Conversar com Tutor de IA | US012 | RF009 | TC034, TC035, TC036 | Coberto |
| UC002 – Responder Quiz | US011 | RF008 | TC031, TC032, TC033 | Coberto |
| UC003 – Matricular-se em Curso | US007 | RF005 | TC019, TC020, TC021 | Coberto |
| UC004 – Cadastrar Quiz com Gabarito | US010 | RF007 | TC028, TC029, TC030 | Coberto |
| UC005 – Realizar Login | US001 | RF017 | TC001, TC002, TC003 | Coberto |
| UC006 – Cadastrar Curso | US004 | RF002 | TC010, TC011, TC012 | Coberto |
| UC007 – Ver Dashboard com Filtro | US013 | RF010 | TC037, TC038, TC039 | Coberto |
| UC008 – Gerenciar Usuários | US016 | RF012 | TC046, TC047, TC048 | Coberto |
| UC009 – Assistir Aula | US008, US009 | RF006 | TC022, TC023, TC024, TC025, TC026, TC027 | Coberto |
| UC010 – Avaliar Curso | US014 | RF011 | TC040, TC041, TC042 | Coberto |
| UC011 – Recuperar Senha | US017 | RF013 | TC049, TC050, TC051 | Coberto |
| UC012 – Cadastrar-se na Plataforma | US002 | RF001 | TC004, TC005, TC006 | Coberto |
| UC013 – Editar Dados do Perfil | US003, US020 | RF001, RF016 | TC007, TC008, TC009, TC058, TC059, TC060 | Coberto |
| UC014 – Gerenciar Módulos do Curso | US005 | RF003 | TC013, TC014, TC015 | Coberto |
| UC015 – Gerenciar Aulas do Curso | US006 | RF004 | TC016, TC017, TC018 | Coberto |
| UC016 – Acessar Área Protegida por Perfil | US015 | RF018 | TC043, TC044, TC045 | Coberto |
| UC017 – Alterar Senha | US003 | RF001 | TC061, TC062 | Coberto |
| UC018 – Excluir e Anonimizar Usuário | US016 | RF012 | TC063 | Coberto |
| UC019 – Processar Pagamento Simulado | US018 | RF014 | TC052, TC053, TC054 | Coberto |
| UC020 – Consultar Catálogo de Cursos | US019 | RF015 | TC055, TC056, TC057 | Coberto |

*Todos os 20 casos de uso e as 20 estórias de usuário possuem casos de teste especificados.*

## 2. Histórico de Medições do CI

As linhas desta tabela serão preenchidas automaticamente pelo pipeline de CI a cada execução da suíte de testes automatizados na branch principal do repositório de código, aferindo a conformidade com a meta de 75% estabelecida no RNF006 (backend) e no RNF021 (frontend):

| Data | Módulo | Cobertura | Meta | Observação |
|---|---|---|---|---|
| *Aguardando início do desenvolvimento do código* | Backend (Core API) | — | 75% | Medição a ser gerada via Pest coverage no CI |
| *Aguardando início do desenvolvimento do código* | Backend (ai-service) | — | 75% | Medição a ser gerada via Pest coverage no CI |
| *Aguardando início do desenvolvimento do código* | Frontend (Web SPA) | — | 75% | Medição a ser gerada via Vitest coverage no CI (RNF021) |
