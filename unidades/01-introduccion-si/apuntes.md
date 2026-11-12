# Unidad I · Sistemas de información y desarrollo

## Propósito de estudio

Comprender qué transforma un sistema de información, a quién sirve y cómo se organiza su desarrollo. Esta base permite delimitar el proyecto antes de diseñar pantallas, diagramas o tablas.

## Sistema, datos e información

Un **sistema** es un conjunto de elementos relacionados que actúan dentro de una frontera y con un propósito. Para describirlo se identifican sus entradas, transformaciones, salidas y relaciones con el entorno.

Los **datos** representan hechos registrados: una fecha, un código de oferta o el estado de una solicitud. La **información** surge cuando esos datos se interpretan en un contexto para responder una pregunta. El número de postulaciones por oferta informa sobre la demanda; una lista de códigos sin significado para el usuario no responde por sí sola a esa necesidad.

Un **sistema de información** articula personas, procedimientos, datos y tecnología para obtener, procesar, conservar y comunicar información. Una aplicación web es uno de sus componentes. Diseñar el software exige comprender también quién registra datos, quién puede decidir y qué reglas gobiernan el proceso.

## Frontera, entradas y salidas

En la gestión de pasantías, una oferta publicada y una solicitud estudiantil son datos distintos. Registrar una solicitud no equivale a aprobar una pasantía. La frontera del sistema permite decidir qué responsabilidades pertenecen a la aplicación y cuáles corresponden a actores externos.

| Pregunta de análisis | Ejemplo en pasantías |
|---|---|
| ¿Quién interactúa? | Estudiante, empresa, coordinación y tutor académico |
| ¿Qué recibe el sistema? | Datos de oferta y solicitud de postulación |
| ¿Qué transforma o conserva? | Registro de postulaciones y sus estados |
| ¿Qué comunica? | Confirmación de registro y consultas autorizadas |
| ¿Qué queda fuera? | Las funciones excluidas del alcance acordado en E1 |

La última fila se define para cada proyecto; no debe convertirse en una exclusión institucional sin analizar el dominio.

## Tipos de sistemas de información

Las categorías describen el uso principal de la información; una misma solución puede incluir funciones de varias categorías.

| Tipo | Finalidad | Ejemplo |
|---|---|---|
| Transaccional | Registrar operaciones del trabajo cotidiano | Registrar una postulación y consultar su estado |
| De apoyo a decisiones | Organizar y analizar datos para comparar alternativas | Examinar demanda de ofertas por área y período |
| Estratégico | Apoyar objetivos y decisiones de largo alcance | Analizar tendencias para orientar convenios académicos |

Un gráfico no convierte automáticamente una aplicación en un sistema de apoyo a decisiones: debe responder a una necesidad concreta de un actor y contar con datos adecuados. Un reporte operativo tampoco es estratégico solo por dirigirse a una autoridad.

## Ciclo de vida del sistema

El ciclo de vida permite relacionar necesidades, diseño, construcción y evolución. No exige que toda solución avance una única vez por una secuencia rígida.

| Trabajo | Pregunta central | Relación con PP4 |
|---|---|---|
| Identificar y analizar | ¿Qué problema se atiende y qué necesita cada actor? | E1 y E2 |
| Especificar y diseñar | ¿Cómo se describen procesos, datos e interfaces? | E3–E6 |
| Implementar y verificar | ¿La solución realiza lo requerido y con qué evidencia? | E7 |
| Documentar y mantener | ¿Cómo se utiliza, modifica y conserva? | E8 |

Un cambio en una regla puede exigir revisar requisitos, DFD, diccionarios, interfaz, BD y pruebas. Esa relación entre evidencias se denomina trazabilidad. Los entregables organizan el trabajo académico, pero no convierten las fases del ciclo de vida en compartimentos aislados.

## Scrum y Kanban

Scrum y Kanban ayudan a organizar trabajo y aprendizaje; no sustituyen el análisis del sistema ni son tipos de sistemas de información.

| Aspecto | Scrum | Método Kanban |
|---|---|---|
| Organización | Marco con responsabilidades, eventos y artefactos definidos | Método de gestión aplicado al flujo de trabajo existente |
| Atención principal | Inspeccionar y adaptar resultados en Sprints | Visualizar y mejorar el flujo, limitando trabajo en curso |
| Aplicación al equipo | Ordenar trabajo hacia un objetivo y revisar el incremento | Hacer visibles bloqueos y capacidad antes de iniciar más trabajo |

Un tablero con columnas no equivale por sí solo a aplicar Scrum o Kanban. En E1, describir cómo se organiza el equipo, cómo se prioriza, cómo se revisan resultados y cómo se atienden cambios. Utilizar el término «Sprint» para una evaluación del curso no demuestra, por sí mismo, que el equipo aplique todo Scrum.

## De los conceptos a E1

La caracterización debe relacionar problema, justificación, objetivos, alcance, actores, requisitos y reglas de negocio. Una tecnología responde a una decisión de implementación; no reemplaza la formulación del problema. «Usar Django» no explica qué necesidad institucional se resuelve.

Consultar el [ejemplo de caracterización](ejemplo-caracterizacion.md) y elaborar la [entrega E1](../../proyecto-integrador/entregables/e01.md) sobre el proyecto asignado. El ejemplo es material de estudio, no una entrega adicional.

## Lecturas

- [Bibliografía del Tema I](../../recursos/bibliografia.md#tema-1): Kendall y Kendall, capítulos 1–3 y 6; textos complementarios de sistemas de información.
- [Guía Scrum, versión española de noviembre de 2020](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-Spanish-European.pdf): marco, responsabilidades, eventos y artefactos.
- [Guía del método Kanban de Kanban University](https://kanban.university/kanban-guide/): gestión del flujo y prácticas del método.

[Unidad I](README.md) · [Inicio](../../README.md)
