import html, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from slides_data import S, SECTIONS

esc = lambda t: html.escape(t, quote=False)

def quotes_html(quotes, small=False):
    cls = "pull-quote" + (" is-small" if small else "")
    out = []
    for q, attr in quotes:
        out.append(f'<div class="quote-item reveal"><blockquote class="{cls}">{esc(q)}</blockquote>'
                   f'<div class="pull-attr">{esc(attr)}</div></div>')
    return "\n".join(out)

def aside_html(a):
    label, text = a
    return (f'<div class="aside reveal"><span class="aside-label">{esc(label)}</span>'
            f'<p class="aside-text">{esc(text)}</p></div>')

def cards_html(cards):
    out = ['<div class="contrast-row reveal">']
    for label, value, note in cards:
        n = f'<p class="contrast-note">{esc(note)}</p>' if note else ''
        out.append(f'<div class="contrast-col"><span class="contrast-label">{esc(label)}</span>'
                   f'<p class="contrast-value">{esc(value)}</p>{n}</div>')
    out.append('</div>')
    return "\n".join(out)

def rows_html(rows):
    out = ['<div class="rows reveal">']
    for label, desc in rows:
        out.append(f'<div class="row"><span class="row-label">{esc(label)}</span><span class="row-desc">{esc(desc)}</span></div>')
    out.append('</div>')
    return "\n".join(out)

def slide_html(i, s):
    t = s["type"]
    notes = s.get("notes", "")
    notes_html = f'<div class="notes" hidden>{esc(notes)}</div>' if notes else '<div class="notes" hidden></div>'
    if t == "section":
        num, title = SECTIONS[s["sec"]]
        return (f'<section class="slide slide--hero" data-index="{i}">'
                f'<div class="frame"><div class="kicker reveal">Section {num}</div>'
                f'<h1 class="headline reveal">{esc(title)}</h1></div>'
                f'<span class="pagenum"></span>{notes_html}</section>')
    ph = " is-placeholder" if s.get("ph") else ""
    parts = []
    if s.get("kicker"):
        parts.append(f'<div class="kicker reveal">{esc(s["kicker"])}</div>')
    hs = " is-md" if (t in ("finding", "quote", "rows") or len(s.get("headline", "")) > 62) else ""
    if s.get("headline"):
        parts.append(f'<h1 class="headline{hs}{ph} reveal">{esc(s["headline"])}</h1>')
    if t == "finding" and s.get("numeral"):
        parts.append(f'<div class="numeral-row reveal"><div class="numeral">{esc(s["numeral"])}</div>'
                     f'<p class="numeral-caption">{esc(s["caption"])}</p></div>')
    if t == "contrast" and s.get("cards"):
        parts.append(cards_html(s["cards"]))
    if t == "rows" and s.get("rows"):
        parts.append(rows_html(s["rows"]))
    if s.get("quotes"):
        small = len(s["quotes"]) > 1 or t == "finding"
        parts.append(quotes_html(s["quotes"], small=small))
    if s.get("body"):
        cls = "body-lede" + (" is-mono" if s["body"].startswith("signals.") else "")
        parts.append(f'<p class="{cls}{ph} reveal">{esc(s["body"])}</p>')
    if s.get("aside"):
        parts.append(aside_html(s["aside"]))
    return (f'<section class="slide" data-index="{i}"><div class="frame">{"".join(parts)}</div>'
            f'<div class="visual-slot"><span class="visual-slot-label">+ Visual</span></div>'
            f'<span class="pagenum"></span>{notes_html}</section>')

slides = "\n\n".join(slide_html(i, s) for i, s in enumerate(S))
tpl = open(__file__.rsplit('/', 1)[0] + "/template.html").read()
out = tpl.replace("{{SLIDES}}", slides).replace("{{COUNT}}", str(len(S)))
open(sys.argv[1], "w").write(out)
print("slides:", len(S))
