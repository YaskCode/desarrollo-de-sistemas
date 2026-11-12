"""Genera únicamente la guía pública, sin importar configuración ni secretos del ejemplo."""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "ejemplos/django-postgresql"
sys.path.insert(0, str(PROJECT))
from django.conf import settings
settings.configure(
    INSTALLED_APPS=[], STATIC_URL="assets/", USE_TZ=True,
    TEMPLATES=[{"BACKEND":"django.template.backends.django.DjangoTemplates", "DIRS":[PROJECT / "gestion/templates"], "APP_DIRS":False}],
)
import django
django.setup()
from django.template.loader import render_to_string
from gestion.codelab_content import steps


def build(output):
    destination = output / "codelabs/postulaciones-django"
    assets = destination / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    content = render_to_string("gestion/codelab.html", {"steps":steps(), "public":True})
    assert "csrfmiddlewaretoken" not in content
    assert 'class="check"' not in content
    assert len(steps()) == 7
    (destination / "index.html").write_text(content)
    for name in ("codelab.css", "codelab.js"):
        shutil.copyfile(PROJECT / "gestion/static/gestion" / name, assets / name)
    (output / ".nojekyll").touch()
    (output / "index.html").write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PP4 · Desarrollo de Sistemas</title><h1>PP4 · Desarrollo de Sistemas</h1><p><a href="codelabs/postulaciones-django/">Codelab: Postulaciones con Django y PostgreSQL</a></p><p><a href="https://github.com/YaskCode/desarrollo-de-sistemas">Material de la asignatura</a></p></html>')
    print("Guía pública generada:", destination / "index.html")

if __name__ == "__main__":
    build(Path(sys.argv[1]) if len(sys.argv)>1 else ROOT / "_site")
