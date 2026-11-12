# L5. Modelo relacional y SQL

**Propuesta complementaria** · [Unidad 5](../unidades/unidad-05/README.md) · Apoya E6.

## Requisitos

PostgreSQL, pgAdmin y un modelo ER del dominio.

## Caso de práctica

Mini caso sintético: organizaciones y ofertas; una organización tiene muchas ofertas.

## Procedimiento

1. Crear el ER e identificar cardinalidades y claves.
2. Describir dependencias funcionales y justificar 1FN, 2FN y 3FN.
3. Abrir una BD local de práctica y ejecutar el SQL siguiente dentro de una transacción.
4. Insertar una organización y una oferta; consultar su unión. Intentar una oferta con organización inexistente y registrar el rechazo de la clave foránea.
5. Ejecutar ROLLBACK para dejar la BD sin cambios; redactar el diccionario BD.

```sql
BEGIN;
CREATE TABLE organizacion (
  id integer PRIMARY KEY,
  nombre varchar(120) NOT NULL
);
CREATE TABLE oferta (
  id integer PRIMARY KEY,
  organizacion_id integer NOT NULL REFERENCES organizacion(id),
  descripcion text NOT NULL
);
INSERT INTO organizacion VALUES (1, 'Organización de prueba');
INSERT INTO oferta VALUES (1, 1, 'Oferta sintética');
SELECT o.descripcion, g.nombre FROM oferta o
JOIN organizacion g ON g.id = o.organizacion_id;
-- Debe fallar: organización 99 inexistente.
INSERT INTO oferta VALUES (2, 99, 'Referencia inválida');
ROLLBACK;
```


## Evidencia propuesta

ER, justificación, SQL y evidencia de consulta/restricción.

## Comprobación y resultado esperado

La unión devuelve la organización de la oferta y una referencia inexistente falla. No quedan tablas al terminar la transacción.

## Dificultades frecuentes

Tras el error esperado, PostgreSQL exige ROLLBACK; volver a iniciar la transacción para repetir el ejercicio.

[Recursos](../recursos/herramientas.md) · [Entregables](../proyecto-integrador/entregables/README.md) · [Laboratorios](README.md)
