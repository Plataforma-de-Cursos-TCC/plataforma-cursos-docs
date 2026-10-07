# plataforma-cursos-docs

Documentação da **Plataforma de Cursos**, projeto da disciplina Especificação de Software, BSI PUCPR, 2026.

A Plataforma de Cursos é um ambiente de cursos online em que instrutores publicam cursos em módulos e aulas, com quiz e gabarito, e alunos estudam com apoio de um **Tutor de IA** que responde dúvidas no contexto da aula.

Este repositório não tem código do sistema. Ele guarda três coisas:

1. a **especificação** que o grupo entrega na disciplina (pasta `especificacao/`);
2. a **base de conhecimento** que sustenta a especificação: pesquisa de mercado, decisões e regras de escrita;
3. o **processo** de trabalho do grupo: plano de tarefas, critérios de aceite e convenções.

| Integrante | GitHub | Área funcional |
|---|---|---|
| A definir | | A: acesso e conta |
| A definir | | B: autoria do instrutor |
| A definir | | C: aprendizagem do aluno |
| A definir | | D: Tutor de IA, analytics e administração |

## Estado atual

O repositório começa cru. Cada parte da estrutura abaixo entra por um pull request próprio, para que o histórico mostre de onde veio cada decisão. Enquanto um PR não for integrado, a pasta correspondente não existe na `main`.

## Mapa do repositório (estrutura prevista)

```
.
├── README.md                  este arquivo
├── CONTEXT.md                 porta de entrada: o que está decidido e o que ler para cada item
├── AGENTS.md                  regras para assistentes de IA (Codex, Copilot, Cursor e outros)
├── CLAUDE.md                  faz o Claude Code carregar o AGENTS.md e o CONTEXT.md
│
├── especificacao/             a entrega: itens 1 a 11 do template da disciplina
├── entregas/                  plano de tarefas e critérios de aceite de cada entrega
│
├── pesquisa/                  pesquisa de mercado: produtos similares e concorrentes
├── docs/
│   ├── adr/                   decisões do projeto, uma por arquivo
│   ├── agents/                configuração das skills de IA (issues, rótulos, domínio)
│   ├── prd.md                 Product Requirements Document
│   ├── sdd.md                 Software Design Document (arquitetura, componentes, integrações)
│   ├── tdd.md                 Technical Design Document (stack, dados, APIs)
│   ├── ssd/                   diagramas de sequência do sistema, um por caso de uso
│   ├── testes/                estratégia, casos de teste e cobertura
│   └── design-system.md       tokens, componentes e acessibilidade
│
├── graphify-out/              grafo de conhecimento gerado a partir dos arquivos acima
└── .graphifyignore            o que fica fora do grafo
```

## Como trabalhamos

### Tarefas e board

- As tarefas são issues no board do projeto da organização. As do RA1 têm o rótulo `ra1`.
- Os itens 6, 7, 8 e 10 da especificação têm uma tarefa-mãe e 4 sub-issues, uma por área.
- Quem puxar uma tarefa sem responsável se atribui e move o card para **In progress**.

### Branches e pull requests

- Uma branch por tarefa, em minúsculas e sem acentos:
  - tarefas da especificação: `ra1/<tarefa>-<descricao-curta>` (ex.: `ra1/t05-atores`);
  - estrutura e documentos de apoio: `docs/<descricao-curta>` ou `chore/<descricao-curta>`.
- Nada entra na `main` sem **pull request**. O título do PR é o título da issue, e o corpo traz `Closes #<n>` e a evidência de cada critério de aceite.
- Com o PR aberto, o card vai para **In review**. Outro integrante revisa, e o card vai para **Done** depois do merge (merge commit).

### Commits

Mensagem em inglês, no imperativo, explicando o porquê da mudança.

## Licença

[MIT](LICENSE).
