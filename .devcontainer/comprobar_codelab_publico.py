"""Comprueba la guía estática real por HTTP, sin simular validaciones técnicas."""
from pathlib import Path
import subprocess
import sys
import time
import urllib.request
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
OUT = ROOT / 'ejemplos/django-postgresql/reporte-codelab'
OUT.mkdir(exist_ok=True)
subprocess.run([sys.executable, str(ROOT/'scripts/construir_codelab.py')], check=True)
server = subprocess.Popen([sys.executable,'-m','http.server','8765','--bind','127.0.0.1','--directory',str(SITE)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for attempt in range(40):
        try:
            urllib.request.urlopen('http://127.0.0.1:8765/',timeout=2)
            break
        except OSError:
            if attempt==39: raise
            time.sleep(.25)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context(viewport={'width':1440,'height':1000},permissions=['clipboard-read','clipboard-write'])
        page = context.new_page()
        errors, requests = [], []
        page.on('pageerror',lambda error:errors.append(str(error)))
        page.on('request',lambda request:requests.append(request.url))
        page.goto('http://127.0.0.1:8765/codelabs/postulaciones-django/')
        expect(page.locator('.public-notice')).to_be_visible()
        expect(page.locator('.about')).to_contain_text('Autoría y diseño didáctico')
        expect(page.locator('.about')).to_contain_text('Dra. Yaskelly Yedra')
        expect(page.locator('header')).to_contain_text('YaskCode Codelabs')
        assert page.locator('[data-criterion],.check,[name=csrfmiddlewaretoken]').count()==0
        assert page.locator('nav').bounding_box()['x'] < page.locator('main').bounding_box()['x']
        page.screenshot(path=str(OUT/'publico-escritorio.png'),full_page=True)
        page.keyboard.press('Tab')
        expect(page.locator('.skip')).to_be_focused()
        page.keyboard.press('Enter')
        expect(page.locator('#contenido')).to_be_focused()
        page.locator('nav a').nth(1).click()
        expect(page.locator('#paso-2')).to_be_visible()
        expect(page.locator('#paso-2')).to_be_focused()
        page.locator('#paso-2 .private-link').click()
        expect(page.locator('#paso-1')).to_be_visible()
        copy = page.locator('#paso-1 .copy').first
        command = page.locator('#paso-1 code').first.inner_text()
        copy.click()
        expect(copy).to_have_text('Copiado')
        assert page.evaluate('navigator.clipboard.readText()')==command
        page.locator('#paso-1 .paging a').click()
        expect(page.locator('#paso-2')).to_be_visible()
        page.reload()
        expect(page.locator('#paso-2')).to_be_visible()
        page.set_viewport_size({'width':390,'height':844})
        assert not page.evaluate('document.documentElement.scrollWidth>innerWidth')
        page.screenshot(path=str(OUT/'publico-movil.png'),full_page=True)
        page.locator('nav a').last.click()
        expect(page.locator('#paso-7')).to_be_visible()
        expect(page.locator('#paso-7 h3')).to_have_count(5)
        assert page.locator('#paso-7 .check').count()==0
        expect(page.locator('#paso-7')).to_contain_text('¡Felicitaciones por tu recorrido!')
        page.screenshot(path=str(OUT/'publico-cierre.png'),full_page=True)
        assert not any('/estado/' in url or '/comprobar/' in url for url in requests), requests
        assert not errors,errors
        # Sin JS sigue siendo una guía completa de siete pasos.
        nojs=browser.new_context(java_script_enabled=False)
        plain=nojs.new_page()
        plain.goto('http://127.0.0.1:8765/codelabs/postulaciones-django/')
        assert plain.locator('[data-step]:visible').count()==7
        browser.close()
    print('Guía pública: menú lateral, navegación, foco, copia exacta, móvil, sin JS y sin llamadas al validador: OK')
finally:
    server.terminate()
    server.wait(timeout=10)
