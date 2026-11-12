"""Regresiones del codelab contra PostgreSQL real, fuera de pytest (sin recursión)."""
import os
from pathlib import Path
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1] / 'ejemplos/django-postgresql'
sys.path.insert(0, str(ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ['PP4_CODELAB'] = '1'
import django
django.setup()
from django.contrib.auth import get_user_model
from django.test import Client
from gestion import codelab
from gestion.codelab_content import steps, inline


def main():
    User = get_user_model()
    user = User.objects.create_user(username='codelab_ci_temporal')
    client = Client(enforce_csrf_checks=True)
    client.force_login(user)
    try:
        response = client.get('/codelab/')
        assert response.status_code == 200
        assert len(steps()) == 7
        assert 'javascript:' not in inline('[x](javascript:alert)')
        assert '&lt;script&gt;' in inline('<script>')
        token = client.cookies['csrftoken'].value
        url = '/codelab/comprobar/entorno/'
        assert client.post(url).status_code == 403
        assert client.post(url, HTTP_X_CSRFTOKEN=token, HTTP_ORIGIN='https://ajeno.invalid').status_code == 403
        assert Client(enforce_csrf_checks=True).post(url).status_code == 403
        anonymous = Client()
        assert anonymous.get('/codelab/').status_code == 302
        assert anonymous.post(url).status_code == 302
        assert client.get(url).status_code == 405
        assert client.post('/codelab/comprobar/comando-inventado/', HTTP_X_CSRFTOKEN=token).status_code == 404
        for criterion in codelab.CRITERIA:
            data = client.post('/codelab/comprobar/'+criterion+'/', HTTP_X_CSRFTOKEN=token).json()
            assert data['estado'] == 'aprobado', data
            print(criterion, data['estado'], data['evidencia'])
        assert client.get('/codelab/estado/').json()['resultados']['suite']['estado'] == 'aprobado'
        with patch.object(codelab, 'identity', return_value='otra-version'):
            assert client.get('/codelab/estado/').json()['resultados']['suite']['estado'] == 'anterior'
        with patch.object(codelab, 'BOOT', 'otro-servidor'):
            assert client.get('/codelab/estado/').json()['resultados']['suite']['estado'] == 'anterior'
        with patch.object(codelab, 'environment', side_effect=RuntimeError('BD no disponible')):
            assert client.post(url, HTTP_X_CSRFTOKEN=token).json()['estado'] == 'error_entorno'
            assert client.get('/codelab/estado/').json()['estado'] == 'error_entorno'
        # Mutación temporal real del servicio: el validador debe detectar el fallo.
        service = ROOT / 'gestion/services.py'
        original = service.read_bytes()
        try:
            service.write_text('def registrar_postulacion(*, estudiante, oferta):\n    return None, False\n')
            data = client.post('/codelab/comprobar/registro/', HTTP_X_CSRFTOKEN=token).json()
            assert data['estado'] == 'fallo', data
            print('mutación real:', data['estado'], data['evidencia'])
            assert client.get('/codelab/estado/').json()['resultados']['suite']['estado'] == 'anterior'
        finally:
            service.write_bytes(original)
        # El resultado fallido tampoco cubre la restauración.
        assert client.get('/codelab/estado/').json()['resultados']['registro']['estado'] == 'anterior'
        with patch.dict(os.environ, {'PP4_CODELAB':'0'}):
            assert client.get('/codelab/').status_code == 404
        print('CSRF, autenticación, métodos, estados e invalidación: OK')
    finally:
        user.delete()

if __name__ == '__main__':
    main()
