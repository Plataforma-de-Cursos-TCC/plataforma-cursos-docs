#!/usr/bin/env python3
"""Gera o documento de especificação (DOCX; PDF com --pdf) a partir do Template.docx.

Uso:
    python3 scripts/build_doc.py [de] [até] [--template T.docx] [--saida DIR] [--pdf]
    python3 scripts/build_doc.py --check

Exemplos: `1 11` gera o RA1 (padrão), `6 8` só os itens 6 a 8, `1 15` tudo.
O template da disciplina não fica no repositório: passe --template ou
defina ESSW_TEMPLATE. Precisa de pandoc, soffice (LibreOffice) e pdftotext
(o soffice gera um PDF interno só para numerar as páginas do sumário).
"""
import argparse
import copy
import itertools
import os
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

REPO = Path(__file__).resolve().parent.parent
ESP = REPO / "especificacao"
DECLARACAO = REPO / "entregas" / "declaracao-uso-de-ia.md"

AUTORES = [
    "Lucas Stopinski da Silva",
    "Lucas Bruno e Silva",
    "Adrian Antônio de Souza Gomes",
    "Vinicius Lima Teider",
]
PRODUTO = "Plataforma de Cursos"
ANO = "2026"

# Item -> lista de arquivos (relativos a especificacao/) ou (título, nota) quando
# a fonte ainda não está pronta para o documento.
ITEMS = {
    1: ["01-3-objetivos.md"],
    2: ["02-e-nao-e-faz-nao-faz.md"],
    3: ["03-visao-do-produto.md"],
    4: ["04-mapeamento-de-negocios.md"],
    5: ["05-atores-usuarios.md"],
    6: ["06-requisitos-funcionais/00-item.md"],
    7: ["07-estorias-de-usuario/00-item.md"]
    + [f"07-estorias-de-usuario/area-{a}.md" for a in "abcd"],
    8: ["08-requisitos-nao-funcionais/00-item.md"],
    9: ["09-diagrama-geral-de-casos-de-uso.md"],
    10: ["10-especificacoes-de-caso-de-uso/00-item.md"]
    + [f"10-especificacoes-de-caso-de-uso/area-{a}.md" for a in "abcd"],
    11: ["11-diagrama-de-atividades.md"],
    12: ("MODELO DE DADOS", "docs/tdd.md, seção 2"),
    13: ("DIAGRAMA DE CLASSES", "docs/tdd.md, seção Diagrama de Classes"),
    14: ("DIAGRAMAS DE SEQUÊNCIA", "docs/ssd/"),
    15: ("CASOS DE TESTE", "docs/testes/casos-de-teste.md"),
}

# Converte <br> (HTML cru dentro das células de tabela) em quebra de linha do Word.
LUA_BR = """
function RawInline(el)
  if el.format == 'html' and el.text:match('^<br%s*/?>$') then
    return pandoc.LineBreak()
  end
end
"""

# Parágrafos que, logo antes de uma tabela, são o título do quadro no template
# (linhas mescladas no topo da tabela). O título da estória é um Heading 2.
TITULO = re.compile(
    r"^(QUADRO “|VISÃO DE PRODUTO$|NOME DO PRODUTO:|PRODUTO:|COMO:|Critérios de Aceite:$|US\d{3} –)"
)
US = re.compile(r"^US\d{3} –")

TOC_TAB = 10466  # posição do tab direito com pontilhado no estilo Sumrio1 do template


def parse_range(de, ate):
    if not (1 <= de <= 15 and 1 <= ate <= 15):
        raise ValueError(f"itens devem estar entre 1 e 15 (recebido {de} {ate})")
    if de > ate:
        raise ValueError(f"'de' ({de}) maior que 'até' ({ate})")
    return list(range(de, ate + 1))


def drop_column(md, header):
    """Remove de todas as tabelas markdown a coluna cujo cabeçalho é `header`."""
    out, idx = [], None
    for line in md.split("\n"):
        if not line.startswith("|"):
            idx = None
            out.append(line)
            continue
        cells = line.strip().strip("|").split("|")
        if idx is None and header in [c.strip() for c in cells]:
            idx = [c.strip() for c in cells].index(header)
        if idx is not None and idx < len(cells):
            del cells[idx]
            line = "|" + "|".join(cells) + "|"
        out.append(line)
    return "\n".join(out)


def preprocess(path):
    md = path.read_text(encoding="utf-8")
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    # Links para outros .md do repositório não fazem sentido no documento.
    md = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)]*\.md[^)]*)\)", r"\1", md)
    md = drop_column(md, "ARQUIVO")
    # Caminho absoluto das imagens, porque os arquivos são concatenados.
    md = re.sub(
        r"!\[([^\]]*)\]\(([^)<>]+)\)",
        lambda m: f"![{m.group(1)}](<{(path.parent / m.group(2)).resolve()}>)",
        md,
    )
    return md.strip() + "\n"


def build_markdown(items):
    parts = []
    for n in items:
        src = ITEMS[n]
        if isinstance(src, tuple):
            titulo, fonte = src
            parts.append(f"# {n} {titulo}\n\nEm elaboração (RA2). Fonte de trabalho: {fonte}.\n")
        else:
            parts += [preprocess(ESP / f) for f in src]
    parts.append(preprocess(DECLARACAO))
    return renumber_figures("\n\n".join(parts))


def renumber_figures(md):
    """Legendas `Figura N –` numeradas na ordem em que aparecem no documento."""
    n = itertools.count(1)
    return re.sub(r"Figura \d+ –", lambda m: f"Figura {next(n)} –", md)


def child(parent, tag, index=None):
    """Filho `tag` de `parent`, criado (no fim ou em `index`) se não existir."""
    el = parent.find(qn(tag))
    if el is None:
        el = OxmlElement(tag)
        parent.append(el) if index is None else parent.insert(index, el)
    return el


