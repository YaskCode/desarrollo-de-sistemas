"""Validador optativo para un espacio de desarrollo privado y confiable."""
import fcntl
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

ROOT = settings.BASE_DIR
BOOT = uuid.uuid4().hex
LOCK = threading.Lock()
TEST = "gestion/tests/test_postulaciones.py"
CRITERIA = {
    "entorno": [],
    "registro": [TEST + "::test_primera_postulacion", TEST + "::test_post_correcto_redirige_y_muestra_confirmacion"],
    "duplicado": [TEST + "::test_segundo_intento_no_duplica", TEST + "::test_bd_rechaza_duplicado_aunque_se_omita_servicio", TEST + "::test_post_duplicado_devuelve_conflicto_sin_segunda_fila"],
    "aislamiento": [TEST + "::test_cuenta_solo_consulta_sus_registros", TEST + "::test_campo_estudiante_falsificado_no_cambia_identidad", TEST + "::test_otro_estudiante_puede_postular_a_misma_oferta", TEST + "::test_anonimo_no_puede_registrar"],
    "suite": [TEST, "gestion/tests/test_entorno.py"],
}


def enabled():
    if os.environ.get("PP4_CODELAB") != "1":
        raise Http404


def identity():
    """Incluye archivos sin commit. No devuelve variables ni credenciales."""
    digest = hashlib.sha256()
    repo = ROOT.parent.parent
    excluded = {".venv", "__pycache__", ".pytest_cache", ".git", "reporte-codelab"}
    for directory in (ROOT, repo / ".devcontainer", repo / "codelabs"):
        for folder, directories, files in directory.walk():
            directories[:] = sorted(name for name in directories if name not in excluded)
            for name in sorted(files):
                file = folder / name
                if file.suffix not in (".py", ".html", ".js", ".css", ".txt", ".ini", ".json", ".yaml", ".sh", ".md"):
                    continue
                digest.update(str(file.relative_to(repo)).encode())
                digest.update(file.read_bytes())
    # Solo la huella se publica; nunca el contenido del entorno.
    digest.update(json.dumps(sorted(os.environ.items())).encode())
    digest.update(sys.version.encode())
    return digest.hexdigest()


def environment():
    # Límites de conexión y consultas solo durante esta comprobación.
    original = connection.settings_dict.get("OPTIONS", {}).copy()
    connection.close()
    connection.settings_dict["OPTIONS"] = {
        **original, "connect_timeout": 5,
        "options": original.get("options", "") + " -c statement_timeout=5000",
    }
    try:
        if connection.vendor != "postgresql":
            raise RuntimeError("Se requiere PostgreSQL")
        with connection.cursor() as cursor:
            cursor.execute("SELECT version(), current_database(), pg_postmaster_start_time()")
            version, database, started = cursor.fetchone()
        executor = MigrationExecutor(connection)
        if executor.migration_plan(executor.loader.graph.leaf_nodes()):
            raise RuntimeError("Migraciones pendientes")
        return hashlib.sha256((version + database + str(started) + str(sorted(executor.loader.applied_migrations))).encode()).hexdigest()
    finally:
        connection.close()
        connection.settings_dict["OPTIONS"] = original


def run_tests(selectors):
    # Entradas cerradas; sin shell ni comandos recibidos del navegador.
    with tempfile.TemporaryDirectory(prefix="pp4-check-") as directory:
        report = Path(directory) / "result.xml"
        env = dict(os.environ, PP4_CODELAB="0")
        env.pop("PYTEST_ADDOPTS", None)
        with tempfile.TemporaryFile() as output:
            process = subprocess.Popen(
                [sys.executable, "-m", "pytest", "-q", "--tb=no", "--junitxml=" + str(report), *selectors],
                cwd=ROOT, env=env, stdout=output, stderr=subprocess.STDOUT, start_new_session=True,
            )
            try:
                code = process.wait(timeout=90)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
                return "error_entorno", {"motivo": "Timeout técnico de 90 segundos; vuelve a comprobar tras revisar el entorno."}
        if code not in (0, 1) or not report.exists():
            return "error_entorno", {"motivo": "No se pudo completar pytest. Ejecuta las pruebas en la segunda terminal para diagnosticar."}
        suites = ET.parse(report).getroot().iter("testsuite")
        counts = {key: 0 for key in ("tests", "failures", "errors", "skipped")}
        for suite in suites:
            for key in counts:
                counts[key] += int(suite.get(key, 0))
        expected = 19 if selectors == CRITERIA["suite"] else len(selectors)
        if counts["errors"] or counts["skipped"] or counts["tests"] != expected:
            state = "error_entorno"
        else:
            state = "aprobado" if code == 0 and not counts["failures"] else "fallo"
        return state, counts


@login_required
@require_GET
def page(request):
    enabled()
    from .codelab_content import steps
    return render(request, "gestion/codelab.html", {"steps": steps()})


@login_required
@require_GET
def status(request):
    enabled()
    try:
        current = identity()
        database = environment()
        results = request.session.get("codelab", {})
        for result in results.values():
            if result["codigo"] != current or result["entorno"] != database or result["sesion_servidor"] != BOOT:
                result["estado"] = "anterior"
        response = JsonResponse({"resultados": results})
        response["Cache-Control"] = "no-store"
        return response
    except Exception:
        return JsonResponse({"resultados": {}, "estado": "error_entorno", "mensaje": "No se puede confirmar el estado actual. Revisa PostgreSQL y migraciones."})


@login_required
@require_POST
def check(request, criterion):
    enabled()
    if criterion not in CRITERIA:
        raise Http404
    if not LOCK.acquire(blocking=False):
        return JsonResponse({"estado": "error_entorno", "mensaje": "Hay una comprobación en curso; espera y repite."}, status=409)
    try:
        # Serializa también entre procesos que compartan el mismo entorno.
        with open(Path(tempfile.gettempdir()) / "pp4-codelab.lock", "w") as lockfile:
            try:
                fcntl.flock(lockfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                return JsonResponse({"estado": "error_entorno", "mensaje": "Hay otra comprobación en curso."}, status=409)
            try:
                before = identity()
                database = environment()
                state, evidence = ("aprobado", {"motivo": "Conexión PostgreSQL real y migraciones aplicadas."}) if criterion == "entorno" else run_tests(CRITERIA[criterion])
                if before != identity() or database != environment():
                    state = "anterior"
                result = {"criterio": criterion, "estado": state, "codigo": before, "entorno": database,
                          "sesion_servidor": BOOT, "fecha_utc": datetime.now(timezone.utc).isoformat(),
                          "tipo": "entorno" if criterion == "entorno" else "prueba_del_ejemplo",
                          "evidencia": evidence, "pruebas": CRITERIA[criterion]}
                results = request.session.get("codelab", {})
                results[criterion] = result
                request.session["codelab"] = results
                return JsonResponse(result)
            except Exception:
                return JsonResponse({"estado": "error_entorno", "mensaje": "Comprueba conexión, migraciones, permisos de creación de BD y dependencias desde la segunda terminal."})
    finally:
        LOCK.release()
