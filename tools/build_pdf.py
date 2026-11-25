"""Build methodology.pdf (English) and ru/methodology.pdf (Russian) from the markdown sources.

The PDF is generated, not edited by hand: change the markdown, then run

    pip install reportlab
    python3 tools/build_pdf.py            # both languages
    python3 tools/build_pdf.py --lang ru  # one language

Fonts: DejaVu Sans / DejaVu Sans Mono (Cyrillic support). Pass --font-dir if they
are not in a standard location.
"""

import argparse
import html
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, ListFlowable, ListItem, PageBreak, Paragraph, Preformatted,
    SimpleDocTemplate, Spacer, Table, TableStyle,
)

ROOT = Path(__file__).resolve().parent.parent
REPO_URL = "https://github.com/polomodov/requirements-to-acceptance"

BOOKS = {
    "en": {
        "out": ROOT / "methodology.pdf",
        "base": ROOT,
        "title": "From requirement to acceptance",
        "subtitle": "How to connect PMI project management with RUP iterations",
        "kicker": "A sample consulting method",
        "author": "Alexander Polomodov",
        "contents": "Contents",
        "note": "All events, observations and estimates in the case are fictional. "
                "Licensed under CC BY 4.0. Source: " + REPO_URL,
        "sections": [
            ("when-to-use.md", "When to use the method", "Symptoms and the core of the approach"),
            ("method.md", "The method", "Decisions, roles and working materials"),
            ("example.md", "Worked example", "Partial shipments in a B2B ordering portal"),
            ("agent-practice.md", "Skills and quality checks", "Three procedures and reproducible evals"),
            ("evals/README.md", "Running the evals", "Commands, rubric and an example run"),
            ("consulting-engagement.md", "Consulting practice", "Diagnosis, pilot and hand-over to the team"),
            ("NEXT.md", "Where to dig next", "Directions and open questions"),
        ],
    },
    "ru": {
        "out": ROOT / "ru" / "methodology.pdf",
        "base": ROOT / "ru",
        "title": "От требования до приёмки",
        "subtitle": "Как связать проектное управление PMI с итерациями RUP",
        "kicker": "Образец консультационной методики",
        "author": "Александр Поломодов",
        "contents": "Содержание",
        "note": "Все события, наблюдения и оценки в кейсе вымышлены. "
                "Лицензия CC BY 4.0. Исходники: " + REPO_URL,
        "sections": [
            ("when-to-use.md", "Когда применять методику", "Признаки проблемы и суть подхода"),
            ("method.md", "Методика", "Решения, роли и рабочие материалы"),
            ("example.md", "Учебный пример", "Частичные отгрузки в B2B-портале заказов"),
            ("agent-practice.md", "Скиллы и проверка качества", "Три рабочие процедуры и воспроизводимые проверки"),
            ("evals/README.md", "Как провести эвалы", "Команды, рубрика и пример прогона"),
            ("consulting-engagement.md", "Консультационная практика", "Диагностика, пилот и передача практики команде"),
            ("NEXT.md", "Куда копать дальше", "Направления и открытые вопросы"),
        ],
    },
}

ACCENT = colors.HexColor("#1f4e79")
MUTED = colors.HexColor("#5b6670")
RULE = colors.HexColor("#c9d3dc")
HEAD_BG = colors.HexColor("#eef3f8")


def register_fonts(font_dir):
    candidates = [Path(font_dir)] if font_dir else []
    candidates += [Path("/usr/share/fonts/truetype/dejavu"), Path("/usr/share/fonts/dejavu"),
                   Path("/Library/Fonts"), Path.home() / "Library/Fonts", Path("C:/Windows/Fonts")]
    required = {"Body": "DejaVuSans.ttf", "Body-Bold": "DejaVuSans-Bold.ttf", "Mono": "DejaVuSansMono.ttf"}
    optional = {"Body-Italic": ("DejaVuSans-Oblique.ttf", "Body"),
                "Body-BoldItalic": ("DejaVuSans-BoldOblique.ttf", "Body-Bold")}
    for directory in candidates:
        if all((directory / f).exists() for f in required.values()):
            for name, f in required.items():
                pdfmetrics.registerFont(TTFont(name, str(directory / f)))
            faces = {}
            for name, (f, fallback) in optional.items():
                if (directory / f).exists():
                    pdfmetrics.registerFont(TTFont(name, str(directory / f)))
                    faces[name] = name
                else:
                    faces[name] = fallback
            pdfmetrics.registerFontFamily("Body", normal="Body", bold="Body-Bold",
                                          italic=faces["Body-Italic"], boldItalic=faces["Body-BoldItalic"])
            return
    sys.exit("DejaVu fonts not found; pass --font-dir")


