# Principios de arquitectura de Servicios Mineros Cordillera

## PA01 Continuidad demostrable de los servicios cr�ticos
- **Declaraci�n:** todo servicio cr�tico dispone de una alternativa operativa y pruebas peri�dicas de recuperaci�n.
- **Raz�n:** la falla del radioenlace y el respaldo satelital vencido ocasionaron 14 horas sin registro de avance y una penalidad.
- **Implicancias:** controlar contratos, renovar el respaldo, probar conmutaci�n y restauraci�n; definir RTO y RPO con el BIA validado. La existencia de un enlace alterno no demuestra continuidad.
- **Trazabilidad:** FICHA, G y H; inventario, secciones 4 y 6.

## PA02 Dato �nico con responsabilidad asignada
- **Declaraci�n:** cada entidad cr�tica tiene una fuente autoritativa, un responsable por cargo y reglas de conciliaci�n.
- **Raz�n:** personal y contratos carecen de fuente autoritativa; existen diferencias en asistencia, horas de equipos y horas facturables.
- **Implicancias:** aprobar maestros y due�os antes de integrar o producir tableros; registrar discrepancias y mantener la procedencia del dato. No declarar que los conteos de poblaciones diferentes deben coincidir.
- **Trazabilidad:** inventario, secciones 5 y 7.

## PA03 Integraciones documentadas y mantenibles
- **Declaraci�n:** toda integraci�n cr�tica tiene documentaci�n, pruebas, responsable y soporte vigente.
- **Raz�n:** la integraci�n de control de personal depende de un exempleado y se mantiene por correo; el ERP recibe un archivo mensual.
- **Implicancias:** recuperar documentaci�n y derechos de mantenimiento, validar interfaces disponibles, probar con datos de prueba y mantener reversi�n. Usar servicios cuando los proveedores los soporten; no imponer una API inexistente.
- **Trazabilidad:** inventario, secci�n 4.

## PA04 Identidad individual y privilegio m�nimo
- **Declaraci�n:** las acciones privilegiadas son atribuibles a una persona y los servicios cr�ticos incorporan autenticaci�n reforzada compatible.
- **Raz�n:** dos personas comparten cuentas de administrador y el segundo factor solo se usa en correo.
- **Implicancias:** inventariar cuentas, separar identidades personales y t�cnicas, limitar privilegios, habilitar MFA donde sea viable y revisar registros. Documentar excepciones y controles compensatorios.
- **Trazabilidad:** FICHA, F.

## PA05 Evidencia desde el dise�o
- **Declaraci�n:** cada control, cambio y obligaci�n contractual produce evidencia verificable con responsable y fecha.
- **Raz�n:** nueve observaciones de homologaci�n permanecen abiertas; no se registran incidentes y los cambios se documentan despu�s de aplicarlos.
- **Implicancias:** crear registro de observaciones, incidentes y cambios, aprobar antes de ejecutar y controlar vencimientos. Verificar el detalle de las nueve observaciones antes de afirmar que un proyecto las resuelve.
- **Trazabilidad:** FICHA, C, F y H.

## PA06 Protecci�n de los datos seg�n su clasificaci�n
- **Declaraci�n:** los datos personales y restringidos reciben acceso por necesidad, trazabilidad y conservaci�n definida.
- **Raz�n:** el control de personal usa biometr�a y la entidad personal est� clasificada como restringida; proveedores contiene contacto y documento de identidad.
- **Implicancias:** usar datos agregados en el informe, excluir identificadores personales y secretos de las vistas, revisar finalidad y permisos antes de integrar SSO y personal. Validar requisitos con el responsable competente.
- **Trazabilidad:** FICHA, C e I; inventario, secci�n 5; gu�a, secci�n 1.3.

## PA07 Reutilizar capacidades con soporte antes de duplicarlas
- **Declaraci�n:** las mejoras eval�an primero las capacidades y contratos vigentes del ERP y del SaaS.
- **Raz�n:** el ERP tiene soporte y SLA, mientras programaci�n, contratos y reportes de asistencia dependen de hojas de c�lculo sin soporte.
- **Implicancias:** verificar m�dulos y licencias, comparar costo total y probar migraci�n; retirar hojas solo despu�s de aceptaci�n y reversi�n probadas. El presupuesto TI de S/ 1 460 000 no equivale a saldo disponible para nuevos proyectos.
- **Trazabilidad:** FICHA, B y C; inventario, secci�n 2.
