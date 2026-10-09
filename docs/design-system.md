---
id: design-system
titulo: "Design system"
tipo: documento-projeto
status: rascunho
atualizado: 2026-10-08
---
# Design system

Este documento descreve o visual da Plataforma de Cursos a partir dos 16 protótipos do item 10 (8 telas em baixa e 8 em alta fidelidade). Os valores de cor, tamanho e espaçamento foram **estimados do protótipo**: medidos por amostragem de pixels nas imagens, sem acesso ao arquivo de origem. Onde o protótipo não define nada, o texto traz uma proposta, marcada no código-fonte por comentário `proposta`.

Fato extraído do cabeçalho do protótipo de alta fidelidade: o design system se chama "Institucional Confiável", usa Source Serif 4 e Inter e é baseado em shadcn/ui. [Fato]

Os protótipos de alta fidelidade foram medidos **em tema escuro**. Todo valor "estimado do protótipo" da seção 1.1 é, portanto, do tema escuro. O tema claro (seção 1.2) é o padrão dos protótipos e do DOCX; o escuro fica em `png/escuro/` (seção 6).

## 1. Tokens de cor

### 1.1 Tema escuro (estimado do protótipo)

| Token | Hex | Uso | Onde aparece |
|---|---|---|---|
| `bg` | `#101417` | fundo da página e dos campos | tela 1 (fundo e inputs) |
| `surface` | `#181D20` | cartões, linhas de módulo, cartões de KPI, tabela | telas 1 a 8 |
| `surface-raised` | `#222A2C` | bloco que envolve cada tela, bolha do tutor, tag "Aluno" | telas 2, 3, 8 |
| `border` | `#2B3033` | contorno de campos e cartões (estimado, 1 px) | telas 1, 5, 6 |
| `text` | `#FBFFFF` | títulos e texto principal | todas |
| `text-muted` | `#A1A6A9` | rótulos, metadados, cabeçalho de tabela | telas 1, 2, 7, 8 |
| `text-placeholder` | `#767A7B` | texto de exemplo em campo | telas 1, 5, 6 |
| `primary` | `#52A19B` | botão principal, link, progresso, linha do gráfico, opção marcada | telas 1, 2, 3, 4, 5, 6, 7 |
| `on-primary` | `#001E15` | texto sobre `primary` | telas 1, 2, 4, 5, 6 |
| `accent` | `#A59CDD` (texto) sobre `accent-bg` `#252142` | categoria do curso, perfil Instrutor, pergunta do Aluno no chat, carimbo "Aula 2 · 04:12" | telas 2, 3, 8 |
| `success` | `#8DBA9D` sobre `#1E3022` | status "Ativo"; variação positiva no KPI (texto `#8AB89B` sobre `surface`) | telas 7, 8 |
| `danger` | `#CE857F` sobre `#332323` | status "Bloqueado"; botão "Excluir" (texto e contorno) | tela 8 |
| `neutral-chip` | `#A3AFAF` sobre `#222A2C` | perfil Aluno | tela 8 |

Observações:

- O protótipo mostra um degradê `#56A09F` para `#978FE4` (primária para roxo) na miniatura do curso, tela 2. É capa provisória de curso, não token de interface.
- A paleta é um neutro frio quase verde-azulado com uma primária verde-água e um roxo de apoio. Não há cor de **aviso** no protótipo. <!-- proposta: aviso necessário para estados como "prazo do quiz" ou "senha fraca"; sugerido `warning` `#E3B341` no escuro, contraste 8,73:1 sobre `surface` -->
- Os valores acima têm precisão de amostragem de imagem JPEG: esperar diferença de 1 a 3 níveis por canal em relação ao design de origem.

### 1.2 Tema claro

Tema padrão: os protótipos e o DOCX usam este tema. Os tokens derivam dos escuros e passam em WCAG 2.1 AA.

