# AGENTS.md

## Base de conhecimento do projeto (leia antes de qualquer tarefa de documentação)

1. Leia `CONTEXT.md` (raiz). Ele resume produto, atores, glossário, decisões D1 a D6 e áreas, e diz o que ler para cada item da especificação.
2. Abra só os arquivos indicados para o seu item (`CONTEXT.md`, seção 8, ou `pesquisa/README.md`).
3. Precedência: `docs/adr/` (decisões) > `pesquisa/` (pesquisa vigente) > rascunhos e textos antigos. Não contradiga uma decisão; se algo pedir mudança, registre a dúvida para o grupo em vez de mudar o texto.
4. Ao usar número, preço ou recurso de concorrente, cite a fonte pelo número de `pesquisa/fontes.md` e separe [Fato] de [Inferência] quando não for óbvio.
5. Use os nomes exatos: produto "Plataforma de Cursos"; atores "Usuário" (ator geral de Aluno, Instrutor e Administrador), "Visitante", "Aluno", "Instrutor", "Administrador" e "Tutor de IA" (ator sistêmico). Termos do domínio seguem o glossário do `CONTEXT.md`.
6. Grafo: se existir `graphify-out/`, use `graphify-out/GRAPH_REPORT.md` (ou a consulta do Graphify) para **achar** o que ler; decida sempre pelos arquivos Markdown. Não regenere o grafo em branches de tarefa: ele é regerado só a partir da `main`, via PR.
7. Arquivo novo de pesquisa segue o mesmo formato: cabeçalho YAML (`id`, `titulo`, `tipo`, `itens_template`, `areas`, `decisoes`, `fontes`, `relacionados`, `status`, `atualizado`) e seção "Ligações" com links Markdown relativos (os links viram ligações no grafo). Decisão nova segue o formato dos ADRs em `docs/adr/`.
8. Pendência entre áreas: se o texto que você escreve supõe algo que outra área ainda não definiu, não pare e não invente o requisito da outra área. Registre a suposição na issue `pendencia-cruzada` da área que precisa resolver.
9. Changelog: todo pull request acrescenta em `CHANGELOG.md`, na seção `[Não lançado]`, uma linha com o que mudou e por quê, seguida do número do PR. O CI (`changelog`) exige; só PR sem efeito no documento ou no repositório (merge de sincronização, teste de fluxo) usa o label `sem-changelog`. Não crie tag nem feche versão: isso é decisão do grupo, feita no envio ao professor.

## Agent skills

### Issue tracker

Issues live in this repo's GitHub Issues (`gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Default vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` + `docs/adr/` at the repo root. See `docs/agents/domain.md`.
