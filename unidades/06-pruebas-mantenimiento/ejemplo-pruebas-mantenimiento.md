# Ejemplo · Verificar un duplicado y documentar su corrección

Se utiliza la regla hipotética de una postulación por par estudiante–oferta. Este ejemplo relaciona las evidencias de E6, E7 y E8; no constituye otra entrega.

## Casos derivados de la regla

| Caso | Preparación | Resultado esperado |
|---|---|---|
| Primera postulación | Estudiante y oferta válidos sin relación previa | Crear una fila y comunicar registro |
| Duplicado | Ya existe el mismo par estudiante–oferta | Rechazar y mantener una sola fila |
| Otra oferta | Mismo estudiante y una oferta diferente válida | Permitir la nueva relación |
| Referencia inválida | Oferta inexistente | Rechazar sin crear una fila huérfana |

El estado de la BD es parte del resultado. Si el mensaje indica rechazo pero existe una segunda fila, la regla no se cumple.

## Recorrido TDD

Comenzar por la prueba del comportamiento del duplicado en el modelo o servicio elegido. Confirmar que el fallo expresa la ausencia de la regla, no un error de preparación. Implementar la restricción y el tratamiento del rechazo; ejecutar la prueba y los casos válidos. Refactorizar y repetir la suite.

En una prueba de integridad PostgreSQL, capturar el error dentro de un bloque transaccional adecuado permite continuar las comprobaciones. Un error de integridad puede dejar una transacción inutilizable hasta su rollback; una prueba que ignora esto puede fallar por el entorno transaccional y no por la regla.

La [guía de entorno](../../docs/entorno.md) muestra la configuración de pytest-django y una comprobación mínima de BD. Esa comprobación acredita conectividad y escritura, no la implementación del proyecto ni esta regla de negocio.

## Registro de defecto del ejemplo

| Campo | Contenido ilustrativo |
|---|---|
| Identificación | DEF-01 · Duplicado de postulación |
| Precondición | Existe una postulación de estudiante 1 a oferta 10 |
| Pasos | Volver a solicitar el registro del mismo par |
| Esperado | Rechazo y una sola fila |
| Observado | Se crean dos filas |
| Impacto | La consulta y los conteos contienen duplicados |
| Corrección | Restricción única y tratamiento del error en la operación |
| Revisión | Repetir duplicado, primera postulación y otra oferta |

El equipo sustituye el contenido ilustrativo por las versiones, resultados y enlaces reales de su proyecto. No afirmar que se corrigió un defecto sin conservar su evidencia.

## Actualización de E8

Registrar la corrección y la migración correspondiente; explicar el comportamiento en el manual de usuario y las instrucciones de actualización en el manual técnico. Una BD con duplicados previos puede impedir aplicar la restricción: analizar y resolver esos datos antes de migrar, sin borrarlos arbitrariamente.

[Apuntes](apuntes.md) · [Unidad VI](README.md)
