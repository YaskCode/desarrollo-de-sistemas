# L6. Pruebas y mantenimiento

**Propuesta complementaria** · [Unidad 6](../unidades/unidad-06/README.md) · Apoya E7 y E8.

## Requisitos

Aplicación Django del equipo, PostgreSQL de prueba, pytest y pytest-django; guía de entorno completada.

## Caso de práctica

Seleccionar un flujo ya implementado y un permiso de actor definido en E1.

## Procedimiento

1. Registrar el commit y las versiones; preparar datos sintéticos en una BD exclusiva de pruebas.
2. Crear un test unitario de una regla y un test de integración de persistencia; usar la marca django_db donde corresponda.
3. Añadir pruebas de solicitud con el cliente Django para usuario autorizado y no autorizado.
4. Ejecutar python -m pytest; registrar casos, resultados, entorno y defectos encontrados.
5. Recorrer el flujo completo como prueba de sistema y registrar aceptación contra requisitos; las pruebas de aceptación forman parte del tema VI.
6. Corregir un defecto, repetir su prueba y actualizar registro de cambios, manual técnico y manual de usuario.
7. Proponer un cambio correctivo, otro adaptativo y otro perfectivo; automatizar la suite en GitHub Actions cuando el equipo disponga de ella.

## Evidencia propuesta

Resultados de pruebas, registro de defectos, cambio trazable y manuales actualizados.

## Comprobación y resultado esperado

La suite reproduce el defecto antes de la corrección y lo detecta como resuelto después; un permiso indebido continúa rechazado.

## Dificultades frecuentes

No ejecutar pruebas contra una BD institucional ni confundir ausencia de pruebas con aprobación.

[Recursos](../recursos/herramientas.md) · [Entregables](../proyecto-integrador/entregables/README.md) · [Laboratorios](README.md)
