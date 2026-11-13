"""Recorrido real HTTP/navegador en CI; capturas sin cookies ni credenciales."""
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1] / 'ejemplos/django-postgresql'
sys.path.insert(0, str(ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
from playwright.sync_api import sync_playwright, expect

out = ROOT / 'reporte-codelab'
out.mkdir(exist_ok=True)
password = secrets.token_urlsafe(24)
user = get_user_model().objects.create_user(username='codelab_web_ci', password=password)
env = dict(os.environ, PP4_CODELAB='1', PP4_DEBUG='1')
server = subprocess.Popen([sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload'], cwd=ROOT, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for attempt in range(60):
        try:
            urllib.request.urlopen('http://127.0.0.1:8000/entrar/', timeout=2)
            break
        except OSError:
            if attempt == 59:
                raise
            time.sleep(.25)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width':1440,'height':1000})
        errors = []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto('http://127.0.0.1:8000/codelab/')
        page.locator('#id_username').fill(user.username)
        page.locator('#id_password').fill(password)
        page.get_by_role('button', name='Entrar', exact=True).click()
        expect(page.locator('h1')).to_have_text('Postulaciones con Django y PostgreSQL: de la regla a la prueba')
        expect(page.locator('.about')).to_contain_text('Dra. Yaskelly Yedra')
        page.screenshot(path=str(out/'escritorio.png'), full_page=True)
        page.keyboard.press('Tab')
        assert page.locator('.skip').evaluate('(e)=>document.activeElement===e')
        page.keyboard.press('Enter')
        expect(page.locator('#contenido')).to_be_focused()
        page.screenshot(path=str(out/'escritorio.png'), full_page=True)
        page.locator('nav a').nth(1).click()
        expect(page.locator('#paso-2')).to_be_focused()
        box = page.locator('[data-criterion=entorno]')
        box.locator('.check').click()
        expect(box.locator('.result')).to_have_text('Aprobado', timeout=30000)
        # Comprueba el endpoint real, no un resultado interceptado.
        page.locator('nav a').nth(2).click()
        box = page.locator('[data-criterion=registro]')
        box.locator('.check').click()
        expect(box.locator('.result')).to_have_text('Aprobado', timeout=100000)
        box.locator('summary').click()
        data = json.loads(box.locator('.evidence').inner_text())
        assert data['evidencia']['tests'] == 2
        (out/'registro.json').write_text(json.dumps(data,indent=2))
        with page.expect_download() as download:
            box.locator('.download').click()
        download.value.save_as(str(out/'descarga-registro.json'))
        assert json.loads((out/'descarga-registro.json').read_text()) == data
        page.reload()
        expect(box.locator('.result')).to_have_text('Aprobado', timeout=30000)
        page.set_viewport_size({'width':390,'height':844})
        assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
        page.screenshot(path=str(out/'movil.png'), full_page=True)
        # La pérdida de conexión debe retirar el verde; no se simula un aprobado.
        page.route('**/codelab/estado/', lambda route: route.abort())
        expect(box.locator('.result')).to_contain_text('Error del entorno', timeout=12000)
        page.unroute('**/codelab/estado/')
        assert not errors, errors
        browser.close()
        print('HTTP real: login, teclado, foco, navegación, check PostgreSQL, prueba de registro, descarga, sesión, móvil y desconexión: OK')
finally:
    server.terminate()
    server.wait(timeout=10)
    user.delete()
