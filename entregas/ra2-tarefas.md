---
id: ra2-tarefas
titulo: "Quebra de tarefas: RA2 (Especificação do Projeto, itens 12 a 15)"
tipo: processo
status: rascunho, aguardando aprovação do grupo
atualizado: 2026-10-16
relacionados: [ra2-criterios-de-aceite, ra1-tarefas, contexto, adr-0004, adr-0006]
---

# Quebra de Tarefas: RA2 (itens 12 a 15)

> Entrega da Avaliação do RA 2 em 28/11/2026. Mesmo padrão do [RA1](ra1-tarefas.md): uma tarefa-mãe por item e uma sub-issue por área (A a D), atribuída ao dono da área ([ADR-0006](../docs/adr/0006-divisao-por-areas.md)). Critérios em [ra2-criterios-de-aceite](ra2-criterios-de-aceite.md).

## 1. Itens e prazos

| Item | Entrega | Prazo da tarefa formativa | Mãe | Filhas (A, B, C, D) |
|---|---|---|---|---|
| 12 | Modelo lógico do banco (UML, relacional) | 15/10 (TE4) | #90 | #91, #92, #93, #94 |
| 13 | Diagrama de classes | 29/10 (TE5) | #95 | #96, #97, #98, #99 |
| 14 | Diagramas de sequência, >= 4 casos de uso | 05/11 (TE5) | #100 | #101, #102, #103, #104 |
| 15 | Planilha de casos de teste, >= 4 casos de uso | 12/11 (TE6) | #105 | #106, #107, #108, #109 |
| Geral | Revisão cruzada, DOCX/PDF, envio no Canvas | 28/11 | sem issue; fazer depois das mães | |

## 2. Responsáveis

| Área | Responsável | GitHub |
|---|---|---|
| A Acesso e conta | Lucas Stopinski da Silva | `LucasStop` |
| B Autoria do instrutor | Adrian Antônio de Souza Gomes | `adrian69-droid` |
| C Aprendizagem do aluno | Lucas Bruno e Silva | `Luc-Bruno` |
| D Tutor de IA, analytics e administração | Vinicius Lima Teider | `Teider011` |

## 3. Fontes existentes por item

- 12 e 13: `docs/tdd.md` seção 2 (modelo, dicionário, diagrama de classes); pendências #6 (normalização, Módulo–Quiz).
- 14: `docs/ssd/UC001` a `UC020`; pendência #7 (arquitetura única, `alt` nas exceções).
- 15: `docs/testes/`; pendência #8 (colunas da disciplina, UC011, US017 a US020).
- Decisão a respeitar: pagamento simulado (#51).

## 4. Ordem

12 -> 13 -> 14. O 15 parte dos fluxos do item 10 e roda em paralelo. A mãe de cada item integra as 4 áreas antes de fechar. A revisão cruzada e o envio vêm depois das quatro mães.

## 5. Como fazer (modelo: Área A)

A Área A já está pronta e serve de exemplo. Copie a estrutura, troque as tabelas pelas da sua área e preencha o `area-X.md` correspondente (hoje com "a preencher"). Decisão de formato: [ADR-0011](../docs/adr/0011-diagramas-do-ra2-em-plantuml.md).

| Item | Modelo | O que fazer na sua área |
|---|---|---|
| 12 | [area-a.md](../especificacao/12-modelo-de-dados/area-a.md), [.puml](../especificacao/diagramas/12-modelo-de-dados-area-a.puml) | Um diagrama PlantUML das tabelas da área (PK/FK à esquerda, obrigatórios em negrito, seta da FK para a PK, cardinalidade `1` e `n`) e o dicionário de dados. |
| 13 | [area-a.md](../especificacao/13-diagrama-de-classes/area-a.md), [negocial](../especificacao/diagramas/13-classes-area-a-negocial.puml), implementação ([cadastro e login](../especificacao/diagramas/13-classes-area-a-implementacao-login.puml), [recuperação de senha](../especificacao/diagramas/13-classes-area-a-implementacao-recuperacao.puml), [perfil](../especificacao/diagramas/13-classes-area-a-implementacao-perfil.puml)) | Uma figura negocial e uma ou mais de implementação (Controller, Service, FormRequest, DTO). Sem id de FK como atributo; identificadores em inglês. |
| 14 | [area-a.md](../especificacao/14-diagramas-de-sequencia/area-a.md), [exemplo](../especificacao/diagramas/14-sequencia-uc005.puml) | Um diagrama por UC (mínimo 4 no total; a Área A entrega 5), com `alt` para exceções e `opt` para alternativos; mensagens são os métodos do item 13. |
| 15 | [area-a.md](../especificacao/15-casos-de-teste/area-a.md) | Uma seção por UC com a linha de rastreio e a tabela ID, Cenário, Caso de Teste, Entradas e Resultado Esperado; FP é o cenário 1 e cada FA e FE vira cenário. Os IDs seguem os de `docs/testes/casos-de-teste.md`: a Área A usou TC065 a TC089, e as outras áreas numeram a partir de TC090 (conferir o último ID antes de criar). Resultados com erro de API citam o status e o `code` da tabela de erros do TDD (seção 3.1). |

Gerar o PNG: `PLANTUML_LIMIT_SIZE=8192 plantuml -tpng especificacao/diagramas/<arquivo>.puml` (sem o limite maior, o PlantUML corta a imagem em 4096 px). Cada imagem deve caber legível na página: diagrama largo, divida em dois. Gerar o DOCX para conferir: `python3 scripts/build_doc.py 12 15 --pdf`. Se o seu texto supõe algo que outra área ainda não definiu, registre na issue `pendencia-cruzada` dela (AGENTS.md, regra 8).

## 6. Quando entrar o segundo idioma (en ou es)

Decisão do grupo: a interface e as mensagens ficam só em pt-BR; a estrutura já está pronta (`User.locale`, arquivos de tradução, regra `locale` > `Accept-Language` > pt-BR no TDD seção 3.1), e o seletor de idioma só entra junto com o segundo idioma. Quando isso acontecer, ajustar:

- RNF013 (item 8 e `docs/sdd.md`): voltar a citar o idioma novo.
- RF001 e US003 (itens 6 e 7), UC012 (idioma inicial no cadastro) e UC013 (campo Idioma no perfil), com os critérios de aceite correspondentes.
- Protótipos `meu-perfil` e `cadastro` (item 10): incluir o seletor e regerar as capturas com `python3 scripts/render_prototypes.py`.
- Item 12: incluir o idioma novo na lista de idiomas ativos do dicionário de `User.locale`; item 13: novo valor em `Locale`; regerar os PNGs com `PLANTUML_LIMIT_SIZE=8192`.
- Item 15: casos de teste do UC012 e do UC013 para o seletor e para o idioma padrão.
- Conteúdo do curso e resposta do Tutor de IA: decidir à parte (fora do escopo hoje).
