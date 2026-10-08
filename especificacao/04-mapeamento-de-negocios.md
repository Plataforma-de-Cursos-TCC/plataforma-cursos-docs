# 4 MAPEAMENTO DE NEGÓCIOS

O template exige o mapeamento dos principais processos do negócio. O diagrama é BPMN 2.0 como código (ADR-0004).

O mapeamento representa o fluxo de valor do produto (TO BE), organizado em quatro raias: Instrutor, Aluno, Plataforma e Tutor de IA.

**Aluno:** consulta o catálogo, escolhe um curso e solicita a matrícula (com pagamento simulado se o curso for pago), assiste às aulas e, se tiver dúvida, pergunta ao tutor de IA, que responde com citação da aula e timestamp. Ao final do módulo, responde ao quiz e pode avaliar o curso.

**Instrutor:** cria curso, módulos e aulas com vídeo, cadastra quiz e gabarito, publica o curso e consulta o painel de métricas por período.

**Plataforma e Tutor de IA:** a plataforma processa o pagamento simulado, registra a matrícula, armazena, transcreve e indexa as aulas, calcula a nota do quiz, registra o progresso e agrega o engajamento da turma; o tutor de IA busca trechos do curso e responde com citação de origem, ou informa que não há conteúdo relacionado.

Esse fluxo é a base para a Relação de Requisitos Funcionais (item 6) e para as Especificações de Caso de Uso (item 10) do restante do documento.

Fonte: `diagramas/04-mapeamento-de-negocios.mmd`


```mermaid
%% BPMN (TO BE) em Mermaid: raias como subgraph; eventos (círculo), tarefas (retângulo), gateways (losango)
flowchart TB
  classDef ev fill:#fff,stroke:#222,stroke-width:2px
  classDef fim fill:#fff,stroke:#222,stroke-width:5px
  classDef gw fill:#fff7d6,stroke:#8a6d00
  classDef lane fill:#f7f7f7,stroke:#555

  subgraph POOL["Plataforma de Cursos (to be)"]
  direction TB
  subgraph INS["Instrutor"]
    i0((Início)):::ev --> i1[Cria curso, módulos e aulas com vídeo]
    i2[Cadastra quiz com gabarito] --> i3[Publica o curso]
    i3 --> i4((Fim: curso no catálogo)):::fim
    i8[Consulta o painel de métricas por período] --> i9((Fim: turma acompanhada)):::fim
  end

  subgraph ALU["Aluno"]
    a0((Início)):::ev --> a1[Consulta o catálogo e escolhe um curso]
    a1 --> a2[Solicita a matrícula]
    a3[Assiste à aula] --> a4{Tem dúvida?}:::gw
    a4 -- sim --> a5[Pergunta ao tutor de IA]
    a4 -- não --> a7{{Junção}}:::gw
    a6[Lê a resposta e retoma a aula] --> a7
    a7 --> a8[Responde ao quiz do módulo]
    a10{Deseja avaliar o curso?}:::gw -- sim --> a11[Avalia o curso]
    a11 --> a12((Fim: curso avaliado)):::fim
    a10 -- não --> a13((Fim: aula concluída)):::fim
    a14((Fim: matrícula não concluída)):::fim
  end

  subgraph PLA["Plataforma"]
    p1[Armazena o vídeo, transcreve e indexa a aula]
    p2{Curso é pago?}:::gw
    p3[Processa o pagamento simulado]
    p4{Pagamento aprovado?}:::gw
    p5{{Junção}}:::gw
    p6[Registra a matrícula]
    p7[Informa a recusa do pagamento]
    p8[Calcula a nota e registra o progresso]
    p9{{Em paralelo}}:::gw
    p10[Agrega progresso e engajamento da turma]
  end

  subgraph TUT["Tutor de IA"]
    t1[Busca trechos do curso]
    t2{Há conteúdo relacionado?}:::gw
    t3[Responde citando aula e timestamp]
    t4[Informa que não há conteúdo no curso]
    t5{{Junção}}:::gw
  end

  i1 --> p1 --> i2
  a2 --> p2
  p2 -- sim --> p3 --> p4
  p2 -- não --> p5
  p4 -- sim --> p5
  p4 -- não --> p7 --> a14
  p5 --> p6 --> a3
  a5 --> t1 --> t2
  t2 -- sim --> t3 --> t5
  t2 -- não --> t4 --> t5
  t5 --> a6
  a8 --> p8 --> p9
  p9 --> a10
  p9 --> p10 --> i8
  i3 -.->|"curso publicado"| a1
  end

```

*Figura 1 – Mapeamento de Negócios — fluxo entre Aluno, Instrutor, Plataforma e Tutor de IA*
