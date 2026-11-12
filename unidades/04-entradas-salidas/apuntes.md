# Unidad IV · Diseñar entradas y salidas para el usuario

## De una necesidad a una interacción

El diseño de entradas y salidas relaciona requisitos, datos y tareas. Un formulario recoge información necesaria para un proceso; un reporte permite responder una pregunta. La apariencia visual ayuda a comunicar, pero no reemplaza reglas, permisos o datos correctos.

Distinguir **UI**, los elementos con los que se interactúa, de **UX**, la experiencia al realizar una tarea. Una pantalla puede verse ordenada y aun así no explicar si una solicitud quedó registrada o por qué fue rechazada.

## Diseñar entradas

Identificar actor, propósito, datos de entrada, formato, validaciones y resultado. Utilizar etiquetas explícitas y mensajes que expliquen cómo resolver el problema. No depender únicamente de colores para indicar errores.

La validación en el navegador facilita la interacción; el servidor debe volver a verificar los datos y la autorización. Deshabilitar un botón no protege una operación frente a una solicitud construida directamente.

## Diseñar salidas

Un reporte debe indicar a quién sirve, qué pregunta responde, qué datos muestra, cómo se filtra y qué permisos requiere. Distinguir «sin resultados» de «no autorizado» y de «error de consulta» sin revelar información privada.

La exportación debe conservar el significado de campos y filtros. Una descarga no autoriza por sí misma a compartir datos. En el proyecto docente, usar datos sintéticos para demostrar el comportamiento.

## Prototipar y validar en Figma

Representar el recorrido de la tarea, no solo su pantalla inicial. Mostrar estados relevantes: inicio, entrada inválida, confirmación y ausencia de resultados. Las variantes documentan decisiones de E5; no son entregas adicionales.

Contrastar el prototipo con el actor y requisito correspondiente. Pedir a la persona que explique qué haría y qué interpreta del resultado permite observar problemas de comprensión. Registrar el escenario y los hallazgos; si la revisión es simulada, identificarla como tal.

La accesibilidad del prototipo no garantiza la del HTML final. Al implementar, revisar etiquetas, foco, teclado, mensajes y contraste. Consultar las guías W3C de la bibliografía.

Leer el [ejemplo de formulario y reporte](ejemplo-entradas-salidas.md) y preparar [E5](../../proyecto-integrador/entregables/e05.md).

[Lecturas del Tema IV](../../recursos/bibliografia.md#tema-4) · [Unidad IV](README.md)
