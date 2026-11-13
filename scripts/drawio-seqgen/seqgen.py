"""Generate draw.io sequence diagrams (one layout for all) from a PlantUML subset.

Subset: actor/boundary/control/entity/database, A -> B / A --> B with ++ / --,
alt / else / opt / end, deactivate. Usage: seqgen.py in.puml out.drawio
"""
import html, math, re, sys
import xml.etree.ElementTree as ET

FONT = 'fontFamily=Helvetica;fontSize=12;fontColor=#000000;'
LINE = 'strokeColor=#000000;strokeWidth=1.5;'
ICON = {'actor': ('shape=umlActor;verticalLabelPosition=bottom;', 30, 50),
        'boundary': ('shape=umlBoundary;', 50, 40), 'control': ('shape=umlControl;', 40, 46),
        'entity': ('shape=umlEntity;', 40, 40), 'database': ('shape=cylinder3;size=8;boundedLbl=1;', 40, 46)}
MINGAP, MAXGAP, BAR, TOP = 160, 260, 10, 110   # BAR = half width of an activation bar

def up10(v): return int(math.ceil(v / 10.0) * 10)

def tw(s):
    """Approximate rendered width of Helvetica 12 px text (deliberately generous)."""
    return sum(3.6 if c in " iIljtf.,:;()[]'\"!|" else 10.5 if c in 'mwMW' else
               8.0 if c.isupper() or c in '_%@' else 6.4 for c in s)

def wrap(text, width):
    lines, cur = [], ''
    for word in text.split():
        if cur and tw(cur + ' ' + word) > width: lines.append(cur); cur = word
        else: cur = (cur + ' ' + word).strip()
    return lines + [cur] if cur else lines

def need(text, maxlines=3):
    """Smallest box width that fits the text in at most maxlines lines."""
    w = up10(max(tw(x) for x in text.split()))
    while len(wrap(text, w)) > maxlines: w += 10
    return w

def parse(path):
    parts, events, stack, root = [], [], [], {'kids': [], 'idx': set()}
    cur = root
    for raw in open(path, encoding='utf-8'):
        ln = raw.strip()
        m = re.match(r'(actor|boundary|control|entity|database)\s+(?:"([^"]+)"|(\w+))(?:\s+as\s+(\w+))?$', ln)
        if m:
            parts.append({'kind': m[1], 'name': m[2] or m[3], 'id': m[4] or m[3] or m[2]}); continue
        ids = [p['id'] for p in parts]
        m = re.match(r'(\w+)\s*(-->|->)\s*(\w+)\s*(\+\+|--)?\s*(?::\s*(.*))?$', ln)
        if m and m[1] in ids and m[3] in ids:
            e = {'t': 'msg', 's': ids.index(m[1]), 'd': ids.index(m[3]), 'ret': m[2] == '-->', 'act': m[4], 'text': m[5] or ''}
            events.append(e)
            for f in stack: f['idx'] |= {e['s'], e['d']}
            continue
        m = re.match(r'(alt|opt)\s+(.*)$', ln)
        if m:
            f = {'t': 'frag', 'kind': m[1], 'cond': m[2], 'idx': set(), 'kids': [], 'below': 0}
            (stack[-1] if stack else root)['kids'].append(f); stack.append(f); events.append(f); continue
        m = re.match(r'else\s+(.*)$', ln)
        if m: events.append({'t': 'else', 'f': stack[-1], 'cond': m[1]}); continue
        if ln == 'end': events.append({'t': 'end', 'f': stack.pop()}); continue
        m = re.match(r'deactivate\s+(\w+)$', ln)
        if m: events.append({'t': 'deact', 'p': ids.index(m[1])})
    assert not stack, 'unclosed fragment'
    def depth(f):
        f['below'] = 1 + max([depth(k) for k in f['kids']], default=-1); return f['below']
    for f in root['kids']: depth(f)
    return parts, events

