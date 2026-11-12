#!/usr/bin/env bash
set -euo pipefail
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python -m pip install --disable-pip-version-check -r requirements.txt
python -m pip check
python - <<'PY'
import os
import time
import psycopg

for intento in range(30):
    try:
        with psycopg.connect(
            dbname=os.environ['PP4_DB_NAME'], user=os.environ['PP4_DB_USER'],
            password=os.environ['PP4_DB_PASSWORD'], host=os.environ['PP4_DB_HOST'],
            port=os.environ['PP4_DB_PORT'], connect_timeout=2,
        ):
            break
    except psycopg.OperationalError:
        if intento == 29:
            raise SystemExit('PostgreSQL no estuvo disponible. Revisar el servicio db y volver a preparar.')
        time.sleep(2)
PY
python manage.py check
python manage.py migrate --noinput
