#!/usr/bin/env python3
"""Gera o documento de especificação (DOCX e PDF) a partir do Template.docx.

Uso:
    python3 scripts/build_doc.py [de] [até] [--template T.docx] [--saida DIR]
    python3 scripts/build_doc.py --check

Exemplos: `1 11` gera o RA1 (padrão), `6 8` só os itens 6 a 8, `1 15` tudo.
O template da disciplina não fica no repositório: passe --template ou
defina ESSW_TEMPLATE. Precisa de pandoc, soffice (LibreOffice) e pdftotext.
"""
import argparse
import copy
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

-- A declaração de IA começa em página nova (o título ficava órfão no pé da página).
function Header(el)
  if el.level == 1 and pandoc.utils.stringify(el):match('^Declaração') then
    return {pandoc.RawBlock('openxml', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'), el}
  end
end
"""

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
    return "\n\n".join(parts)


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


def assemble(pandoc_docx, template, out_docx, pages):
    """Capa, sumário, cabeçalho e rodapé do template sobre a saída do pandoc."""
    tdoc = docx.Document(template)
    doc = docx.Document(pandoc_docx)
    body = doc.element.body
    tbody = list(tdoc.element.body)

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

    # Sumário estático: o LibreOffice não atualiza o campo TOC na conversão.
    # ponytail: sem campo, o Word não atualiza o sumário; regere pelo script.
    headings = [
        (int(p.style.name[-1]), p.text.strip())
        for p in doc.paragraphs
        if p.style.name in ("Heading 1", "Heading 2") and p.text.strip()
    ]
    sdt = cover[25]
    content = sdt.find(qn("w:sdtContent"))
    for p in list(content)[2:]:
        content.remove(p)
    for (level, text), page in zip(headings, pages or [0] * len(headings)):
        content.append(toc_entry(level, text, page))

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
    # O leitor gfm do pandoc divide a largura por igual; a coluna "#" ficava com
    # metade da página. Coluna curta (até 20 caracteres) recebe a largura do seu
    # maior texto; as longas repartem o resto pelo tamanho do texto.
    for tbl in body.iter(qn("w:tbl")):
        cols = tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol"))
        lens = [1] * len(cols)
        for tr in tbl.findall(qn("w:tr")):
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

    # O texto do .md já traz o número do item; a numeração automática duplicaria.
    for name in ("Heading 1", "Heading 2", "Heading 3"):
        ppr = doc.styles[name].element.find(qn("w:pPr"))
        if ppr is not None and ppr.find(qn("w:numPr")) is not None:
            ppr.remove(ppr.find(qn("w:numPr")))

    doc.save(out_docx)
    patch_parts(out_docx, {
        "word/header1.xml": [(r"(>202</w:t>.*?<w:t[^>]*>)5<", r"\g<1>6<")],
        "word/footer2.xml": [(r">Nome do Produto de Software<", f">{PRODUTO}<"),
                             (r"w:val=\"00B0F0\"", "w:val=\"000000\"")],
        # O pandoc marca as células de tabela com o estilo Compact. Sem ele no
        # styles.xml, o LibreOffice tira o texto das células e desmonta a tabela.
        "word/styles.xml": [(r"</w:styles>", COMPACT_STYLE + "</w:styles>")],
    })
    return headings


COMPACT_STYLE = (
    '<w:style w:type="paragraph" w:customStyle="1" w:styleId="Compact">'
    '<w:name w:val="Compact"/><w:qFormat/>'
    '<w:pPr><w:spacing w:before="36" w:after="36"/></w:pPr></w:style>'
)


def patch_parts(path, subs):
    """Substituições de texto nas partes XML do cabeçalho e do rodapé."""
    with zipfile.ZipFile(path) as z:
        data = {n: z.read(n) for n in z.namelist()}
    for name, rules in subs.items():
        xml = data[name].decode("utf-8")
        for pat, rep in rules:
            xml, n = re.subn(pat, rep, xml, count=1, flags=re.S)
            assert n == 1, (name, pat)
        data[name] = xml.encode("utf-8")
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
    print("check ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("de", nargs="?", type=int, default=1)
    ap.add_argument("ate", nargs="?", type=int, default=11, metavar="até")
    ap.add_argument("--template", default=os.environ.get("ESSW_TEMPLATE"))
    ap.add_argument("--saida", default=str(REPO / "build"))
    ap.add_argument("--check", action="store_true")
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
        pdf = to_pdf(final, saida, tmp / "lo")
    print(final)
    print(pdf)


if __name__ == "__main__":
    main()