def styles():
    s = {}
    s["body"] = ParagraphStyle("body", fontName="Body", fontSize=9.6, leading=13.6, spaceAfter=6, alignment=TA_LEFT)
    s["cell"] = ParagraphStyle("cell", parent=s["body"], fontSize=8.2, leading=11, spaceAfter=0)
    s["cellh"] = ParagraphStyle("cellh", parent=s["cell"], fontName="Body-Bold")
    s["h1"] = ParagraphStyle("h1", fontName="Body-Bold", fontSize=18, leading=23, textColor=ACCENT, spaceAfter=10, keepWithNext=1)
    s["h2"] = ParagraphStyle("h2", fontName="Body-Bold", fontSize=12.5, leading=16, textColor=ACCENT,
                             spaceBefore=10, spaceAfter=5, keepWithNext=1)
    s["kicker"] = ParagraphStyle("kicker", fontName="Body-Bold", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=4)
    s["code"] = ParagraphStyle("code", fontName="Mono", fontSize=8, leading=10.5, backColor=HEAD_BG,
                               borderPadding=5, spaceBefore=4, spaceAfter=8)
    s["cover_title"] = ParagraphStyle("ct", fontName="Body-Bold", fontSize=34, leading=40, textColor=ACCENT)
    s["cover_sub"] = ParagraphStyle("cs", fontName="Body", fontSize=15, leading=20, textColor=colors.black)
    s["cover_small"] = ParagraphStyle("csm", fontName="Body", fontSize=9, leading=13, textColor=MUTED)
    s["toc"] = ParagraphStyle("toc", fontName="Body-Bold", fontSize=11, leading=14)
    s["toc_sub"] = ParagraphStyle("tocs", fontName="Body", fontSize=9, leading=12, textColor=MUTED)
    return s


def inline(text):
    """Convert inline markdown to ReportLab mini-HTML."""
    out, pos = [], 0
    for m in re.finditer(r"`([^`]+)`", text):
        out.append(("t", text[pos:m.start()]))
        out.append(("c", m.group(1)))
        pos = m.end()
    out.append(("t", text[pos:]))
    parts = []
    for kind, chunk in out:
        if kind == "c":
            parts.append('<font name="Mono">%s</font>' % html.escape(chunk, quote=False))
            continue
        chunk = html.escape(chunk, quote=False)
        def link(m):
            label, url = m.group(1), html.unescape(m.group(2))
            if url.startswith(("http://", "https://", "mailto:")):
                return '<link href="%s" color="#1f4e79"><u>%s</u></link>' % (html.escape(url), label)
            return label
        chunk = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, chunk)
        chunk = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", chunk)
        chunk = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", chunk)
        parts.append(chunk)
    return "".join(parts)


def table(lines, st, width):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    rows = [r for r in rows if not all(re.fullmatch(r":?-{3,}:?", c) for c in r)]
    ncol = len(rows[0])
    data = [[Paragraph(inline(c), st["cellh"] if i == 0 else st["cell"]) for c in r[:ncol]] for i, r in enumerate(rows)]
    plain = [[re.sub(r"\[([^\]]+)\]\([^)]+\)|[*`]", lambda m: m.group(1) or "", c) for c in r] for r in rows]
    lens = [max(6, min(max(len(r[j]) if j < len(r) else 0 for r in plain), 200)) for j in range(ncol)]
    # never squeeze a column below its longest word (about 5 pt per character at 8.2 pt)
    floor = [max(len(w) for r in plain if j < len(r) for w in (r[j].split() or [""])) * 5.0 + 10 for j in range(ncol)]
    total = sum(lens)
    widths = [max(width * l / total, f) for l, f in zip(lens, floor)]
    extra = sum(widths) - width
    if extra > 0:
        flexible = [j for j in range(ncol) if widths[j] > floor[j]]
        room = sum(widths[j] - floor[j] for j in flexible) or 1
        widths = [w - extra * (w - floor[j]) / room if j in flexible else w for j, w in enumerate(widths)]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEAD_BG),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return [t, Spacer(1, 8)]


