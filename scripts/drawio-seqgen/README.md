# Ferramentas de diagrama (draw.io)

Dois scripts em Python (só biblioteca padrão) que mantêm os diagramas do RA2 com um estilo só, conforme a [ADR-0013](../../docs/adr/0013-diagramas-do-ra2-em-drawio.md).

## `seqgen.py`: diagramas de sequência (item 14)

Lê uma descrição em um subconjunto de PlantUML e gera o `.drawio` com o leiaute padrão (grade de 10, Helvetica 12, traço de 1,5 px, preto e branco, ícones de boundary, control, entity e BD, fragmentos `alt` e `opt`).

```
python3 scripts/drawio-seqgen/seqgen.py entrada.puml especificacao/diagramas/14-sequencia-ucNNN.drawio
draw.io -x -f png -s 2 -b 20 -o especificacao/diagramas/14-sequencia-ucNNN.png especificacao/diagramas/14-sequencia-ucNNN.drawio
```

Sintaxe aceita: `actor`, `boundary`, `control`, `entity`, `database`; mensagens `A -> B : texto` e `A --> B : texto` (retorno), com `++` e `--` para abrir e fechar a barra de ativação; `alt`, `else`, `opt`, `end`; `deactivate`. Os exemplos da Área A estão em [exemplos/](exemplos/): copie um e troque os participantes e as mensagens. O script confere a grade, o tamanho dos rótulos e o número de setas, e para com erro se algo não cabe.

A `.puml` de entrada é só insumo: não entra no PNG nem precisa ser versionada (a fonte do diagrama é o `.drawio`).

Regra do item 14: cancelar e confirmar são `alt` (cancelar encerra o diagrama), nunca `opt` seguido de continuação.

## `typeicon.py`: tipo do elemento no diagrama de classes (item 13)

Acrescenta o círculo com a letra do tipo (C classe, A classe abstrata, I interface, E enumeração) no canto esquerdo do cabeçalho de cada elemento:

```
python3 scripts/drawio-seqgen/typeicon.py especificacao/diagramas/13-classes-area-x-*.drawio
```

Pode rodar de novo depois de editar o diagrama: os ícones antigos são refeitos e as enumerações continuam E. A letra vem do cabeçalho: `<<enumeration>>` vira E (e o texto sai, o círculo o substitui), `<<interface>>` vira I, nome em itálico vira A (classe abstrata) e o resto vira C. Confira o PNG. No XML, o papel do elemento vai escapado: `&lt;&lt;Controller&gt;&gt;`.
