# Estudiar el mini proyecto en un dev container

Este entorno abre exclusivamente el [mini proyecto docente](../ejemplos/django-postgresql/README.md) como carpeta de trabajo; el repositorio completo queda montado en `/workspaces/desarrollo-de-sistemas`. Usa Python 3.12, las dependencias fijadas en requirements.txt y PostgreSQL 16. Las etiquetas de imágenes reciben actualizaciones: no garantizan una imagen idéntica bit a bit. No añade actividades ni modifica E1–E8.

## 1. Abrir

**En el equipo local:** instalar Git, Docker con Compose y VS Code con la extensión Dev Containers. Iniciar Docker, clonar el repositorio, seleccionar la rama que contiene esta configuración y abrir su raíz en VS Code. Ejecutar **Dev Containers: Reopen in Container**. No es necesario instalar Python, PostgreSQL ni pgAdmin en el anfitrión. La primera apertura descarga las imágenes y necesita conexión a Internet.

**En GitHub Codespaces:** antes de crear uno, revisar en la cuenta u organización la disponibilidad, quién paga, cuotas de cómputo y almacenamiento, presupuestos y límites. No se garantiza gratuidad para todas las cuentas. Si existe un costo o se requiere autorización de la organización, resolverlo antes de crear el entorno. En el repositorio, seleccionar la rama que contiene el ejemplo, ir a **Code → Codespaces** y crear el entorno con esta configuración cuando esté autorizado. Mientras el PR no esté fusionado, utilizar `feat/unidad-01-material-docente`.

## 2. Preparar

Esperar a que finalice la preparación automática: instala dependencias, comprueba su compatibilidad, espera la conexión a PostgreSQL y aplica migraciones. Se repite al reiniciar y puede ejecutarse manualmente en la terminal del contenedor:

```bash
bash /workspaces/desarrollo-de-sistemas/.devcontainer/preparar.sh
```

No crear otro proyecto Django, una segunda BD ni un entorno virtual adicional. Compose aporta las variables PP4 al contenedor. Las contraseñas y clave de esta configuración son **valores públicos exclusivos de desarrollo desechable**, no credenciales de cuentas reales. El rol de PostgreSQL administra esta instancia aislada y puede crear la BD de pytest; no usarlo fuera de ella. No introducir datos institucionales ni reutilizar estas claves en otros servicios. `.env` está ignorado por Git, pero Django no lo carga automáticamente: las variables propias se exportan en la sesión. No subir contraseñas reales.

## 3. Ejecutar

Primero, abrir **Terminal → Nueva terminal** (botón **+**). Comprobar la carpeta y las pruebas:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python manage.py check
python manage.py migrate --check
python -m pytest -q
```

La suite existente contiene 19 pruebas y usa una base de pruebas separada.

Para preparar los datos por primera vez, ejecutar **esta línea sola**:

```bash
read -r -s -p 'Contraseña de demostración (al menos 12 caracteres): ' PP4_DEMO_PASSWORD
```

Escribir una contraseña propia y pulsar Enter; no se muestra mientras se escribe. No pegar el siguiente bloque hasta terminar de introducirla. Conservarla sin incluirla en Git ni capturas. Después ejecutar:

```bash
export PP4_DEMO_PASSWORD
python manage.py sembrar_demo
unset PP4_DEMO_PASSWORD
python manage.py runserver 0.0.0.0:8000
```

El comando crea las cuentas `estudiante_uno` y `estudiante_dos` y ofertas sintéticas. No cambia contraseñas de cuentas existentes. Para restablecer una, abrir otra terminal, entrar en la carpeta del ejemplo y ejecutar `python manage.py changepassword estudiante_dos` (o `estudiante_uno`); introducir la nueva contraseña dos veces.

Cuando aparezca `Starting development server`, dejar esa terminal abierta: está ocupada por Django y no ejecuta comandos de shell. Para ejecutar pruebas o diagnósticos sin detener el servidor, usar otra terminal con el botón **+** y esperar el indicador terminado en `$`.

En VS Code local, abrir el puerto reenviado 8000 en `http://localhost:8000/entrar/`. En Codespaces, usar **Ports → 8000 → Open in Browser**, comprobar que la dirección termine en `/entrar/` y comprobar que la visibilidad sea **Private** antes de utilizarlo. La configuración solicita visibilidad privada y desactiva el reenvío automático de otros puertos. PostgreSQL no publica ningún puerto del anfitrión; no reenviar 5432 manualmente.

Django acepta el host concreto del puerto 8000 de ese Codespace y su origen HTTPS para los formularios protegidos por CSRF. Exclusivamente en Codespaces, también acepta el origen exacto `https://localhost:8000` observado en el túnel privado; conserva la comprobación de cookie y token CSRF. No utiliza comodines. Si cambia el dominio de reenvío, reiniciar el contenedor y comprobar sus variables. No desactivar CSRF para resolver un error de acceso.

## 4. Explorar, modificar y probar

Leer la especificación y seguir la regla hipotética por modelo → migración → servicio → formulario/vista → prueba. Revisar el [recorrido del ejemplo](../ejemplos/django-postgresql/README.md) y contrastar estos resultados en una sola pestaña:

| Paso | Resultado esperado |
|---|---|
| Entrar con estudiante_uno y registrar una oferta | Aparece una postulación propia |
| Seleccionar la misma oferta y pulsar Registrar postulación de nuevo | Mensaje de duplicado y una sola postulación |
| Salir y entrar con estudiante_dos, sin registros previos | No muestra la postulación del primero |
| Registrar la misma oferta con estudiante_dos | Crea un registro propio para la segunda cuenta |