def render(md, st, width, kicker):
    lines = md.splitlines()
    if lines and lines[0].startswith("---"):  # front matter
        end = lines.index("---", 1)
        lines = lines[end + 1:]
    flow, i, para = [], 0, []

    def flush():
        if para:
            flow.append(Paragraph(inline(" ".join(para)), st["body"]))
            para.clear()

    first_h1 = True
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            flush()
            lang = line[3:].strip()
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            if lang != "mermaid":
                flow.append(Preformatted("\n".join(lines[i + 1:j]), st["code"]))
            i = j + 1
            continue
        if line.startswith("|"):
            flush()
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            flow += table(lines[i:j], st, width)
            i = j
            continue
        m = re.match(r"^(#{1,3})\s+(.*)", line)
        if m:
            flush()
            level, text = len(m.group(1)), m.group(2)
            if level == 1:
                if first_h1:
                    flow.append(Paragraph(kicker.upper(), st["kicker"]))
                    first_h1 = False
                flow.append(Paragraph(inline(text), st["h1"]))
            else:
                flow.append(Paragraph(inline(text), st["h2"]))
            i += 1
            continue
        m = re.match(r"^(\d+\.|-)\s+(.*)", line)
        if m:
            flush()
            ordered = m.group(1) != "-"
            items, j = [], i
            while j < len(lines):
                mm_ = re.match(r"^(\d+\.|-)\s+(.*)", lines[j])
                if mm_:
                    items.append(mm_.group(2))
                elif lines[j].startswith("   ") and items:
                    items[-1] += " " + lines[j].strip()
                else:
                    break
                j += 1
            flow.append(ListFlowable(
                [ListItem(Paragraph(inline(t), st["body"]), leftIndent=14) for t in items],
                bulletType="1" if ordered else "bullet", start="1" if ordered else None,
                bulletFontName="Body", bulletFontSize=9, leftIndent=14))
            i = j
            continue
        if not line.strip():
            flush()
        else:
            para.append(line.strip())
        i += 1
    flush()
    return flow


def build(lang, st):
    book = BOOKS[lang]
    width = A4[0] - 40 * mm
    story = [Spacer(1, 50 * mm),
             Paragraph(book["author"].upper(), st["kicker"]),
             Paragraph(book["kicker"], st["cover_small"]), Spacer(1, 10 * mm),
             Paragraph(book["title"], st["cover_title"]), Spacer(1, 6 * mm),
             Paragraph(book["subtitle"], st["cover_sub"]), Spacer(1, 70 * mm),
             Paragraph(inline(book["note"].replace(REPO_URL, "[%s](%s)" % (REPO_URL, REPO_URL))), st["cover_small"]),
             PageBreak(), Paragraph(book["contents"], st["h1"])]
    for _, title, sub in book["sections"]:
        story += [Paragraph(title, st["toc"]), Paragraph(sub, st["toc_sub"]), Spacer(1, 6)]
    for path, title, _ in book["sections"]:
        story.append(PageBreak())
        story += render((book["base"] / path).read_text(encoding="utf-8"), st, width, title)

    def footer(canvas, doc):
        if doc.page == 1:
            return
        canvas.saveState()
        canvas.setFont("Body", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(20 * mm, 12 * mm, book["title"])
        canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, str(doc.page))
        canvas.restoreState()

    doc = SimpleDocTemplate(str(book["out"]), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                            topMargin=18 * mm, bottomMargin=20 * mm, title=book["title"],
                            subject=book["subtitle"], author=book["author"], creator=book["author"])
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("wrote", book["out"].relative_to(ROOT))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lang", choices=sorted(BOOKS), action="append")
    parser.add_argument("--font-dir")
    args = parser.parse_args()
    register_fonts(args.font_dir)
    st = styles()
    for lang in args.lang or sorted(BOOKS):
        build(lang, st)


if __name__ == "__main__":
    main()