| Token | Hex | Contraste (par) |
|---|---|---|
| `bg` | `#FFFFFF` | |
| `surface` | `#F4F6F6` | |
| `surface-raised` | `#E6EBEB` | |
| `border` | `#7A8285` | 3,92:1 sobre `bg`; 3,61:1 sobre `surface` (componente, mínimo 3:1) |
| `field-border` | `#6B7274` | 4,90:1 sobre `bg`; 4,52:1 sobre `surface` |
| `text` | `#14191B` | 17,73:1 sobre `bg`; 14,73:1 sobre `surface-raised` |
| `text-muted` | `#4B5557` | 7,67:1 sobre `bg`; 7,08:1 sobre `surface` |
| `text-placeholder` | `#6B7274` | 4,90:1 sobre `bg`; 4,52:1 sobre `surface` |
| `primary` | `#0F6E6A` | 6,07:1 sobre `bg`; 5,60:1 sobre `surface`; 5,04:1 sobre `surface-raised` |
| `on-primary` | `#FFFFFF` | 6,07:1 sobre `primary` |
| `accent` / `accent-bg` | `#5B4FB5` / `#EEEBFA` | 5,54:1 |
| `success` / `success-bg` | `#1F6B3A` / `#E3F2E8` | 5,63:1 |
| `danger` / `danger-bg` | `#A32B22` / `#FBE9E7` | 6,12:1 |
| `warning` / `warning-bg` | `#8A5A00` / `#FFF4D6` | 5,41:1 |
| `neutral-chip` | `#4B5557` sobre `surface-raised` | 6,38:1 |

A `primary` do escuro (`#52A19B`) é a variação clara de `#0F6E6A`. Sobre o fundo escuro `#101417`, `#0F6E6A` dá só 3,05:1 e reprova AA; `#52A19B` dá 6,11:1. Por isso cada tema tem a sua.

### 1.3 Contraste dos pares do protótipo (escuro)

Razão calculada pela fórmula de luminância relativa da WCAG 2.1. Mínimo: 4,5:1 para texto normal, 3:1 para componente de interface.

| Par (texto sobre fundo) | Razão | AA |
|---|---|---|
| `text` `#FBFFFF` sobre `surface` `#181D20` | 16,88:1 | passa |
| `text-muted` `#A1A6A9` sobre `surface` | 6,91:1 | passa |
| `text-muted` `#A1A6A9` sobre `surface-raised` `#222A2C` | 5,95:1 | passa |
| `primary` `#52A19B` sobre `bg` `#101417` (link, ícone) | 6,11:1 | passa |
| `primary` sobre `surface` | 5,61:1 | passa |
| `primary` sobre `surface-raised` | 4,83:1 | passa |
| `on-primary` `#001E15` sobre `primary` (botão) | 5,79:1 | passa |
| `accent` `#A59CDD` sobre `accent-bg` `#252142` | 6,11:1 | passa |
| `success` `#8DBA9D` sobre `#1E3022` | 6,42:1 | passa |
| `danger` `#CE857F` sobre `#332323` | 5,18:1 | passa |
| `text-placeholder` `#767A7B` sobre `bg` `#101417` | 4,27:1 | **falha** (texto) |
| `border` `#2B3033` sobre `surface` `#181D20` | 1,27:1 | **falha** (componente, mínimo 3:1) |

Duas falhas no protótipo: o texto de exemplo dos campos e o contorno dos campos. <!-- proposta: corrigir no tema escuro com `text-placeholder` `#8F9496` (6,03:1 sobre `bg`) e `border` de campo `#6B7274` (3,47:1 sobre `surface`, 3,78:1 sobre `bg`) -->

## 2. Tipografia

Estimado do protótipo (aparência das letras e legenda do próprio arquivo):

| Papel | Família | Peso | Tamanho estimado | Onde aparece |
|---|---|---|---|---|
| Título de página e de cartão | Source Serif 4 (serifada) | 600 a 700 | 17 a 20 px | "Entrar", "Novo curso", "Quiz — Módulo 1", "Turma — Fundamentos de Pesquisa", título do curso (tela 2, cerca de 20 px) |
| Valor de KPI | Source Serif 4 | 700 | 22 a 24 px | "128", "64%", "8,3" (tela 7) |
| Preço | Source Serif 4 | 700 | 17 px | "R$ 249,90" (tela 2) |
| Texto de interface | Inter | 400 a 500 | 12 a 13 px | corpo, campos, opções do quiz, bolhas do chat |
| Botão e título de seção | Inter | 600 | 12 a 13 px | "Entrar", "Matricular-se", "Progresso ao longo do período" |
| Rótulo de campo | Inter | 500 | 10 a 11 px | "E-mail", "Título", "Preço (R$)" |
| Cabeçalho de tabela | Inter, caixa alta | 600 | 9 a 10 px | "USUÁRIO", "E-MAIL", "PERFIL", "STATUS" (tela 8) |
| Etiqueta e carimbo | Inter | 600 | 9 a 10 px | categoria do curso, "Aula 2 · 04:12", status |

