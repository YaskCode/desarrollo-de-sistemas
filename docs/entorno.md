# Entorno docente · guía complementaria propuesta

Prerrequisitos: Python, PostgreSQL y Git instalados; VS Code, pgAdmin y acceso a GitHub. Registrar las versiones en el README del equipo. Las operaciones se realizan en el repositorio del equipo, no en este repositorio académico.

## Preparación local

```bash
python --version
git --version
psql --version
python -m venv .venv
```

Activar con `source .venv/bin/activate` en bash o `.venv\Scripts\Activate.ps1` en PowerShell.

```bash
python -m pip install Django "psycopg[binary]" pytest pytest-django
python -m django startproject config .
python manage.py startapp gestion
python -m pip freeze > requirements.txt
```

`psycopg` es el adaptador PostgreSQL, no un framework adicional. Añadir `gestion` a `INSTALLED_APPS`. Crear una BD local y usuario propio en pgAdmin; configurar `DATABASES` con `django.db.backends.postgresql` y variables de entorno para nombre, usuario, contraseña, host y puerto. No versionar contraseñas, `.venv` ni archivos de configuración privada. Seguir la [documentación de bases de datos de Django](https://docs.djangoproject.com/en/stable/ref/databases/).

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Resultado esperado: comprobaciones sin errores, migraciones aplicadas y página inicial accesible en el servidor local. Si PostgreSQL rechaza la conexión, comprobar servicio, puerto, usuario y permisos; no cambiar silenciosamente a otra BD.

Configurar `pytest.ini` con `DJANGO_SETTINGS_MODULE = config.settings` dentro de `[pytest]`. Añadir pruebas en el equipo y ejecutar `python -m pytest`. La salida «no tests ran» no acredita una suite aprobada. Incorporar GitHub Actions cuando exista una suite: instalar dependencias, provisionar PostgreSQL de prueba, aplicar migraciones y ejecutar pytest. Esta automatización está prevista para los proyectos; no existe aún una aplicación docente aquí.

[Herramientas](../recursos/herramientas.md) · [Guía estudiantil](README.md)