def build(src, dst):
    parts, events = parse(src)
    n = len(parts)
    frags = [e for e in events if e['t'] == 'frag']
    for f in frags:
        f['lo'], f['hi'] = min(f['idx']), max(f['idx'])
        if f['lo'] == f['hi']: f['hi'] = min(n - 1, f['lo'] + 1)
    gapof = lambda e: e['s'] if e['d'] > e['s'] else e['s'] - 1      # gap next to the sender
    # column gaps: wide enough for names, for the labels next to the sender and for the conditions
    gap = [MINGAP] * (n - 1)
    for i in range(n - 1):
        want = [(tw(parts[i]['name']) + tw(parts[i + 1]['name'])) / 2 + 30]
        want += [need(e['text']) + 2 * BAR + 30 for e in events if e['t'] == 'msg' and e['text'] and gapof(e) == i]
        want += [need(e['cond'] + '[]') + 2 * BAR + 30 for e in events
                 if (e['t'] == 'frag' and e['lo'] == i) or (e['t'] == 'else' and e['f']['lo'] == i)]
        gap[i] = min(MAXGAP, max(MINGAP, up10(max(want))))
    maxbelow = max([f['below'] for f in frags], default=0)
    X = [up10(max(80 + 10 * maxbelow, tw(parts[0]['name']) / 2 + 20))]
    for g in gap: X.append(X[-1] + g)

    cells, labels = {k: [] for k in ('frame', 'life', 'bar', 'edge', 'text')}, []
    def cell(layer, style, value='', geo=None, pts=None):
        c = ET.Element('mxCell', value=value, style=style, parent='1')
        if pts:
            c.set('edge', '1'); g = ET.SubElement(c, 'mxGeometry', relative='1')
            for (x, y), role in zip(pts, ('sourcePoint', 'targetPoint')):
                ET.SubElement(g, 'mxPoint', {'x': str(x), 'y': str(y), 'as': role})
        else:
            c.set('vertex', '1'); x, y, w, h = geo
            assert all(v % 10 == 0 for v in geo), ('off grid', value, geo)
            g = ET.SubElement(c, 'mxGeometry', x=str(x), y=str(y), width=str(w), height=str(h))
        g.set('as', 'geometry'); cells[layer].append(c)
    def text(lines, x, w, bottom, style):
        h = up10(14.4 * len(lines) + 10)
        assert all(tw(l) <= w for l in lines), ('label wider than its box', lines, w)
        box = (x, bottom - h, w, h)
        for o in labels:
            assert box[0] >= o[0] + o[2] or o[0] >= box[0] + box[2] or box[1] >= o[1] + o[3] or o[1] >= box[1] + box[3], ('label overlap', lines)
        labels.append(box)
        cell('text', 'text;html=1;strokeColor=none;fillColor=none;verticalAlign=bottom;spacing=0;spacingBottom=5;' + style + FONT,
             '<br>'.join(html.escape(l) for l in lines), box)
    def gapbox(i):                                  # free box between lifelines i and i+1
        return X[i] + BAR + 10, gap[i] - 2 * BAR - 20

    for i, p in enumerate(parts):
        st, w, h = ICON[p['kind']]
        cell('life', st + 'html=1;fillColor=#FFFFFF;' + LINE + FONT, '', (X[i] - w // 2 - (X[i] - w // 2) % 10 if False else up10(X[i] - w / 2 - 5), 20, up10(w), up10(h)))
        nw = up10(tw(p['name']) + 10); nx = X[i] - nw // 2
        cell('text', 'text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;spacing=0;' + FONT,
             html.escape(p['name']), (nx - nx % 10, 70, nw + (10 if nx % 10 else 0), 20))

    y, active, last, arrows = TOP, {}, {}, 0
    def close(p, end):
        y0 = active.pop(p)
        cell('bar', 'html=1;fillColor=#FFFFFF;' + LINE, '', (X[p] - BAR, y0, 2 * BAR, max(20, end - y0)))
    def condrow(f, cond, top):
        bx, bw = gapbox(f['lo']); lines = wrap('[' + cond + ']', bw)
        h = up10(14.4 * len(lines) + 10); text(lines, bx, bw, top + 10 + h, 'align=left;fontStyle=1;')
        return top + 10 + h + 10
    for e in events:
        if e['t'] == 'msg':
            s, d = e['s'], e['d']; lines = wrap(e['text'], gapbox(gapof(e))[1]) if e['text'] else []
            y += 10 + (up10(14.4 * len(lines) + 10) if lines else 20)
            if lines: bx, bw = gapbox(gapof(e)); text(lines, bx, bw, y, 'align=center;')
            if e['act'] == '++' and not e['ret']: active.setdefault(d, y)
            right = d > s
            edge = lambda p, out: X[p] + (BAR if out else -BAR) if p in active else X[p]
            cell('edge', 'html=1;rounded=0;' + LINE + ('dashed=1;endArrow=open;endSize=8;' if e['ret'] else 'endArrow=block;endFill=1;endSize=8;'),
                 pts=[(edge(s, right), y), (edge(d, not right), y)])
            arrows += 1; last[s] = last[d] = y
            if e['act'] == '--': close(s, y + 10)
            if e['act'] == '++' and e['ret']: active.setdefault(d, y)
        elif e['t'] == 'frag':
            y += 30; e['top'] = y; e['div'] = []
            y = condrow(e, e['cond'], y) - 10
        elif e['t'] == 'else':
            y += 30; e['f']['div'].append(y); y = condrow(e['f'], e['cond'], y) - 10
        elif e['t'] == 'end':
            f = e['f']; y += 30
            l, r = X[f['lo']] - 60 - 10 * f['below'], X[f['hi']] + 60 + 10 * f['below']
            cell('frame', 'shape=umlFrame;html=1;width=40;height=20;fillColor=#F2F2F2;swimlaneFillColor=none;pointerEvents=0;fontStyle=1;' + LINE + FONT,
                 f['kind'], (l, f['top'], r - l, y - f['top']))
            for dy in f['div']:
                cell('frame', 'html=1;rounded=0;endArrow=none;dashed=1;' + LINE, pts=[(l, dy), (r, dy)])
        elif e['t'] == 'deact' and e['p'] in active:
            close(e['p'], last[e['p']] + 10)
    for p in list(active): close(p, last[p] + 10)
    y += 50
    for i in range(n):
        cell('life', 'html=1;rounded=0;endArrow=none;dashed=1;dashPattern=4 4;strokeColor=#000000;strokeWidth=1;', pts=[(X[i], 96), (X[i], y)])
    assert arrows == sum(1 for e in events if e['t'] == 'msg')

    name = dst.rsplit('/', 1)[-1][:-7]
    mx = ET.Element('mxfile', host='Electron', compressed='false')
    model = ET.SubElement(ET.SubElement(mx, 'diagram', id=name, name=name), 'mxGraphModel', grid='1', gridSize='10',
                          page='0', math='0', shadow='0')
    root = ET.SubElement(model, 'root'); ET.SubElement(root, 'mxCell', id='0'); ET.SubElement(root, 'mxCell', id='1', parent='0')
    k = 2
    for layer in ('frame', 'life', 'bar', 'edge', 'text'):
        for c in cells[layer]: c.set('id', '%s_%d' % (layer, k)); k += 1; root.append(c)
    ET.indent(mx, '  '); ET.ElementTree(mx).write(dst, encoding='UTF-8', xml_declaration=True)
    print('%s: %d participantes, %d mensagens, %d fragmentos, %dx%d' % (name, n, arrows, len(frags), X[-1] + 80, y))

if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2])