Altura de linha: cerca de 1,4 a 1,5 no texto corrido, estimado visualmente. Escala resultante: 10 / 12 / 13 / 17 / 20 / 24 px.

Os tamanhos são pequenos para leitura confortável: o protótipo é mostrado reduzido numa tela de pré-visualização e o texto de interface chega a 10 px. <!-- proposta: na implementação, corpo mínimo de 16 px (1 rem), rótulo 14 px, título de página 28 px, título de seção 20 px, KPI 32 px, altura de linha 1,5; fontes via `next/font` -->

## 3. Espaçamento e grid

Estimado do protótipo:

- Unidade base de 4 px; passos observados: 4, 8, 12, 16, 24.
- Cartão de formulário: padding interno de cerca de 24 px; largura de 220 a 420 px, centralizado em bloco largo (login, quiz, cadastro de curso e de quiz).
- Entre campos: cerca de 16 a 20 px; entre rótulo e campo: cerca de 4 a 6 px.
- Linhas de módulo e de usuário: altura de cerca de 40 px, vão de 4 a 8 px.
- Dashboard: três cartões de KPI em linha, com vão de cerca de 12 a 16 px, e gráfico de largura total abaixo.
- Aula: duas colunas, vídeo (cerca de 60%) e chat do Tutor de IA (cerca de 30%).
- Raio de borda: cerca de 6 a 8 px em campos e botões, 10 a 12 px em cartões, pílula total em etiquetas.

Breakpoints: o protótipo mostra só a largura de computador. <!-- proposta: breakpoints do Tailwind (sm 640, md 768, lg 1024, xl 1280); em largura menor que `lg`, a aula empilha o chat do Tutor de IA abaixo do vídeo e a tabela de usuários vira lista de cartões -->

## 4. Componentes

Todos vêm do protótipo de alta fidelidade, em tema escuro. Estados padrão: o que o protótipo mostra. Estados de foco, desabilitado e erro não aparecem em nenhuma tela.

<!-- proposta: para todo componente, foco = anel de 2 px `primary` com deslocamento de 2 px; desabilitado = 50% de opacidade e cursor bloqueado; erro = contorno `danger` e mensagem em texto abaixo do campo -->

### Botão
- **Primário**: fundo `primary`, texto `on-primary`, peso 600, raio pequeno. "Entrar" (tela 1, largura total), "Matricular-se" (tela 2), "Enviar respostas" (tela 4, largura total), "Publicar" (tela 5), "Salvar quiz" (tela 6).
- **Secundário** (contorno): fundo `surface`, texto `text`, contorno `border`. "Continuar assistindo" (tela 2), "Salvar rascunho" (tela 5), "+ Adicionar pergunta" (tela 6), "Bloquear" e "Desbloquear" (tela 8).
- **Destrutivo** (contorno): contorno e texto `danger`. "Excluir" (tela 8).
- **Ícone**: quadrado `primary` com seta de envio, no campo do chat (tela 3).
- No protótipo de baixa fidelidade o botão primário é branco sobre fundo cinza; só o de alta usa `primary`.

### Campo de formulário
Rótulo acima, campo com fundo `bg`, contorno `border`, texto de exemplo em `text-placeholder`. Variantes: texto e senha (tela 1), área de texto com alça de redimensionar (descrição, tela 5), seleção (categoria, tela 5), busca (tela 8). Na tela 5 os campos aparecem já preenchidos (por exemplo, título "Fundamentos de Pesquisa com Usuários" e preço "249,90") em cor de texto normal, não como texto de exemplo.
Link "Esqueci minha senha" em `primary`, tela 1. No rodapé do cartão de login, "Não tem conta? Criar conta", com "Criar conta" em `primary`.

### Cartão de curso e página do curso
Tela 2. Miniatura com degradê e ícone de reproduzir, etiqueta de categoria (`accent`), título em serifa, metadados ("Instrutor: Marina Alves · 8 módulos · 3h40 de conteúdo"), preço em serifa, "Matricular-se" e "Continuar assistindo". Abaixo, lista de aulas em linhas `surface`, com ícone de estado: concluída (círculo com visto), em andamento (triângulo), bloqueada (cadeado, com a palavra "Bloqueado"), e a duração à direita.
O protótipo traz uma página do curso, não uma grade de cartões de catálogo. <!-- proposta: cartão de catálogo reaproveita miniatura, etiqueta, título, instrutor e preço da tela 2, sem lista de aulas -->

