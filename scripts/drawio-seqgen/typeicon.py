"""Add a circled type letter (C/A/E) to every class header of a draw.io class diagram."""
import re, sys, html
import xml.etree.ElementTree as ET

for path in sys.argv[1:]:
    tree = ET.parse(path); root = tree.getroot().find('.//root')
    old = {}
    for c in list(root):
        if c.get('id', '').startswith('typeicon_'):
            old[c.get('id')[9:]] = c.get('value'); root.remove(c)
    for c in list(root):
        st, val = c.get('style', ''), c.get('value', '')
        if c.get('vertex') != '1' or c.get('parent') != '1' or 'fillColor=#F2F2F2' not in st or '<b>' not in val:
            continue
        g = c.find('mxGeometry'); x, y, w = (float(g.get(k)) for k in ('x', 'y', 'width'))
        m = re.search(r'startSize=(\d+)', st); head = float(m.group(1)) if m else float(g.get('height'))
        enum = 'enumeration' in val
        letter = 'E' if enum or old.get(c.get('id')) == 'E' else 'I' if 'interface' in val else 'A' if '<i>' in val else 'C'
        if enum:
            val = re.sub(r'&lt;&lt;enumeration&gt;&gt;\s*(<br\s*/?>)?', '', val); c.set('value', val)
        longest = max(len(html.unescape(html.unescape(re.sub(r'<[^>]+>', '', p)))) for p in re.split(r'<br\s*/?>', val))
        st = re.sub(r'spacingLeft=\d+;', '', st) + 'spacingLeft=30;'
        if '<br' not in val: st = st.replace('verticalAlign=top', 'verticalAlign=middle')
        c.set('style', st)
        ic = ET.SubElement(root, 'mxCell', id='typeicon_' + c.get('id'), value=letter, vertex='1', parent='1',
            style='ellipse;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=1.5;fontFamily=Helvetica;fontSize=11;fontStyle=1;fontColor=#000000;')
        ET.SubElement(ic, 'mxGeometry', {'x': str(int(x + 6)), 'y': str(int(y + (head - 20) / 2)), 'width': '20', 'height': '20', 'as': 'geometry'})
        print(path.split('/')[-1][:-7], c.get('id'), letter)
    ET.indent(tree, '  '); tree.write(path, encoding='UTF-8', xml_declaration=True)
