# Mini proyecto docente · Django y PostgreSQL

Ejemplo de PP4 para estudiar el paso de una especificación a modelos, código y pruebas. Registra postulaciones a ofertas sintéticas y muestra únicamente los registros de la cuenta autenticada. La regla de no duplicar el par estudiante–oferta es hipotética, no una afirmación sobre el reglamento de FEC-LUZ.

## Qué aprenderás

- E6: relacionar un modelo con una restricción única y su migración PostgreSQL.
- E7: comprobar registro, duplicados, datos inválidos, autenticación y aislamiento entre cuentas.
- E8: reproducir la instalación y mantener versiones, pruebas y documentación.

No implementa aprobación académica, empresas, tutores, seguimiento, reportes de coordinación ni todos los módulos del proyecto integrador. El ejemplo es material de estudio y no agrega una entrega.

## Leer el código

| Archivo | Responsabilidad |
|---|---|
| [Especificación](especificacion.md) | Reglas, alcance y comprobaciones |
| [models.py](gestion/models.py) | Oferta y Postulacion; restricción única |
| [0001_initial.py](gestion/migrations/0001_initial.py) | Esquema reproducible |
| [forms.py](gestion/forms.py) | Selección de ofertas activas |
| [services.py](gestion/services.py) | Registro sin duplicar el mismo par |
| [views.py](gestion/views.py) | Identidad desde sesión y consulta de registros propios |
| [Pruebas del caso](gestion/tests/test_postulaciones.py) | Evidencias de reglas y comportamiento HTTP |
| [Pruebas del entorno](gestion/tests/test_entorno.py) | Las tres comprobaciones de la guía general |
| [Historial](CHANGELOG.md) | Alcance de esta versión docente |

## Abrir con Dev Containers o Codespaces

La [guía de apertura y uso](../../docs/devcontainer.md) prepara este mini proyecto automáticamente con Python 3.12 y PostgreSQL 16. Permite estudiar, modificar y probar el código sin instalar PostgreSQL en el equipo anfitrión.

## Preparar el entorno

Desde la raíz del repositorio académico, entrar en `ejemplos/django-postgresql`. Usar Python 3.12 y PostgreSQL 16. Crear y activar `.venv` como indica la [guía de entorno](../../docs/entorno.md), e instalar:

```bash
python -m pip install -r requirements.txt
python -m pip check
```

En pgAdmin, crear el rol local `pp4_local` con contraseña propia y permiso de creación de bases para pytest; crear `pp4_desarrollo` con ese propietario. Configurar `PP4_DB_NAME`, `PP4_DB_USER`, `PP4_DB_PASSWORD`, `PP4_DB_HOST`, `PP4_DB_PORT` y `PP4_SECRET_KEY` siguiendo los comandos bash o PowerShell de la guía.

El proyecto ya incluye configuración, modelos y migración. **No ejecutar startproject, startapp ni copiar la prueba de entorno otra vez.**

```bash
python manage.py check
python manage.py migrate --noinput
python -m pytest -q
```

La suite contiene 19 pruebas. Exige PostgreSQL y crea una BD de pruebas separada; no utilizar cuentas o bases institucionales. Un fallo de conexión no es una prueba de negocio aprobada.

## Probar la interfaz local

Establecer `PP4_DEMO_PASSWORD` en la sesión con una contraseña local de al menos 12 caracteres, sin guardarla en Git. En bash usar `read -r -s -p 'Contraseña de demostración: ' PP4_DEMO_PASSWORD` y después `export PP4_DEMO_PASSWORD`. En PowerShell usar `$env:PP4_DEMO_PASSWORD = [System.Net.NetworkCredential]::new("", (Read-Host "Contraseña de demostración" -AsSecureString)).Password`.

```bash
python manage.py sembrar_demo
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/entrar/`. Iniciar sesión con `estudiante_uno` y la contraseña elegida, registrar una postulación y repetir la misma solicitud. La segunda devuelve un mensaje de duplicado y no crea otra fila. Salir e ingresar con `estudiante_dos`: esa cuenta no consulta los registros del primero y puede postular a la misma oferta.

`sembrar_demo` no cambia contraseñas de cuentas existentes. Si ya existían, usar su contraseña o restablecerla mediante `python manage.py changepassword estudiante_uno`. Para administrar ofertas localmente, crear una cuenta con `python manage.py createsuperuser` y acceder a `/admin/`. No otorgar privilegios administrativos a las cuentas usadas como estudiantes.

El servidor y los datos de demostración son locales. Esta configuración no es una guía de despliegue de producción.

## Ver las comprobaciones en GitHub

El [workflow del ejemplo](../../.github/workflows/ejemplo-django-postgresql.yml) prepara PostgreSQL 16 temporal, aplica migraciones y ejecuta pytest. Consultar [Actions del repositorio](https://github.com/YaskCode/desarrollo-de-sistemas/actions) y localizar la ejecución **Ejemplo Django y PostgreSQL** del commit o PR revisado.

El estado aprobado acredita esas pruebas y migraciones, no la aceptación institucional del sistema. El reporte JUnit queda como artefacto de la ejecución. Para los equipos, la [guía de integración continua](../../docs/integracion-continua.md) explica la adaptación al repositorio propio.

## Recorrido de estudio

Leer la especificación y localizar su regla en el modelo, la migración, la operación y las pruebas. Para practicar el ciclo TDD, comenzar en una copia de estudio por la prueba de un comportamiento antes de implementarlo; no asumir que el estado final del código demuestra por sí solo el orden en que fue escrito.

DDD se aplica al vocabulario; SDD a la especificación; TDD al ciclo de desarrollo; V&V al contraste de evidencias y necesidades. La restricción evita duplicados concurrentes del mismo par, pero la suite no ejecuta una prueba de carga o de concurrencia. La validación de oferta activa ocurre al procesar el formulario y no garantiza exclusión frente a una desactivación concurrente.

[Enfoques](../../docs/enfoques-ingenieria.md) · [Unidad V](../../unidades/05-bases-de-datos/README.md) · [Unidad VI](../../unidades/06-pruebas-mantenimiento/README.md) · [Inicio](../../README.md)

## Codelab autoguiado opcional

[Postulaciones: de la regla a la prueba](../../codelabs/postulaciones-django/codelab.md). Reutiliza este ejemplo para E6–E8, con comprobaciones técnicas reales desde el mismo entorno privado. No añade entregas. Consulta su preparación antes de activar el validador.
