# 5 Arquitectura empresarial

## 5.1 Principios de arquitectura

Servicios Mineros Cordillera requiere arquitectura que haga verificables la continuidad, la integridad de la informaci�n y las obligaciones del cliente. El incidente de conectividad y los contratos vencidos justifican priorizar control operativo antes de ampliar automatizaciones.

Los siete principios est�n desarrollados, con declaraci�n, raz�n, implicancias y trazabilidad, en [AR01_principios.md](AR01_principios.md): continuidad demostrable, dato �nico con responsabilidad, integraciones mantenibles, identidad individual, evidencia desde el dise�o, protecci�n por clasificaci�n y reutilizaci�n de capacidades con soporte.

## 5.2 Arquitectura actual

### 5.2.1 Capa de negocio

La cadena operativa comprende licitaci�n y contrataci�n, planificaci�n y ejecuci�n del servicio, seguridad y salud ocupacional, control de personal y campamento, mantenimiento de equipos y facturaci�n/valorizaciones. El cliente minero recibe reportes y exige homologaci�n con evidencia. Gerencia de Operaciones conduce los servicios; la Superintendencia de TI depende de esa gerencia y cuenta con cinco personas.

Los procesos auxiliares documentados presentan contratos sin control efectivo de vencimiento, incidentes no registrados, cambios formalizados despu�s de aplicar y nueve observaciones sin cierre. No existe comit� de TI ni PETI aprobado en el caso. La pol�tica de seguridad existe desde 2022 sin difusi�n ni revisi�n posterior.

### 5.2.2 Capa de datos

La matriz [AR02_entidades.csv](AR02_entidades.csv) registra seis entidades. Personal, Equipo, Contrato y Servicio provienen del inventario; Proveedor y Pago se incorporan desde los datasets descritos en la ficha, sin atribuirles un sistema de origen no documentado.

**Entidades expresamente sin fuente autoritativa: 2 de 6.** Otras dos no tienen fuente documentada; por tanto, no se acredita fuente declarada para 4 de 6. Esto distingue una carencia confirmada de un dato a�n no obtenido.

Contrato no tiene due�o; Personal tiene responsabilidad de hecho en Operaciones; Proveedor y Pago no tienen due�o documentado. Solo Equipo y Servicio identifican expl�citamente cargos responsables: Superintendente de Mantenimiento y Gerente de Operaciones. El objetivo propone formalizar responsabilidades con aceptaci�n de las �reas.

La diferencia de 20 equipos entre ERP y registro del cliente no demuestra por s� sola p�rdida de equipos. Los 700 registros de picos de campamento no son equivalentes a la planilla de 420. Las cifras requieren conciliar cobertura y fecha; la ficha adem�s registra 421 personas en A y 420 en el dataset de I. En Servicio, 36 por a�o no es un conteo desagregado para cada sistema. Personal contiene datos sensibles; Proveedor y Pago contienen informaci�n personal y se propone clasificarlos como confidenciales.

### 5.2.3 Capa de aplicaci�n

El ERP internacional integra proyectos, compras y finanzas en nube privada con SLA; mantenimiento es un m�dulo del ERP. SSO opera como SaaS y el control de personal combina biometr�a con sistema del proveedor en campamento.

Tres hojas de c�lculo operan como componentes de aplicaci�n: programaci�n de servicios, control de vencimiento de contratos y reportes de asistencia. La integraci�n de personal depende de mantenimiento por correo con un exempleado; al ERP se remite archivo mensual. SSO no se integra al ERP. Estas condiciones explican las propuestas de documentaci�n, soporte y conciliaci�n, sin afirmar que existe una API disponible.

### 5.2.4 Capa de tecnolog�a

La tecnolog�a comprende nube privada del ERP, plataforma SaaS de SSO, servidor del campamento, 90 estaciones en Tacna y 40 en campamento, redes de ambas sedes y su enlace. El radioenlace cuenta nominalmente con alternativa satelital, pero el contrato venci� y no hab�a redundancia efectiva cuando ocurri� el incidente. Los respaldos a disco conectado no acreditan independencia respecto del servidor. El segundo factor se usa solo en correo.

El enlace y el sat�lite se modelan en tecnolog�a, aunque el inventario los liste junto con sistemas. No se incluyen IP, credenciales ni rutas internas.

### 5.2.5 Cooperaci�n proceso aplicaci�n

[AR04_proceso_aplicacion.csv](AR04_proceso_aplicacion.csv) vincula los seis procesos con sus aplicaciones y la evaluaci�n anal�tica de soporte. **Cinco de seis procesos tienen soporte parcial o deficiente; uno es deficiente y cuatro parciales. Ninguno aparece totalmente sin sistema.** Licitaci�n y contrataci�n dispone de ERP y no se documenta deficiencia directa de su soporte.

![Arquitectura actual para revisi�n](../graficos/V01_actual_revision.png)

## 5.3 Arquitectura objetivo

### 5.3.1 Derivaci�n

El objetivo de TI acreditado es cerrar las observaciones de homologaci�n y asegurar la continuidad del enlace. [AR06_derivacion_objetivo.md](AR06_derivacion_objetivo.md) vincula este objetivo y los hechos del caso con seis capacidades propuestas: obligaciones/evidencia, conectividad, conciliaci�n, integraciones mantenibles, identidad y gesti�n de servicios.

Debe completarse la trazabilidad a las secciones 2.2, 3.1.5, 3.5, 4.1.5 y 4.2 del PETI grupal. Las propuestas no sustituyen una visi�n o un FODA previamente aprobados. No se reutilizan las secciones de Bitel o de la cl�nica porque pertenecen a organizaciones diferentes.

