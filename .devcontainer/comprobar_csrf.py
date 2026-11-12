"""Regresión del origen observado en el túnel privado, sin conexión a BD."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ejemplos/django-postgresql"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from django.conf import settings
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.test import RequestFactory, override_settings

factory = RequestFactory()
middleware = CsrfViewMiddleware(lambda request: None)

def comprobar(origin, token_valido):
    request = factory.post(
        "/entrar/", HTTP_HOST="pp4-prueba-8000.app.github.dev",
        HTTP_ORIGIN=origin,
    )
    token = get_token(request)
    request.COOKIES[settings.CSRF_COOKIE_NAME] = request.META["CSRF_COOKIE"]
    if token_valido:
        request.META["HTTP_X_CSRFTOKEN"] = token
    middleware.process_request(request)
    return middleware.process_view(request, lambda request: None, (), {})

for origin in settings.CSRF_TRUSTED_ORIGINS:
    assert comprobar(origin, True) is None, origin
    assert comprobar(origin, False).status_code == 403, origin
assert comprobar("https://sitio-ajeno.example", True).status_code == 403
with override_settings(CSRF_TRUSTED_ORIGINS=[]):
    assert comprobar("https://localhost:8000", True).status_code == 403
print("CSRF: orígenes admitidos con token; sin token y origen ajeno rechazados.")
