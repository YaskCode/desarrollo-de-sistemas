"""Renderizador limitado del Markdown propio: todo texto/URL se escapa."""
import html
import re
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from django.utils.safestring import mark_safe

SOURCE = Path(__file__).resolve().parents[3] / "codelabs/postulaciones-django/codelab.md"
BASE = "https://github.com/YaskCode/desarrollo-de-sistemas/blob/main/codelabs/postulaciones-django/"

def inline(text):
    def link(match):
        label, target = match.groups()
        url = urljoin(BASE, target)
        if urlsplit(url).scheme not in ("https", "http"):
            return html.escape(label)
        return '<a href="' + html.escape(url, quote=True) + '">' + html.escape(label) + '</a>'
    parts = re.split(r"(\[[^]]+\]\([^)]+\))", text)
    return "".join(link(re.fullmatch(r"\[([^]]+)\]\(([^)]+)\)", part)) if re.fullmatch(r"\[([^]]+)\]\(([^)]+)\)", part) else html.escape(part) for part in parts)

def steps():
    sections = SOURCE.read_text().split("\n## ")[1:]
    result = []
    checks = [None, "entorno", "registro", "duplicado", "aislamiento", "suite", None]
    for index, section in enumerate(sections):
        title, body = section.split("\n", 1)
        blocks = []
        chunks = re.split(r"(```[^\n]*\n.*?```)", body, flags=re.S)
        for chunk in chunks:
            if chunk.startswith("```"):
                code = chunk.split("\n", 1)[1].rsplit("```", 1)[0].rstrip()
                blocks.append('<div class="code"><button type="button" class="copy">Copiar comando</button><pre><code>' + html.escape(code) + '</code></pre></div>')
            else:
                blocks.extend('<p>' + inline(paragraph.strip()) + '</p>' for paragraph in chunk.split("\n\n") if paragraph.strip())
        result.append({"title": title, "body": mark_safe("".join(blocks)), "criterion": checks[index], "number": index + 1})
    return result
