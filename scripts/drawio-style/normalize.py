"""Padroniza setas e legenda dos diagramas dos itens 12 e 13 (.drawio).

Setas: estilo ortogonal sem cantos arredondados, sem pontos de saída/entrada fixos e sem
waypoints, para o draw.io traçar a linha reta entre as caixas. Legenda: uma só, em coluna,
cantos retos, abaixo e à direita do conteúdo, com os itens que o diagrama usa.

Uso: python3 scripts/drawio-style/normalize.py [arquivo.drawio ...]  (sem argumento: todos)
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / "especificacao" / "diagramas"
W, ROW, PAD = 300, 26, 10
ENUM = "#D0F0F0"
ROLES = {  # cor -> papel, na ordem da legenda
    "#DAE8FC": "Controller", "#D5E8D4": "Service", "#FFE6CC": "Repository",
    "#E1D5E7": "DTO / Request", "#FFF2CC": "Resource", "#F5F5F5": "Entity",
    "#F8CECC": "Interface", ENUM: "Enumeração",
}
LINES = {  # tipo -> (estilo da amostra, texto)
    "assoc": ("endArrow=open;endFill=0;", "Associação navegável"),
    "plain": ("endArrow=none;", "Associação"),
    "comp": ("startArrow=diamond;startFill=1;endArrow=none;", "Composição (a parte não existe sem o todo)"),
    "agreg": ("startArrow=diamond;startFill=0;endArrow=none;", "Agregação"),
    "gen": ("endArrow=block;endFill=0;", "Generalização (herança)"),
    "real": ("dashed=1;endArrow=block;endFill=0;", "Realização (implementa interface)"),
    "dep": ("dashed=1;endArrow=open;endFill=0;", "Dependência (usa)"),
    "fk": ("endArrow=block;endFill=1;", "Chave estrangeira (FK aponta para a PK)"),
}
DROP = re.compile(r"rounded=[^;]*;?|edgeStyle=[^;]*;?|curved=[^;]*;?")


def prop(style, key):
    m = re.search(rf"(?:^|;){key}=([^;]*)", style)
    return m.group(1) if m else None


def setprop(style, key, val):
    style = re.sub(rf"(^|;){key}=[^;]*", "", style).strip(";")
    return f"{style};{key}={val}" if style else f"{key}={val}"


def kind(style, item12):
    dashed = prop(style, "dashed") == "1"
    start, end = prop(style, "startArrow") or "none", prop(style, "endArrow") or "none"
    if item12:
        return "fk"
    if start.startswith("diamond"):
        return "comp" if prop(style, "startFill") != "0" else "agreg"
    if end == "block" and prop(style, "endFill") == "0":
        return "real" if dashed else "gen"
    if dashed:
        return "dep"
    return "plain" if end == "none" else "assoc"


def normalize(path):
    tree = ET.parse(path)
    root = tree.find(".//root")
    item12 = path.name.startswith("12-")
    cells = list(root)
    byid = {c.get("id"): c for c in cells}

    # Legenda antiga: a célula "Legenda", seus filhos e o que estiver dentro da caixa dela.
    old = [c for c in cells if "Legenda" in (c.get("value") or "")]
    gone = set()
    for lg in old:
        g = lg.find("mxGeometry")
        x, y = float(g.get("x", 0)), float(g.get("y", 0))
        w, h = float(g.get("width", 0)), float(g.get("height", 0))
        gone.add(lg.get("id"))
        for c in cells:
            cg = c.find("mxGeometry")
            if c.get("parent") == "1" and c.get("vertex") == "1" and cg is not None:
                cx, cy = float(cg.get("x", -1e9)), float(cg.get("y", -1e9))
                if x <= cx < x + w and y <= cy < y + h:
                    gone.add(c.get("id"))
    changed = True
    while changed:
        changed = False
        for c in cells:
            if c.get("parent") in gone and c.get("id") not in gone:
                gone.add(c.get("id"))
                changed = True
    for c in cells:
        if c.get("id") in gone or (c.get("edge") == "1" and ({c.get("source"), c.get("target")} & gone)):
            root.remove(c)
    cells = list(root)

    used_lines, loose = [], []
    for c in cells:
        if c.get("edge") != "1":
            continue
        st = DROP.sub("", c.get("style", "")).strip(";")
        k = kind(st, item12)
        if k == "assoc" and prop(st, "endArrow") == "block":  # seta cheia em associação vira aberta
            st = setprop(setprop(st, "endArrow", "open"), "endFill", "0")
        if k == "dep" and (prop(st, "endArrow") or "none") == "none":
            st = setprop(setprop(st, "endArrow", "open"), "endFill", "0")
        c.set("style", "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;" + st)
        g = c.find("mxGeometry")
        if g is not None:
            for arr in g.findall("Array"):
                g.remove(arr)
        if not c.get("source") or not c.get("target"):
            loose.append(c.get("id"))
        if k not in used_lines:
            used_lines.append(k)

    # Caixas: enumeração ganha cor própria; papéis presentes vêm da cor de preenchimento.
    tops = [c for c in cells if c.get("vertex") == "1" and c.get("parent") == "1"]
    fills = set()
    dashed_box = False
    for c in tops:
        st, val = c.get("style", ""), (c.get("value") or "")
        if "shape=note" in st:  # notas: amarelo de post-it, distinto de qualquer papel
            c.set("style", setprop(st, "fillColor", "#FFF9DB"))
            continue
        if not st.startswith("swimlane") and "shape=table" not in st:
            continue
        if not item12 and (c.get("id", "").lower().startswith("enum") or "enum" in val.lower()):
            st = setprop(st, "fillColor", ENUM)
            c.set("style", st)
        elif not item12 and path.name.endswith("negocial.drawio"):
            st = setprop(st, "fillColor", "#F5F5F5")
            c.set("style", st)
        f = (prop(st, "fillColor") or "").upper()
        if f in ROLES:
            fills.add(f)
        dashed_box |= prop(st, "dashed") == "1"

    # Legenda nova, abaixo e à direita de todo o conteúdo.
    xs, ys = [], []
    for c in tops:
        g = c.find("mxGeometry")
        if g is not None and g.get("width"):
            xs.append(float(g.get("x", 0)) + float(g.get("width")))
            ys.append(float(g.get("y", 0)) + float(g.get("height", 0)))
    x0, y0 = max(xs) - W, max(ys) + 40
    rows = []
    if not item12:
        rows += [("role", f) for f in ROLES if f in fills]
        rows.append(("text", "(C) Classe · (A) Abstrata · (I) Interface · (E) Enumeração"))
    else:
        rows.append(("text", "PK: chave primária · FK: chave estrangeira · 1, 0..*: cardinalidade"))
    if dashed_box:
        rows.append(("dashed", "Classe de outra área (só referenciada)" if not item12 else "Tabela de outra área (só referenciada)"))
    rows += [("line", k) for k in LINES if k in used_lines]

    def add(id_, value, style, x, y, w, h, **kw):
        el = ET.SubElement(root, "mxCell", id=id_, value=value, style=style, parent="legend", **kw)
        geo = ET.SubElement(el, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h))
        geo.set("as", "geometry")
        return el

    H = 30 + len(rows) * (ROW + 6) + PAD
    box = ET.SubElement(root, "mxCell", id="legend", value="Legenda", vertex="1", parent="1",
                        style="swimlane;html=1;rounded=0;startSize=26;fontStyle=1;fillColor=#4D4D4D;fontColor=#FFFFFF;"
                              "swimlaneFillColor=#FFFFFF;strokeColor=#000000;collapsible=0;")
    ET.SubElement(box, "mxGeometry", x=str(x0), y=str(y0), width=str(W), height=str(H)).set("as", "geometry")
    y = 32
    for i, (t, v) in enumerate(rows):
        if t == "role":
            add(f"legend_{i}", ROLES[v], f"rounded=0;html=1;fillColor={v};strokeColor=#000000;fontStyle=1;",
                PAD, y, W - 2 * PAD, ROW, vertex="1")
        elif t == "text":
            add(f"legend_{i}", v, "text;html=1;align=left;verticalAlign=middle;fontSize=10;whiteSpace=wrap;",
                PAD, y, W - 2 * PAD, ROW, vertex="1")
        elif t == "dashed":
            add(f"legend_{i}a", "", "rounded=0;html=1;dashed=1;fillColor=#FFFFFF;strokeColor=#000000;",
                PAD, y + 4, 40, ROW - 8, vertex="1")
            add(f"legend_{i}", v, "text;html=1;align=left;verticalAlign=middle;fontSize=10;", PAD + 50, y,
                W - 2 * PAD - 50, ROW, vertex="1")
        else:
            sty, txt = LINES[v]
            a = add(f"legend_{i}s", "", "point;size=1;strokeColor=none;fillColor=none;", PAD, y + ROW / 2, 1, 1, vertex="1")
            b = add(f"legend_{i}t", "", "point;size=1;strokeColor=none;fillColor=none;", PAD + 50, y + ROW / 2, 1, 1, vertex="1")
            add(f"legend_{i}e", "", "edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;endSize=8;startSize=10;" + sty,
                0, 0, 0, 0, edge="1", source=a.get("id"), target=b.get("id")).find("mxGeometry").set("relative", "1")
            add(f"legend_{i}", txt, "text;html=1;align=left;verticalAlign=middle;fontSize=10;whiteSpace=wrap;",
                PAD + 60, y, W - 2 * PAD - 60, ROW, vertex="1")
        y += ROW + 6
    ET.indent(tree)
    tree.write(path, encoding="UTF-8", xml_declaration=True)
    return loose


if __name__ == "__main__":
    files = [Path(a) for a in sys.argv[1:]] or sorted(DIR.glob("1[23]-*.drawio"))
    for f in files:
        loose = normalize(f)
        print(f.name, f"pontas soltas: {loose}" if loose else "ok")
