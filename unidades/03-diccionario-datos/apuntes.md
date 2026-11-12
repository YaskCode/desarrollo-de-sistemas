# Unidad III · Datos y procesos sin ambigüedad

## Del diagrama a una definición verificable

Un DFD nombra flujos y almacenes; el diccionario explica su contenido. Si dos documentos usan «solicitud» con significados diferentes, el equipo no comparte una especificación aunque ambos diagramas se vean correctos.

En E3 se definen flujos, almacenes, estructuras y elementos. Un flujo puede transportar una estructura compuesta; un almacén conserva colecciones de estructuras. Cada elemento necesita significado, tipo, dominio y restricciones. Un identificador entero positivo no equivale a cualquier entero; un estado necesita valores definidos.

## Metadatos y consistencia

Los metadatos describen los datos: nombre, definición, fuente, composición, tipo, dominio y reglas. Mantener identificadores estables facilita relacionar DFD, procesos, tablas y pruebas sin depender de nombres parecidos.

No documentar datos sensibles reales como ejemplos. Describir su naturaleza y utilizar valores sintéticos. Una definición de dato debe permitir distinguir qué representa, quién lo proporciona y qué condiciones lo hacen válido.

## E3 y E6: dos vistas diferentes

| Vista | Qué explica | Ejemplo |
|---|---|---|
| Diccionario DFD, E3 | Datos que circulan y se conservan lógicamente | Solicitud de postulación: estudiante y oferta |
| Diccionario BD, E6 | Tablas, columnas, claves y restricciones físicas o lógicas del esquema | postulacion.estudiante_id: clave foránea |

Puede existir trazabilidad entre ambas vistas, pero no correspondencia uno a uno: un flujo puede reunir datos de varias tablas y una tabla puede servir a varios procesos.

## Especificar un proceso primitivo

E4 explica qué hace un proceso que ya no se descompone en el DFD presentado. Identificar entradas, precondiciones, reglas, pasos, salidas y excepciones. Las reglas deben permitir determinar el resultado sin depender de una interpretación informal del programador.

El lenguaje estructurado expresa decisiones y operaciones con claridad. Una tabla de decisión organiza combinaciones de condiciones y acciones. No es necesario repetir la misma regla en varias representaciones si eso introduce contradicciones.

## Revisar decisiones

Las condiciones relevantes deben cubrir los casos válidos y los rechazos. Si dos filas se pueden aplicar al mismo caso y producen acciones incompatibles, revisar la regla. Si ninguna fila se aplica a una combinación posible, falta definir el comportamiento.

Consultar el [ejemplo de diccionario y especificación](ejemplo-datos-procesos.md). Completar [E3](../../proyecto-integrador/entregables/e03.md) y [E4](../../proyecto-integrador/entregables/e04.md) para los procesos del proyecto propio.

[Lecturas del Tema III](../../recursos/bibliografia.md#tema-3) · [Unidad III](README.md)
