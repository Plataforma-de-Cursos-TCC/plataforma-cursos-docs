---
id: ra2-analise-do-professor
titulo: "Análise do professor sobre o documento (itens 1 a 15) e como cada ponto foi tratado"
tipo: processo
status: vigente
atualizado: 2026-11-13
relacionados: [ra2-tarefas, ra2-criterios-de-aceite, adr-0013, contexto]
---

# Análise do professor Evandro e o que fazer em cada área

Em 12/11/2026 o professor devolveu uma análise do documento enviado (itens 1 a 15), com um ponto crítico por item. Os itens 1 a 11 e a Área A dos itens 12 a 15 já foram corrigidos (PR #129 e #131, ver [CHANGELOG](../CHANGELOG.md)). Esta página existe para as Áreas B, C e D aplicarem o mesmo olhar ao próprio trabalho: o professor aponta o que faltou na Área A, e o mesmo tipo de falha pode aparecer nas outras.

## Itens 1 a 11 (corrigidos, só para conferência)

| Item | Ponto do professor | Como foi tratado |
|---|---|---|
| 1 a 3 | Sem ponto crítico | Nada a fazer |
| 4 | Progresso só era registrado depois do quiz, contra o RF006 e o UC009 | BPMN separa "Registra o progresso da aula" do cálculo da nota |
| 5 | Tutor de IA descrito como componente do sistema e como ator | Serviço externo de IA, fora da fronteira; D5 mantida |
| 6 | RF012 prevê perfis de acesso, mas nenhum caso de uso os alterava | UC008 ganha a alteração de perfil pelo Administrador (A4, E3) |
| 7 | US018 dizia "nenhuma matrícula" e o UC003 dizia "pendente" no pagamento recusado | US018 passa a deixar a matrícula pendente |
| 8 | RNF011 só cobria backup do banco, não dos vídeos | RNF011 cobre vídeos e materiais |
| 9 | Sem ponto crítico adicional | Nada a fazer |
| 10 | UC014 apagava módulo sem tratar o histórico dos alunos | UC014 e UC015 bloqueiam a exclusão com histórico (R-4, R-5, E4) |
| 11 | Atividades do Tutor não verificavam se a aula está processada | E-1 do UC001 entra no diagrama |

## Itens 12 a 15 (valem para as Áreas B, C e D)

| Item | Ponto do professor | O que cada área faz |
|---|---|---|
| 12 | O modelo cobria só acesso e conta; faltava o núcleo do negócio (cursos, aulas, matrículas, pagamentos, progresso, conversas) | Modelar as entidades da área e as relações com as outras áreas, de modo que cada função especificada tenha onde persistir. Modelo: Área A. |
| 13 | As classes cobriam só a Área A | Diagramas negocial e de implementação da área, ligados às classes da Área A (por exemplo `User`) e às das outras áreas. Tipo do elemento num círculo (C, A, I, E). |
| 14 | Cancelar aparecia num `opt` e a sequência seguia depois dele alterando a senha | Cancelar e confirmar são `alt` (caminhos exclusivos), e o cancelamento encerra o diagrama. As mensagens são os métodos do item 13. |
| 15 | O UC011 não testava a nova senha fora da política | Um cenário negativo para cada regra de negócio, com o estado anterior verificado como inalterado. IDs a partir de TC091. |

## Antes de abrir o PR de uma área

- Cada entidade, classe e caso de teste cita uma regra, um caso de uso ou uma estória que existe nos itens 6, 7 e 10.
- Nenhuma regra nova foi inventada no diagrama: se faltar, registre na issue `pendencia-cruzada` da área dona (AGENTS.md, regra 8).
- Nomes de atores, entidades e termos iguais aos do [glossário](../CONTEXT.md) e aos da Área A.
- Formato, ferramentas e fluxo: [ra2-tarefas.md](ra2-tarefas.md) e [ADR-0013](../docs/adr/0013-diagramas-do-ra2-em-drawio.md).

## Ligações

- **Fluxo e modelo:** [ra2-tarefas.md](ra2-tarefas.md), [ra2-criterios-de-aceite.md](ra2-criterios-de-aceite.md)
- **Decisão de formato:** [ADR-0013](../docs/adr/0013-diagramas-do-ra2-em-drawio.md)
- **Ferramentas:** [scripts/drawio-seqgen/](../scripts/drawio-seqgen/README.md)
