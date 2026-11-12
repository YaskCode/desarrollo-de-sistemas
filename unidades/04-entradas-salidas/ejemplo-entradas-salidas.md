# Ejemplo · Registrar y consultar una postulación

Escenario hipotético del caso de estudio de pasantías. Las pantallas descritas sirven como referencia para diseñar el prototipo en Figma; no existe un archivo Figma adicional en este repositorio.

## Entrada: postulación a una oferta

**Actor:** estudiante identificado. **Propósito:** registrar su interés por una oferta, sin confundirlo con la aprobación académica.

| Elemento | Diseño y comportamiento |
|---|---|
| Oferta seleccionada | Mostrar título e identificador para comprobar el destino de la solicitud |
| Estudiante | Derivar la identidad de la sesión; no permitir registrar en nombre de otro estudiante modificando un campo |
| Acción de registro | Botón con una etiqueta concreta: «Registrar postulación» |
| Resultado confirmado | Mostrar identificador y estado del registro, sin afirmar aprobación |
| Duplicado | Explicar que ya existe una postulación y permitir consultar la existente según permisos |
| Error de entrada | Identificar el dato inválido y mantener los datos válidos cuando corresponda |

Estos comportamientos deben corresponder a E1, E3 y E4. El servidor comprueba identidad, referencias y duplicados aunque el formulario parezca válido.

## Salida: consulta para coordinación

**Pregunta:** ¿qué postulaciones se registraron para una oferta? **Actor:** coordinación autorizada.

| Aspecto | Definición del ejemplo |
|---|---|
| Filtro | Identificador de oferta |
| Datos mostrados | Identificador de postulación, estudiante sintético y estado |
| Sin resultados | Informar que no hay postulaciones para ese filtro |
| Acceso no autorizado | Rechazar la consulta sin mostrar registros |
| Exportación | Si se incluye, respetar los filtros y permisos de la consulta |

## Recorrido de validación

Plantear el escenario «quieres saber si tu solicitud quedó registrada». Observar si la persona localiza la oferta, entiende la acción e interpreta la confirmación. Registrar el hallazgo concreto: por ejemplo, «interpretó registrada como aprobada». Revisar el mensaje y repetir la comprobación del mismo flujo.

Este recorrido forma parte de la revisión de E5. No es una actividad evaluada aparte ni demuestra aceptación por la institución.

[Apuntes](apuntes.md) · [Unidad IV](README.md)