### 5.3.2 Cambios por capa

En negocio se propone gestionar contratos y homologaci�n con responsables y evidencia, revisar la pol�tica y registrar incidentes/cambios. En datos se formalizan fuentes y due�os, y se concilian horas y personal. En aplicaci�n se documentan y soportan integraciones, se eval�a intercambio m�nimo SSO/ERP y programaci�n integrada, y se registra la configuraci�n. En tecnolog�a se recupera redundancia efectiva, se prueban copias aisladas o inmutables y se extiende autenticaci�n reforzada donde los productos la soporten.

Cada cambio se identifica en el CSV de brechas con origen y conceptos de ambos estados. Las metas espec�ficas, frecuencias, RTO/RPO y costos requieren validaci�n. No se declara cerrado ninguno de los nueve puntos de homologaci�n sin su texto y aceptaci�n.

### 5.3.3 Vistas objetivo

El archivo [AR05_Cordillera.archimate](AR05_Cordillera.archimate) contiene el modelo actual y objetivo y cuatro vistas. Las PNG adjuntas son previsualizaciones de revisi�n; la evidencia final debe exportarse desde Archi despu�s de comprobar elementos y relaciones.

![Arquitectura objetivo propuesta](../graficos/V02_objetivo_revision.png)

## 5.4 An�lisis de brechas

### 5.4.1 Brechas por capa y tipo

[AR03_brechas.csv](AR03_brechas.csv) registra 17 brechas: seis de negocio, cinco de aplicaci�n, tres de datos y tres de tecnolog�a. El programa asigna tres esfuerzos bajos, doce medios y dos altos. La escala expresa complejidad relativa; no estima presupuesto ni duraci�n.

| ID | Cambio principal | Capa | Paquete |
|---|---|---|---|
| BR01 | Alertas y responsabilidad contractual | Negocio | PT01 |
| BR02 | Redundancia efectiva y prueba de conmutaci�n | Tecnolog�a | PT03 |
| BR03 | Soporte y documentaci�n de integraci�n de personal | Aplicaci�n | PT04 |
| BR04 | Transferencia de personal con validaci�n y frecuencia aprobada | Aplicaci�n | PT04 |
| BR05 | Intercambio m�nimo SSO ERP | Aplicaci�n | PT04 |
| BR06 | Fuente y due�o de Personal | Datos | PT02 |
| BR07 | Fuente y due�o de Contrato | Datos | PT02 |
| BR08 | Programaci�n integrada y conciliada | Aplicaci�n | PT04 |
| BR09 | Administraci�n con identidad individual | Negocio | PT05 |
| BR10 | MFA en servicios cr�ticos compatibles | Tecnolog�a | PT05 |
| BR11 | Copias aisladas o inmutables y restauraci�n | Tecnolog�a | PT03 |
| BR12 | Registro y tratamiento de incidentes | Negocio | PT06 |
| BR13 | Evaluaci�n y aprobaci�n previa de cambios | Negocio | PT06 |
| BR14 | Inventario y registro de configuraci�n | Aplicaci�n | PT06 |
| BR15 | Registro y validaci�n de cierre de homologaci�n | Negocio | PT01 |
| BR16 | Revisi�n difusi�n y capacitaci�n sobre pol�tica | Negocio | PT01 |
| BR17 | Conciliaci�n de horas de equipos | Datos | PT02 |

### 5.4.2 Paquetes de trabajo derivados

Las brechas se agrupan en seis paquetes: PT01 Gobierno contractual y evidencia; PT02 Gobierno y conciliaci�n del dato; PT03 Continuidad de enlace y respaldos; PT04 Integraci�n y programaci�n operativa; PT05 Identidad y control de acceso; PT06 Gesti�n de servicios, cambios y activos.

[AR03_paquetes.csv](AR03_paquetes.csv) conserva las brechas de cada paquete, su esfuerzo m�ximo y dependencias. La asignaci�n se verifica para evitar brechas hu�rfanas. Estos paquetes son insumo del portafolio de la secci�n 7.1, sujeto a evaluaci�n de beneficios, costos y recursos. Los S/ 1 460 000 del presupuesto anual de TI no son saldo acreditado para financiarlos.

### 5.4.3 Dependencias y secuencia obligada por el dise�o propuesto

El algoritmo valida referencias y ciclos y calcula niveles de precedencia:

1. PT01 establece responsables, obligaciones y evidencias.
2. PT02, PT03, PT05 y PT06 preparan datos, continuidad, identidad y operaci�n controlada. Pueden avanzar en paralelo seg�n recursos.
3. PT04 utiliza esas condiciones para poner en operaci�n las integraciones propuestas.

La salida se guarda en [AR03_secuencia.json](AR03_secuencia.json) y [AR03_salida.txt](../evidencias/S10/salidas/AR03_salida.txt). La secuencia es consecuencia del grafo de dependencias dise�ado por el equipo; debe ratificarse con Operaciones y TI antes de construir la hoja de ruta. No se espera al paquete de integraci�n para recuperar el respaldo satelital.

La comprobaci�n estructural valid� IDs �nicos, referencias internas y 17 brechas con conceptos en ambos estados. Contin�an pendientes la validaci�n sem�ntica en Archi, el contraste con el PETI grupal y la conformidad del cierre del taller; las evidencias preparadas se publican en el repositorio del Grupo 1.
