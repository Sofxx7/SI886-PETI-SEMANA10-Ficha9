# Derivaci�n de la arquitectura objetivo

## Base estrat�gica acreditada

La FICHA A declara como objetivo de TI cerrar las observaciones de homologaci�n del cliente y asegurar la continuidad del enlace. La FICHA G documenta 14 horas sin registro de avance por la falla del radioenlace y la falta de respaldo operativo. La FICHA H identifica tres riesgos no tratados: homologaci�n, vencimientos contractuales y redundancia.

Las secciones grupales 2.2, 3.1.5, 3.5, 4.1.5 y 4.2 no se incluyeron en el documento recibido. Los avances del repositorio personal de Bitel y del caso cl�nico no corresponden a esta empresa. La arquitectura se deriva provisionalmente de los hechos y del objetivo del caso 09; su trazabilidad al PETI grupal debe completarse con esos documentos.

## Capacidades y metas propuestas para validaci�n

| C�digo | Capacidad propuesta | Criterio de aceptaci�n propuesto | Fuente y condici�n |
|---|---|---|---|
| CP01 | Gestionar obligaciones y evidencias | Las nueve observaciones tienen responsable, plazo, control asociado y evidencia de aceptaci�n del cliente | FICHA C y H. Primero solicitar el texto de las nueve observaciones; no se presume que los 17 cambios las cierran todas |
| CP02 | Sostener conectividad cr�tica | Conmutaci�n y recuperaci�n verificadas contra RTO/RPO aprobados por Operaciones | FICHA G y H. No se inventan valores del BIA ni una disponibilidad contratada |
| CP03 | Conciliar personal y horas operativas | Cada diferencia relevante se identifica, resuelve o acepta con responsable antes de remitir reportes y valorizaciones | Inventario 4 y 5. La frecuencia y tolerancia las aprueba el due�o del proceso |
| CP04 | Mantener integraciones | Documentaci�n, soporte, pruebas y reversi�n disponibles para cada integraci�n cr�tica | Inventario 4; validar capacidades del proveedor |
| CP05 | Atribuir acciones privilegiadas | Acciones administrativas atribuibles; excepciones t�cnicas documentadas y revisadas | FICHA F; viabilidad de MFA por producto pendiente |
| CP06 | Gestionar servicios y activos | Incidentes, cambios y activos cr�ticos registrados con responsable | FICHA F; validar cobertura y herramientas |

## Cambios por capa

| Capa | Actual | Objetivo propuesto | Origen | Brechas |
|---|---|---|---|---|
| Negocio | Contratos sin aviso efectivo; observaciones abiertas; pol�tica sin revisi�n | Gesti�n contractual y de homologaci�n con evidencia; pol�tica difundida | CP01; PA05; FICHA B C F H | BR01 BR15 BR16 |
| Negocio | Cuentas compartidas; incidentes sin registro; cambios ex post | Responsabilidad individual, registro y aprobaci�n previa | CP05 CP06; PA04 PA05; FICHA F | BR09 BR12 BR13 |
| Datos | Personal y contrato sin fuente; horas de equipo discrepantes | Maestros con due�o, fuente y conciliaci�n | CP03; PA02; inventario 5 | BR06 BR07 BR17 |
| Aplicaci�n | Dependencia del exempleado, archivo mensual y SSO aislado | Integraci�n mantenible, validada y m�nima | CP03 CP04; PA03 PA06; inventario 4 | BR03 BR04 BR05 |
| Aplicaci�n | Programaci�n en hoja y activos sin inventario | Programaci�n integrada y registro de configuraci�n | CP06; PA05 PA07; FICHA F; inventario 2 | BR08 BR14 |
| Tecnolog�a | Respaldo satelital inoperativo; disco conectado | Enlace redundante y copias aisladas o inmutables probadas | CP02; PA01; FICHA F G H | BR02 BR11 |
| Tecnolog�a | MFA solo en correo | Autenticaci�n reforzada en servicios cr�ticos compatibles | CP05; PA04; FICHA F | BR10 |

## L�mites de la propuesta

No se fijan precios, cronogramas, RTO/RPO ni productos nuevos sin evaluaci�n. El presupuesto anual de TI de S/ 1 460 000 no acredita disponibilidad para financiar estos paquetes. Tampoco se atribuye a una norma un cambio concreto sin contrastar su aplicabilidad; las obligaciones del cliente deben extraerse de la homologaci�n y de los contratos.
