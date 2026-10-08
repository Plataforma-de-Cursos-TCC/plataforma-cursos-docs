---
id: matriz-comparativa
titulo: "Matriz comparativa de similares (seção 3.3)"
tipo: similar-matriz
secao_original: "3.3"
itens_template: [2, 3, 6]
areas: [B, C, D]
decisoes: [D5]
fontes: []
relacionados: [similares, lacunas-e-diferencial, alura, coursera, dio, duolingo, edx, hotmart, khan-academy, rocketseat, skillshare, udemy]
status: vigente
atualizado: 2026-10-07
---
# Matriz comparativa de similares (seção 3.3)

> Base de conhecimento do projeto · síntese gerada a partir das 10 fichas individuais de produtos similares em [fichas/](README.md) · convenções de separação entre [Fato] e [Inferência] conforme o padrão do projeto.

Legenda e convenções: as informações de concorrentes refletem os dados documentados nas fichas de pesquisa vigentes (uma por produto, linkadas na primeira coluna); a coluna final apresenta a proposta de escopo e arquitetura do projeto **Plataforma de Cursos**.

---

### Tabela 1: Eixos de Negócio, Autoria e Avaliação

| Produto | Público-alvo | Modelo de negócio | Autoria do instrutor | Quiz e avaliação |
|---|---|---|---|---|
| [Alura](alura.md) | Estudantes e profissionais de tecnologia, design e negócios digitais; empresas no B2B | Assinatura anual B2C (Plus, Pro, Ultra Lab) e planos corporativos B2B | Fechada/centralizada (time interno e instrutores convidados); sem marketplace aberto | Exercícios de múltipla escolha e práticos com correção; certificado por curso |
| [Coursera](coursera.md) | Estudantes globais, profissionais em upskilling, governos e empresas B2B | Parcerias universitárias/empresariais, freemium, compras avulsas e Coursera Plus | Fechada a parceiros institucionais credenciados (universidades e grandes empresas) | Quizzes formativos e somativos com gabarito automático, prazos e certificados formais |
| [DIO](dio.md) | Desenvolvedores e estudantes de tecnologia focados em empregabilidade | Freemium B2C com planos PRO e Global; B2B para recrutamento de talentos | Mista (equipe interna e instrutores parceiros em bootcamps estruturados) | Questionários objetivos de fixação, desafios de código e projetos práticos |
| [Duolingo](duolingo.md) | Estudantes de idiomas e reforço escolar (alfabetização, matemática, música) | Freemium com anúncios, assinaturas pagas (Super Duolingo, Duolingo Max) | Fechada e gamificada por especialistas pedagógicos internos | Exercícios interativos curtos e dinâmicos com correção e feedback instantâneos |
| [edX](edx.md) | Estudantes universitários, profissionais globais e corporações | Cursos gratuitos no modo audit com venda de certificados, programas e B2B | Fechada a universidades de elite e instituições parceiras globais | Avaliações graduadas e autoavaliações de múltipla escolha com gabarito automático |
| [Hotmart](hotmart.md) | Produtores digitais/creators, afiliados e compradores de cursos/infoprodutos | Marketplace transacional de infoprodutos (taxa percentual por venda) | Aberta a qualquer produtor de conteúdo com painel e fluxo de publicação | Quizzes do tipo Exercício (com gabarito e nota mínima) ou Pesquisa; certificados |
| [Khan Academy](khan-academy.md) | Estudantes da educação básica, professores escolares e famílias | Gratuito e filantrópico (ONG suportada por doações e parcerias educacionais) | Fechada e centralizada pela equipe pedagógica interna da fundação | Exercícios interativos de fixação com gabarito imediato, dicas e resolução passo a passo |
| [Rocketseat](rocketseat.md) | Desenvolvedores de software buscando formação profissional e transição de carreira | Assinatura anual única B2C (Rocketseat ONE) e planos empresariais B2B | Fechada e centralizada por time interno de educadores e referências da comunidade | Quiz objetivo obrigatório (exige aproveitamento mínimo de 70%) para certificado |
| [Skillshare](skillshare.md) | Criadores, designers, fotógrafos e profissionais em habilidades criativas | Assinatura anual com acesso ilimitado ao catálogo de aulas criativas | Aberta a qualquer criador ("anyone can teach") com envio e curadoria básica | Avaliação por projetos práticos compartilhados na galeria comunitária (sem quiz nativo) |
| [Udemy](udemy.md) | Alunos em upskilling/reskilling, instrutores independentes e empresas (B2B) | Híbrido: marketplace com venda avulsa de cursos e assinatura (Personal Plan e B2B) | Aberta a qualquer instrutor cadastrado via Instructor Dashboard | Quizzes com gabarito automático, simulados e emissão automática de certificado |
| **Plataforma de Cursos (proposta)** | Alunos em busca de cursos online e Instrutores cadastrados | Sistema web de cursos online (sem camada transacional de pagamento no escopo inicial) | Aberta a qualquer Instrutor cadastrado (cadastro de curso, módulo, aula e quiz) | Quiz associado a módulo ou aula com gabarito e correção automática |

---

