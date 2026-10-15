# Taller S10 Grupo 1 Caso 09

**Repositorio:** https://github.com/Sofxx7/SI886-PETI-SEMANA10-Ficha9

**Estado:** archivos y análisis preparados; validación del modelo y exportaciones desde Archi pendientes. La guía solicita repositorio privado; esta publicación pública no acredita ese requisito.

## Integrantes
- Carbajal Vargas, Andre Alejandro
- Yupa Gómez, Fátima Sofía
- Llanos Niño, Vincenzo Rafael

Los códigos se reservan para la carátula del informe de entrega. El caso es ficticio y sus insumos ya son públicos; véase [PROCEDENCIA.md](PROCEDENCIA.md).

## Contenido
- `INFORME_S10_Grupo1_avance.md`: contenido desarrollado siguiendo las siete secciones del documento grupal.
- `05_arquitectura/AR01_principios.md`: siete principios con los cinco campos.
- `05_arquitectura/AR02_entidades.csv`: seis entidades y sus límites de evidencia.
- `05_arquitectura/AR03_brechas.py`: análisis reproducible con pandas.
- `05_arquitectura/AR03_brechas.csv`: 17 brechas con IDs de ambos estados del modelo.
- `05_arquitectura/AR03_paquetes.csv`, `AR03_secuencia.json`: seis paquetes y secuencia por dependencias.
- `05_arquitectura/AR04_proceso_aplicacion.csv`: seis procesos y evaluación del soporte.
- `05_arquitectura/AR05_Cordillera.archimate`: modelo nativo generado, con cuatro vistas.
- `05_arquitectura/AR05_modelo.py`: generador y comprobación estructural del modelo.
- `05_arquitectura/AR05_catalogo.csv`: conceptos del modelo y su documentación.
- `05_arquitectura/AR06_derivacion_objetivo.md`: propuesta y trazabilidad al caso.
- `05_arquitectura/05_arquitectura_empresarial.md`: sección 5 del PETI.
- `graficos/`: tres PNG de revisión. Todavía no son exportaciones de Archi.
- `evidencias/S10/salidas/`: salidas de las ejecuciones realizadas.
- `fuentes/`: enlaces a los insumos públicos del caso ficticio 09 del curso.

## Reproducir

Requiere Python 3.11 o superior, pandas y Pillow. La ejecuci�n de este avance us� Python 3.13.15 y pandas 2.3.3.

```text
cd 05_arquitectura
python AR03_brechas.py
python AR05_modelo.py
```

## Cerrar el taller

1. Incorporar la visiín, capacidades, estrategias y marcos del PETI grupal del caso 09. No usar las secciones de Bitel o de la clínica.
2. Abrir `AR05_Cordillera.archimate` en Archi. Revisar elementos, relaciones y correspondencia con el caso. La comprobación XML no reemplaza esta validación.
3. Exportar desde Archi tres vistas PNG y reemplazar las previsualizaciones de revisión.
4. Validar sistemas de origen y due�os de Proveedor y Pago, cobertura de conteos de Personal y el BIA. Obtener las nueve observaciones de homologación.
5. Integrar el contenido al Word grupal, actualizar índice, revisar todas las páginas y exportar `SI886-S10-TALLER-Grupo1.pdf`.
6. Revisar el PR de `taller-10-caso09` hacia `develop` en este repositorio. Los archivos se publican como avance, con sus validaciones pendientes.
7. Crear `v0.10` y `taller-10` sobre el commit final, y publicar ambas etiquetas en el repositorio del equipo.
8. Sustituir las rutas locales del informe por URLs reales verificadas del repositorio y PR. El docente debe poder abrirlas con su cuenta autorizada. No declarar cumplida esta parte antes de verificar acceso.

Comandos de cierre después de las revisiones:

```text
git add 05_arquitectura graficos evidencias/S10
git commit -m "S10: arquitectura empresarial del caso 09 y analisis de brechas"
```

Después de fusionar el PR y situarse en el commit entregado:

```text
git tag -a v0.10 -m "PETI v0.10 arquitectura empresarial"
git tag -a taller-10 -m "Taller 10 SI886 Grupo 1 Caso 09"
git push origin v0.10 taller-10
```

Este repositorio corresponde al caso 09. La publicación de artefactos no acredita validación en Archi, etiquetas ni cierre de homologación. Los textos de las nueve observaciones todavía deben obtenerse y contrastarse.
