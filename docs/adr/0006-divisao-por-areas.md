---
id: adr-0006
titulo: "ADR-0006 — Divisão do trabalho em áreas A a D"
tipo: decisao
decisao: D6
status: aceita
data: 2026-10-07
decisor: Grupo (proposta de Lucas Stopinski)
itens_template: [6, 7, 8, 10]
areas: [A, B, C, D]
relacionados: [adr-0001, adr-0005]
---
# ADR-0006 — Divisão do trabalho em áreas A a D

- **Status:** aceita · **Data:** 07/10/2026 · **Decisor:** grupo, por proposta de Lucas Stopinski

## Contexto

- O grupo tem 4 integrantes e os itens 6, 7, 8 e 10 pedem uma parte por integrante.
- Sem uma divisão por assunto, duas pessoas escrevem o mesmo RF e outras partes do sistema ficam sem dono.

## Opções consideradas

- **(a)** Divisão por item (um integrante faz todos os RFs, outro todas as estórias…).
- **(b)** **Divisão por área funcional**: cada integrante fica com uma área e escreve RF, estória, RNF e caso de uso dela.

## Decisão

**(b)**, com quatro áreas:

| Área | Escopo | Casos de uso de partida | RNF ISO/IEC 25010 sugeridos |
|---|---|---|---|
| A | Acesso e conta | Cadastrar-se, Realizar login, Recuperar senha, Editar dados do perfil | Segurança (LGPD), Compatibilidade |
| B | Autoria do instrutor | Cadastrar curso, Gerenciar módulos, Gerenciar aulas, Cadastrar quiz com gabarito | Manutenibilidade, Portabilidade |
| C | Aprendizagem do aluno | Matricular-se em curso, Assistir aula, Responder quiz, Avaliar curso | Capacidade de interação (inclui inclusividade, antiga acessibilidade, na ISO/IEC 25010:2023) |
| D | Tutor de IA, analytics e administração | Conversar com Tutor de IA, Ver dashboard com filtro, Gerenciar usuários, Acessar área protegida por perfil | Eficiência de desempenho, Confiabilidade |

- O responsável de cada área fica na tabela do [README](../../README.md).
- Os itens 1 a 5, 9 e 11 são do grupo: quem puxar a tarefa escreve, e outro integrante revisa.
- Dependência entre áreas (ex.: área C usa o quiz cadastrado na área B) vira issue com a label `pendencia-cruzada`.

## Consequências

- Cada área tem um arquivo próprio nos itens 7 e 10 (`area-a.md` … `area-d.md`), o que reduz conflito de merge. Os itens 6 e 8 ficam num `00-item.md` único, porque o template pede uma tabela só, ordenada por ID.
- A numeração final dos IDs segue a [ADR-0001](0001-minimo-por-integrante-e-numeracao-provisoria.md).
- Na ISO/IEC 25010:2023, acessibilidade é a subcaracterística "inclusividade" de **Capacidade de interação**, e não uma característica própria. RNF de acessibilidade (ex.: WCAG) é classificado assim.

---

## Ligações

- **Itens da especificação:** itens 6, 7, 8 e 10 em [especificacao/](../../especificacao/)
- **Outras decisões:** [D1](0001-minimo-por-integrante-e-numeracao-provisoria.md), [D5](0005-tutor-de-ia-como-ator-sistemico.md)
- **Índice das decisões:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