### Tabela 2: Tutor de IA, Analytics, Preço, Acessibilidade e Idiomas

| Produto | Tutor de IA e contexto da aula | Analytics para instrutor (e admin) | Preço | Acessibilidade e i18n |
|---|---|---|---|---|
| [Alura](alura.md) | Luri: contextualizada no conteúdo e na aula assistida; ícone na tela de aula | Sem dashboard de instrutor no B2C; dashboard corporativo B2B para gestores | Assinatura de R$ 1.188 a R$ 2.388/ano (Plus, Pro e Ultra Lab) | Transcrições e legendas; interface em pt-BR e es (Alura LATAM) |
| [Coursera](coursera.md) | Coursera Coach: contextualizado nos vídeos, transcrições e leituras da aula | Course Analytics com funil de retenção, tempo e desempenho por questão | Audit gratuito; cursos avulsos US$ 49-99; Coursera Plus US$ 399/ano | Legendas e transcrições em múltiplos idiomas; suporte a WCAG 2.1 AA |
| [DIO](dio.md) | DIO Agent: mentor de estudos geral com skills pré-definidas (sem RAG rígido da aula) | Sem dashboard aberto para instrutor; painel B2B voltado a contratação | Gratuito básico; planos PRO (R$ 49,90/mês ou R$ 514/ano) e Global | Legendas em conteúdos selecionados; predominantemente pt-BR |
| [Duolingo](duolingo.md) | Duolingo Max (Explain My Answer / Roleplay): IA integrada ao exercício em resolução | Duolingo for Schools com relatórios de turmas para professores | Gratuito com anúncios; Super Duolingo e Duolingo Max (faixa paga) | Alta acessibilidade visual/auditiva; múltiplos idiomas |
| [edX](edx.md) | edX Xpert: tutor lateral contextualizado no material didático e vídeos do curso | edX Insights com engajamento semanal, abandono e métricas por questão | Cursos no modo audit gratuitos; certificados verificados US$ 50-300 | Legendas e transcrições em múltiplos idiomas; conformidade formal WCAG |
| [Hotmart](hotmart.md) | Hotmart Tutor: IA treinada estritamente com o conteúdo do curso do produtor | Insights da Área de Membros com dúvidas frequentes, engajamento e vendas | Gratuito para publicar; taxa transacional de 9,9% + R$ 2,49 por venda | Legendas com transcrição automática por IA; suporte a pt-BR, en e es |
| [Khan Academy](khan-academy.md) | Khanmigo: tutor socrático que guia o raciocínio sem dar a resposta pronta | Teacher Dashboard com progresso da turma e habilidades em dificuldade | Gratuito na plataforma geral; Khanmigo a US$ 4/mês ou US$ 44/ano | Legendas e transcrições; suporte formal a acessibilidade; multilíngue |
| [Rocketseat](rocketseat.md) | Houston: busca semântica em catálogo/vídeos e suporte contínuo na plataforma | Sem dashboard de instrutor externo; dashboard corporativo B2B para gestores | Rocketseat ONE por R$ 2.197,00/ano (em até 12x) | Legendas e transcrições via sistema interno Júpiter; foco em pt-BR |
| [Skillshare](skillshare.md) | Não possui tutor de IA contextual para alunos nas fontes oficiais consultadas | Teacher Stats com alunos, minutos assistidos e rendimentos financeiros | US$ 167,88/ano (ou US$ 13,99/mês faturado anualmente) | Transcrições automáticas e legendas em vários idiomas; foco inicial em en |
| [Udemy](udemy.md) | Udemy AI Assistant: tira dúvidas no player da aula e gera testes práticos | Instructor Dashboard completo com receitas, matrículas, notas e dúvidas | Venda avulsa promocional (R$ 27,90 a R$ 89,90); Personal Plan US$ 16-32/mês | Legendas automáticas e editáveis; interface em mais de 75 idiomas |
| **Plataforma de Cursos (proposta)** | Tutor de IA como ator sistêmico respondendo contextualizado à aula assistida | Dashboard com métricas de desempenho dos cursos para Instrutor e Admin | Gratuito / plataforma educacional de especificação acadêmica | Sistema web responsivo, aderente a boas práticas de usabilidade; foco em pt-BR |

---

## Ligações

- **Decisões:** [ADR-0005 — Tutor de IA como ator sistêmico](../../docs/adr/0005-tutor-de-ia-como-ator-sistemico.md)
- **Itens da especificação:** [Item 2 — É / Não é / Faz / Não faz](../../especificacao/02-e-nao-e-faz-nao-faz.md), [Item 3 — Visão do Produto](../../especificacao/03-visao-do-produto.md), [Item 6 — Requisitos Funcionais](../../especificacao/06-requisitos-funcionais/00-item.md)
- **Relacionados:** [similares](README.md), [lacunas-e-diferencial](lacunas-e-diferencial.md), [alura](alura.md), [coursera](coursera.md), [dio](dio.md), [duolingo](duolingo.md), [edx](edx.md), [hotmart](hotmart.md), [khan-academy](khan-academy.md), [rocketseat](rocketseat.md), [skillshare](skillshare.md), [udemy](udemy.md)
- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
