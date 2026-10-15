# Base estratégica del caso 09 para la sección 5

**Estado:** propuesta académica elaborada para completar la derivación del taller S10. No es un PETI previo aprobado ni una decisión implantada. Se limita al caso ficticio Cordillera y debe incorporarse y ratificarse en las secciones indicadas del PETI del equipo.

**Fuentes:** [FICHA A–I](https://github.com/OscarJimenezFlores/PETI/blob/main/SEMANA-10/RECURSOS-TALLER/EMPRESA-09-servicios-mineros-cordillera/FICHA.md) e [inventario 2–7](https://github.com/OscarJimenezFlores/PETI/blob/main/SEMANA-10/RECURSOS-TALLER/EMPRESA-09-servicios-mineros-cordillera/arquitectura-actual.md). El objetivo explícito de TI es cerrar observaciones de homologación y asegurar la continuidad del enlace. Las metas siguientes son propuestas, no mediciones realizadas.

## 2.2 Visión y métricas propuestas

TI sostiene servicios mineros trazables y recuperables, con información conciliada y evidencia de los controles exigidos por el cliente, reutilizando plataformas con soporte.

| Código | Resultado propuesto | Línea base acreditada | Métrica y meta de aceptación propuesta |
|---|---|---|---|
| V01 | Homologación con evidencia | 9 observaciones abiertas; FICHA C/H | 9/9 con responsable, plazo y evidencia; cierre solo cuando el cliente acepte cada observación |
| V02 | Continuidad demostrable | 14 h sin registro; respaldo vencido; FICHA G | 100% de enlaces alternos críticos con contrato vigente y prueba de conmutación; tiempos comparados con RTO/RPO aprobados tras validar BIA |
| V03 | Información confiable | Personal y Contrato sin fuente; horas discrepantes; inventario 5 | 6/6 entidades del alcance con fuente y dueño definidos; discrepancias de horas resueltas o aceptadas antes de emitir reportes |
| V04 | Operación de TI atribuible y controlada | Cuentas compartidas; incidentes sin registro; cambios ex post; FICHA F | 100% de administradores personales identificados; 100% de cambios críticos con aprobación previa e incidentes críticos registrados; excepciones documentadas |

No se fijan disponibilidad, plazos contractuales, RTO/RPO ni costos no suministrados. Los responsables de proceso deben aprobar umbrales y periodicidad antes de ejecución.

## 3.1.3 Hallazgos de diagnóstico que sustentan los principios

| Hallazgo | Evidencia | Consecuencia | Principios |
|---|---|---|---|
| H01 | FICHA F/G/H: vencimientos, satélite inoperativo y 14 h sin registro | Continuidad nominal sin respaldo efectivo | PA01 PA05 |
| H02 | Inventario 5/7: fuentes ausentes y horas diferentes | Reportes y valorizaciones no conciliados | PA02 |
| H03 | Inventario 4: exempleado, archivo mensual y SSO sin integración | Dependencia de personas y transferencias no gobernadas | PA03 PA07 |
| H04 | FICHA F: cuentas compartidas y MFA solo en correo | Falta de atribución y alcance limitado de autenticación | PA04 |
| H05 | FICHA B/C/F: política sin revisión, cambios ex post y 9 observaciones | Falta de evidencia y seguimiento | PA05 PA06 |
| H06 | Inventario 2 y FICHA C: ERP/SaaS con soporte; hojas sin soporte | Duplicación operativa pese a capacidades existentes | PA07 |

## 3.1.5 Capacidades requeridas propuestas

Escala operativa de este ejercicio: 0 no acreditada; 1 práctica parcial o informal; 2 práctica definida, con responsable y prueba. No equivale a una evaluación de madurez certificada.

| Código | Capacidad | Nivel actual interpretado | Nivel objetivo | Evidencia de aceptación |
|---|---|---|---|---|
| CP01 | Obligaciones y homologación | 1 | 2 | Registro de contratos/observaciones con responsables, alertas y aceptación |
| CP02 | Conectividad y recuperación | 1 | 2 | Conmutación y restauración probadas, BIA validado |
| CP03 | Gobierno y conciliación del dato | 1 | 2 | Fuentes/dueños aceptados y conciliaciones de personal, contratos y horas |
| CP04 | Integraciones mantenibles | 1 | 2 | Documentación, soporte, pruebas y reversión |
| CP05 | Identidad y privilegio mínimo | 1 | 2 | Identidades individuales, MFA compatible y excepciones |
| CP06 | Gestión de servicios, cambios y activos | 1 | 2 | Registros verificables de incidentes, cambios y configuración |

## 3.5 FODA cruzado y estrategias propuestas

Fortaleza F1: ERP y SaaS con soporte (FICHA C). Debilidades D1: contratos y continuidad (F/G); D2: fuentes e integración (inventario 4/5); D3: cuentas y controles informales (F). Amenazas A1: penalidad por interrupción ya ocurrida (G); A2: observaciones de homologación sin cerrar (C/H). Oportunidad O1: aprovechar capacidades del proveedor con soporte; disponibilidad específica y licencias aún por verificar, por lo que no se presenta como hecho contratado.

| Estrategia | Cruce | Acción | Visión / capacidad |
|---|---|---|---|
| E01 | DA: D1/D3–A1/A2 | Gobierno contractual, política y evidencia de homologación | V01 V02 / CP01 |
| E02 | DA: D1–A1 | Recuperar respaldo efectivo y verificar recuperación | V02 / CP02 |
| E03 | DA: D2–A1/A2 | Formalizar maestros, responsables y conciliación | V03 / CP03 |
| E04 | FO/DO: F1/D2–O1 | Integración soportada y programación sin duplicación no controlada | V03 / CP04 |
| E05 | DA: D3–A2 | Identidades individuales y autenticación reforzada viable | V04 / CP05 |
| E06 | FA: F1–A1/A2 | Gestión de incidentes, aprobación previa de cambios e inventario | V04 / CP06 |

## 4.1.5 Proyectos no negociables propuestos y condición de aplicabilidad

| Código | Compromiso acreditado o condición | Cambio mínimo propuesto | Límite |
|---|---|---|---|
| NN01 | Homologación anual exigida por cliente; FICHA C | Registro de las nueve observaciones, responsables y evidencia de cierre | Solicitar texto y criterio del cliente antes de afirmar cobertura o cierre |
| NN02 | Enlace crítico sin respaldo efectivo e incidente; FICHA G/H | Regularizar contrato, conmutación y recuperación verificables | Es prioridad contractual/operativa; no se atribuye a una norma un plazo inexistente |
| NN03 | Personal y biometría; FICHA C e inventario 5 | Acceso mínimo, minimización, clasificación y revisión de finalidad antes de integrar | La ficha menciona Ley 29733; aplicabilidad concreta y controles deben revisarse con responsable competente. No se certifica cumplimiento legal |

## 4.2 Marcos adoptados como método académico

- **TOGAF ADM B/C/D:** separar negocio, sistemas de información y tecnología; comparar estados y derivar brechas.
- **ArchiMate 3.2:** lenguaje de elementos y relaciones, con revisión de la matriz de relaciones distribuida por Archi.
- **COBIT 2019 APO03:** arquitectura y trazabilidad; DSS04 como referencia para continuidad, DSS02 para incidentes y BAI06 para cambios. Son referencias seleccionadas para el diseño, no controles certificados ni obligaciones públicas de una empresa privada.
- La clasificación y el tratamiento de datos se toman del caso; no se atribuye un marco de gobierno digital estatal obligatorio a esta empresa.

La matriz AR07_trazabilidad.csv conecta cada una de las 17 brechas con esta base, el modelo y los principios. La ratificación por el equipo y los responsables del caso sigue siendo una condición distinta de la consistencia documental.
