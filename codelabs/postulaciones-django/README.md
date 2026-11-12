# Codelab propio de PP4

[Leer el recorrido](codelab.md). La fuente Markdown se utiliza tanto para lectura en GitHub como para los siete pasos de `/codelab/` en Django. No depende de claat ni de servicios nuevos. La lectura en GitHub no ejecuta comprobaciones.

## Ejecutar la experiencia interactiva

Utilizar la [guía del entorno](../../docs/devcontainer.md), en una copia confiable del repositorio y un entorno privado. Seleccionar la rama que contiene este codelab. Desde la carpeta del mini proyecto, después de preparar las cuentas sintéticas y migraciones:

```bash
PP4_CODELAB=1 python manage.py runserver 0.0.0.0:8000
```

Abrir `/codelab/` desde el enlace actual del puerto 8000 privado; entrar con la cuenta sintética existente. En ejecución manual, definir también las variables PP4 documentadas y `PP4_DEBUG=1` para servir los archivos estáticos con el servidor de desarrollo. Al desactivar `PP4_CODELAB`, las rutas del codelab no se habilitan. El código del ejemplo permanece en `ejemplos/django-postgresql/`.

## Diseño del validador

| Componente | Responsabilidad |
|---|---|
| `codelab.md` | Contenido y recursos enlazados |
| `gestion/codelab_content.py` | Renderizador limitado: párrafos, enlaces HTTP(S) y bloques copiables; escapa HTML |
| `gestion/codelab.py` | Criterios cerrados, ejecución, evidencia y vigencia |
| Plantilla, CSS y JS de `gestion` | Navegación, teclado, estados, descarga y consulta de vigencia |
| `.devcontainer/comprobar_codelab.py` | Regresiones con Django y PostgreSQL reales |
| `.devcontainer/comprobar_codelab_web.py` | Recorrido HTTP con Chromium y capturas de revisión |

La interfaz y el validador usan el mismo origen, sesión y middleware CSRF del ejemplo. No hay CORS ni llamadas desde Pages hacia Codespaces. El POST admite exclusivamente cinco identificadores predefinidos; no recibe comandos, rutas o argumentos de pytest. El proceso usa una lista de argumentos sin shell, timeout de 90 segundos y terminación de su grupo de procesos al agotarlo. Un bloqueo de hilo y otro de archivo serializan las comprobaciones del mismo entorno. No ejecutar pytest manualmente al mismo tiempo contra la misma base de pruebas.

Ejecutar pytest ejecuta código del repositorio con los permisos del usuario de desarrollo. La activación es exclusivamente para una copia confiable en el entorno privado desechable, sin secretos ni datos institucionales. No es un servicio para ejecutar código de terceros ni una sandbox multiusuario. El rol de desarrollo necesita permiso para crear la base temporal de pytest; PostgreSQL no se publica.

No se devuelven logs crudos de pytest: la respuesta resume el reporte JUnit, los selectores, fecha UTC, huellas e identificador de instancia. Para investigar una aserción se usa la segunda terminal. `fallo` significa aserciones fallidas; `error_entorno` cubre errores de preparación, colección, permisos, pruebas omitidas o timeout. La consulta de entorno verifica PostgreSQL y migraciones, sin ejecutar pruebas del caso.

Las evidencias se guardan en la sesión Django existente, sin tablas ni cuentas nuevas. Cada consulta de estado recalcula huellas de archivos, variables de proceso, Python, versión e inicio del servidor PostgreSQL, nombre de BD y migraciones aplicadas. Reiniciar Django cambia el identificador de instancia. El navegador consulta cada cinco segundos y al recuperar visibilidad; una desconexión retira el aprobado visible. No usa localStorage como evidencia. Los resultados no son certificados firmados, no comprueban autoría y no describen todo el contenido de la BD. No detectan cambios transitorios revertidos entre consultas ni reemplazan la revisión del código y las pruebas.

## Mantenimiento y comprobaciones

Al añadir o quitar pasos, mantener la correspondencia de secciones Markdown con los criterios en `steps()`. El renderizador admite deliberadamente un subconjunto pequeño de Markdown. Los enlaces del modo interactivo y público apuntan a main. Los enlaces relativos de la fuente Markdown siguen funcionando en la referencia que se esté leyendo en GitHub.

Con el entorno preparado, desde el mini proyecto:

```bash
python ../../.devcontainer/comprobar_codelab.py
```

El workflow también ejecuta el recorrido de navegador contra Django y PostgreSQL reales, con una cuenta efímera y una contraseña generada en memoria. Conserva capturas de escritorio y móvil y JSON de una ejecución real como artefacto temporal de revisión. No exporta cookies, formularios con tokens ni credenciales. La prueba de navegador no sustituye una auditoría completa con lectores de pantalla ni validación con estudiantes.

La guía pública se genera con `python scripts/construir_codelab.py` en `_site/codelabs/postulaciones-django/index.html`. El workflow `codelab-pages.yml` guarda una vista previa en los PR y publica únicamente los cambios de main en GitHub Pages. La generación no importa settings.py, no necesita PostgreSQL ni variables PP4 y no exporta tokens de sesión. El modo público conserva navegación y comandos; sustituye el validador por instrucciones explícitas para abrir el entorno privado, sin solicitudes a su API ni estados de aprobado.

Dirección prevista de la guía: https://yaskcode.github.io/desarrollo-de-sistemas/codelabs/postulaciones-django/ . Para la habilitación inicial, seleccionar GitHub Actions en Settings → Pages → Build and deployment → Source. El token automático del workflow puede publicar, pero no habilitar Pages por primera vez. Después, ejecutar de nuevo el workflow desde Actions si todavía no hubo despliegue. Ofrecer una demo pública Django o introducir seguimiento del alumnado sigue siendo una decisión independiente.
