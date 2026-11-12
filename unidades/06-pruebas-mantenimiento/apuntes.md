# Unidad VI · Probar, documentar y mantener

## Qué aporta una prueba

Una prueba relaciona condiciones, entrada, acción y resultado esperado. Su valor depende de la pregunta que permite responder. Una ejecución exitosa del flujo principal no cubre automáticamente permisos, errores de entrada o restricciones de integridad.

| Nivel | Alcance habitual | Ejemplo |
|---|---|---|
| Unitaria | Regla o componente delimitado | Decisión de rechazo según condiciones definidas |
| Integración | Interacción de componentes | Modelo Django y restricción PostgreSQL |
| Sistema | Comportamiento de la aplicación integrada | Registrar y consultar una postulación |
| Aceptación | Adecuación a criterios y necesidades de usuarios | El actor interpreta el estado y completa su tarea |

El alcance define el nivel; el nombre del archivo de prueba no lo determina. La técnica de caja negra deriva casos del comportamiento especificado. La caja blanca utiliza conocimiento de la estructura interna. Ambas pueden aportar evidencia complementaria.

## TDD y suite de regresión

En TDD se escribe una prueba que falle por el comportamiento aún ausente, se implementa lo mínimo y se refactoriza manteniendo las pruebas aprobadas. Un fallo de importación o de conexión no demuestra por sí mismo que la regla de negocio esté ausente.

La suite de regresión ayuda a detectar cambios que rompen comportamientos previos. Ejecutarla localmente y en GitHub Actions facilita reproducir resultados. Una ejecución de CI aprobada no prueba que el sistema completo satisfaga todas las necesidades.

## Registrar un defecto

Identificar versión, entorno, precondiciones, pasos, resultado esperado y observado. Clasificar el impacto y enlazar la corrección. Evitar capturas aisladas sin contexto y credenciales o datos personales en logs.

Una corrección necesita volver a comprobar el caso y los comportamientos relacionados. Conservar el commit presentado y los posteriores de corrección mantiene trazabilidad.

## Tipos de mantenimiento

| Tipo | Propósito | Ejemplo |
|---|---|---|
| Correctivo | Resolver un defecto | Impedir postulaciones duplicadas |
| Adaptativo | Responder a cambios del entorno | Ajustar compatibilidad al actualizar una dependencia |
| Perfectivo | Mejorar funciones, rendimiento o facilidad de uso | Simplificar una consulta frecuente sin cambiar su objetivo |

Un cambio puede involucrar varias motivaciones. Documentar el motivo concreto y su alcance es más útil que aplicar una etiqueta sin explicación.

## Documentación de E8

El manual técnico debe permitir preparar y operar la versión: dependencias, configuración, migraciones, pruebas y tratamiento de errores. El manual de usuario explica tareas, estados y mensajes desde la perspectiva del actor. El registro de cambios relaciona versiones y modificaciones; el plan de mantenimiento explica qué se conserva y cómo se revisa.

Leer el [ejemplo de prueba y defecto](ejemplo-pruebas-mantenimiento.md), preparar [E7](../../proyecto-integrador/entregables/e07.md) y mantener la documentación de [E8](../../proyecto-integrador/entregables/e08.md).

[Lecturas del Tema VI](../../recursos/bibliografia.md#tema-6) · [Unidad VI](README.md)