### Player de aula
Tela 3. Área de vídeo 16:9 em `#151A1D` com triângulo de reproduzir ao centro; abaixo, título da aula ("2. Entrevistas de descoberta") e trilha ("Módulo 1 · Fundamentos de Pesquisa com Usuários"). Controles, barra de progresso, legenda e transcrição não aparecem. <!-- proposta: barra de controle com reproduzir/pausar, tempo, velocidade, legenda e tela cheia, operável por teclado; transcrição em painel recolhível -->

### Chat do Tutor de IA
Tela 3, coluna à direita do vídeo. Cabeçalho com ícone de balão e "Tutor de IA". Pergunta do Aluno em bolha `accent-bg`, alinhada à esquerda; resposta em bolha `surface-raised`, com carimbo de origem em `accent` ("Aula 2 · 04:12", aula e momento do vídeo, conforme o UC001). Campo "Pergunte sobre esta aula..." e botão de envio na base. A resposta cita a origem no conteúdo da aula, que é o diferencial do produto (CONTEXT.md, seção 1). [Fato]

### Quiz
Telas 4 (responder) e 6 (cadastrar).
- Resposta: cartão com título em serifa, barra de progresso fina em `primary`, enunciado numerado, opções como linhas de contorno com botão de rádio; a marcada ganha contorno `primary` e fundo levemente esverdeado; "Enviar respostas" em largura total.
- Cadastro: campo "Título do quiz", bloco por pergunta com enunciado e alternativas, rádio para marcar o gabarito, aviso em verde "Gabarito marcado — alternativa 1", botões "+ Adicionar pergunta" e "Salvar quiz".

### Tabela
Tela 8. Linhas em `surface`, cabeçalho em caixa alta `text-muted`. Colunas: Usuário (avatar circular com iniciais e nome), E-mail, Perfil (etiqueta), Status (etiqueta) e uma última coluna de ações sem cabeçalho. O protótipo grafa "João Sliva" na segunda linha, provável erro de digitação. <!-- proposta: dar cabeçalho "Ações" à coluna (também visível só para leitor de tela) e corrigir para "João Silva" --> Etiquetas: Instrutor (`accent`), Aluno (`neutral-chip`), Ativo (`success`), Bloqueado (`danger`). Ações: "Bloquear" ou "Desbloquear" (secundário) e "Excluir" (destrutivo). Acima, busca por nome ou e-mail e seleção "Todos os perfis".
A coluna Perfil mostra um dos perfis do glossário; o ator "Administrador" não aparece nos dados de exemplo.

### Filtro de período, KPI e gráfico
Tela 7. Duas seleções no canto superior direito do cabeçalho: período ("Últimos 30 dias") e curso ("Todos os cursos"). Três cartões de KPI: rótulo, valor em serifa, variação em `success` com seta nos dois primeiros ("↑ 12% no período", "↑ 5 pts") e, no terceiro, "estável" em `text-muted`, sem seta. Gráfico de linha de `primary` com área preenchida e ponto final, título "Progresso ao longo do período" e intervalo "Aug 1 – Aug 30". O intervalo está em inglês, divergindo do restante da interface em português. <!-- proposta: formatar datas em pt-BR ("1 a 30 de ago.") -->
O gráfico não mostra eixos nem valores; só a forma da curva. <!-- proposta: rótulos de eixo, tooltip e tabela alternativa dos dados para leitor de tela -->

## 5. Acessibilidade

Meta: WCAG 2.1 nível AA. O protótipo cobre pouco desta seção; o que é medido vem da seção 1.3 e o resto é proposta.

- **Contraste de texto**: 10 dos 12 pares medidos passam. Falham o texto de exemplo dos campos e o contorno dos campos (seção 1.3).
- **Cor não é o único indicador**: o protótipo já acompanha cor com texto ou ícone em status ("Ativo", "Bloqueado"), variação do KPI (seta) e aula (ícone de concluída, em andamento, bloqueada). [Fato]
- **Foco visível**: não aparece no protótipo. <!-- proposta: anel de foco de 2 px em `primary` em todo controle, contraste mínimo de 3:1 com o fundo -->
- **Teclado**: <!-- proposta: ordem de tabulação segue a ordem visual; opções do quiz navegáveis por setas; Esc fecha seleções abertas; envio no chat com Enter -->
- **Rótulos**: os formulários do protótipo já têm rótulo visível acima de cada campo, exceto a busca e o campo do chat, que usam só texto de exemplo. <!-- proposta: `aria-label` nesses dois campos; nunca usar placeholder como único rótulo -->
- **Aulas**: <!-- proposta: legenda em todo vídeo e transcrição em texto, como requisito de publicação da aula -->
- **Gráfico e tabela**: <!-- proposta: alternativa textual do gráfico do dashboard; `scope` nos cabeçalhos da tabela -->
- **Alvos de toque**: <!-- proposta: mínimo de 44 por 44 px em dispositivo móvel -->
- **Mensagens do Tutor de IA**: <!-- proposta: região `aria-live="polite"` para a resposta nova -->