def titles_into_tables(body):
    """Move os títulos dos quadros para linhas mescladas no topo da tabela, como no template."""
    for tbl in list(body.iter(qn("w:tbl"))):
        # O pandoc gera cabeçalho vazio para `| | |`; o template não tem essa linha.
        for tr in tbl.findall(qn("w:tr")):
            if not text_of(tr).strip() and tr.find(".//" + qn("w:drawing")) is None:
                tbl.remove(tr)
        rows = tbl.findall(qn("w:tr"))
        header = rows[0].find(qn("w:trPr") + "/" + qn("w:tblHeader")) is not None
        ncols = len(tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol")))
        titles, prev = [], tbl.getprevious()
        while prev is not None and prev.tag == qn("w:p") and TITULO.match(text_of(prev).strip()):
            titles.insert(0, prev)
            prev = prev.getprevious()
        for p in titles:
            child(child(p, "w:pPr", 0), "w:pStyle", 0).set(qn("w:val"), "Compact")
            if US.match(text_of(p).strip()):  # deixa de ser Heading 2: negrito à mão
                for r in p.findall(qn("w:r")):
                    bold_run(r)
            tr, tc = OxmlElement("w:tr"), OxmlElement("w:tc")
            if header:
                child(tr, "w:trPr").append(OxmlElement("w:tblHeader"))
            child(tc, "w:tcPr").append(OxmlElement("w:gridSpan"))
            tc.find(qn("w:tcPr"))[0].set(qn("w:val"), str(ncols))
            tc.append(p)
            tr.append(tc)
            rows[0].addprevious(tr)
        # Sem parágrafo entre elas, tabelas vizinhas se fundem numa só ao renderizar.
        prev = tbl.getprevious()
        while prev is not None and prev.tag in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
            prev = prev.getprevious()
        if titles and prev is not None and prev.tag == qn("w:tbl"):
            tbl.addprevious(OxmlElement("w:p"))
        # Linha não se parte entre páginas.
        for tr in tbl.findall(qn("w:tr")):
            idx = 1 if tr.find(qn("w:tblPrEx")) is not None else 0
            child(child(tr, "w:trPr", idx), "w:cantSplit", 0)


def set_text(par, text):
    """Primeiro w:t recebe o texto novo; os demais ficam vazios (preserva formatação)."""
    ts = par.findall(".//" + qn("w:t"))
    ts[0].text = text
    for t in ts[1:]:
        t.text = ""


def text_of(el):
    return "".join(t.text or "" for t in el.iter(qn("w:t")))


def rel_targets(doc):
    return {rid: r.target_ref for rid, r in doc.part.rels.items()}


def toc_entry(level, text, page):
    p = OxmlElement("w:p")
    ppr = OxmlElement("w:pPr")
    style = OxmlElement("w:pStyle")
    style.set(qn("w:val"), f"Sumrio{level}")
    ppr.append(style)
    tabs = OxmlElement("w:tabs")
    tab = OxmlElement("w:tab")
    tab.set(qn("w:val"), "right")
    tab.set(qn("w:leader"), "dot")
    tab.set(qn("w:pos"), str(TOC_TAB))
    tabs.append(tab)
    ppr.append(tabs)
    p.append(ppr)
    num, _, rest = text.partition(" ")
    pieces = [num, "\t", rest] if level == 1 and num.isdigit() else [text]
    for piece in pieces + ["\t", str(page)]:
        r = OxmlElement("w:r")
        if piece == "\t":
            r.append(OxmlElement("w:tab"))
        else:
            t = OxmlElement("w:t")
            t.set(qn("xml:space"), "preserve")
            t.text = piece
            r.append(t)
        p.append(r)
    return p


def fld_run(kind, instr=None):
    """Run com w:fldChar do tipo `kind` ou, sem tipo, com a instrução do campo."""
    r = OxmlElement("w:r")
    if kind:
        el = OxmlElement("w:fldChar")
        el.set(qn("w:fldCharType"), kind)
    else:
        el = OxmlElement("w:instrText")
        el.set(qn("xml:space"), "preserve")
        el.text = instr
    r.append(el)
    return r


def bold_run(r):
    """w:b logo após rStyle/rFonts, na ordem que o schema exige."""
    rpr = child(r, "w:rPr", 0)
    head = [e for e in rpr if e.tag in (qn("w:rStyle"), qn("w:rFonts"))]
    child(rpr, "w:b", len(head))


def set_run_font(r, font_name="Arial", size_half_pts=None):
    rpr = child(r, "w:rPr", 0)
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.insert(0, rf)
    for k in list(rf.attrib.keys()):
        del rf.attrib[k]
    for k in ("ascii", "hAnsi", "cs", "eastAsia"):
        rf.set(qn(f"w:{k}"), font_name)
    if size_half_pts is not None:
        sz = rpr.find(qn("w:sz"))
        if sz is None:
            sz = OxmlElement("w:sz")
            rpr.append(sz)
        sz.set(qn("w:val"), str(size_half_pts))
        szCs = rpr.find(qn("w:szCs"))
        if szCs is None:
            szCs = OxmlElement("w:szCs")
            rpr.append(szCs)
        szCs.set(qn("w:val"), str(size_half_pts))


def format_tables_and_captions(doc):
    """Negrito e centro no cabeçalho, no título do quadro e na coluna de número; legenda em Caption."""
    def para_fmt(cell, bold, v_center=False):
        if v_center:
            tcPr = cell.get_or_add_tcPr()
            vAlign = tcPr.find(qn("w:vAlign"))
            if vAlign is None:
                vAlign = OxmlElement("w:vAlign")
                tcPr.append(vAlign)
            vAlign.set(qn("w:val"), "center")
        for p in cell.iter(qn("w:p")):
            ppr = child(p, "w:pPr", 0)
            rpr = ppr.find(qn("w:rPr"))  # jc vem antes de rPr no schema
            child(ppr, "w:jc", None if rpr is None else list(ppr).index(rpr)).set(qn("w:val"), "center")
            if bold:
                for r in p.findall(qn("w:r")):
                    bold_run(r)

    for tbl in doc.element.body.iter(qn("w:tbl")):
        rows_txt = [
            " ".join(text_of(c).strip() for c in tr.findall(qn("w:tc")))
            for tr in tbl.findall(qn("w:tr"))[:3]
        ]
        full_head = " | ".join(rows_txt)
        first_p = tbl.find(".//" + qn("w:p"))
        first_txt = text_of(first_p).strip() if first_p is not None else ""
        is_us = bool(re.match(r"^US\d{3}\s*–", first_txt))
        is_box1 = "QUADRO “3 OBJETIVOS”" in full_head

        for tr in tbl.findall(qn("w:tr")):
            tcs = tr.findall(qn("w:tc"))
            if len(tcs) == 1 and tr.find(".//" + qn("w:gridSpan")) is not None:
                para_fmt(tcs[0], False)  # título do quadro (já em negrito no texto)
            elif tr.find(qn("w:trPr") + "/" + qn("w:tblHeader")) is not None:
                for tc in tcs:
                    para_fmt(tc, True)
            elif tcs and re.fullmatch(r"\d+", text_of(tcs[0]).strip()):
                if is_box1:
                    # Item 1: numeração 1/2/3 sem a centralização extra de hoje, Arial sz 24, vAlign center
                    tcPr = tcs[0].get_or_add_tcPr()
                    vAlign = tcPr.find(qn("w:vAlign"))
                    if vAlign is None:
                        vAlign = OxmlElement("w:vAlign")
                        tcPr.append(vAlign)
                    vAlign.set(qn("w:val"), "center")
                    for p in tcs[0].iter(qn("w:p")):
                        ppr = child(p, "w:pPr", 0)
                        jc = ppr.find(qn("w:jc"))
                        if jc is not None:
                            ppr.remove(jc)
                else:
                    para_fmt(tcs[0], True, v_center=True)
    caption = doc.styles["Caption"].style_id
    for p in doc.element.body.iter(qn("w:p")):
        if re.match(r"Figura \d+ –", text_of(p).strip()):
            child(child(p, "w:pPr", 0), "w:pStyle", 0).set(qn("w:val"), caption)
            for i in list(p.iter(qn("w:i"), qn("w:iCs"))):
                i.getparent().remove(i)


def sync_pic_ext(root, extent):
    """Iguala a:ext do pic:spPr ao wp:extent, senão o renderizador usa o tamanho antigo."""
    for ext in root.iter(qn("a:ext")):
        if ext.getparent().tag == qn("a:xfrm"):
            ext.set("cx", extent.get("cx"))
            ext.set("cy", extent.get("cy"))


def format_images(doc):
    """Padroniza imagens em 15 cm de largura, proporção travada e centralizadas."""
    w_15cm = 5400000  # 15 cm em EMUs (15 * 360000)
    for p in doc.paragraphs:
        for dr in p._p.iter(qn("w:drawing")):
            inline = dr.find(qn("wp:inline"))
            if inline is None:
                continue
            docPr = inline.find(qn("wp:docPr"))
            if docPr is not None and "Caixa de Texto" in docPr.get("name", ""):
                continue
            extent = inline.find(qn("wp:extent"))
            if extent is not None:
                cx = int(extent.get("cx"))
                cy = int(extent.get("cy"))
                extent.set("cx", str(w_15cm))
                extent.set("cy", str(int(cy * w_15cm / cx)))
                sync_pic_ext(dr, extent)
            for cNvPicPr in dr.iter(qn("pic:cNvPicPr")):
                picLocks = cNvPicPr.find(qn("a:picLocks"))
                if picLocks is None:
                    picLocks = OxmlElement("a:picLocks")
                    cNvPicPr.append(picLocks)
                picLocks.set("noChangeAspect", "1")
            ppr = child(p._p, "w:pPr", 0)
            rpr = ppr.find(qn("w:rPr"))
            child(ppr, "w:jc", None if rpr is None else list(ppr).index(rpr)).set(qn("w:val"), "center")
            nxt = p._p.getnext()
            flat = [ppr]
            # FirstParagraph não existe em styles.xml; o LibreOffice ignora o jc nesse caso.
            for ps in ppr.findall(qn("w:pStyle")):
                if ps.get(qn("w:val")) == "FirstParagraph":
                    ppr.remove(ps)
            if nxt is not None and nxt.tag == qn("w:p") and re.match(r"Figura \d+ –", text_of(nxt).strip()):
                flat.append(child(nxt, "w:pPr", 0))
            for fp in flat:
                # Imagem e legenda centralizadas na página: sem lista (recuo) e sem recuo próprio.
                for np_ in fp.findall(qn("w:numPr")):
                    fp.remove(np_)
                for old_ind in fp.findall(qn("w:ind")):
                    fp.remove(old_ind)
                ind = OxmlElement("w:ind")
                for k in ("w:left", "w:right", "w:firstLine", "w:hanging"):
                    ind.set(qn(k), "0")
                jc = fp.find(qn("w:jc"))
                if jc is not None:
                    jc.addprevious(ind)
                else:
                    fp.append(ind)
                child(fp, "w:jc", None).set(qn("w:val"), "center")

    # Prototipos dos UC (item 10): linha em branco antes, legenda centralizada e borda de 1 px.
    # Itens 9 e 11 ficam de fora (o 11 tem tratamento próprio em paisagem).
    item = ""
    for p in doc.paragraphs:
        if p.style.name == "Heading 1":
            item = p.text.split(" ")[0]
            continue
        pictures = [d for d in p._p.iter(qn("wp:docPr")) if "Caixa de Texto" not in d.get("name", "")]
        if item != "10" or not pictures:
            continue

        prev = p._p.getprevious()
        has_blank = (
            prev is not None
            and prev.tag == qn("w:p")
            and not text_of(prev).strip()
            and prev.find(".//" + qn("w:drawing")) is None
        )
        if not has_blank:
            p._p.addprevious(OxmlElement("w:p"))

        ppr = child(p._p, "w:pPr", 0)
        if ppr.find(qn("w:keepNext")) is None:
            pstyle = ppr.find(qn("w:pStyle"))
            ppr.insert(0 if pstyle is None else list(ppr).index(pstyle) + 1, OxmlElement("w:keepNext"))

        caption = p._p.getnext()
        if caption is not None and caption.tag == qn("w:p") and re.match(r"Figura \d+ –", text_of(caption).strip()):
            cppr = child(caption, "w:pPr", 0)
            crpr = cppr.find(qn("w:rPr"))
            child(cppr, "w:jc", None if crpr is None else list(cppr).index(crpr)).set(qn("w:val"), "center")

        for pic_sppr in p._p.iter(qn("pic:spPr")):
            for old in pic_sppr.findall(qn("a:ln")):
                pic_sppr.remove(old)
            ln = OxmlElement("a:ln")
            ln.set("w", "9525")  # 1 px
            fill = OxmlElement("a:solidFill")
            color = OxmlElement("a:srgbClr")
            color.set("val", "000000")
            fill.append(color)
            ln.append(fill)
            pic_sppr.append(ln)


def apply_table_box_layout(tbl, kind):
    """Aplica métricas do template aos quadros dos itens 1, 2, 3 e 5."""
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), "10490")

    tblInd = tblPr.find(qn("w:tblInd"))
    if tblInd is None:
        tblInd = OxmlElement("w:tblInd")
        tblPr.append(tblInd)
    tblInd.set(qn("w:type"), "dxa")
    tblInd.set(qn("w:w"), "-5")

    tblStyle = tblPr.find(qn("w:tblStyle"))
    if tblStyle is None:
        tblStyle = OxmlElement("w:tblStyle")
        tblPr.append(tblStyle)
    tblStyle.set(qn("w:val"), "Tabelacomgrade")

    tblGrid = tbl.find(qn("w:tblGrid"))
    if tblGrid is None:
        tblGrid = OxmlElement("w:tblGrid")
        tbl.insert(1, tblGrid)
    for col in tblGrid.findall(qn("w:gridCol")):
        tblGrid.remove(col)

    if kind == "1":
        col_widths = [2019, 8471]
    elif kind == "2":
        col_widths = [5030, 5460]
    elif kind == "3.1":
        col_widths = [2268, 8222]
    elif kind == "3.2":
        col_widths = [3402, 7088]
    elif kind == "5":
        col_widths = [718, 9772]
    else:
        col_widths = [10490]

    for w in col_widths:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(w))
        tblGrid.append(gc)

    rows = tbl.findall(qn("w:tr"))
    for r_idx, r in enumerate(rows):
        trPr = child(r, "w:trPr", 0)
        # Item 2 tem células de texto muito altas no template; só define trHeight nos cabeçalhos
        if kind != "2" or r_idx in (0, 1):
            trHeight = trPr.find(qn("w:trHeight"))
            if trHeight is None:
                trHeight = OxmlElement("w:trHeight")
                trPr.append(trHeight)
            trHeight.set(qn("w:val"), "567")

        tcs = r.findall(qn("w:tc"))
        for c_idx, tc in enumerate(tcs):
            tcPr = tc.find(qn("w:tcPr"))
            if tcPr is None:
                tcPr = OxmlElement("w:tcPr")
                tc.insert(0, tcPr)

            gridSpan = tcPr.find(qn("w:gridSpan"))
            span = int(gridSpan.get(qn("w:val"))) if gridSpan is not None else 1
            if span > 1:
                tc_w = sum(col_widths[:span])
            else:
                tc_w = col_widths[c_idx] if c_idx < len(col_widths) else col_widths[-1]

            tcW = tcPr.find(qn("w:tcW"))
            if tcW is None:
                tcW = OxmlElement("w:tcW")
                tcPr.append(tcW)
            tcW.set(qn("w:type"), "dxa")
            tcW.set(qn("w:w"), str(tc_w))

            if kind != "2" or r_idx in (0, 1):
                vAlign = tcPr.find(qn("w:vAlign"))
                if vAlign is None:
                    vAlign = OxmlElement("w:vAlign")
                    tcPr.append(vAlign)
                vAlign.set(qn("w:val"), "center")

            for p in tc.findall(qn("w:p")):
                ppr = child(p, "w:pPr", 0)
                jc = ppr.find(qn("w:jc"))
                r_txt = text_of(tc).strip()
                # Título e cabeçalho centralizados (exceto linha NOME DO PRODUTO)
                if r_idx == 0:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                elif r_idx == 1 and ("OBJETIVOS" in r_txt or "DESCRIÇÃO" in r_txt or "ATOR / USUÁRIO" in r_txt):
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                elif r_idx == 2 and ("OBJETIVOS" in r_txt or "DESCRIÇÃO" in r_txt):
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                elif "NOME DO PRODUTO:" in r_txt and jc is not None:
                    ppr.remove(jc)

                for run in p.findall(qn("w:r")):
                    set_run_font(run, font_name="Arial", size_half_pts=24)


