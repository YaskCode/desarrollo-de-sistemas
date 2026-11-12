# Unidad II · Modelar transformaciones de datos

## Qué describe un DFD

Un diagrama de flujo de datos representa de dónde vienen los datos, cómo se transforman, dónde se conservan y a quién se comunican. No representa el orden de las instrucciones de un programa ni el recorrido de una pantalla.

Un proceso recibe datos y produce otros con significado para el sistema. Una entidad externa origina o recibe datos desde fuera de la frontera; un almacén conserva información utilizada por los procesos. Los flujos se nombran como datos: «Solicitud de postulación», en lugar de «Hacer clic».

## Elegir componentes

| Componente | Pregunta | Ejemplo |
|---|---|---|
| Entidad externa | ¿Quién origina o recibe información? | Estudiante |
| Proceso | ¿Qué transformación ocurre? | 1.0 Registrar postulación |
| Flujo | ¿Qué datos se transfieren? | Solicitud de postulación |
| Almacén | ¿Qué información persiste? | D1: Postulaciones |

Las formas y conexiones se documentan con las [convenciones Mermaid del curso](README.md). Un diagrama que se dibuja correctamente puede seguir teniendo errores de modelado.

## Contexto y descomposición

El contexto muestra el sistema como un proceso y sus intercambios con entidades externas. Los almacenes internos aparecen al descomponerlo, no como entidades externas del contexto.

En el nivel 1 se distinguen las transformaciones principales. El nivel 2 detalla un proceso seleccionado. Los identificadores 1.1, 1.2 y 1.3 indican pertenencia a la descomposición de 1.0; no expresan por sí solos una secuencia temporal.

El **balance** conserva los datos que cruzan la frontera del proceso entre el padre y sus hijos. No obliga a conservar el mismo número de flechas internas. Si un flujo se divide, el diccionario debe permitir reconstruir su composición y comprobar equivalencia.

## Revisar el modelo

Comprobar que cada proceso tenga entradas y salidas justificadas, que sus resultados puedan obtenerse con los datos y reglas disponibles y que toda lectura o escritura de un almacén pase por un proceso. Una entidad no consulta directamente un almacén en el DFD.

Evitar procesos que solo reciben sin producir resultado, que producen datos sin entradas suficientes o que no transforman nada identificable. Evitar agregar una salida en nivel 2 que no exista en la frontera del padre: puede revelar un requisito omitido que debe revisarse en E1 y en los niveles superiores.

## Trabajo sobre E2

Leer el [ejemplo de descomposición](ejemplo-dfd.md), trasladar la técnica al alcance propio y mantener correspondencia con E1. Verificar con una tabla de frontera antes de presentar [E2](../../proyecto-integrador/entregables/e02.md).

[Lecturas del Tema II](../../recursos/bibliografia.md#tema-2) · [Unidad II](README.md)
