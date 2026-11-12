# Preparación reproducible del entorno

Realizar estos pasos en el repositorio del equipo, en una carpeta de trabajo nueva. Esta guía prepara Django, PostgreSQL y pytest; no implementa los módulos del proyecto ni constituye otra entrega.

## 1. Requisitos y versiones

Instalar Python 3.12, Git, PostgreSQL 16 y pgAdmin. Usar VS Code para editar. La combinación de referencia utiliza Python 3.12.14, Django 5.2.19, psycopg 3.3.9, pytest 9.2.0 y pytest-django 4.14.0. Estas versiones documentan la reproducción; al actualizar dependencias, volver a comprobar compatibilidad y pruebas.

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar con `source .venv/bin/activate` en bash o `.venv\Scripts\Activate.ps1` en PowerShell. Si Windows utiliza `py -3.12`, usar ese comando para crear el entorno. Comprobar que `python --version` y `python -m pip --version` corresponden al entorno activado.

Guardar el siguiente contenido en `requirements.txt` del equipo:

```text
Django==5.2.19
psycopg[binary]==3.3.9
pytest==9.2.0
pytest-django==4.14.0
```

```bash
python -m pip install -r requirements.txt
python -m pip check
python -m django startproject config .
python manage.py startapp gestion
```

No ejecutar `startproject` otra vez sobre un proyecto existente. Añadir `gestion` a `INSTALLED_APPS` en `config/settings.py`.

## 2. Preparar PostgreSQL y pgAdmin

Iniciar el servicio PostgreSQL local. Desde pgAdmin, conectarse con la cuenta administradora de la instalación y crear:

- Un rol de inicio de sesión llamado `pp4_local`, con contraseña local y permiso **Create databases** para que pytest pueda crear su BD de prueba. No necesita ser superusuario.
- Una base de datos `pp4_desarrollo`, cuyo propietario sea `pp4_local`.

No utilizar una BD institucional ni una cuenta de producción para estas comprobaciones. El rol debe poder crear y eliminar únicamente sus bases de prueba en el entorno local de desarrollo.

## 3. Configurar las variables de la sesión

En bash:

```bash
export PP4_DB_NAME=pp4_desarrollo
export PP4_DB_USER=pp4_local
export PP4_DB_HOST=127.0.0.1
export PP4_DB_PORT=5432
read -r -s -p 'Contraseña PostgreSQL local: ' PP4_DB_PASSWORD
export PP4_DB_PASSWORD
export PP4_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
```

En PowerShell:

```powershell
$env:PP4_DB_NAME = "pp4_desarrollo"
$env:PP4_DB_USER = "pp4_local"
$env:PP4_DB_HOST = "127.0.0.1"
$env:PP4_DB_PORT = "5432"
$env:PP4_DB_PASSWORD = [System.Net.NetworkCredential]::new("", (Read-Host "Contraseña PostgreSQL local" -AsSecureString)).Password
$env:PP4_SECRET_KEY = python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Las variables pertenecen a esta sesión; repetir su configuración al abrir otra terminal. No se cargan archivos `.env` automáticamente y no se necesita una biblioteca adicional para leer variables del sistema.

## 4. Configurar Django

Añadir `import os` al comienzo de `config/settings.py`. Sustituir la asignación generada de `SECRET_KEY` por:

```python
SECRET_KEY = os.environ["PP4_SECRET_KEY"]
```

Sustituir el bloque `DATABASES` generado por:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["PP4_DB_NAME"],
        "USER": os.environ["PP4_DB_USER"],
        "PASSWORD": os.environ["PP4_DB_PASSWORD"],
        "HOST": os.environ["PP4_DB_HOST"],
        "PORT": os.environ["PP4_DB_PORT"],
    }
}
```

El servidor de desarrollo y `DEBUG=True` del proyecto recién creado se utilizan solo localmente. La preparación de producción exige otra configuración; esta guía no publica la aplicación.

