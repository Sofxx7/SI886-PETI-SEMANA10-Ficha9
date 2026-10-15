# Derivación de la arquitectura objetivo

## Base estratégica acreditada

La FICHA A declara como objetivo de TI cerrar las observaciones de homologación del cliente y asegurar la continuidad del enlace. La FICHA G documenta 14 horas sin registro de avance por la falla del radioenlace y la falta de respaldo operativo. La FICHA H identifica tres riesgos no tratados: homologación, vencimientos contractuales y redundancia.

Se añadió [00_base_estrategica_caso09.md](00_base_estrategica_caso09.md): visión 2.2, hallazgos 3.1.3, capacidades 3.1.5, FODA cruzado 3.5, proyectos no negociables 4.1.5 y marcos 4.2, todos formulados como propuesta académica del caso 09, no como antecedentes aprobados. [AR07_trazabilidad.csv](AR07_trazabilidad.csv) conecta cada brecha con esos insumos, principios, conceptos AS/TB y criterio de aceptación. Su consistencia es comprobable; la ratificación del negocio y del equipo no se presume.

## Capacidades y metas propuestas para validación

| Código | Capacidad propuesta | Criterio de aceptación propuesto | Fuente y condición |
|---|---|---|---|
| CP01 | Gestionar obligaciones y evidencias | Las nueve observaciones tienen responsable, plazo, control asociado y evidencia de aceptación del cliente | FICHA C y H. Primero solicitar el texto de las nueve observaciones; no se presume que los 17 cambios las cierran todas |
| CP02 | Sostener conectividad crítica | Conmutación y recuperación verificadas contra RTO/RPO aprobados por Operaciones | FICHA G y H. No se inventan valores del BIA ni una disponibilidad contratada |
| CP03 | Conciliar personal y horas operativas | Cada diferencia relevante se identifica, resuelve o acepta con responsable antes de remitir reportes y valorizaciones | Inventario 4 y 5. La frecuencia y tolerancia las aprueba el dueño del proceso |
| CP04 | Mantener integraciones | Documentación, soporte, pruebas y reversión disponibles para cada integración crítica | Inventario 4; validar capacidades del proveedor |
| CP05 | Atribuir acciones privilegiadas | Acciones administrativas atribuibles; excepciones técnicas documentadas y revisadas | FICHA F; viabilidad de MFA por producto pendiente |
| CP06 | Gestionar servicios y activos | Incidentes, cambios y activos críticos registrados con responsable | FICHA F; validar cobertura y herramientas |

## Cambios por capa

| Capa | Actual | Objetivo propuesto | Origen | Brechas |
|---|---|---|---|---|
| Negocio | Contratos sin aviso efectivo; observaciones abiertas; política sin revisión | Gestión contractual y de homologación con evidencia; política difundida | CP01; PA05; FICHA B C F H | BR01 BR15 BR16 |
| Negocio | Cuentas compartidas; incidentes sin registro; cambios ex post | Responsabilidad individual, registro y aprobación previa | CP05 CP06; PA04 PA05; FICHA F | BR09 BR12 BR13 |
| Datos | Personal y contrato sin fuente; horas de equipo discrepantes | Maestros con dueño, fuente y conciliación | CP03; PA02; inventario 5 | BR06 BR07 BR17 |
| Aplicación | Dependencia del exempleado, archivo mensual y SSO aislado | Integración mantenible, validada y mínima | CP03 CP04; PA03 PA06; inventario 4 | BR03 BR04 BR05 |
| Aplicación | Programación en hoja y activos sin inventario | Programación integrada y registro de configuración | CP06; PA05 PA07; FICHA F; inventario 2 | BR08 BR14 |
| Tecnología | Respaldo satelital inoperativo; disco conectado | Enlace redundante y copias aisladas o inmutables probadas | CP02; PA01; FICHA F G H | BR02 BR11 |
| Tecnología | MFA solo en correo | Autenticación reforzada en servicios críticos compatibles | CP05; PA04; FICHA F | BR10 |

## Límites de la propuesta

No se fijan precios, cronogramas, RTO/RPO ni productos nuevos sin evaluación. El presupuesto anual de TI de S/ 1 460 000 no acredita disponibilidad para financiar estos paquetes. Tampoco se atribuye a una norma un cambio concreto sin contrastar su aplicabilidad; las obligaciones del cliente deben extraerse de la homologación y de los contratos.
