# 5 Arquitectura empresarial

## 5.1 Principios de arquitectura

Servicios Mineros Cordillera requiere arquitectura que haga verificables la continuidad, la integridad de la información y las obligaciones del cliente. El incidente de conectividad y los contratos vencidos justifican priorizar control operativo antes de ampliar automatizaciones.

Los siete principios están desarrollados, con declaración, razón, implicancias y trazabilidad, en [AR01_principios.md](AR01_principios.md): continuidad demostrable, dato único con responsabilidad, integraciones mantenibles, identidad individual, evidencia desde el diseño, protección por clasificación y reutilización de capacidades con soporte.

## 5.2 Arquitectura actual

### 5.2.1 Capa de negocio

La cadena operativa comprende licitación y contratación, planificación y ejecución del servicio, seguridad y salud ocupacional, control de personal y campamento, mantenimiento de equipos y facturación/valorizaciones. El cliente minero recibe reportes y exige homologación con evidencia. Gerencia de Operaciones conduce los servicios; la Superintendencia de TI depende de esa gerencia y cuenta con cinco personas.

Los procesos auxiliares documentados presentan contratos sin control efectivo de vencimiento, incidentes no registrados, cambios formalizados después de aplicar y nueve observaciones sin cierre. No existe comité de TI ni PETI aprobado en el caso. La política de seguridad existe desde 2022 sin difusión ni revisión posterior.

### 5.2.2 Capa de datos

La matriz [AR02_entidades.csv](AR02_entidades.csv) registra seis entidades. Personal, Equipo, Contrato y Servicio provienen del inventario; Proveedor y Pago se incorporan desde los datasets descritos en la ficha, sin atribuirles un sistema de origen no documentado.

**Entidades expresamente sin fuente autoritativa: 2 de 6.** Otras dos no tienen fuente documentada; por tanto, no se acredita fuente declarada para 4 de 6. Esto distingue una carencia confirmada de un dato aun no obtenido.

Contrato no tiene dueño; Personal tiene responsabilidad de hecho en Operaciones; Proveedor y Pago no tienen dueño documentado. Solo Equipo y Servicio identifican explícitamente cargos responsables: Superintendente de Mantenimiento y Gerente de Operaciones. El objetivo propone formalizar responsabilidades con aceptación de las áreas.

La diferencia de 20 equipos entre ERP y registro del cliente no demuestra por sí sola pérdida de equipos. Los 700 registros de picos de campamento no son equivalentes a la planilla de 420. Las cifras requieren conciliar cobertura y fecha; la ficha además registra 421 personas en A y 420 en el dataset de I. En Servicio, 36 por año no es un conteo desagregado para cada sistema. Personal contiene datos sensibles; Proveedor y Pago contienen información personal y se propone clasificarlos como confidenciales.

### 5.2.3 Capa de aplicación

El ERP internacional integra proyectos, compras y finanzas en nube privada con SLA; mantenimiento es un módulo del ERP. SSO opera como SaaS y el control de personal combina biometría con sistema del proveedor en campamento.

Tres hojas de cálculo operan como componentes de aplicación: programación de servicios, control de vencimiento de contratos y reportes de asistencia. La integración de personal depende de mantenimiento por correo con un exempleado; al ERP se remite archivo mensual. SSO no se integra al ERP. Estas condiciones explican las propuestas de documentación, soporte y conciliación, sin afirmar que existe una API disponible.

### 5.2.4 Capa de tecnología

La tecnología comprende nube privada del ERP, plataforma SaaS de SSO, servidor del campamento, 90 estaciones en Tacna y 40 en campamento, redes de ambas sedes y su enlace. El radioenlace cuenta nominalmente con alternativa satelital, pero el contrato venció y no había redundancia efectiva cuando ocurrió el incidente. Los respaldos a disco conectado no acreditan independencia respecto del servidor. El segundo factor se usa solo en correo.

El enlace y el satélite se modelan en tecnología, aunque el inventario los liste junto con sistemas. No se incluyen IP, credenciales ni rutas internas.

### 5.2.5 Cooperación proceso aplicación

[AR04_proceso_aplicacion.csv](AR04_proceso_aplicacion.csv) vincula los seis procesos con sus aplicaciones y la evaluación analítica de soporte. **Cinco de seis procesos tienen soporte parcial o deficiente; uno es deficiente y cuatro parciales. Ninguno aparece totalmente sin sistema.** Licitación y contratación dispone de ERP y no se documenta deficiencia directa de su soporte.

![Arquitectura actual exportada de Archi](../graficos/V01_actual.png)

## 5.3 Arquitectura objetivo

### 5.3.1 Derivación

El objetivo de TI acreditado es cerrar las observaciones de homologación y asegurar la continuidad del enlace. [AR06_derivacion_objetivo.md](AR06_derivacion_objetivo.md) vincula este objetivo y los hechos del caso con seis capacidades propuestas: obligaciones/evidencia, conectividad, conciliación, integraciones mantenibles, identidad y gestión de servicios.

La base [00_base_estrategica_caso09.md](00_base_estrategica_caso09.md) desarrolla las secciones 2.2, 3.1.3, 3.1.5, 3.5, 4.1.5 y 4.2 como propuesta académica. La matriz [AR07_trazabilidad.csv](AR07_trazabilidad.csv) enlaza las 17 brechas a visión, capacidades, estrategias, obligaciones, principios y conceptos de ambos estados. No se presenta esta base como un PETI anterior aprobado; su ratificación por el equipo y el negocio queda pendiente.

### 5.3.2 Cambios por capa