Crear `.gitignore` con, al menos:

```text
.venv/
__pycache__/
*.pyc
.pytest_cache/
.env
.env.*
```

No versionar contraseñas ni valores locales. Conservar las migraciones y dependencias necesarias para reproducir el proyecto.

## 5. Comprobar configuración y migraciones

```bash
python manage.py check
python manage.py migrate
```

Resultado esperado: ninguna incidencia en `check` y migraciones aplicadas en `pp4_desarrollo`. Si hay error de conexión, revisar servicio, host, puerto, usuario, contraseña y propietario de la BD; no cambiar silenciosamente a SQLite.

## 6. Configurar pytest-django

Crear `pytest.ini` en la raíz del equipo:

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = tests.py test_*.py *_tests.py
```

Crear `gestion/test_entorno.py` para comprobar el arranque del entorno:

```python
import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError, connection, transaction


@pytest.mark.django_db
def test_escritura_en_postgresql():
    assert connection.vendor == "postgresql"
    user = get_user_model().objects.create_user(username="estudiante_prueba")
    assert get_user_model().objects.filter(pk=user.pk).exists()


@pytest.mark.django_db
def test_integridad_de_usuario():
    User = get_user_model()
    User.objects.create_user(username="estudiante_prueba")
    with pytest.raises(IntegrityError):
        with transaction.atomic():
            User.objects.create_user(username="estudiante_prueba")
    assert User.objects.filter(username="estudiante_prueba").count() == 1


def test_administracion_requiere_inicio_de_sesion(client):
    response = client.get("/admin/")
    assert response.status_code == 302
    assert "/admin/login/" in response["Location"]
```

```bash
python -m pytest -q
```

Resultado esperado: **3 passed**. La BD de pruebas se crea separada de `pp4_desarrollo` y se elimina al terminar. No apuntar pytest a datos que se deban conservar.

Estas pruebas verifican el entorno y el comportamiento integrado del usuario de Django; no acreditan reglas de pasantías, cobertura de E7 ni permisos de los módulos que el equipo aún debe implementar. «No tests ran» no es una comprobación aprobada.

## 7. Levantar el servidor local

```bash
python manage.py runserver
```

Abrir `http://127.0.0.1:8000/`. Detener con Ctrl+C al terminar. La página inicial confirma el arranque; todavía no es la aplicación del proyecto.

## 8. Conservar la reproducción

Registrar en el README del equipo las versiones de Python y PostgreSQL, el commit evaluable, la preparación de variables, las migraciones y el comando de pruebas. Mantener `requirements.txt` en Git y generar un registro de las dependencias efectivamente instaladas con `python -m pip freeze`, sin incluir entornos de otras tareas.

Consultar [integración continua](integracion-continua.md) para ejecutar las mismas comprobaciones en GitHub Actions. Las pruebas y el workflow deben pertenecer al repositorio del equipo.

## Dificultades frecuentes

| Síntoma | Comprobación |
|---|---|
| Variable PP4 ausente | Configurar la sesión antes de ejecutar Django o pytest |
| Conexión rechazada | Iniciar PostgreSQL y revisar host/puerto |
| Autenticación fallida | Revisar rol y contraseña en la instalación local |
| Permiso denegado al crear test_pp4_desarrollo | Dar CREATEDB al rol local de pruebas o utilizar un entorno de pruebas autorizado |
| No se encuentra config.settings | Ejecutar desde la raíz que contiene manage.py y pytest.ini |
| Error tras IntegrityError | Usar un bloque atomic y rollback antes de nuevas consultas |

[Compatibilidad de Django 5.2](https://docs.djangoproject.com/en/5.2/faq/install/) · [PostgreSQL en Django](https://docs.djangoproject.com/en/5.2/ref/databases/) · [pytest-django](https://pytest-django.readthedocs.io/en/latest/tutorial.html) · [Guía estudiantil](README.md)
