# Validación del taller S10 — 15 de octubre de 2026

## 1. Carga, capas y relaciones

Se ejecutó **Archi 5.10.0 para Linux**, distribución oficial con SHA-256 `f9422455a00a22f5340dc28692ceafe0ad720c8cde839eaafb0fab1cea57287f`. Su CLI cargó el modelo, generó las imágenes de las siete vistas y guardó una copia nativa. La copia se volvió a cargar y exportar para comprobar el ciclo de lectura/escritura.

Comando reproducible, sustituyendo ARCHI por la ubicación del ejecutable:

```bash
"$ARCHI" -application com.archimatetool.commandline.app -consoleLog -nosplash -a \
  --loadModel "$PWD/05_arquitectura/AR05_Cordillera.archimate" \
  --html.createReport "$PWD/reporte-archi" \
  --saveModel "$PWD/cordillera-roundtrip.archimate"
python 05_arquitectura/AR09_validar.py --archi-home /ruta/a/Archi
```

Las PNG publicadas en `graficos/` se copiaron sin redibujar de la salida `images/` del exportador HTML de Archi. No son imágenes de Pillow ni capturas de una interfaz gráfica. Evidencia: [Archi_exportacion.txt](../evidencias/S10/salidas/Archi_exportacion.txt), [Archi_roundtrip.txt](../evidencias/S10/salidas/Archi_roundtrip.txt) y [AR09_pruebas.txt](../evidencias/S10/salidas/AR09_pruebas.txt).

Revisión: procesos, roles, actores, objetos y servicios de negocio en negocio; componentes, servicios y objetos de datos en aplicación; nodos, dispositivos, red y servicios de tecnología en tecnología. Las seis entidades se representan como `DataObject` en aplicación, no como una cuarta capa ArchiMate inventada. Se verificaron 113 relaciones contra `relationships.xml` y `relationships-keys.xml` distribuidos con esta versión de Archi: **0 tipos de relación inválidos**. Esto comprueba admisibilidad de tipos; no convierte el contenido en una arquitectura operativa aprobada.

## 2. Correspondencia de las aplicaciones actuales

| ID AS | Aplicación | Fuente del caso | Resultado |
|---|---|---|---|
| AS_A01 | ERP corporativo | FICHA C; inventario 2 | Existencia acreditada |
| AS_A02 | Gestión SSO | FICHA C; inventario 2 | Existencia acreditada; SSO significa seguridad y salud ocupacional, no inicio de sesión único |
| AS_A03 | Control de personal e integración | FICHA C; inventario 2 y 4 | Existencia acreditada; el nombre agrupa el control y su soporte de integración, no un producto adicional |
| AS_A04 | Mantenimiento | FICHA C; inventario 2 | Módulo del mismo ERP, no producto independiente |
| AS_A05 | Hoja de programación | Inventario 2 | Incluida como componente de aplicación |
| AS_A06 | Hoja de vencimientos | Inventario 2 | Incluida como componente de aplicación |
| AS_A07 | Hoja de asistencia al cliente | Inventario 2 | Incluida como componente de aplicación |

El enlace se retiró de aplicación y se mantiene en tecnología. No se atribuyen ERP de proveedores/pagos, APIs ni productos nuevos al estado actual. Los servicios de negocio son abstracciones analíticas de los seis procesos de FICHA D, no contratos/SLA adicionales.

## 3. Correspondencia de las brechas en ambos modelos

Las 17 filas de [AR07_trazabilidad.csv](AR07_trazabilidad.csv) conservan origen, concepto AS, concepto TB y criterio de aceptación. Ambos extremos se muestran en la vista **07 Brechas actual objetivo**, incluso cuando un mismo concepto interviene en dos brechas. BR14 parte del soporte reactivo AS_P09 y propone un registro de configuración TB_A08; no afirma que existiera un inventario actual. BR05 parte del SaaS aislado y propone su servicio de intercambio, no una integración ya existente.

El chequeo automático exige 17 IDs únicos de brecha, referencias válidas, extremos visibles y cobertura de la matriz estratégica. Se probaron orden topológico, ciclo y dependencia desconocida. Las imágenes se revisaron para comprobar presencia de etiquetas, flechas y estados; los PNG grandes deben consultarse a tamaño original, no solo dentro de la página del informe.

## 4. Problemas corregidos y límites

- Se añadieron servicios y objetos de negocio, servicios de aplicación visibles y vistas de controles y datos conectadas.
- La cooperación incluye evaluación del soporte; las brechas pueden señalarse en ambos estados.
- Se eliminó la dependencia de una fuente Windows: el generador ya no renderiza PNG; los exporta Archi.
- Se reparó UTF-8 y se actualizaron PR, enlaces, índice y figuras del informe.
- **Privacidad pendiente:** el equipo indicó mantener público el repositorio. No se declara cumplida la condición de repositorio privado ni se publica la carátula con códigos estudiantiles en GitHub.
- **Fuentes pendientes:** no constan sistema de origen de Proveedor/Pago, conteos de Servicio por sistema, texto de las nueve observaciones ni aceptación del BIA. Esos faltantes no se inventan. La clasificación propuesta y los dueños objetivo deben ratificarse.
- La base estratégica es una propuesta académica nueva para este caso, no un documento histórico ni una aprobación de la organización.
- Se usó el motor nativo y exportador de Archi vía CLI; no se registra una sesión interactiva humana en la GUI. Si el docente exige evidencia específica de esa interacción, debe añadirla el equipo.