US_PER_PAGE = 2


def apply_us_table_layout(tbl, is_first_us=False):
    """Aplica layout do template à tabela de estória de usuário (item 7)."""
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), "10490")

    tblInd = tblPr.find(qn("w:tblInd"))
    if tblInd is None:
        tblInd = OxmlElement("w:tblInd")
        tblPr.append(tblInd)
    tblInd.set(qn("w:type"), "dxa")
    tblInd.set(qn("w:w"), "-5")

    tblStyle = tblPr.find(qn("w:tblStyle"))
    if tblStyle is None:
        tblStyle = OxmlElement("w:tblStyle")
        tblPr.append(tblStyle)
    tblStyle.set(qn("w:val"), "Tabelacomgrade")

    tblLayout = tblPr.find(qn("w:tblLayout"))
    if tblLayout is None:
        tblLayout = OxmlElement("w:tblLayout")
        tblPr.append(tblLayout)
    tblLayout.set(qn("w:type"), "fixed")

    tblGrid = tbl.find(qn("w:tblGrid"))
    if tblGrid is None:
        tblGrid = OxmlElement("w:tblGrid")
        tbl.insert(1, tblGrid)
    for col in tblGrid.findall(qn("w:gridCol")):
        tblGrid.remove(col)

    col_widths = [567, 9923]
    for w in col_widths:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(w))
        tblGrid.append(gc)

    rows = tbl.findall(qn("w:tr"))
    for r_idx, r in enumerate(rows):
        trPr = child(r, "w:trPr", 0)
        if r_idx == 0:
            trHeight = trPr.find(qn("w:trHeight"))
            if trHeight is None:
                trHeight = OxmlElement("w:trHeight")
                trPr.append(trHeight)
            trHeight.set(qn("w:val"), "380")

        tcs = r.findall(qn("w:tc"))
        for c_idx, tc in enumerate(tcs):
            tcPr = tc.find(qn("w:tcPr"))
            if tcPr is None:
                tcPr = OxmlElement("w:tcPr")
                tc.insert(0, tcPr)

            gridSpan = tcPr.find(qn("w:gridSpan"))
            span = int(gridSpan.get(qn("w:val"))) if gridSpan is not None else 1
            if span > 1:
                tc_w = sum(col_widths[:span])
            else:
                tc_w = col_widths[c_idx] if c_idx < len(col_widths) else col_widths[-1]

            tcW = tcPr.find(qn("w:tcW"))
            if tcW is None:
                tcW = OxmlElement("w:tcW")
                tcPr.append(tcW)
            tcW.set(qn("w:type"), "dxa")
            tcW.set(qn("w:w"), str(tc_w))

            if r_idx == 0 or (r_idx >= 3 and c_idx == 0):
                vAlign = tcPr.find(qn("w:vAlign"))
                if vAlign is None:
                    vAlign = OxmlElement("w:vAlign")
                    tcPr.append(vAlign)
                vAlign.set(qn("w:val"), "center")

            for p in tc.findall(qn("w:p")):
                ppr = child(p, "w:pPr", 0)
                jc = ppr.find(qn("w:jc"))
                if r_idx >= 3 and c_idx == 0:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                else:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "left")

                sp = ppr.find(qn("w:spacing"))
                if sp is None:
                    sp = OxmlElement("w:spacing")
                    ppr.append(sp)
                sp.set(qn("w:before"), "60")
                sp.set(qn("w:after"), "60")

                ind = ppr.find(qn("w:ind"))
                if ind is None:
                    ind = OxmlElement("w:ind")
                    ppr.append(ind)
                ind.set(qn("w:left"), "30")
                ind.set(qn("w:hanging"), "30")

                for run in p.findall(qn("w:r")):
                    set_run_font(run, font_name="Arial", size_half_pts=22)
                    if r_idx == 0:
                        bold_run(run)

                # Mantém as linhas da tabela juntas (sem separar título do corpo/critérios)
                if r_idx < len(rows) - 1:
                    child(ppr, "w:keepNext", 0)


