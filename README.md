# Taller S10 · Grupo 1 · Caso 09

Arquitectura empresarial de Servicios Mineros Cordillera S.A.C., organización ficticia del curso SI-886.

## Estado verificable

- Modelo nativo cargado, guardado y exportado con **Archi 5.10.0 / ArchiMate 3.2**: 106 conceptos, 113 relaciones y siete vistas.
- Tres hojas de cálculo actuales como componentes; seis servicios de negocio por estado y datos/gobierno explícitos.
- 17 brechas con tipo, esfuerzo ordinal y dependencias; seis paquetes en tres niveles.
- [Base estratégica propuesta](05_arquitectura/00_base_estrategica_caso09.md), [trazabilidad](05_arquitectura/AR07_trazabilidad.csv) y [validación](05_arquitectura/AR08_validacion.md).
- [Informe versionable sin códigos personales](INFORME_S10_Grupo1_avance.md). El Word y PDF con carátula completa se entregan por Drive/aula virtual, no en este repositorio público.
- El PR #1 ya estaba fusionado en develop; las correcciones se integran por [PR #2](https://github.com/Sofxx7/SI886-PETI-SEMANA10-Ficha9/pull/2) y se sincronizan con main.
- [Estado entregado `taller-10`](https://github.com/Sofxx7/SI886-PETI-SEMANA10-Ficha9/tree/taller-10); `v0.10` identifica el estado del PETI. Las etiquetas no certifican implantación o conformidad del negocio.

## Integrantes

Carbajal Vargas, Andre Alejandro · Yupa Gómez, Fátima Sofía · Llanos Niño, Vincenzo Rafael. Códigos reservados para la carátula del documento de entrega.

## Reproducir

Python 3.11+ y pandas (revisión con pandas 2.2.3). No se requiere Pillow ni una fuente Windows para generar el modelo.

```bash
python 05_arquitectura/AR03_brechas.py
python 05_arquitectura/AR05_modelo.py
python 05_arquitectura/AR09_validar.py --archi-home /ruta/a/Archi
```

Las PNG se exportan **desde Archi**; regenerar el XML no las actualiza automáticamente. Comando y procedencia en AR08_validacion.md. `graficos/V01_actual.png`, `V02_objetivo.png` y `V03_cooperacion.png` son las vistas principales; V04–V07 amplían datos, controles y brechas.

## Reservas de entrega

1. **Repositorio público por decisión expresa del equipo.** La guía exige privado; esa condición sigue pendiente. No se han cambiado permisos ni invitado colaboradores.
2. La base estratégica es una propuesta académica nueva, no un PETI histórico aprobado.
3. Sistema de origen de Proveedor/Pago, conteos por sistema de Servicio, detalle de las nueve observaciones y BIA deben confirmarse con fuentes adicionales. No se inventan datos ni aprobaciones.
4. La carga y exportación se ejecutaron con el motor de Archi vía CLI; no se afirma una sesión interactiva humana en su GUI.

Fuentes y alcance: [PROCEDENCIA.md](PROCEDENCIA.md).
