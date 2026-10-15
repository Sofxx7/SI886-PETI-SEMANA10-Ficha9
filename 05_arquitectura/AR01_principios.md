# Principios de arquitectura de Servicios Mineros Cordillera

## PA01 Continuidad demostrable de los servicios críticos
- **Declaración:** todo servicio crítico dispone de una alternativa operativa y pruebas periódicas de recuperación.
- **Razón:** la falla del radioenlace y el respaldo satelital vencido ocasionaron 14 horas sin registro de avance y una penalidad.
- **Implicancias:** controlar contratos, renovar el respaldo, probar conmutación y restauración; definir RTO y RPO con el BIA validado. La existencia de un enlace alterno no demuestra continuidad.
- **Trazabilidad:** FICHA, G y H; inventario, secciones 4 y 6.

## PA02 Dato único con responsabilidad asignada
- **Declaración:** cada entidad crítica tiene una fuente autoritativa, un responsable por cargo y reglas de conciliación.
- **Razón:** personal y contratos carecen de fuente autoritativa; existen diferencias en asistencia, horas de equipos y horas facturables.
- **Implicancias:** aprobar maestros y dueños antes de integrar o producir tableros; registrar discrepancias y mantener la procedencia del dato. No declarar que los conteos de poblaciones diferentes deben coincidir.
- **Trazabilidad:** inventario, secciones 5 y 7.

## PA03 Integraciones documentadas y mantenibles
- **Declaración:** toda integración crítica tiene documentación, pruebas, responsable y soporte vigente.
- **Razón:** la integración de control de personal depende de un exempleado y se mantiene por correo; el ERP recibe un archivo mensual.
- **Implicancias:** recuperar documentación y derechos de mantenimiento, validar interfaces disponibles, probar con datos de prueba y mantener reversión. Usar servicios cuando los proveedores los soporten; no imponer una API inexistente.
- **Trazabilidad:** inventario, sección 4.

## PA04 Identidad individual y privilegio mínimo
- **Declaración:** las acciones privilegiadas son atribuibles a una persona y los servicios críticos incorporan autenticación reforzada compatible.
- **Razón:** dos personas comparten cuentas de administrador y el segundo factor solo se usa en correo.
- **Implicancias:** inventariar cuentas, separar identidades personales y técnicas, limitar privilegios, habilitar MFA donde sea viable y revisar registros. Documentar excepciones y controles compensatorios.
- **Trazabilidad:** FICHA, F.

## PA05 Evidencia desde el diseño
- **Declaración:** cada control, cambio y obligación contractual produce evidencia verificable con responsable y fecha.
- **Razón:** nueve observaciones de homologación permanecen abiertas; no se registran incidentes y los cambios se documentan después de aplicarlos.
- **Implicancias:** crear registro de observaciones, incidentes y cambios, aprobar antes de ejecutar y controlar vencimientos. Verificar el detalle de las nueve observaciones antes de afirmar que un proyecto las resuelve.
- **Trazabilidad:** FICHA, C, F y H.

## PA06 Protección de los datos según su clasificación
- **Declaración:** los datos personales y restringidos reciben acceso por necesidad, trazabilidad y conservación definida.
- **Razón:** el control de personal usa biometría y la entidad personal está clasificada como restringida; proveedores contiene contacto y documento de identidad.
- **Implicancias:** usar datos agregados en el informe, excluir identificadores personales y secretos de las vistas, revisar finalidad y permisos antes de integrar SSO y personal. Validar requisitos con el responsable competente.
- **Trazabilidad:** FICHA, C e I; inventario, sección 5; guía, sección 1.3.

## PA07 Reutilizar capacidades con soporte antes de duplicarlas
- **Declaración:** las mejoras evalúan primero las capacidades y contratos vigentes del ERP y del SaaS.
- **Razón:** el ERP tiene soporte y SLA, mientras programación, contratos y reportes de asistencia dependen de hojas de cálculo sin soporte.
- **Implicancias:** verificar módulos y licencias, comparar costo total y probar migración; retirar hojas solo después de aceptación y reversión probadas. El presupuesto TI de S/ 1 460 000 no equivale a saldo disponible para nuevos proyectos.
- **Trazabilidad:** FICHA, B y C; inventario, sección 2.

## Trazabilidad al diagnóstico y al PETI

La base [00_base_estrategica_caso09.md](00_base_estrategica_caso09.md), sección 3.1.3, organiza los hallazgos H01–H06 del caso. PA01 → H01/V02/CP02; PA02 → H02/V03/CP03; PA03 → H03/V03/CP04; PA04 → H04/V04/CP05; PA05 → H01/H05/V01/CP01/CP06; PA06 → H05/NN03; PA07 → H03/H06/E04. Esta base es propuesta académica de esta revisión, no diagnóstico previamente aprobado.