def apply_us_summary_table_layout(tbl):
    """Aplica layout da tabela de relação de estórias de usuário (item 7)."""
    tblPr = tbl.find(qn("w:tblPr"))
    if tblPr is None:
        tblPr = OxmlElement("w:tblPr")
        tbl.insert(0, tblPr)
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:type"), "dxa")
    tblW.set(qn("w:w"), "10490")

    tblInd = tblPr.find(qn("w:tblInd"))
    if tblInd is None:
        tblInd = OxmlElement("w:tblInd")
        tblPr.append(tblInd)
    tblInd.set(qn("w:type"), "dxa")
    tblInd.set(qn("w:w"), "-5")

    tblStyle = tblPr.find(qn("w:tblStyle"))
    if tblStyle is None:
        tblStyle = OxmlElement("w:tblStyle")
        tblPr.append(tblStyle)
    tblStyle.set(qn("w:val"), "Tabelacomgrade")

    tblLayout = tblPr.find(qn("w:tblLayout"))
    if tblLayout is None:
        tblLayout = OxmlElement("w:tblLayout")
        tblPr.append(tblLayout)
    tblLayout.set(qn("w:type"), "fixed")

    tblGrid = tbl.find(qn("w:tblGrid"))
    if tblGrid is None:
        tblGrid = OxmlElement("w:tblGrid")
        tbl.insert(1, tblGrid)
    for col in tblGrid.findall(qn("w:gridCol")):
        tblGrid.remove(col)

    col_widths = [1200, 8090, 1200]
    for w in col_widths:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(w))
        tblGrid.append(gc)

    rows = tbl.findall(qn("w:tr"))
    for r_idx, r in enumerate(rows):
        tcs = r.findall(qn("w:tc"))
        for c_idx, tc in enumerate(tcs):
            tcPr = tc.find(qn("w:tcPr"))
            if tcPr is None:
                tcPr = OxmlElement("w:tcPr")
                tc.insert(0, tcPr)

            gridSpan = tcPr.find(qn("w:gridSpan"))
            span = int(gridSpan.get(qn("w:val"))) if gridSpan is not None else 1
            if span > 1:
                tc_w = sum(col_widths[:span])
            else:
                tc_w = col_widths[c_idx] if c_idx < len(col_widths) else col_widths[-1]

            tcW = tcPr.find(qn("w:tcW"))
            if tcW is None:
                tcW = OxmlElement("w:tcW")
                tcPr.append(tcW)
            tcW.set(qn("w:type"), "dxa")
            tcW.set(qn("w:w"), str(tc_w))

            vAlign = tcPr.find(qn("w:vAlign"))
            if vAlign is None:
                vAlign = OxmlElement("w:vAlign")
                tcPr.append(vAlign)
            vAlign.set(qn("w:val"), "center")

            for p in tc.findall(qn("w:p")):
                ppr = child(p, "w:pPr", 0)
                jc = ppr.find(qn("w:jc"))
                if r_idx == 0:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                elif r_idx == 1:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                elif c_idx in (0, 2):
                    child(ppr, "w:jc", 0).set(qn("w:val"), "center")
                else:
                    child(ppr, "w:jc", 0).set(qn("w:val"), "left")

                for run in p.findall(qn("w:r")):
                    set_run_font(run, font_name="Arial", size_half_pts=22)
                    if r_idx in (0, 1):
                        bold_run(run)


