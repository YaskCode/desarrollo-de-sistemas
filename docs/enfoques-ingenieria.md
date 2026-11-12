# Prácticas y estrategias de ingeniería de software

Estas estrategias se aplican dentro de las seis unidades y los entregables E1–E8. Permiten comprender el dominio, especificar comportamientos y comprobar resultados. No añaden unidades, entregables ni porcentajes al [plan de evaluación](evaluacion.md).

## Qué aporta cada enfoque

| Enfoque | Significado utilizado en PP4 | Aplicación |
|---|---|---|
| SDD | Specification-Driven Development: desarrollo guiado por especificaciones | Mantener requisitos, modelos, reglas y criterios verificables que orienten la implementación y sus cambios |
| DDD | Domain-Driven Design: diseño guiado por el dominio | Comprender conceptos, lenguaje y reglas con los actores del dominio; conservar su significado en los modelos y el software |
| TDD | Test-Driven Development: desarrollo guiado por pruebas | Desarrollar una regla mediante ciclos de prueba que falla, implementación mínima y refactorización |
| VDD | Verification-Driven Development: denominación operativa del curso para desarrollo guiado por verificación | Revisar modelos, decisiones y código contra criterios explícitos, conservando evidencias |

Son enfoques y prácticas complementarios, no cuatro metodologías completas que el equipo deba implantar en paralelo. En PP4 tienen mayor presencia la especificación y la verificación; DDD se introduce mediante el lenguaje y las reglas del dominio, y TDD se aplica a reglas concretas durante la implementación.

SDD no significa congelar todos los requisitos antes de escribir código. La especificación debe evolucionar con el aprendizaje y mantenerse coherente con el sistema. GitHub Spec Kit es una referencia de una implementación de SDD; su instalación y sus herramientas asociadas no son requisitos del curso.

El uso de VDD no es uniforme. Aquí se define explícitamente como desarrollo guiado por verificación. No debe confundirse con la propuesta externa denominada *Verification-Driven Delivery Methodology*. El fundamento académico del curso son los principios de verificación y validación (V&V), sin atribuir carácter de estándar a esa propuesta particular.

## Verificación y validación

La **verificación** contrasta una evidencia con una especificación o regla: balance de un DFD, correspondencia del diccionario, restricciones SQL o resultado de una prueba de permisos.

La **validación** contrasta la solución con el uso y las necesidades de sus usuarios: si un formulario se comprende, si una consulta muestra la información necesaria o si el flujo resuelve el problema identificado. Un sistema puede cumplir una especificación y aun así no responder a la necesidad real.

Ambas son prácticas transversales del proyecto: revisar antes de entregar, registrar resultados y corregir discrepancias. No se limitan a ejecutar pruebas al final. El tipo de revisión depende de la evidencia: una revisión de modelo es distinta de una prueba de software, y una prueba automática no sustituye por sí sola la validación con usuarios.

## Aplicación por unidad y entregable

| Unidad | Enfoques | Trabajo integrado en las entregas existentes |
|---|---|---|
| I · Introducción a los SI | SDD e introducción a DDD | E1: actores, vocabulario, requisitos, alcance, reglas y criterios de aceptación |
| II · DFD | SDD y verificación | E2: comprobar flujos, balance y niveles; distinguir renderizado Mermaid de corrección del modelo |
| III · Diccionario y procesos | SDD y DDD | E3–E4: coherencia de nombres, dominios, estructuras y decisiones |
| IV · Entradas y salidas | SDD y validación | E5: contrastar el prototipo Figma con requisitos y necesidades de sus usuarios |
| V · Bases de datos | DDD y verificación | E6: relaciones, normalización, claves y restricciones acordes con el dominio |
| VI · Pruebas y mantenimiento | TDD, verificación y validación | E7–E8: pruebas, defectos, cambios y documentación; CI de la suite en la integración final |

## Flujo de trabajo en cada incremento

1. **Comprender el dominio:** acordar significados con los actores y registrar las reglas del alcance seleccionado.
2. **Especificar:** describir comportamiento, datos y criterios de aceptación; relacionarlos con E1–E6 según corresponda.
3. **Implementar y probar:** para una regla adecuada a TDD, escribir una prueba que falle por el comportamiento ausente, implementar lo mínimo y refactorizar manteniendo las pruebas aprobadas.
4. **Verificar y validar:** revisar las evidencias técnicas y contrastar el resultado con el uso esperado; registrar correcciones.
5. **Actualizar:** mantener alineados requisitos, modelos, código, pruebas y manuales cuando cambie una decisión.

Esta secuencia es didáctica. Las actividades se retroalimentan: un prototipo puede revelar un requisito ambiguo, y una prueba puede descubrir una regla incompleta. Las evaluaciones por sprint no impiden revisar evidencias anteriores.

## Ejemplo transversal · Gestión de Pasantías

Se utiliza la regla hipotética del [ejemplo de E1](../unidades/01-introduccion-si/ejemplo-caracterizacion.md): un estudiante no registra dos postulaciones a la misma oferta. No es una afirmación sobre el reglamento institucional.

| Práctica | Aplicación al ejemplo |
|---|---|
| DDD | Distinguir estudiante, empresa, oferta y postulación; acordar que «registrada» no significa «aprobada» |
| SDD | Identificar RN-01 y RF-01; especificar el rechazo del segundo intento sin crear otra postulación |
| Verificación del modelo | E2 conserva el flujo de solicitud y respuesta; E3–E4 documentan datos y regla; E6 representa la restricción estudiante–oferta |
| TDD | Crear la prueba del duplicado; comprobar su fallo por la regla ausente; implementar la restricción y el manejo del rechazo; refactorizar sin romper los casos válidos |
| Validación | Comprobar con el usuario previsto que el mensaje permite comprender qué ocurrió y qué puede hacer |
| Trazabilidad | Relacionar requisito, regla, modelo, prueba, resultado y commit evaluable |

La prueba del duplicado debe comprobar también que no se creó una segunda fila. Probar únicamente el texto de la respuesta podría ocultar un error de persistencia. En Django/PostgreSQL, una validación de formulario aislada puede ser insuficiente ante solicitudes concurrentes; contrastar la restricción de BD y el tratamiento del error con E6 y E7.

TDD no equivale a escribir pruebas después del código ni obliga a que toda revisión documental tenga una prueba automática. Tampoco exige resolver todo el proyecto con un único patrón de arquitectura.

## Cómo registrar las evidencias

Incorporar referencias cruzadas dentro de los documentos y pruebas de las entregas existentes. Una fila de trazabilidad puede identificar **requisito o regla → modelo o decisión → comprobación → resultado → commit**. No se solicita un noveno entregable ni una herramienta adicional de gestión.

Para una revisión de modelo, anotar el criterio aplicado y su resultado. Para pruebas, conservar la ejecución y los defectos. Para validación de prototipos o flujos, documentar el escenario, el perfil del usuario consultado, los hallazgos y los cambios. Si no hubo acceso a un usuario real, identificar la revisión como simulada; no presentarla como validación institucional.

[Referencias de los enfoques](../recursos/bibliografia.md#enfoques-ingenieria) · [Guía para estudiantes](README.md) · [Entregables](../proyecto-integrador/entregables/README.md)
