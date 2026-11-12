# Bibliografía y recursos por tema

Este índice reúne bibliografía básica, bibliografía complementaria, recursos de libre consulta y documentación técnica. Las lecturas apoyan exclusivamente los [entregables E1–E8](../proyecto-integrador/entregables/README.md); no generan nuevas actividades ni porcentajes de evaluación.

Los libros son comerciales: una ficha editorial no da acceso gratuito al texto completo. «Libre consulta» describe el acceso al recurso enlazado, no una licencia abierta para redistribuirlo. No se incluyen copias no autorizadas ni imágenes de portadas con atribución dudosa.

## Selección prioritaria

| Tema | Lectura central | Recurso práctico | Entregable |
|---|---|---|---|
| [I](#tema-1) | Kendall, caps. 1–3; cap. 6 para agilidad | Guía Scrum | E1 |
| [II](#tema-2) | Kendall, cap. 7 | Mermaid, con IBM DFD como apoyo | E2 |
| [III](#tema-3) | Kendall, caps. 8–9 | Diccionario DFD y documentación de restricciones | E3–E4 |
| [IV](#tema-4) | Kendall, caps. 11–12 y 14 | Figma y W3C | E5 |
| [V](#tema-5) | Elmasri y Navathe; Kendall, cap. 13 | PostgreSQL y Mermaid ER | E6 |
| [VI](#tema-6) | Kendall, cap. 16; ISTQB CTFL 4.0.1 | Django, pytest y pytest-django | E7–E8 |

## Bibliografía fundamental

### Texto principal verificado

Kendall, K. E., y Kendall, J. E. *Systems Analysis and Design* (11.ª ed.). Pearson. Publicación: 2023; copyright: 2024. ISBN de la edición impresa estadounidense: **9780137947805**; eText: **9780137947850**. [Ficha oficial e índice de capítulos de Pearson](https://www.pearson.com/en-us/subject-catalog/p/systems-analysis-and-design/P200000009877). **Libro comercial en inglés.**

La numeración de capítulos de este índice se comprobó en esa edición inglesa. El programa cita el título en español; no se presume que exista una traducción con el mismo año, ISBN o paginación. La numeración de páginas debe corresponder a la edición consultada.

### Texto complementario de análisis y diseño

Valacich, J. S., y George, J. F. *Modern Systems Analysis and Design* (8.ª ed., Global Edition). Pearson. ISBN impreso: **9781292154145**. [Catálogo oficial de Pearson con edición, autores e ISBN](https://www.pearson.com/content/dam/one-dot-com/one-dot-com/apac/japan/catalog/2019-hed-catalog.pdf). **Libro comercial; el catálogo es de libre consulta.**

El catálogo identifica esta edición con Valacich y George. La atribución «Hoffer, Ramesh y Topi» del programa no corresponde a esa ficha y difiere de la ficha del catálogo editorial; el listado del programa se reproduce más abajo para identificar la diferencia. No se utiliza la portada de otra obra como identificación bibliográfica.

### Obras originales del programa

Se conservan las nueve referencias originales. Salvo las verificaciones señaladas arriba, el listado conserva los datos del programa tal como aparecen en su bibliografía. La conservación de una referencia no confirma que todos sus datos sean correctos.

1. Kendall, K. & Kendall, J. Análisis y Diseño de Sistemas. 11ª ed. Pearson.
2. Whitten, J.; Bentley, L. & Dittman, K. Análisis, Diseño e Implementación de Sistemas. 7ª ed. McGraw-Hill.
3. Hoffer, J.; Ramesh, V. & Topi, H. Modern Systems Analysis and Design. 8ª ed. Pearson.
4. Senn, J. Análisis y Diseño de Sistemas de Información. 2ª ed. McGraw-Hill.
5. Laudon, K. & Laudon, J. Sistemas de Información Gerencial. 16ª ed. Pearson.
6. O’Brien, J. & Marakas, G. Sistemas de Información Gerencial. 10ª ed. McGraw- Hill.
7. Elmasri, R. & Navathe, S. Fundamentos de Sistemas de Bases de Datos. 7ª ed. Pearson.
8. Stair, R. & Reynolds, G. Principios de Sistemas de Información. 14ª ed. Cengage.
9. Pérez López, J. Sistemas de Información para la Gestión. Ed. Pirámide.

<a id="tema-1"></a>

## Tema 1. Introducción a los Sistemas de Información

Sistemas, clasificación, ciclo de vida y metodologías ágiles.

### Bibliografía académica

**Básica:** Kendall y Kendall, capítulos 1–3 y 6. **Complementaria:** Laudon y Laudon; Stair y Reynolds, para fundamentos organizacionales y toma de decisiones.

### Recursos de apoyo

| Recurso | Tipo de acceso | Aplicación académica |
|---|---|---|
| [IBM · Information Systems](https://www.ibm.com/think/topics/information-systems) | Recurso de libre consulta | Conceptos y función organizacional de los SI. |
| [Guía Scrum oficial](https://scrumguides.org/download.html) | Guía de libre consulta; versión española disponible | Scrum, responsabilidades, eventos y artefactos. |
| [Kanban University · Kanban Guide](https://kanban.university/kanban-guide/) | Guía de libre consulta | Visualización y gestión del flujo; guía de Kanban University. |

**Aplicación al proyecto:** Caracterizar el sistema, actores, necesidades, requisitos, objetivos y alcance. **E1.**

<a id="tema-2"></a>

## Tema 2. Modelado de Sistemas mediante DFD

Modelado estructurado, procesos, flujos, almacenes, entidades externas y niveles de descomposición.

### Bibliografía académica

**Básica:** Kendall y Kendall, capítulo 7: *Using Data Flow Diagrams*. **Complementaria:** Senn, *Análisis y Diseño de Sistemas de Información*, para el enfoque estructurado.

### Recursos y herramientas

| Recurso | Aplicación académica |
|---|---|
| [Mermaid · Flowcharts](https://mermaid.js.org/syntax/flowchart.html) | Herramienta principal: construcción textual de DFD mediante convenciones explícitas de procesos, entidades, almacenes y flujos. |
| [Mermaid Live Editor](https://mermaid.live/) | Escritura, previsualización y corrección del código. |
| [GitHub · Creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | Bloques Mermaid dentro de archivos Markdown. |
| [IBM · Data Flow Diagram](https://www.ibm.com/think/topics/data-flow-diagram) | Referencia conceptual sobre componentes y reglas de conexión. |
| [diagrams.net](https://www.drawio.com/) | Herramienta gráfica complementaria para comparar métodos de modelado. |
| [Lucidchart · Data Flow Diagram](https://www.lucidchart.com/pages/data-flow-diagram) | Recurso adicional con ejemplos visuales; herramienta con planes comerciales. |

### Aplicación al proyecto integrador · E2

Desarrollar contexto, nivel 1 y nivel 2, con al menos un proceso descompuesto a nivel 2; comprobar balance y consistencia de flujos. Los diagramas se documentan en Markdown con bloques Mermaid, conservando código y representación visual en GitHub.

Ejemplo simplificado del sistema de gestión de pasantías. Mermaid utiliza diagramas de flujo generales; la notación DFD deberá definirse explícitamente mediante convenciones de formas, nombres y conexiones.

La [Unidad II](../unidades/02-modelado-dfd/README.md) reúne la imagen aportada, las convenciones y un ejemplo de código corregido. Mermaid queda estandarizado como herramienta principal para los DFD, coherente con Markdown, Git y GitHub.

<a id="tema-3"></a>

## Tema 3. Diccionario de Datos y Especificación de Procesos

Diccionarios, metadatos, reglas de negocio y decisiones estructuradas.

### Bibliografía académica

**Básica:** Kendall y Kendall, capítulos 8–9. **Complementaria:** Whitten, Bentley y Dittman; consultar el listado bibliográfico del programa.

### Recursos de apoyo

| Recurso | Tipo de acceso | Aplicación académica |
|---|---|---|
| [IBM · Data Dictionary](https://www.ibm.com/think/topics/data-dictionary) | Recurso de libre consulta | Conceptos de documentación y diccionarios de datos. |
| [OMG · Decision Model and Notation](https://www.omg.org/spec/DMN/) | Especificación de libre consulta; profundización opcional | Formalización de decisiones; no se exige implementar DMN. |
| [PostgreSQL · Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) | Documentación técnica | Anticipar restricciones de la futura BD; no sustituye al diccionario lógico del DFD. |

**Aplicación al proyecto:** Documentar flujos, almacenes y elementos en **E3**, y procesos primitivos, reglas y tablas de decisión en **E4**. Distinguir el diccionario DFD del diccionario de BD de E6.

<a id="tema-4"></a>

## Tema 4. Diseño de Entradas y Salidas

Formularios, validaciones, reportes, usabilidad y prototipos.

### Bibliografía académica

**Básica:** Kendall y Kendall, capítulos 11–12 y 14.

### Recursos de apoyo

| Recurso | Tipo de acceso | Aplicación académica |
|---|---|---|
| [Nielsen Norman Group · 10 heurísticas de usabilidad](https://www.nngroup.com/articles/ten-usability-heuristics/) | Artículo de libre consulta | Criterios para revisar la usabilidad del prototipo. |
| [W3C WAI · Forms Tutorial](https://www.w3.org/WAI/tutorials/forms/) | Tutorial de libre consulta | Etiquetas, instrucciones, agrupación y validación accesible. |
| [Figma · Centro de ayuda](https://help.figma.com/) | Documentación técnica; funcionalidades según plan | Wireframes y prototipos navegables. |
| [Django · Working with forms](https://docs.djangoproject.com/en/5.2/topics/forms/) | Documentación técnica, versión 5.2 | Construcción y validación de formularios al implementar el diseño. |

**Aplicación al proyecto:** Diseñar entradas, consultas y reportes en **E5**. Revisar los mensajes y las necesidades del usuario; la implementación en Django se integra posteriormente en E7.

<a id="tema-5"></a>

## Tema 5. Diseño de Bases de Datos para Sistemas de Información

ER, normalización hasta 3FN, modelo relacional, SQL e introducción a NoSQL.

### Bibliografía académica

**Básica:** Elmasri y Navathe, modelado ER y normalización; Kendall y Kendall, capítulo 13. **Complementaria:** Valacich y George, *Modern Systems Analysis and Design*, para el diseño de BD.

### Recursos de apoyo

| Recurso | Tipo de acceso | Aplicación académica |
|---|---|---|
| [PostgreSQL · Tutorial](https://www.postgresql.org/docs/current/tutorial.html) | Documentación técnica | Introducción a las bases de datos relacionales. |
| [PostgreSQL · Data Definition](https://www.postgresql.org/docs/current/ddl.html) | Documentación técnica | Tablas, tipos, claves y restricciones. |
| [PostgreSQL · SQL Language](https://www.postgresql.org/docs/current/sql.html) | Documentación técnica | Definición, consulta y manipulación de datos. |
| [Mermaid · Entity Relationship Diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) | Documentación técnica | Representación y documentación del modelo ER. |
| [MongoDB · NoSQL Explained](https://www.mongodb.com/resources/basics/databases/nosql-explained) | Recurso de libre consulta; profundización conceptual | Introducción a NoSQL; no cambia la BD PostgreSQL del proyecto. |

**Aplicación al proyecto:** Producir ER, cardinalidades, normalización, esquema relacional, scripts SQL y diccionario de BD. **E6.**

<a id="tema-6"></a>

## Tema 6. Pruebas y Mantenimiento de Sistemas

Pruebas unitarias, integración, sistema, aceptación, mantenimiento y documentación.

### Bibliografía académica

**Básica:** Kendall y Kendall, capítulo 16. **Complementaria:** Whitten, Bentley y Dittman; ISTQB, *Certified Tester Foundation Level Syllabus*, versión 4.0.1.

### Recursos de apoyo

| Recurso | Tipo de acceso | Aplicación académica |
|---|---|---|
| [ISTQB · CTFL Syllabus 4.0.1 (PDF)](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) | Programa de libre consulta | Terminología, niveles y técnicas de pruebas; no requiere rendir certificación. |
| [pytest · Documentación](https://docs.pytest.org/en/stable/) | Documentación técnica | Pruebas automatizadas Python. |
| [pytest-django · Documentación](https://pytest-django.readthedocs.io/en/latest/) | Documentación técnica | Configuración y pruebas de BD para Django. |
| [Django · Testing](https://docs.djangoproject.com/en/5.2/topics/testing/) | Documentación técnica, versión 5.2 | Pruebas de aplicaciones Django. |
| [GitHub Actions](https://docs.github.com/en/actions) | Documentación técnica | Ejecución automática de pruebas. |
| [OWASP · Web Security Testing Guide](https://wstg.owasp.org/) | Guía de libre consulta; profundización opcional | Comprobaciones básicas de seguridad en entornos de prueba autorizados. |
| [GitHub · Repositories](https://docs.github.com/en/repositories) | Documentación técnica | Historial, repositorios y gestión de cambios. |

**Aplicación al proyecto:** Integrar la aplicación, ejecutar pruebas y registrar defectos en **E7**; documentar versiones, mantenimiento y manuales en **E8**.

<a id="enfoques-ingenieria"></a>

## Enfoques contemporáneos de ingeniería de software

Lecturas transversales para las [prácticas y estrategias del proyecto](../docs/enfoques-ingenieria.md). Complementan el programa y las evidencias E1–E8, sin crear evaluaciones adicionales.

| Enfoque | Referencia | Acceso y uso académico |
|---|---|---|
| SDD | [GitHub Spec Kit · Documentación oficial](https://github.github.com/spec-kit/) | Libre consulta. Ejemplo de desarrollo guiado por especificaciones; no requiere instalar Spec Kit ni usar agentes en el curso. |
| DDD | [Martin Fowler · Ubiquitous Language](https://martinfowler.com/bliki/UbiquitousLanguage.html) | Artículo de libre consulta. Lenguaje compartido entre desarrolladores y actores del dominio. |
| DDD | [Martin Fowler · Bounded Context](https://martinfowler.com/bliki/BoundedContext.html) | Artículo de libre consulta. Profundización sobre límites de significado; no obliga a adoptar microservicios o una arquitectura DDD completa. |
| TDD | [Kent Beck · Test-Driven Development: By Example](https://www.oreilly.com/library/view/test-driven-development/0321146530/) | Libro comercial, ficha y acceso según suscripción. Prueba que falla, implementación mínima y refactorización. |
| V&V | [ISTQB · Certified Tester Foundation Level](https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/) | Página oficial y materiales de consulta. Fundamentos y terminología de pruebas; no se exige certificación. |
| VDD: lectura crítica | [Verification-Driven Delivery Methodology](https://vdd-methodology.org/) | Propuesta particular emergente, no estándar del curso. Utiliza «Delivery», mientras PP4 define VDD operativamente como «Verification-Driven Development». No se equiparan sus alcances. |

La verificación y la validación fundamentan las revisiones de todos los entregables. Los recursos opcionales amplían la lectura y no incorporan nuevos frameworks obligatorios.

## Uso de versiones y acceso

Las rutas `current`, `stable` y `latest` pueden cambiar con el tiempo. Los enlaces Django 5.2 se conservan como referencia explícita de la selección docente: cada equipo debe consultar la versión que corresponda a su instalación. No se impone una versión nueva por añadir bibliografía.

Fecha de revisión de enlaces: 12 de noviembre de 2026. Ningún recurso opcional incorpora nuevos frameworks obligatorios o entregables.

[Herramientas](herramientas.md) · [Recursos](README.md) · [Inicio](../README.md)