El número del registro identifica una fila global de la BD; «Registro 2» no significa que esa cuenta tenga dos postulaciones. Estos datos y reglas son hipotéticos. Este recorrido es una comprobación del ejemplo, no otra entrega ni validación institucional.

Crear una rama de estudio o trabajar en una copia propia para conservar los cambios. Modificar un comportamiento acotado, explicar el resultado esperado y ejecutar de nuevo `python -m pytest -q`. Si cambia un modelo, generar y revisar su migración con `python manage.py makemigrations`, aplicarla con `python manage.py migrate` y repetir las pruebas. Conservar código, migraciones y explicación juntos.

## 5. Detener y eliminar

Detener Django con **Ctrl+C**. Guardar los cambios de código con Git antes de eliminar el entorno; los datos sintéticos de la BD no forman parte del repositorio.

**Local:** cerrar la conexión de Dev Containers detiene los servicios. Para identificar el proyecto de Compose usado por VS Code, ejecutar `docker compose ls` en el anfitrión. Desde la raíz del repositorio, sustituir `NOMBRE_DEL_PROYECTO` por el nombre exacto mostrado:

```bash
docker compose -p NOMBRE_DEL_PROYECTO -f .devcontainer/compose.yaml stop
# Elimina los contenedores y la BD de ese entorno; no el código montado.
docker compose -p NOMBRE_DEL_PROYECTO -f .devcontainer/compose.yaml down --volumes
```

El volumen conserva la BD entre reinicios y reconstrucciones; `down --volumes` elimina sus datos. Confirmar el proyecto elegido antes de ejecutar el borrado. Las imágenes descargadas permanecen disponibles para reutilizarlas.

**Codespaces:** usar **Stop Current Codespace** o **Stop codespace** desde la lista de [tus Codespaces](https://github.com/codespaces). Cerrar la pestaña del navegador no lo detiene inmediatamente. Si terminaste, guardar o enviar los cambios y usar **Delete** para eliminar ese Codespace y su almacenamiento; detenerlo conserva almacenamiento que puede seguir generando cargos. No eliminar otros entornos.

## Retomar el mismo entorno

Abrir el Codespace existente desde [tus Codespaces](https://github.com/codespaces), sin crear otro. Esperar la preparación automática. En una terminal nueva, ejecutar:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python manage.py check
python manage.py migrate --check
python manage.py runserver 0.0.0.0:8000
```

No repetir la siembra si ya existen los datos. Usar las contraseñas vigentes. Si aparecen migraciones pendientes, detener el servidor, ejecutar `python manage.py migrate --noinput` y volver a iniciarlo.

## Si algo falla

| Síntoma | Comprobación |
|---|---|
| No inicia el entorno local | Docker iniciado, Compose disponible y raíz correcta |
| Falló la preparación | Revisar el log; comprobar conexión a Internet y servicio db; repetir preparar.sh |
| Credenciales no coinciden con el volumen | El volumen conserva las credenciales iniciales; restaurarlas o recrear solo la BD sintética mediante down --volumes |
| No encuentra manage.py | Ejecutar cd hacia la carpeta del ejemplo; la raíz del repositorio no contiene ese archivo |
| Comando pegado sin respuesta en la terminal del servidor | Abrir otra terminal con +; no pegar comandos de shell dentro del proceso Django |
| Error de host u origen CSRF | Usar el enlace del puerto 8000 del Codespace actual, revisar sus variables y comprobar que se utiliza la configuración actualizada |
| CSRF token from POST incorrect | Abrir de nuevo la dirección desde la barra del navegador como GET, sin reenviar el POST; mantener una sola pestaña y usar el formulario recién cargado |
| No aparecen datos | Ejecutar sembrar_demo y usar la contraseña establecida |
| Cambiaron dependencias | Actualizar requirements.txt y volver a ejecutar preparar.sh |

### Acceso privado con error 401

Primero distinguir el servidor del reenvío. Con Django encendido, ejecutar en una **segunda terminal**:

```bash
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8000/entrar/
```

Si devuelve `200`, el formulario responde dentro del entorno. Ese resultado no comprueba el acceso externo ni la autenticación del túnel. En el mismo perfil del navegador, confirmar la sesión de GitHub con la cuenta propietaria del Codespace y abrir el enlace generado en **Puertos**.

Si persiste el 401, probar **Puertos → 8000 → Detener reenvío del puerto**, después **Agregar puerto → 8000**. Confirmar visibilidad **Private**, protocolo interno **HTTP** y abrir el nuevo enlace desde ese panel. Recrear el reenvío no elimina la BD ni el código y no demuestra por sí solo la causa del fallo. La dirección externa HTTPS es compatible con el servidor HTTP interno. No hacer público el puerto para eludir la autenticación.

Si la respuesta interna falla, revisar primero la terminal del servidor. Si vuelve a fallar CSRF con un formulario recién cargado, conservar el motivo exacto y los pasos de reproducción, sin compartir contraseñas, cookies ni tokens. No desactivar el middleware CSRF.

## Referencias

[Dev Containers y Compose](https://code.visualstudio.com/docs/devcontainers/create-dev-container) · [Puertos en Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace) · [Ciclo de vida](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle) · [Facturación de Codespaces](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)

El workflow comprueba el entorno con Compose en un runner temporal. Ese resultado no demuestra por sí solo la experiencia del editor ni una sesión real de Codespaces. Actions comprueba código; Codespaces proporciona desarrollo; una demo pública requeriría otro servicio y decisiones de alojamiento.

[Guía estudiantil](README.md) · [Preparación manual](entorno.md) · [Inicio](../README.md)
