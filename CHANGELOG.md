# Changelog

Registro do caminho do documento de especificação da Plataforma de Cursos até a versão final. O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## Como ler as versões

- Cada versão corresponde a um documento enviado ao professor: `1.0.0` é a entrega do RA1 e `2.0.0` é a entrega do RA2.
- Um novo envio ao professor dentro da mesma entrega sobe a versão secundária (`1.1.0`).
- Um ajuste sem novo envio sobe a correção (`1.0.1`).
- Cada versão enviada recebe a tag `vX.Y.Z` no commit que gerou o PDF.
- Todo pull request registra em `[Não lançado]` o que mudou e por quê, com o número do PR. Os grupos são Adicionado, Alterado, Corrigido e Removido.

## [Não lançado]

### Adicionado

- `CHANGELOG.md`, a regra de registrar toda mudança (`AGENTS.md`, `CONTRIBUTING.md` e template de PR) e o job `changelog` no CI, para que o caminho do documento até a versão final fique registrado e nenhum PR entre sem a sua linha (#127).
- Rubrica do RA2 (Canvas) e as planilhas `Rubricas TCC 1` e `Rubricas TCC 2` em Markdown (`entregas/ra2-rubrica-canvas.md`, `rubricas-tcc-1.md`, `rubricas-tcc-2.md`), para o grupo desenvolver e revisar com os critérios do professor à mão (#138).

### Alterado

- `entregas/ra2-tarefas.md` registra o que a Área A ensinou (tipo do elemento no item 13, gerador e `alt` no item 14, cenário negativo por regra e TC091 no item 15), para as Áreas B, C e D seguirem o mesmo padrão (#133).
- Diagramas dos itens 12 a 14 da Área A refeitos em draw.io, com a ADR-0013 no lugar da ADR-0011, para manter o leiaute sob controle e usar uma ferramenta só no documento; diagramas de classes com o tipo do elemento num círculo (C, A, I, E); os de sequência gerados com um estilo único (#131).

### Corrigido

Correções pedidas na análise do professor Evandro sobre os itens 4 a 11 (#129):

- Item 4: o BPMN registra o progresso a cada aula assistida ("Registra o progresso da aula") e calcula a nota só no quiz, porque a tarefa única fazia o progresso depender do quiz, contra o RF006 e o UC009.
- Item 5: o Tutor de IA é descrito como serviço externo de IA, fora da fronteira do sistema, porque o texto o chamava de componente do sistema e de ator ao mesmo tempo.
- Item 6: o UC008 ganha o fluxo de alteração de perfil pelo Administrador (A4, E3 e regras), com critérios novos na US016 e protótipo, porque o RF012 fala em perfis de acesso e nenhum caso de uso trocava o perfil.
- Item 7: na US018, o pagamento recusado deixa a matrícula pendente, sem liberar o conteúdo, para concordar com o UC003.
- Item 8: o RNF011 passa a cobrir o backup de vídeos e materiais, além do banco de dados.
- Item 10: o UC014 e o UC015 bloqueiam a exclusão de módulo ou aula com histórico de alunos (regra, passo de verificação, exceção E4 e protótipo), porque a exclusão apagaria progresso e respostas.
- Item 11: o diagrama de atividades verifica se a aula está transcrita e indexada antes da busca do Tutor de IA (E-1 do UC001), que antes ficava de fora.
- Item 14: cancelar e confirmar em `alt` no UC011 (parte 2) e no UC017, porque o `opt` de cancelamento deixava o fluxo seguir (análise do professor) (#131).
- Item 15: UC011 ganha a regra R-3, a exceção E4 (nova senha fora da política), o protótipo `UC011-E4-1` e o caso de teste TC090, porque não havia cenário negativo para a política de senha (#131).

## [1.2.0] - 2026-11-12

Pré-versão enviada ao professor para aprovação, com os diagramas do RA1 refeitos.

### Alterado

- Diagramas dos itens 4, 9 e 11 refeitos em draw.io, com a `ADR-0012` no lugar da `ADR-0004`, porque o BPMN e o PlantUML gerados por código não davam controle fino do leiaute (#125).

## [1.1.0] - 2026-10-22

Documento com os itens 1 a 15 (RA2 da Área A) enviado ao professor para análise.

### Adicionado

- Modelo de dados (item 12) da Área A em PlantUML com dicionário de dados e `ADR-0011`, servindo de modelo às demais áreas (#118).
- Diagrama de classes (item 13) da Área A em PlantUML com visões negocial e de implementação para guiar as outras áreas (#119).
- Diagramas de sequência (item 14) da Área A para cinco casos de uso em PlantUML cobrindo fluxos alternativos e de exceção (#120).
- Casos de teste (item 15) da Área A para cinco casos de uso com rastreabilidade a casos de uso, estórias e requisitos funcionais (#121).

### Alterado

- Cenários de exceção e protótipos da revisão do RA1, ordenação dos itens 7 e 10 e arquivos de planejamento do RA2 (#111).
- Registro do e-mail de contato de Adrian no `README.md` e nos critérios de aceite do RA1 (#112).
- Configuração de `CODEOWNERS`, modelo de pull request e regras de fluxo de trabalho no `CONTRIBUTING.md` (#113).
- Workflows para automação do quadro de tarefas e exigência de vínculo com issues para fechamento via pull request (#114).
- Teste ponta a ponta dos fluxos de trabalho automatizados do quadro de tarefas (#116).

## [1.0.0] - 2026-10-10

Entrega do RA1: itens 1 a 11 da especificação.

### Adicionado

- Estrutura inicial do repositório com `CONTEXT.md`, `AGENTS.md` e `README.md`, servindo de base para os documentos subsequentes (#1).
- Decisões arquiteturais iniciais `ADR-0001` a `ADR-0006` em `docs/adr/`, estabelecendo regras para requisitos, estórias e diagramas (#2).
- Esqueletos dos documentos de engenharia (`docs/prd.md`, `docs/sdd.md`, `docs/tdd.md`, SSDs, testes e design system) (#3).
- Esqueleto dos itens 1 a 11 da especificação em `especificacao/`, com divisão em arquivos por área conforme a `ADR-0006` (#10).
- Critérios de aceite e detalhamento de tarefas do RA1 em `entregas/`, definindo os requisitos de entrega e o plano de trabalho (#11).
- Transcrição do conteúdo da v11 para os itens 1 a 5 da especificação, com o mapeamento de processos versionado em Mermaid (#43).
- Transcrição dos requisitos funcionais, estórias de usuário e requisitos não funcionais da v11 distribuídos por área (#44).
- Transcrição dos diagramas de casos de uso, especificações de casos de uso e protótipos da v11 para os itens 9 a 11 (#45).
- Rascunhos de PRD, SDD, design system e propostas para preenchimento de lacunas das áreas (#46).
- Pesquisa de mercado sobre dez produtos similares e catálogo de fontes em `pesquisa/`, servindo de base citável para a especificação (#47).
- Transcrição técnica da v11 para o TDD, diagramas de sequência `UC001` a `UC011`, 48 casos de teste e declaração de uso de IA (#48).
- Grafo de conhecimento inicial da documentação em `graphify-out/`, facilitando a navegação e leitura dos arquivos por assistentes (#50).
- Script `scripts/build_doc.py` para geração da especificação em DOCX e PDF a partir do modelo da disciplina (#55).
- Protótipos em HTML para todos os fluxos de casos de uso do item 10 e script `scripts/render_prototypes.py` (#57).
- Caso de uso `UC020` e estória `US019` para consulta ao catálogo de cursos, garantindo especificação detalhada para o `RF015` (#60).
- Registro da `ADR-0007` formalizando a escolha de Laravel 13, Next.js, MySQL 8 e PostgreSQL com pgvector para a arquitetura (#62).
- Detalhamento da estratégia de testes em `docs/testes/estrategia.md` com definição da pirâmide, TDD e diretrizes do Tutor de IA (#66).
- Expansão dos casos de teste para 63 cenários e matriz formal de rastreabilidade em `docs/testes/cobertura.md` (#70).
- Requisito `RNF021` fixando cobertura mínima de testes de 75% no frontend com bloqueio de merge no CI (#75).
- Decisões arquiteturais `ADR-0008` e `ADR-0009` acompanhadas de pesquisa sobre autenticação com JWT e paginação de listas (#77).
- Diagramas de sequência para os casos de uso `UC012` a `UC020` em `docs/ssd/` e alinhamento de endpoints com o TDD (#79).
- Decisão arquitetural `ADR-0010` e pesquisa em `docs/pesquisas/` sobre infraestrutura de nuvem e autenticação com JWT RS256 (#81).

### Alterado

- Atribuição de responsáveis pelas áreas A, B, C e D e definição do formato de entrega do RA1 em PDF e DOCX (#42).
- Reconciliação dos diagramas de classes e de sequência com as figuras originais da v11, eliminando divergências da primeira ingestão (#49).
- Alinhamento das ADRs, critérios de aceite e `CONTEXT.md` ao plano de ensino vigente e às diretrizes da disciplina (#52).
- Substituição dos diagramas Mermaid dos itens 4, 9 e 11 por BPMN 2.0 e PlantUML, atendendo às exigências da disciplina (#53).
- Revisão de conteúdo dos itens 1 a 11 com consolidação de tabelas únicas, padronização de estórias e rastreabilidade entre requisitos e casos de uso (#54).
- Desmembramento dos casos de uso `UC013`, `UC008` e `UC003` com a criação dos casos de uso de extensão `UC017`, `UC018` e `UC019` (#58).
- Workflows de verificação de integridade da documentação e validação de convenções de commit no GitHub Actions (#59).
- Tema claro como padrão dos protótipos e tokens de cor no design system, assegurando a exibição da cor primária da marca (#63).
- Marcação de 38 critérios de aceite do RA1 com apontamento de evidências diretas no repositório (#64).
- Articulação explícita de problema, valor e métrica de sucesso para cada objetivo estratégico no item 1 (#67).
- Inclusão da coluna de objetivo na matriz de rastreabilidade do item 9 e cópia da rubrica do Canvas em `entregas/` (#68).
- Adequação do TDD e SDD à decisão de pagamento simulado, removendo `payoutInfo` e ajustando os status de `Payment` (#69).
- Ajustes de leiaute no script `scripts/build_doc.py` para sumário de nível 1, centralização de tabelas e quebras de página (#71).
- Redesenho do diagrama de atividades do item 11 em imagem única horizontal com três raias, gerada por script determinístico (#73).
- Ajuste na entidade `Payment` para desvincular matrícula de pagamentos recusados e remoção da meta de testes no frontend (#74).
- Alinhamento do PRD, SDD e TDD com os itens 1 a 11 da especificação após revisão cruzada (#76).
- Atualização do caso de uso `UC013` e da estória `US003` para edição de perfil com novos campos e telas correspondentes (#78).
- Definição dos pontos de quebra responsivos no design system e marcação provisória de contraste no tema escuro (#80).
- Alinhamento do TDD, SDD e diagramas de sequência às decisões dos casos de uso sobre matrículas e respostas da API (#83).
- Marcação dos critérios de consistência `C10.8` e `K.4` como atendidos nos critérios de aceite do RA1 (#84).
- Inclusão do endpoint de quiz no TDD para proteger o gabarito e remoção de referências legadas à v11 (#85).
- Ajustes na especificação, SSDs e TDD após revisão cruzada e configuração do BPMN em seção paisagem no DOCX (#86).
- Nota explicativa no item 5 definindo a Plataforma de Cursos como fronteira do sistema e registro de evidências da rubrica (#87).

### Corrigido

- Correções da auditoria do PDF v12 nos fluxos de casos de uso, critérios de aceite, requisitos não funcionais e declaração de IA (#56).
- Correção de inconsistências mecânicas da revisão do RA1, saneando marcadores de revisão, IDs no PRD e adendos na `ADR-0001` (#65).
- Correção de leiaute do DOCX para centralização de imagens, limite de duas estórias por página e ajuste do item 11 (#72).
- Correções de fluxos nos casos de uso e adição do requisito `RF019` e da estória `US021` para alteração de senha (#82).
- Remoção de atributos `mc:Ignorable` órfãos no script de build para evitar erro de leitura no Microsoft Word (#88).
- Ajuste na capa do DOCX para fluxo normal, cabeçalho e rodapé de largura total em páginas paisagem e bordas nas figuras (#89).

### Removido

- Critério `C06.5` em `entregas/`, porque a coluna de objetivo pertence à matriz de rastreabilidade do item 9 e não ao item 6 (#61).
