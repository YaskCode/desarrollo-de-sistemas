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

Desde la terminal, situada en `ejemplos/django-postgresql`:

```bash
python -m pytest -q
read -r -s -p 'Contraseña de demostración (al menos 12 caracteres): ' PP4_DEMO_PASSWORD
export PP4_DEMO_PASSWORD
python manage.py sembrar_demo
unset PP4_DEMO_PASSWORD
python manage.py runserver 0.0.0.0:8000
```

La suite existente contiene 19 pruebas y usa una base de pruebas separada. El comando de demostración crea datos sintéticos y no cambia contraseñas de cuentas existentes. Para restablecer una, usar `python manage.py changepassword estudiante_uno`.

En VS Code local, abrir el puerto reenviado 8000 en `http://localhost:8000/entrar/`. En Codespaces, usar **Ports → 8000 → Open in Browser**, añadir `/entrar/` y comprobar que la visibilidad sea **Private** antes de utilizarlo. La configuración solicita visibilidad privada y desactiva el reenvío automático de otros puertos. PostgreSQL no publica ningún puerto del anfitrión; no reenviar 5432 manualmente.

Django acepta el host concreto del puerto 8000 de ese Codespace y su origen HTTPS para los formularios protegidos por CSRF. No utiliza comodines. Si cambia el dominio de reenvío, reiniciar el contenedor y comprobar sus variables. No desactivar CSRF para resolver un error de acceso.

## 4. Explorar, modificar y probar

Leer la especificación y seguir la regla hipotética por modelo → migración → servicio → formulario/vista → prueba. Ingresar con `estudiante_uno`, registrar una postulación y repetirla; comparar después con `estudiante_dos`. Revisar el [recorrido del ejemplo](../ejemplos/django-postgresql/README.md).

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

## Si algo falla

| Síntoma | Comprobación |
|---|---|
| No inicia el entorno local | Docker iniciado, Compose disponible y raíz correcta |
| Falló la preparación | Revisar el log; comprobar conexión a Internet y servicio db; repetir preparar.sh |
| Credenciales no coinciden con el volumen | El volumen conserva las credenciales iniciales; restaurarlas o recrear solo la BD sintética mediante down --volumes |
| Error de host o CSRF | Usar el enlace del puerto 8000 del Codespace actual y revisar sus variables |
| No aparecen datos | Ejecutar sembrar_demo y usar la contraseña establecida |
| Cambiaron dependencias | Actualizar requirements.txt y volver a ejecutar preparar.sh |

## Referencias

[Dev Containers y Compose](https://code.visualstudio.com/docs/devcontainers/create-dev-container) · [Puertos en Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace) · [Ciclo de vida](https://docs.github.com/en/codespaces/about-codespaces/understanding-the-codespace-lifecycle) · [Facturación de Codespaces](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)

El workflow comprueba el entorno con Compose en un runner temporal. Ese resultado no demuestra por sí solo la experiencia del editor ni una sesión real de Codespaces. Actions comprueba código; Codespaces proporciona desarrollo; una demo pública requeriría otro servicio y decisiones de alojamiento.

[Guía estudiantil](README.md) · [Preparación manual](entorno.md) · [Inicio](../README.md)