En negocio se propone gestionar contratos y homologación con responsables y evidencia, revisar la política y registrar incidentes/cambios. En datos se formalizan fuentes y dueños, y se concilian horas y personal. En aplicación se documentan y soportan integraciones, se evalúa intercambio mínimo SSO/ERP y programación integrada, y se registra la configuración. En tecnología se recupera redundancia efectiva, se prueban copias aisladas o inmutables y se extiende autenticación reforzada donde los productos la soporten.

Cada cambio se identifica en el CSV de brechas con origen y conceptos de ambos estados. Las metas específicas, frecuencias, RTO/RPO y costos requieren validación. No se declara cerrado ninguno de los nueve puntos de homologación sin su texto y aceptación.

### 5.3.3 Vistas objetivo

El archivo [AR05_Cordillera.archimate](AR05_Cordillera.archimate) contiene los estados actual y objetivo y siete vistas: arquitectura AS, arquitectura TB, cooperación, información, gobierno AS, gobierno TB y comparación de brechas. Las PNG se generaron realmente con Archi 5.10 mediante su exportador HTML y se revisaron visualmente. El registro de carga, guardado y exportación y la revisión de las tres comprobaciones están en [AR08_validacion.md](AR08_validacion.md).

![Arquitectura objetivo propuesta](../graficos/V02_objetivo.png)

## 5.4 Análisis de brechas

### 5.4.1 Brechas por capa y tipo

[AR03_brechas.csv](AR03_brechas.csv) registra 17 brechas: seis de negocio, cinco de aplicación, tres de datos y tres de tecnología. El programa asigna tres esfuerzos bajos, doce medios y dos altos. La escala expresa complejidad relativa; no estima presupuesto ni duración.

| ID | Cambio principal | Capa | Paquete |
|---|---|---|---|
| BR01 | Alertas y responsabilidad contractual | Negocio | PT01 |
| BR02 | Redundancia efectiva y prueba de conmutación | Tecnología | PT03 |
| BR03 | Soporte y documentación de integración de personal | Aplicación | PT04 |
| BR04 | Transferencia de personal con validación y frecuencia aprobada | Aplicación | PT04 |
| BR05 | Intercambio mínimo SSO ERP | Aplicación | PT04 |
| BR06 | Fuente y dueño de Personal | Datos | PT02 |
| BR07 | Fuente y dueño de Contrato | Datos | PT02 |
| BR08 | Programación integrada y conciliada | Aplicación | PT04 |
| BR09 | Administración con identidad individual | Negocio | PT05 |
| BR10 | MFA en servicios críticos compatibles | Tecnología | PT05 |
| BR11 | Copias aisladas o inmutables y restauración | Tecnología | PT03 |
| BR12 | Registro y tratamiento de incidentes | Negocio | PT06 |
| BR13 | Evaluación y aprobación previa de cambios | Negocio | PT06 |
| BR14 | Inventario y registro de configuración | Aplicación | PT06 |
| BR15 | Registro y validación de cierre de homologación | Negocio | PT01 |
| BR16 | Revisión difusión y capacitación sobre política | Negocio | PT01 |
| BR17 | Conciliación de horas de equipos | Datos | PT02 |

### 5.4.2 Paquetes de trabajo derivados

Las brechas se agrupan en seis paquetes: PT01 Gobierno contractual y evidencia; PT02 Gobierno y conciliación del dato; PT03 Continuidad de enlace y respaldos; PT04 Integración y programación operativa; PT05 Identidad y control de acceso; PT06 Gestión de servicios, cambios y activos.

[AR03_paquetes.csv](AR03_paquetes.csv) conserva las brechas de cada paquete, su esfuerzo máximo y dependencias. La asignación se verifica para evitar brechas huérfanas. Estos paquetes son insumo del portafolio de la sección 7.1, sujeto a evaluación de beneficios, costos y recursos. Los S/ 1 460 000 del presupuesto anual de TI no son saldo acreditado para financiarlos.

### 5.4.3 Dependencias y secuencia obligada por el diseño propuesto

El algoritmo valida referencias y ciclos y calcula niveles de precedencia:

1. PT01 establece responsables, obligaciones y evidencias.
2. PT02, PT03, PT05 y PT06 preparan datos, continuidad, identidad y operación controlada. Pueden avanzar en paralelo según recursos.
3. PT04 utiliza esas condiciones para poner en operación las integraciones propuestas.

La salida se guarda en [AR03_secuencia.json](AR03_secuencia.json) y [AR03_salida.txt](../evidencias/S10/salidas/AR03_salida.txt). La secuencia es consecuencia del grafo de dependencias diseñado por el equipo; debe ratificarse con Operaciones y TI antes de construir la hoja de ruta. No se espera al paquete de integración para recuperar el respaldo satelital.

La validación registra carga y guardado con Archi 5.10, exportación de siete vistas, correspondencia documental de aplicaciones actuales, 17 brechas visibles AS/TB y comprobación de tipos de relación frente a la matriz oficial de Archi. No acredita implantación, aceptación del cliente ni aprobación del negocio. El repositorio se mantiene público por indicación del equipo; el requisito de privacidad sigue pendiente.

### Resumen de gobierno del dato

Fuentes: 2/6 declaradas (Equipo/Servicio), 2/6 expresamente ausentes (Personal/Contrato) y 2/6 no documentadas (Proveedor/Pago). Dueños: 2/6 cargos explícitos, 1/6 responsable de hecho (Personal), 1/6 expresamente ausente (Contrato), 2/6 no documentados. No se convierte información desconocida en ausencia comprobada. Proveedor/Pago requieren entrevista o metadatos del sistema de origen; no se inventa su ubicación actual en ERP. La clasificación confidencial de ambas es propuesta académica conservadora; su aprobación operativa no se presume.
