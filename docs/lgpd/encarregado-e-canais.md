---
id: lgpd-encarregado
titulo: "Encarregado pelo Tratamento de Dados (DPO) e Canal Público de Privacidade"
tipo: documento-projeto
status: rascunho
atualizado: 2026-11-25
relacionados: [pesquisa-lgpd, lgpd-ropa, lgpd-ripd, sdd, tdd]
---
# Encarregado pelo Tratamento de Dados (DPO) e Canal Público de Privacidade

> Documento de governança em conformidade com o art. 41 da LGPD (Lei nº 13.709/2018), a Resolução CD/ANPD nº 18/2024 (`[F88]`), a Resolução CD/ANPD nº 15/2024 (`[F87]`) e o **RNF025**.

## 1. Identificação do Encarregado (DPO)

- **Nome / Razão social do Encarregado:** *a definir pelo grupo* (indicação formal obrigatória antes da entrada em produção, por ato escrito conforme Resolução CD/ANPD nº 18/2024).
- **Substituto formal (quando aplicável):** *a definir pelo grupo*.
- **Canal de contato público:** `privacidade@<dominio-da-plataforma>` *(endereço definitivo a publicar junto com o domínio do produto, ADR-0010)*.
- **Local de divulgação obrigatória:** rodapé de 100% das páginas públicas e autenticadas da Plataforma de Cursos e seção dedicada na página pública da Política de Privacidade (RNF025).

> **Nota sobre agente de pequeno porte (Resolução CD/ANPD nº 2/2022):** mesmo que a operação inicial se enquadre como agente de tratamento de pequeno porte, o uso de IA generativa (Tutor de IA) e o potencial tratamento de dados de crianças e adolescentes podem caracterizar tratamento de alto risco, afastando a dispensa de indicação do Encarregado. Independentemente de eventual dispensa, a manutenção de um **canal público de comunicação com titulares** permanece obrigatória ([pesquisa/lgpd.md](../../pesquisa/lgpd.md)).

---

## 2. Atribuições do Encarregado (LGPD, art. 41, § 2º; Res. CD/ANPD nº 18/2024)

1. Aceitar reclamações e comunicações dos titulares (Visitantes, Alunos, Instrutores e Administradores), prestar esclarecimentos e adotar providências.
2. Receber comunicações da Autoridade Nacional de Proteção de Dados (ANPD) e adotar providências.
3. Orientar a equipe de desenvolvimento e operação da Plataforma de Cursos a respeito das práticas de proteção de dados pessoais.
4. Executar as demais atribuições determinadas pelo controlador ou estabelecidas em normas complementares, incluindo supervisão da atualização periódica do [ROPA](ropa.md) e do [RIPD](ripd.md).
5. Atuar com autonomia técnica e sem conflito de interesses (vedada cumulação com função que decida isoladamente sobre finalidades e meios de tratamento sem governança independente).

---

## 3. Canal público e atendimento aos direitos do titular (LGPD, arts. 18 e 19)

O canal público de privacidade (e, quando implementado, o formulário autenticado no perfil do Usuário) deve atender a todas as requisições previstas no art. 18 da LGPD:

| Direito do titular (art. 18) | Prazo legal / operacional | Fluxo previsto na Plataforma de Cursos |
|---|---|---|
| Confirmação de existência de tratamento e acesso simplificado (I, II) | **Imediato** (art. 19, I) | Consulta autenticada dos dados cadastrais em `/api/v1/profile` ou resposta simplificada pelo canal público |
| Declaração clara e completa de origem, critérios e finalidade (II) | **Até 15 dias** (art. 19, II) | Exportação estruturada de dados e relatório de compartilhamentos (operadores listados no [ROPA](ropa.md)) |
| Correção de dados incompletos, inexatos ou desatualizados (III) | Até 15 dias (ou imediato via perfil) | Edição de perfil (`UC013`) e procedimento verificado para alteração de e-mail |
| Anonimização, bloqueio ou eliminação (IV, VI) | Sem demora injustificada (imediato quando solicitado pelo titular) | Solicitação pelo titular vinculada à rotina de anonimização irreversível (`UC018`, ADR-0014), preservando apenas hipóteses legais do art. 16 |
| Portabilidade (V) | Até 15 dias (conforme regulamentação ANPD) | Exportação em formato legível por máquina (JSON/CSV) |
| Informação sobre compartilhamento e consequências da negativa de consentimento (VII, VIII) | Imediato na Política de Privacidade / até 15 dias sob requisição | Política de Privacidade pública e seção 3 do [ROPA](ropa.md) |
| Revogação de consentimento (IX) | Gratuito e facilitado, a qualquer momento | Opção de gestão de consentimentos no perfil ou via canal de privacidade |
| Revisão de decisões automatizadas (art. 20) | Até 15 dias | Canal de contestação humana para bloqueios ou decisões automatizadas que afetem interesses do titular |

---

## 4. Comunicação de incidentes de segurança (LGPD, art. 48; Res. CD/ANPD nº 15/2024)

- **Prazo de comunicação:** até **3 dias úteis** contados da ciência do incidente que possa acarretar risco ou dano relevante aos titulares (em dobro se enquadrado como agente de pequeno porte sem afastamento regulatório), tanto à ANPD quanto aos titulares afetados (`[F87]`).
- **Critérios de risco relevante:** envolvimento de dados pessoais sensíveis, dados de crianças ou adolescentes, dados de autenticação (credenciais/tokens), ou comprometimento em larga escala.
- **Registro interno obrigatório:** manter registro de todos os incidentes de segurança (mesmo os não comunicados) pelo prazo mínimo de **5 anos** (Resolução CD/ANPD nº 15/2024).

---

## Ligações

- **Pesquisa legal:** [pesquisa/lgpd.md](../../pesquisa/lgpd.md) · [pesquisa/fontes.md](../../pesquisa/fontes.md)
- **Demais artefatos LGPD:** [ROPA](ropa.md) · [RIPD](ripd.md)
- **Requisitos e contexto:** [Item 8 — RNFs](../../especificacao/08-requisitos-nao-funcionais/00-item.md) · [SDD](../sdd.md) · [CONTEXT.md](../../CONTEXT.md)