## 6. Modo escuro

Os protótipos de alta fidelidade foram medidos em tema escuro (valores da seção 1.1). O tema claro (seção 1.2) é o padrão dos protótipos e do DOCX. O escuro fica em `png/escuro/` e é ativado com `?tema=escuro` na URL do protótipo. Os protótipos de baixa fidelidade são escuros, em tons de cinza. [Fato]

<!-- proposta: regras de troca de tema -->
- Tokens semânticos (`bg`, `surface`, `text`, `primary`…) como variáveis CSS; o tema muda trocando o conjunto de valores, nunca o nome do token.
- Padrão: seguir `prefers-color-scheme`; o Aluno, o Instrutor e o Administrador podem fixar a preferência (claro, escuro, sistema) em "Editar dados do perfil", e a escolha persiste.
- Aplicar o tema antes da primeira pintura, para evitar o lampejo do tema errado.
- Imagens e miniaturas de curso não mudam com o tema; o degradê da capa provisória fica fora dos tokens.
- Cada par de cor do tema claro e do escuro precisa passar na seção 1.3 antes de entrar no código.

## 7. Protótipos

Imagens em [especificacao/10-especificacoes-de-caso-de-uso/prototipos/](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/). Todos os valores deste documento vêm da alta fidelidade.

| Tela | Caso de uso | Alta fidelidade | Baixa fidelidade |
|---|---|---|---|
| 1. Login | UC005, Realizar login | [alta-tela1-login.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela1-login.jpg) | [baixa-tela1-login.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela1-login.jpg) |
| 2. Página do curso | UC003, Matricular-se em curso | [alta-tela2-pagina-curso.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela2-pagina-curso.jpg) | [baixa-tela2-pagina-curso.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela2-pagina-curso.jpg) |
| 3. Aula e chat com Tutor de IA | UC001, Conversar com Tutor de IA (também UC009) | [alta-tela3-aula-chat.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela3-aula-chat.jpg) | [baixa-tela3-aula-chat.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela3-aula-chat.jpg) |
| 4. Responder quiz | UC002, Responder quiz | [alta-tela4-quiz.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela4-quiz.jpg) | [baixa-tela4-quiz.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela4-quiz.jpg) |
| 5. Cadastrar curso | UC006, Cadastrar curso | [alta-tela5-cadastrar-curso.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela5-cadastrar-curso.jpg) | [baixa-tela5-cadastrar-curso.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela5-cadastrar-curso.jpg) |
| 6. Cadastrar quiz com gabarito | UC004, Cadastrar quiz com gabarito | [alta-tela6-cadastro-quiz.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela6-cadastro-quiz.jpg) | [baixa-tela6-cadastro-quiz.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela6-cadastro-quiz.jpg) |
| 7. Dashboard com filtro | UC007, Ver dashboard com filtro | [alta-tela7-dashboard.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela7-dashboard.jpg) | [baixa-tela7-dashboard.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela7-dashboard.jpg) |
| 8. Gerenciar usuários | UC008, Gerenciar usuários | [alta-tela8-usuarios.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/alta-tela8-usuarios.jpg) | [baixa-tela8-usuarios.jpg](../especificacao/10-especificacoes-de-caso-de-uso/prototipos/baixa-tela8-usuarios.jpg) |

Os protótipos de alta fidelidade cobrem os fluxos dos casos de uso do item 10 (24 telas em `especificacao/10-especificacoes-de-caso-de-uso/prototipos/html/`). Os componentes deste documento seguem os mesmos tokens.

## Pendências para o grupo

- A tela 2 e a tela 5 mostram **preço** do curso ("R$ 249,90", "Preço (R$)"), e o CONTEXT.md manda não assumir pagamento. Decidir se preço é só informativo.
- As correções de contraste da seção 1.3 (escuro) precisam de aprovação antes de virar token de código. O tema claro da seção 1.2 já está nos protótipos.
- O arquivo de origem do protótipo (Figma ou equivalente) não está no repositório; os hex deste documento são amostras de imagem JPEG.
