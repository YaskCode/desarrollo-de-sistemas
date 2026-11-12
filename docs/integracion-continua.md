# Integración continua del repositorio del equipo

GitHub Actions permite ejecutar la suite al actualizar el código. Este ejemplo corresponde al entorno de la [guía de preparación](entorno.md); adaptarlo al nombre real del proyecto cuando cambie. El workflow pertenece al repositorio del equipo y utiliza una BD PostgreSQL efímera de CI.

El repositorio académico también incluye un [workflow del mini proyecto docente](../.github/workflows/ejemplo-django-postgresql.yml), cuyo código está en [ejemplos/django-postgresql](../ejemplos/django-postgresql/README.md).

## Workflow de referencia

Guardar en `.github/workflows/pruebas.yml` del equipo:

```yaml
name: Pruebas Django
on: [push, pull_request]
permissions:
  contents: read
jobs:
  pruebas:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: pp4_desarrollo
          POSTGRES_USER: pp4_local
          POSTGRES_PASSWORD: pp4_ci_efimera
        ports:
          - 5432:5432
        options: >-
          --health-cmd "pg_isready -U pp4_local -d pp4_desarrollo"
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
    env:
      PP4_DB_NAME: pp4_desarrollo
      PP4_DB_USER: pp4_local
      PP4_DB_PASSWORD: pp4_ci_efimera
      PP4_DB_HOST: 127.0.0.1
      PP4_DB_PORT: "5432"
      PP4_SECRET_KEY: clave-solo-para-pruebas-efimeras-de-ci
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m pip install -r requirements.txt
      - run: python -m pip check
      - run: python manage.py check
      - run: python manage.py makemigrations --check --dry-run
      - run: python manage.py migrate --noinput
      - run: python -m pytest -q
```

Las credenciales incluidas solo conectan servicios efímeros del propio job: no reutilizarlas en un entorno persistente. Este workflow no necesita secretos institucionales ni despliega la aplicación. El usuario creado por la imagen oficial posee permisos amplios dentro de ese servicio aislado; no trasladar esa configuración a producción.

## Cómo interpretar el resultado

`makemigrations --check --dry-run` detecta cambios de modelos sin migración versionada. `migrate` comprueba la aplicación de migraciones. pytest ejecuta la suite y devuelve un fallo si no hay pruebas recogidas o si no pasan.

Una ejecución aprobada solo respalda las comprobaciones que contiene la suite. Los modelos, prototipos, decisiones y necesidades de los usuarios requieren las revisiones de E1–E8. Registrar el enlace de la ejecución asociada al commit presentado cuando se utilice esta automatización en el proyecto final.

La ejecución de este workflow debe comprobarse en la pestaña Actions del repositorio del equipo. Confirmar que las migraciones y las pruebas terminan sin errores antes de utilizar su ejecución como evidencia de integración.

[Documentación oficial de GitHub Actions](https://docs.github.com/en/actions) · [Guía estudiantil](README.md) · [E7](../proyecto-integrador/entregables/e07.md) · [E8](../proyecto-integrador/entregables/e08.md)
