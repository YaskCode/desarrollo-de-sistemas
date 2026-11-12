# Ejemplo · Solicitud, resultado y regla de duplicado

Este fragmento continúa el [DFD de estudio](../02-modelado-dfd/ejemplo-dfd.md). Sus reglas son hipotéticas y no sustituyen el análisis institucional del equipo.

## Diccionario lógico de E3

| ID | Nombre | Definición y composición | Tipo o dominio | Restricción |
|---|---|---|---|---|
| F-01 | Solicitud de postulación | Estudiante más oferta seleccionada | Estructura de ID-EST e ID-OFE | Ambos identificadores deben estar presentes |
| ID-EST | Identificador de estudiante | Referencia al estudiante del caso | Entero positivo | Debe corresponder a un estudiante existente |
| ID-OFE | Identificador de oferta | Referencia a la oferta del caso | Entero positivo | Debe corresponder a una oferta existente |
| D1 | Postulaciones | Colección de postulaciones registradas | Conjunto de estudiante, oferta e identificador de postulación | Sin duplicar el par estudiante–oferta |
| F-02 | Resultado del registro | Estado, mensaje e identificador si hay éxito | Estado: confirmado o rechazado | El rechazo no genera nueva postulación |

El mensaje comunica el resultado, pero la comprobación no debe depender solo de su texto: se debe verificar también si se creó o no el registro. Esta tabla ilustra la estructura; el diccionario completo debe cubrir todos los flujos y almacenes de E2.

## Proceso 1.2 · Validar solicitud

**Entradas:** datos de solicitud y postulaciones existentes. **Precondición del fragmento:** la identidad de quien solicita se ha establecido, la operación está autorizada y la oferta existente ha sido seleccionada. El tratamiento de autenticación pertenece a los requisitos del sistema completo.

**Reglas del ejemplo:** los identificadores tienen el formato previsto y no existe otra postulación del mismo estudiante a la misma oferta.

| Datos completos y formato válido | Par estudiante–oferta ya registrado | Acción |
|---|---|---|
| No | No aplica | Rechazar; no crear registro |
| Sí | Sí | Rechazar por duplicado; no crear registro |
| Sí | No | Emitir solicitud válida hacia 1.3 |

«No aplica» no significa que el sistema haya comprobado ausencia de duplicado: indica que no necesita evaluar esa condición para decidir el rechazo por datos incompletos o de formato inválido.

## Contrastar con E2 y E6

La salida de 1.2 es la solicitud válida o el rechazo definido en el DFD. La confirmación la emite 1.3 después del registro, no la validación previa. En E6, la regla de duplicado se refuerza con una restricción única; en E7, se comprueba que un rechazo no crea una segunda fila.

[Apuntes](apuntes.md) · [Unidad III](README.md)