def assemble(pandoc_docx, template, out_docx, pages):
    """Capa, sumário, cabeçalho e rodapé do template sobre a saída do pandoc."""
    tdoc = docx.Document(template)
    doc = docx.Document(pandoc_docx)
    body = doc.element.body
    tbody = list(tdoc.element.body)
    titles_into_tables(body)
    format_tables_and_captions(doc)
    format_images(doc)

    # Elementos 0-28 do template: capa, folha de rosto, sumário e quebra de seção.
    cover = [copy.deepcopy(e) for e in tbody[:29]]
    for i, nome in enumerate(AUTORES, start=1):
        assert text_of(cover[i]).startswith("NOME AUTOR"), text_of(cover[i])
        set_text(cover[i], nome)
    assert "NOME DO PRODUTO" in text_of(cover[10]), text_of(cover[10])
    set_text(cover[10], f"- {PRODUTO.upper()} -")
    assert text_of(cover[21]).strip() == "2025", text_of(cover[21])
    set_text(cover[21], ANO)
    # O template pede para tirar o quadro de aviso e passar o texto azul para preto.
    aviso = [r for r in cover[13].findall(qn("w:r")) if text_of(r).startswith("Aviso")]
    assert len(aviso) == 1, len(aviso)
    cover[13].remove(aviso[0])
    for el in cover:
        for c in el.iter(qn("w:color")):
            if c.get(qn("w:val")) == "00B0F0":
                c.set(qn("w:val"), "000000")

    # "Curitiba" e ano saem do fluxo e ficam numa moldura ancorada na página, perto do rodapé
    # da capa: não dependem de contar parágrafos vazios, então não empurram o sumário.
    cover_frame_y = 13600  # twips a partir do topo da página (~24 cm)
    for el in (cover[20], cover[21]):
        ppr = child(el, "w:pPr", 0)
        for old_frame in ppr.findall(qn("w:framePr")):
            ppr.remove(old_frame)
        frame = OxmlElement("w:framePr")
        for name, value in (
            ("w:w", "9000"),
            ("w:wrap", "around"),
            ("w:vAnchor", "page"),
            ("w:hAnchor", "margin"),
            ("w:xAlign", "center"),
            ("w:y", str(cover_frame_y)),
        ):
            frame.set(qn(name), value)
        before = {qn(t) for t in ("w:pStyle", "w:keepNext", "w:keepLines", "w:pageBreakBefore")}
        ppr.insert(sum(1 for c in ppr if c.tag in before), frame)

    # Sumário estático: mostra apenas itens de nível 1.
    headings = [
        (1, p.text.strip())
        for p in doc.paragraphs
        if p.style.name == "Heading 1" and p.text.strip()
    ]
    sdt = cover[25]
    content = sdt.find(qn("w:sdtContent"))
    for p in list(content)[2:]:
        content.remove(p)
    for (level, text), page in zip(headings, pages or [0] * len(headings)):
        content.append(toc_entry(level, text, page))
    # Campo TOC em volta das entradas: nível 1-1.
    entries = list(content)[2:]
    first_ppr = entries[0].find(qn("w:pPr"))
    for kind, instr in (("separate", None), (None, ' TOC \\o "1-1" \\h \\z \\u '), ("begin", None)):
        first_ppr.addnext(fld_run(kind, instr))
    entries[-1].append(fld_run("end"))

    # Toda referência r:id copiada precisa apontar para o mesmo alvo da saída.
    trels, orels = rel_targets(tdoc), rel_targets(doc)
    for el in cover:
        for node in el.iter():
            for k, v in node.attrib.items():
                if k.startswith("{%s}" % node.nsmap.get("r", "")) and "relationships" in k:
                    assert orels.get(v) == trels[v], (v, trels[v], orels.get(v))

    first = body[0]
    for el in cover:
        first.addprevious(el)

    # Seção final do template (só o rodapé com o nome do produto e a página).
    body.replace(body.find(qn("w:sectPr")), copy.deepcopy(tbody[-1]))

    # Tabelas com borda, como as do template.
    for ts in body.iter(qn("w:tblStyle")):
        ts.set(qn("w:val"), "Tabelacomgrade")

    # Identificação e estilização de tabelas de quadros (itens 1, 2, 3, 5) e estórias de usuário (item 7)
    us_count = 0
    for tbl in body.iter(qn("w:tbl")):
        rows_txt = [
            " ".join(text_of(c).strip() for c in tr.findall(qn("w:tc")))
            for tr in tbl.findall(qn("w:tr"))[:3]
        ]
        full_head = " | ".join(rows_txt)
        first_p = tbl.find(".//" + qn("w:p"))
        first_txt = text_of(first_p).strip() if first_p is not None else ""

        box_kind = None
        if "QUADRO “3 OBJETIVOS”" in full_head:
            box_kind = "1"
        elif "QUADRO “É – NÃO É" in full_head:
            box_kind = "2"
        elif "PROBLEMAS" in full_head and "EXPECTATIVAS" in full_head:
            box_kind = "3.1"
        elif "VISÃO DE PRODUTO" in full_head:
            box_kind = "3.2"
        elif "ATOR / USUÁRIO" in full_head and "#" in full_head and "REQUISITO FUNCIONAL" not in full_head:
            box_kind = "5"

        is_us = bool(re.match(r"^US\d{3}\s*–", first_txt))
        is_us_summary = ("PRODUTO:" in full_head and "USESTÓRIARF" in full_head.replace(" ", ""))

        if box_kind:
            apply_table_box_layout(tbl, box_kind)
            continue
        elif is_us_summary:
            apply_us_summary_table_layout(tbl)
            continue
        elif is_us:
            is_first = (us_count == 0)
            apply_us_table_layout(tbl, is_first_us=is_first)
            # Duas estórias por página (três não cabem de forma estável); a primeira abre página.
            new_page = us_count % US_PER_PAGE == 0
            prev_el = tbl.getprevious()
            while prev_el is not None and prev_el.tag in (qn("w:bookmarkStart"), qn("w:bookmarkEnd")):
                prev_el = prev_el.getprevious()
            if prev_el is not None and prev_el.tag == qn("w:p"):
                if new_page:
                    child(child(prev_el, "w:pPr", 0), "w:pageBreakBefore", 0)
            else:
                p_break = OxmlElement("w:p")
                if new_page:
                    child(child(p_break, "w:pPr", 0), "w:pageBreakBefore", 0)
                tbl.addprevious(p_break)
            us_count += 1
            continue

        if first_txt == "RF" and "OBJETIVO" in full_head and "JUSTIFICATIVA" in full_head:
            # Matriz de rastreabilidade (9.1): larguras fixas somando a largura útil de 10490.
            widths = [1000, 1500, 1400, 900, 1600, 4090]
            tblPr = tbl.find(qn("w:tblPr"))
            tblW = tblPr.find(qn("w:tblW"))
            tblW.set(qn("w:type"), "dxa")
            tblW.set(qn("w:w"), str(sum(widths)))
            lay = OxmlElement("w:tblLayout")
            lay.set(qn("w:type"), "fixed")
            tblW.addnext(lay)
            for g, w in zip(tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol")), widths):
                g.set(qn("w:w"), str(w))
            for tr in tbl.findall(qn("w:tr")):
                for tc, w in zip(tr.findall(qn("w:tc")), widths):
                    tcW = child(tc.find(qn("w:tcPr")), "w:tcW", 0)
                    tcW.set(qn("w:type"), "dxa")
                    tcW.set(qn("w:w"), str(w))
            continue

        # Heurística para demais tabelas
        cols = tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol"))
        lens = [1] * len(cols)
        for tr in tbl.findall(qn("w:tr")):
            if tr.find(".//" + qn("w:gridSpan")) is not None:  # título mesclado
                continue
            for c, tc in enumerate(tr.findall(qn("w:tc"))[:len(cols)]):
                lens[c] = max(lens[c], len(text_of(tc)))
        total = sum(int(g.get(qn("w:w"))) for g in cols)
        fixed = {c: 300 + 110 * n for c, n in enumerate(lens) if n <= 20}
        longs = {c: min(60, n) for c, n in enumerate(lens) if n > 20}
        rest = total - sum(fixed.values())
        if not longs or rest < 1500 * len(longs):  # tudo curto: proporcional
            fixed, longs, rest = {}, dict(enumerate(lens)), total
        for c, g in enumerate(cols):
            w = fixed[c] if c in fixed else rest * longs[c] // sum(longs.values())
            g.set(qn("w:w"), str(w))

    # Cada item de nível 1 (2 em diante) e a declaração de IA começam em página nova.
    # O item 1 já começa na página seguinte à do sumário pela quebra de seção da capa.
    for p in doc.paragraphs:
        if p.style.name == "Heading 1" and not p.text.startswith("1 ") and not p.text.startswith("11 "):
            child(child(p._p, "w:pPr", 0), "w:pageBreakBefore", 0)

    # Subseção 9.1 começa em página nova, depois da Figura 2.
    for p in doc.paragraphs:
        if p.style.name.startswith("Heading") and p.text.startswith("9.1 "):
            ppr = child(p._p, "w:pPr", 0)
            if ppr.find(qn("w:pageBreakBefore")) is None:
                pstyle = ppr.find(qn("w:pStyle"))
                ppr.insert(0 if pstyle is None else list(ppr).index(pstyle) + 1, OxmlElement("w:pageBreakBefore"))

    # Itens 4 (BPMN largo) e 11 em seção paisagem (cabeçalho e rodapé preservados):
    for land_prefix in ("4 ", "11 "):
      p11 = None
      p_next_h1 = None
      for p in doc.paragraphs:
        if p11 is None and p.style.name == "Heading 1" and p.text.startswith(land_prefix):
            p11 = p
        elif p11 is not None and p_next_h1 is None and p.style.name == "Heading 1":
            p_next_h1 = p

      if p11 is not None:
          port_sect = copy.deepcopy(body.find(qn("w:sectPr")))
          land_sect = copy.deepcopy(port_sect)
          pgSz = land_sect.find(qn("w:pgSz"))
          pgSz.set(qn("w:w"), "16838")
          pgSz.set(qn("w:h"), "11906")
          pgSz.set(qn("w:orient"), "landscape")

          # Quebra de seção contínua para paisagem antes do item 11:
          p_break1 = OxmlElement("w:p")
          child(child(p_break1, "w:pPr", 0), "w:sectPr", 0).extend(list(port_sect))
          p11._p.addprevious(p_break1)

          # Ajusta as imagens do diagrama de atividades (todas as partes) para ocupar a largura útil
          # da página paisagem, mantendo a altura calculada pela proporção real de cada imagem.
          # Cada imagem começa em página própria, com a legenda logo abaixo dela:
          max_w = 8532000  # largura útil em paisagem A4 com margens de 3cm/2cm (~23.7 cm)
          max_h = 3400000  # altura máxima para caber com título, texto e legenda na mesma página
          imgs = []
          started = False
          for p in doc.paragraphs:
              if p._p is p11._p:
                  started = True
              elif started and p_next_h1 is not None and p._p is p_next_h1._p:
                  break
              elif started and p._p.find(".//" + qn("w:drawing")) is not None:
                  imgs.append(p)
          for i, para in enumerate(imgs):
              extent = para._p.find(".//" + qn("wp:extent"))
              orig_cx = int(extent.get("cx"))
              orig_cy = int(extent.get("cy"))
              ratio = orig_cy / orig_cx
              target_w = max_w
              target_h = int(target_w * ratio)
              if target_h > max_h:
                  target_h = max_h
                  target_w = int(target_h / ratio)
              extent.set("cx", str(target_w))
              extent.set("cy", str(target_h))
              sync_pic_ext(para._p, extent)
              if i > 0:
                  para.paragraph_format.page_break_before = True

          # Quebra de seção retornando ao retrato após o item 11:
          if p_next_h1 is not None:
              p_break2 = OxmlElement("w:p")
              child(child(p_break2, "w:pPr", 0), "w:sectPr", 0).extend(list(land_sect))
              p_next_h1._p.addprevious(p_break2)

    # O texto do .md já traz o número do item; a numeração automática duplicaria.
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        ppr = doc.styles[name].element.find(qn("w:pPr"))
        if ppr is not None and ppr.find(qn("w:numPr")) is not None:
            ppr.remove(ppr.find(qn("w:numPr")))

    doc.save(out_docx)
    patch_docx_files(out_docx)
    return headings


def patch_docx_files(path):
    """Ajusta cabeçalho, rodapé, estilos e fontes Arial no pacote docx."""
    import xml.etree.ElementTree as ET
    ET.register_namespace("w", "http://schemas.openxmlformats.org/wordprocessingml/2006/main")
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    def set_arial_fonts(rPr):
        rf = rPr.find("w:rFonts", ns)
        if rf is None:
            rf = ET.SubElement(rPr, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
        for k in list(rf.attrib.keys()):
            del rf.attrib[k]
        for k in ("ascii", "hAnsi", "cs", "eastAsia"):
            rf.set(f"{{http://schemas.openxmlformats.org/wordprocessingml/2006/main}}{k}", "Arial")

    with zipfile.ZipFile(path) as z:
        data = {n: z.read(n) for n in z.namelist()}

    # word/header1.xml
    if "word/header1.xml" in data:
        xml = data["word/header1.xml"].decode("utf-8")
        xml, n = re.subn(r"(>202</w:t>.*?<w:t[^>]*>)5<", r"\g<1>6<", xml, count=1, flags=re.S)
        if n == 1:
            data["word/header1.xml"] = xml.encode("utf-8")

    # word/footer2.xml
    if "word/footer2.xml" in data:
        xml = data["word/footer2.xml"].decode("utf-8")
        xml, _ = re.subn(r">Nome do Produto de Software<", f">{PRODUTO}<", xml, count=1, flags=re.S)
        xml = xml.replace('w:val="00B0F0"', 'w:val="000000"')
        data["word/footer2.xml"] = xml.encode("utf-8")

    # word/styles.xml
    if "word/styles.xml" in data:
        root = ET.fromstring(data["word/styles.xml"])
        dd_rpr = root.find(".//w:docDefaults/w:rPrDefault/w:rPr", ns)
        if dd_rpr is not None:
            set_arial_fonts(dd_rpr)
            sz = dd_rpr.find("w:sz", ns)
            if sz is None:
                sz = ET.SubElement(dd_rpr, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sz")
            sz.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val", "22")
            szCs = dd_rpr.find("w:szCs", ns)
            if szCs is None:
                szCs = ET.SubElement(dd_rpr, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}szCs")
            szCs.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val", "22")

        for s_id in ["Normal", "Sumrio1", "Sumrio2", "Sumrio3", "Legenda"]:
            s = root.find(f'.//w:style[@w:styleId="{s_id}"]', ns)
            if s is not None:
                rpr = s.find("w:rPr", ns)
                if rpr is None:
                    rpr = ET.SubElement(s, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr")
                set_arial_fonts(rpr)

        compact = root.find('.//w:style[@w:styleId="Compact"]', ns)
        if compact is None:
            compact = ET.SubElement(root, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}style")
            compact.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}type", "paragraph")
            compact.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}customStyle", "1")
            compact.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}styleId", "Compact")
            name_el = ET.SubElement(compact, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}name")
            name_el.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val", "Compact")
            ET.SubElement(compact, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}qFormat")
            pPr_el = ET.SubElement(compact, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr")
            sp_el = ET.SubElement(pPr_el, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}spacing")
            sp_el.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}before", "36")
            sp_el.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after", "36")
            rPr_c = ET.SubElement(compact, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr")
            set_arial_fonts(rPr_c)
        else:
            rpr_c = compact.find("w:rPr", ns)
            if rpr_c is None:
                rpr_c = ET.SubElement(compact, "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr")
            set_arial_fonts(rpr_c)

        # Varre runs/estilos com rFonts explícito diferente de Arial
        for rf in root.findall(".//w:rFonts", ns):
            for k in list(rf.attrib.keys()):
                if rf.attrib[k] != "Arial":
                    rf.attrib[k] = "Arial"

        data["word/styles.xml"] = ET.tostring(root, encoding="utf-8")

    # Varre runs em word/document.xml com rFonts explícito diferente de Arial
    if "word/document.xml" in data:
        doc_root = ET.fromstring(data["word/document.xml"])
        for rf in doc_root.findall(".//w:rFonts", ns):
            for k in list(rf.attrib.keys()):
                if rf.attrib[k] != "Arial":
                    rf.attrib[k] = "Arial"
        data["word/document.xml"] = ET.tostring(doc_root, encoding="utf-8")

    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in data.items():
            z.writestr(n, b)


def to_pdf(docx_path, outdir, profile):
    subprocess.run(
        ["soffice", f"-env:UserInstallation=file://{profile}", "--headless",
         "--convert-to", "pdf", "--outdir", str(outdir), str(docx_path)],
        check=True, capture_output=True,
    )
    return Path(outdir) / (Path(docx_path).stem + ".pdf")


def norm(s):
    return re.sub(r"\s+", " ", s).strip().upper()


def heading_pages(pdf, headings):
    """Número de página impresso no rodapé de cada título, na ordem do documento."""
    text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                          check=True, capture_output=True, text=True).stdout
    pages = text.split("\f")
    labels = []
    for pg in pages:
        m = re.search(re.escape(PRODUTO) + r"\s+(\d+)\s*$", pg.rstrip())
        labels.append(int(m.group(1)) if m else None)
    start = next(i for i, l in enumerate(labels) if l is not None)
    result, i = [], start
    for _, h in headings:
        while i < len(pages) and norm(h) not in norm(pages[i]):
            i += 1
        assert i < len(pages), f"título não encontrado no PDF: {h}"
        result.append(labels[i])
    return result


def check():
    assert sorted(ITEMS) == list(range(1, 16))
    for n, src in ITEMS.items():
        if isinstance(src, list):
            for f in src:
                assert (ESP / f).is_file(), f
    assert DECLARACAO.is_file()
    assert parse_range(1, 11) == list(range(1, 12))
    assert parse_range(6, 6) == [6]
    for bad in [(9, 3), (0, 5), (1, 16)]:
        try:
            parse_range(*bad)
        except ValueError:
            continue
        raise AssertionError(bad)
    md = drop_column("| A | ARQUIVO |\n|---|---|\n| x | [a.md](a.md) |\n\ntexto", "ARQUIVO")
    assert md == "| A |\n|---|\n| x |\n\ntexto", md
    md = renumber_figures("*Figura 7 – a*\n*Figura 2 – b*\nver Figura 7")
    assert md == "*Figura 1 – a*\n*Figura 2 – b*\nver Figura 7", md
    assert TITULO.match("QUADRO “3 OBJETIVOS”") and TITULO.match("US001 – REQUISITO RF017: x")
    assert not TITULO.match("1 QUADRO “3 OBJETIVOS”") and not TITULO.match("Rastreabilidade")
    print("check ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("de", nargs="?", type=int, default=1)
    ap.add_argument("ate", nargs="?", type=int, default=11, metavar="até")
    ap.add_argument("--template", default=os.environ.get("ESSW_TEMPLATE"))
    ap.add_argument("--saida", default=str(REPO / "build"))
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--pdf", action="store_true", help="também gera o PDF")
    a = ap.parse_args()
    if a.check:
        return check()
    try:
        items = parse_range(a.de, a.ate)
    except ValueError as e:
        ap.error(str(e))
    if not a.template or not Path(a.template).is_file():
        ap.error("informe o Template.docx com --template ou ESSW_TEMPLATE")

    saida = Path(a.saida)
    saida.mkdir(parents=True, exist_ok=True)
    nome = f"Especificação - itens {a.de}-{a.ate}"
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "in.md").write_text(build_markdown(items), encoding="utf-8")
        (tmp / "br.lua").write_text(LUA_BR)
        subprocess.run(
            ["pandoc", "-f", "gfm", "-t", "docx", f"--reference-doc={a.template}",
             f"--lua-filter={tmp / 'br.lua'}", "-o", str(tmp / "pandoc.docx"),
             str(tmp / "in.md")],
            check=True,
        )
        # Passo 1 com páginas zeradas (mesmo layout); passo 2 com as páginas reais.
        draft = tmp / f"{nome}.docx"
        headings = assemble(tmp / "pandoc.docx", a.template, draft, None)
        pages = heading_pages(to_pdf(draft, tmp, tmp / "lo"), headings)
        final = saida / f"{nome}.docx"
        assemble(tmp / "pandoc.docx", a.template, final, pages)
        if a.pdf:
            print(to_pdf(final, saida, tmp / "lo"))
    print(final)


if __name__ == "__main__":
    main()
