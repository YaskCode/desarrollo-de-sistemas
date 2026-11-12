# Unidad V · Del dominio al esquema de base de datos

## Tres vistas del diseño

El modelo conceptual ER describe entidades, relaciones y cardinalidades. El esquema relacional expresa tablas, atributos y claves. Los scripts SQL implementan esas decisiones en PostgreSQL. E6 debe mantener la correspondencia entre las tres vistas.

Una entidad no se identifica únicamente porque aparezca como sustantivo en un enunciado. Analizar su identidad, datos y relaciones dentro del dominio. Una relación muchos a muchos puede transformarse en una tabla asociativa que también contenga datos propios de esa relación.

## Claves y cardinalidades

La clave primaria identifica cada fila. Una clave candidata puede expresarse como restricción única. Una clave foránea mantiene una referencia válida a otra tabla; no establece por sí sola todas las reglas del negocio.

Si toda postulación necesita estudiante y oferta, las referencias deben ser obligatorias. Tener una clave artificial `id` no impide duplicar el par estudiante–oferta: esa regla requiere otra restricción.

## Normalización y dependencias

La normalización analiza dependencias entre atributos, no solo la cantidad de tablas. En 1FN, evitar grupos repetidos y representar valores conforme al dominio de cada atributo. En 2FN, los atributos no primos no dependen de una parte propia de una clave candidata. En 3FN, para cada dependencia funcional no trivial X → A, X es superclave o A es un atributo primo.

En los casos introductorios habituales, esto ayuda a reconocer atributos que dependen de otra entidad y que se están repitiendo sin necesidad. La justificación debe declarar las claves y dependencias del caso; «cada tabla tiene id» no prueba 3FN.

## Restricciones y diccionario de BD

Documentar tipo, nulabilidad, dominio, valores predeterminados, claves y restricciones. `NOT NULL`, `CHECK`, `UNIQUE` y `FOREIGN KEY` responden a condiciones distintas. En PostgreSQL, un CHECK que produce valor desconocido por NULL no equivale a un rechazo; combinarlo con NOT NULL cuando el dato sea obligatorio.

Conservar los scripts reproducibles y utilizar una BD de prueba. Verificar tanto inserciones válidas como rechazos esperados, sin convertir errores previstos en una ejecución aparentemente exitosa.

## Introducción a NoSQL

NoSQL agrupa alternativas con modelos distintos, como documentos, clave–valor o grafos. Comparar sus usos no cambia la elección PostgreSQL del curso. Elegir almacenamiento exige considerar acceso, integridad, estructura y relaciones; no basta con afirmar que «NoSQL es más flexible».

Consultar el [ejemplo ER y SQL](ejemplo-base-datos.md) para preparar [E6](../../proyecto-integrador/entregables/e06.md).

[Lecturas del Tema V](../../recursos/bibliografia.md#tema-5) · [Unidad V](README.md)
