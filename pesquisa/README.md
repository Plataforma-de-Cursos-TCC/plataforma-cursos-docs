# Pesquisa de mercado

Pesquisa vigente sobre produtos similares à Plataforma de Cursos. Na ordem de precedência do [CONTEXT](../CONTEXT.md), ela fica abaixo das decisões ([docs/adr/](../docs/adr/README.md)) e acima de rascunhos e textos antigos.

## Conteúdo

- [similares/](similares/README.md): 10 fichas de produto (Udemy, Coursera, Khan Academy, edX, Duolingo, Skillshare, Alura, Hotmart, DIO e Rocketseat), mais a síntese:
  - [matriz-comparativa.md](similares/matriz-comparativa.md): os 10 produtos lado a lado nos eixos de análise;
  - [lacunas-e-diferencial.md](similares/lacunas-e-diferencial.md): lacunas do mercado, diferencial da Plataforma de Cursos e insumos para os itens 1, 2 e 3.
- [fontes.md](fontes.md): todas as fontes com numeração global (F01, F02, ...), sem duplicatas por URL.

## Convenções

- Cada afirmação sobre concorrente leva [Fato] (confirmada na fonte) ou [Inferência] (dedução nossa), seguida do ID da fonte, por exemplo `[Fato][F04]`.
- Os IDs são os de [fontes.md](fontes.md). Ao citar número, preço ou recurso de concorrente em qualquer item da especificação, use o mesmo ID.
- Todas as fontes foram consultadas em 2026-10-07. A data de verificação de cada ficha está no campo `verificado:` do cabeçalho.

## O que ler para cada item

| Item | Arquivo |
|---|---|
| 1 - 3 Objetivos | [lacunas e diferencial](similares/lacunas-e-diferencial.md) |
| 2 - É / Não é / Faz / Não faz | [lacunas e diferencial](similares/lacunas-e-diferencial.md), [matriz](similares/matriz-comparativa.md) |
| 3 - Visão do Produto | [similares](similares/README.md), [matriz](similares/matriz-comparativa.md), [lacunas e diferencial](similares/lacunas-e-diferencial.md) |
| 6 - RFs | [matriz](similares/matriz-comparativa.md) |

## Limitações conhecidas

- **Khan Academy:** nenhuma fonte pôde ser confirmada na consulta. Por isso, todas as afirmações da [ficha](similares/khan-academy.md) estão marcadas como [Inferência]. Reconsultar antes de citar a ficha em um item da especificação.
- **Seções "Não encontrado":** algumas fichas têm essa seção, que lista o que não tem fonte pública (por exemplo, o percentual do Teacher Fund do Skillshare). Esses pontos não devem ser citados como fato.
