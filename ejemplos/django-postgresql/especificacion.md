# Especificación del fragmento docente

El sistema permite registrar una postulación sobre una oferta sintética. Una cuenta Django representa al estudiante para este ejemplo; no incorpora un expediente estudiantil ni una estructura completa de perfiles.

| ID | Regla o comportamiento | Evidencia |
|---|---|---|
| RF-01 | Registrar una postulación de la cuenta autenticada | POST válido crea una fila y redirige a la consulta |
| RF-02 | Consultar solo postulaciones propias | Filtro por identidad de sesión y prueba con dos cuentas |
| RN-01 | Un par estudiante–oferta tiene como máximo una postulación | UniqueConstraint y prueba que omite el servicio |
| RN-02 | Registrar no significa aprobar académicamente | Confirmación y listado dicen registrada, sin aprobación |
| RN-03 | El formulario solo acepta ofertas activas al validarse | Rechazo de oferta inexistente o inactiva |
| SEG-01 | El cliente no elige en nombre de quién registra | Un campo estudiante falsificado no altera request.user |
| SEG-02 | Las operaciones de registro exigen protección CSRF | POST sin token se rechaza |

Las reglas son hipotéticas. El flujo es selección → registro o rechazo → consulta propia. La identidad y la selección se comprueban en la frontera HTTP. El servicio se invoca desde esa frontera validada y utiliza la restricción de BD para resolver intentos repetidos.

## Casos esperados

Una postulación nueva genera una fila. Repetir el mismo par devuelve conflicto HTTP 409 y mantiene una fila. Otra cuenta o una oferta distinta pueden originar otro par. Datos de oferta inválidos devuelven HTTP 400. Sin sesión, se solicita iniciar sesión; un método no permitido se rechaza.

## Límites de la evidencia

Las pruebas automáticas comprueban los casos especificados y el arranque del entorno. No prueban todos los requisitos no funcionales ni sustituyen la validación de comprensión con usuarios. La lista de campos, el vocabulario y las reglas deben revisarse si cambia el dominio.

[Ejemplo](README.md) · [Reglas y datos de estudio](../../unidades/03-diccionario-datos/ejemplo-datos-procesos.md)
