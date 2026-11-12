# Ejemplo de estudio · Caracterización de una postulación de pasantía

Este caso hipotético explica cómo relacionar componentes de E1. Se limita al registro y consulta de una postulación: no es una especificación completa del proyecto de pasantías ni una descripción de procedimientos oficiales de FEC-LUZ. Las reglas y los valores de prueba siguientes pertenecen únicamente al ejemplo.

## Problema y justificación

En el escenario del ejemplo, las solicitudes llegan por canales separados y no comparten un identificador único. El estudiante no puede consultar de forma consistente si su postulación quedó registrada; la coordinación necesita reunir la información para revisarla.

Centralizar el registro permitiría identificar cada solicitud y consultar su estado. Esta justificación explica la utilidad esperada; no demuestra una reducción de tiempos sin contar con mediciones.

## Objetivos y alcance

**Objetivo general:** facilitar el registro y la consulta trazable de postulaciones a ofertas de pasantía.

**Objetivos específicos:** identificar cada postulación, comunicar el resultado del registro y ofrecer consultas según el actor autorizado.

Para este fragmento del caso se incluyen ofertas previamente publicadas, registro de la solicitud y consulta. La publicación de ofertas, aprobación académica, tutoría y seguimiento se analizan en otras partes del proyecto completo. Esa delimitación reduce el ejemplo, no el alcance mínimo de la asignatura.

## Actores del fragmento

| Actor | Interacción |
|---|---|
| Estudiante | Consulta una oferta, registra una postulación y consulta sus propias solicitudes |
| Coordinación | Consulta postulaciones para su revisión |

La ficha del proyecto completo incluye también empresa y tutor académico. No deben desaparecer del análisis de E1 por no participar en este fragmento.

## Requisitos y reglas

| ID | Tipo | Enunciado del ejemplo | Comprobación |
|---|---|---|---|
| RF-01 | Funcional | El estudiante identificado puede registrar una postulación a una oferta publicada | El registro genera un identificador y una confirmación |
| RF-02 | Funcional | El estudiante puede consultar el estado de sus propias postulaciones | Una consulta autorizada muestra el identificador, oferta y estado |
| RF-03 | Funcional | La coordinación puede consultar las postulaciones de una oferta | La consulta devuelve las solicitudes asociadas a esa oferta |
| RNF-01 | No funcional: control de acceso | Las consultas de un estudiante solo exponen sus propias postulaciones | Una solicitud sobre la postulación de otra cuenta se rechaza sin exponer sus datos |
| RN-01 | Regla de negocio hipotética | Un estudiante no registra dos postulaciones a la misma oferta | Un segundo intento sobre el mismo par estudiante–oferta se rechaza |
| RN-02 | Regla de negocio hipotética | Registrar una postulación no representa su aprobación académica | La confirmación indica registro; no comunica asignación aprobada |

RF-02 describe una capacidad; RNF-01 exige una propiedad de seguridad de esa capacidad. RN-01 expresa una restricción del dominio que afecta al registro. No todos los requisitos no funcionales se expresan con un tiempo de respuesta; todos necesitan una comprobación verificable.

## Trazabilidad inicial

| Necesidad | Requisitos y reglas | Evidencia que se desarrollará en el proyecto |
|---|---|---|
| Saber que la solicitud quedó registrada | RF-01, RN-01 y RN-02 | E2: flujo de solicitud y confirmación; E3: estructura de postulación; E7: pruebas de registro y duplicado |
| Consultar el estado sin revelar datos ajenos | RF-02 y RNF-01 | E5: consulta y mensajes; E7: pruebas con dos cuentas distintas |
| Reunir solicitudes para revisión | RF-03 | E4: especificación de consulta; E6: relación entre oferta y postulación |

La tabla es parcial. El equipo debe mantener la correspondencia de todos los requisitos de su proyecto con los diseños y pruebas que elabore.

## Organización del trabajo del ejemplo

El equipo puede representar las tareas de caracterización en un tablero con estados «Por hacer», «En curso» y «Revisado». Registrar una tarea de alcance, otra de requisitos y otra de revisión cruzada facilita comprobar qué evidencia existe y qué falta.

La metodología de E1 debe describir las prácticas efectivamente utilizadas. Crear el tablero no basta para declarar que se aplica Scrum completo; para comprender las diferencias, consultar los [apuntes de la unidad](apuntes.md).

## Qué observar al leer el ejemplo

El problema se formula antes de elegir herramientas. Los objetivos responden al problema. El alcance distingue el fragmento estudiado del proyecto completo. Cada regla hipotética se identifica como tal y cada requisito tiene una forma de comprobación. La selección tecnológica del curso se utiliza al implementar, sin reemplazar el análisis.

Para presentar la caracterización del proyecto asignado, seguir la [ficha E1](../../proyecto-integrador/entregables/e01.md) y la [guía para estudiantes](../../docs/README.md).

[Unidad I](README.md) · [Bibliografía del Tema I](../../recursos/bibliografia.md#tema-1)
