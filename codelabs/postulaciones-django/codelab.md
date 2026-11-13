# Postulaciones con Django y PostgreSQL: de la regla a la prueba

## Introducción y preparación

PP4 – Desarrollo de Sistemas (960116), sexto semestre, Licenciatura en Computación. Facultad Experimental de Ciencias, Universidad del Zulia, Venezuela. Docente: Dra. Yaskelly Yedra.

En este codelab explorarás un ejemplo ya resuelto: seguirás una regla de negocio desde los modelos y la persistencia hasta las pruebas y la evidencia. No necesitas construir una aplicación desde cero para recorrerlo.

Recorrido autoguiado sin límite pedagógico de tiempo. Puedes retroceder, retomar y repetir las comprobaciones. Complementa E6–E8; no añade una entrega ni modifica la evaluación. Es un ejemplo hipotético, sin procedimientos oficiales de FEC-LUZ. Los proyectos completos permanecen en [YaskCode-laboratory](https://github.com/YaskCode-laboratory).

Utiliza la rama main del repositorio. Necesitas la copia confiable del repositorio, Python y PostgreSQL del entorno preparado y una cuenta sintética del ejemplo. Sigue [apertura y recuperación del entorno](../../docs/devcontainer.md) o la [preparación manual](../../docs/entorno.md). Codespaces es opcional: revisa disponibilidad, cuotas y facturación antes de crear uno. También puedes usar VS Code, Docker y Dev Containers localmente.

Concede confianza a la carpeta si has revisado su origen. En una terminal del contenedor:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python manage.py check
python manage.py migrate --check
```

Para preparar cuentas y contraseñas propias, sigue la sección 3 de la guía de entorno. No hay contraseña predeterminada. La siembra no cambia contraseñas existentes. Para restablecer una cuenta:

```bash
python manage.py changepassword estudiante_dos
```

Activa el validador solo en este entorno privado de desarrollo confiable. Detén el servidor anterior con Ctrl+C y arranca:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
PP4_CODELAB=1 python manage.py runserver 0.0.0.0:8000
```

Deja esa terminal ocupada por el servidor. Usa una segunda terminal con + para diagnósticos y pruebas. En Codespaces abre el enlace actual del panel Puertos, confirma Private y entra en /codelab/. Localmente abre http://localhost:8000/codelab/. Inicia sesión con una cuenta sintética. No publiques el puerto ni reenvíes PostgreSQL.

## Entorno y migraciones · E6 y E8

Lee la [especificación](../../ejemplos/django-postgresql/especificacion.md) y el [modelo de datos](../../ejemplos/django-postgresql/gestion/models.py). Identifica las claves foráneas y la restricción estudiante–oferta. Explica por qué protege la base aunque se omita el servicio. Esta reflexión no tiene comprobación automática de comprensión.

El botón de este paso consulta PostgreSQL real y comprueba que no queden migraciones pendientes en la base de desarrollo. No crea postulaciones ni ejecuta la suite. Espera “aprobado” solo si ambas condiciones se cumplen.

Si falla, revisa el servicio db y, en la segunda terminal, aplica las migraciones:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python manage.py migrate --noinput
```

## Registro válido · E7

Examina [servicio](../../ejemplos/django-postgresql/gestion/services.py), [formulario](../../ejemplos/django-postgresql/gestion/forms.py) y [vistas](../../ejemplos/django-postgresql/gestion/views.py). En la aplicación / registra una oferta sintética con estudiante_uno. Observa la confirmación y vuelve al codelab.

El botón ejecuta las pruebas de primera postulación y POST válido en una base PostgreSQL de pruebas separada, con datos sintéticos nuevos. Verifica el comportamiento actual del ejemplo; no inspecciona tu clic anterior ni demuestra que modificaste el código. Espera dos pruebas aprobadas. Las postulaciones de desarrollo permanecen intactas.

Si falla, ejecuta esas pruebas en la segunda terminal y compara el comportamiento con la especificación:

```bash
python -m pytest -q gestion/tests/test_postulaciones.py::test_primera_postulacion gestion/tests/test_postulaciones.py::test_post_correcto_redirige_y_muestra_confirmacion
```

## Duplicados · E6 y E7

En la aplicación, repite la misma oferta con la misma cuenta. Espera un mensaje de duplicado y una sola fila propia. Revisa la [migración inicial](../../ejemplos/django-postgresql/gestion/migrations/0001_initial.py).

El botón ejecuta tres pruebas: repetición del servicio, restricción directa de BD y conflicto HTTP sin segunda fila. Este es un resultado de pruebas del ejemplo, independiente del recorrido manual. Si falla, revisa UniqueConstraint, get_or_create y la respuesta de la vista.

Exploración opcional, sin nueva obligación evaluada: en una copia o rama propia, cambia temporalmente el servicio para usar create en lugar de get_or_create conservando su contrato de retorno. Predice el fallo de duplicados, compruébalo y restaura el servicio; vuelve a comprobar. No retires la restricción ni borres datos. El cambio de huella y el fallo acreditan esa ejecución concreta, no la comprensión ni la autoría del cambio.

## Separación entre cuentas · E7

Cierra sesión en / y entra como estudiante_dos. Si no tenía registros propios, debe ver una lista vacía. Puede registrar la misma oferta con su identidad. Cada cuenta puede tener una contraseña diferente.

El botón ejecuta cuatro pruebas de consulta propia, identidad falsificada, misma oferta con otra cuenta y rechazo anónimo. No inspecciona el historial personal de las cuentas del recorrido manual. Si falla, revisa el filtro por request.user y la autenticación antes de registrar o consultar.

## Suite y reproducción · E8

Revisa [pruebas originales](../../ejemplos/django-postgresql/gestion/tests/test_postulaciones.py), [guía del ejemplo](../../ejemplos/django-postgresql/README.md) e [integración continua](../../docs/integracion-continua.md). Relaciona la evidencia con [E6](../../proyecto-integrador/entregables/e06.md), [E7](../../proyecto-integrador/entregables/e07.md) y [E8](../../proyecto-integrador/entregables/e08.md).

El botón ejecuta los dos archivos originales: 19 pruebas del caso y del entorno, en PostgreSQL. No incluye las pruebas internas del codelab para evitar ejecuciones recursivas. Si hay errores de preparación, permisos o dependencias, se informa error del entorno; si una aserción falla, se informa fallo. El límite técnico es 90 segundos por proceso de pruebas y no limita el tiempo del codelab.

Para diagnosticar desde la segunda terminal:

```bash
cd /workspaces/desarrollo-de-sistemas/ejemplos/django-postgresql
python -m pytest -q gestion/tests/test_postulaciones.py gestion/tests/test_entorno.py
```

El verde acredita únicamente esos criterios sobre la huella mostrada y la instancia de servidor indicada. No acredita todo el sistema, comprensión, una modificación del estudiante ni aprobación académica. El código ya está resuelto al comenzar. Puedes descargar la evidencia JSON para contrastarla con la ejecución; es evidencia local informativa, no un certificado firmado ni un registro docente.

Los resultados quedan en la sesión Django existente. Al cambiar archivos, variables, migraciones, versión del servidor PostgreSQL o reiniciar Django, se muestran como anteriores o se pide comprobar otra vez. Se revisa su vigencia periódicamente y al volver a la pestaña. Una edición no comprobada nunca debe interpretarse como cubierta por un resultado anterior. Un entorno caído impide confirmar vigencia. La huella no certifica el contenido completo de la base ni detecta cambios transitorios revertidos entre comprobaciones.

## Conclusiones y cierre

### Qué te llevas de este recorrido

Una regla de negocio puede expresarse en la especificación, protegerse mediante una restricción de PostgreSQL y contrastarse mediante pruebas. El servicio y la vista completan esa colaboración: la base conserva la integridad y la aplicación comunica el resultado al usuario.

La autenticación identifica a la cuenta; filtrar las consultas por esa identidad protege la separación entre registros. Comprobar registro, duplicados y aislamiento permite contrastar comportamientos concretos, más allá de que una página cargue correctamente.

La reproducción del entorno y la evidencia de pruebas permiten revisar qué se comprobó y sobre qué versión. Esa es la conexión de este ejemplo con E6, E7 y E8: modelos y persistencia, pruebas y reproducción documentada.

### Revisa tu evidencia

Si ejecutaste las comprobaciones, revisa sus resultados vigentes y conserva el JSON que necesites junto con la versión estudiada. Si un criterio falló o el entorno no permitió comprobarlo, vuelve al paso correspondiente, consulta la ayuda y repite la validación después de corregirlo. Leer hasta el final no sustituye esas comprobaciones.

Para reflexionar: ¿qué protege la restricción única que no garantiza por sí solo un formulario? ¿Por qué estar autenticado no basta para aislar los registros? ¿Qué evidencia tendrías que renovar después de cambiar el servicio? Son preguntas para explicar tu razonamiento, sin calificación ni comprobación automática de comprensión.

### Detén el entorno y conserva tu trabajo

Guarda tus cambios con Git antes de eliminar un entorno y conserva la explicación de cualquier exploración opcional. No incorpores contraseñas, cookies ni tokens al repositorio o a las capturas.

Detén Django con Ctrl+C. Si utilizaste Codespaces, detén ese Codespace desde GitHub; cerrar la pestaña no confirma su parada. Detener no elimina el almacenamiento. Eliminar el entorno o su volumen borra sus datos sintéticos: sigue la [guía de parada y eliminación](../../docs/devcontainer.md) solo cuando hayas conservado lo que necesites. No es necesario borrar recursos para completar este recorrido.

### Retomar y encontrar ayuda

La navegación usa el fragmento de la URL: puedes guardar ese enlace para volver al paso. El progreso técnico pertenece a la sesión actual; no hay cuentas adicionales, notas, seguimiento docente ni sincronización entre dispositivos. La caducidad de la sesión y la cuota o suspensión de Codespaces son independientes del tiempo pedagógico del codelab.

Si aparece 401 externo pero Django responde 200 internamente, sigue la recuperación del reenvío privado de la guía. No se conoce una causa única de ese error. Si el formulario tiene token CSRF no vigente, abre de nuevo la página como GET; si persiste con un formulario nuevo, investígalo sin desactivar CSRF. No compartas cookies, contraseñas ni tokens.

Si una comprobación no termina o pierde la conexión, se quita el verde y se muestra error del entorno. Espera a que termine el proceso antes de repetir. No ejecutes otra suite de pytest simultáneamente contra la misma base de pruebas.

Consulta [ayuda completa](../../docs/devcontainer.md), [preguntas frecuentes](../../docs/preguntas-frecuentes.md) y [bibliografía](../../recursos/bibliografia.md). Puedes volver a cualquier paso; el codelab no tiene fecha de caducidad pedagógica.

### ¡Felicitaciones por tu recorrido!

Si completaste la exploración y contrastaste los resultados, ¡felicitaciones por el trabajo de examinar, probar y corregir! Lo valioso es poder explicar la relación entre la regla, el código y la evidencia, incluyendo los límites de lo comprobado.

Puedes continuar aplicando esa forma de trabajo a tu proyecto integrador, según las orientaciones de E6–E8. Este cierre no añade una entrega, no otorga una certificación y no cambia la evaluación de la asignatura.

Esta experiencia propia de YaskCode se inspira en el aprendizaje guiado; no es un producto ni una certificación oficial de Google. La guía en Markdown se puede leer en GitHub. La guía pública en Pages conserva el menú por pasos y no ejecuta el validador. Las comprobaciones se realizan en el entorno privado.
