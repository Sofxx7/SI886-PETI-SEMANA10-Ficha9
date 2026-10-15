# Taller S10 Grupo 1 Caso 09

**Repositorio:** https://github.com/Sofxx7/SI886-PETI-SEMANA10-Ficha9

**Estado:** archivos y an�lisis preparados; validaci�n del modelo y exportaciones desde Archi pendientes. La gu�a solicita repositorio privado; esta publicaci�n p�blica no acredita ese requisito.

## Integrantes
- Carbajal Vargas, Andre Alejandro
- Yupa G�mez, F�tima Sof�a
- Llanos Ni�o, Vincenzo Rafael

Los c�digos se reservan para la car�tula del informe de entrega. El caso es ficticio y sus insumos ya son p�blicos; v�ase [PROCEDENCIA.md](PROCEDENCIA.md).

## Contenido
- `INFORME_S10_Grupo1_avance.md`: contenido desarrollado siguiendo las siete secciones del documento grupal.
- `05_arquitectura/AR01_principios.md`: siete principios con los cinco campos.
- `05_arquitectura/AR02_entidades.csv`: seis entidades y sus l�mites de evidencia.
- `05_arquitectura/AR03_brechas.py`: an�lisis reproducible con pandas.
- `05_arquitectura/AR03_brechas.csv`: 17 brechas con IDs de ambos estados del modelo.
- `05_arquitectura/AR03_paquetes.csv`, `AR03_secuencia.json`: seis paquetes y secuencia por dependencias.
- `05_arquitectura/AR04_proceso_aplicacion.csv`: seis procesos y evaluaci�n del soporte.
- `05_arquitectura/AR05_Cordillera.archimate`: modelo nativo generado, con cuatro vistas.
- `05_arquitectura/AR05_modelo.py`: generador y comprobaci�n estructural del modelo.
- `05_arquitectura/AR05_catalogo.csv`: conceptos del modelo y su documentaci�n.
- `05_arquitectura/AR06_derivacion_objetivo.md`: propuesta y trazabilidad al caso.
- `05_arquitectura/05_arquitectura_empresarial.md`: secci�n 5 del PETI.
- `graficos/`: tres PNG de revisi�n. Todav�a no son exportaciones de Archi.
- `evidencias/S10/salidas/`: salidas de las ejecuciones realizadas.
- `fuentes/`: enlaces a los insumos p�blicos del caso ficticio 09 del curso.

## Reproducir

Requiere Python 3.11 o superior, pandas y Pillow. La ejecuci�n de este avance us� Python 3.13.15 y pandas 2.3.3.

```text
cd 05_arquitectura
python AR03_brechas.py
python AR05_modelo.py
```

## Cerrar el taller

1. Incorporar la visi�n, capacidades, estrategias y marcos del PETI grupal del caso 09. No usar las secciones de Bitel o de la cl�nica.
2. Abrir `AR05_Cordillera.archimate` en Archi. Revisar elementos, relaciones y correspondencia con el caso. La comprobaci�n XML no reemplaza esta validaci�n.
3. Exportar desde Archi tres vistas PNG y reemplazar las previsualizaciones de revisi�n.
4. Validar sistemas de origen y due�os de Proveedor y Pago, cobertura de conteos de Personal y el BIA. Obtener las nueve observaciones de homologaci�n.
5. Integrar el contenido al Word grupal, actualizar �ndice, revisar todas las p�ginas y exportar `SI886-S10-TALLER-Grupo1.pdf`.
6. Revisar el PR de `taller-10-caso09` hacia `develop` en este repositorio. Los archivos se publican como avance, con sus validaciones pendientes.
7. Crear `v0.10` y `taller-10` sobre el commit final, y publicar ambas etiquetas en el repositorio del equipo.
8. Sustituir las rutas locales del informe por URLs reales verificadas del repositorio y PR. El docente debe poder abrirlas con su cuenta autorizada. No declarar cumplida esta parte antes de verificar acceso.

Comandos de cierre despu�s de las revisiones:

```text
git add 05_arquitectura graficos evidencias/S10
git commit -m "S10: arquitectura empresarial del caso 09 y analisis de brechas"
```

Despu�s de fusionar el PR y situarse en el commit entregado:

```text
git tag -a v0.10 -m "PETI v0.10 arquitectura empresarial"
git tag -a taller-10 -m "Taller 10 SI886 Grupo 1 Caso 09"
git push origin v0.10 taller-10
```

Este repositorio corresponde al caso 09. La publicaci�n de artefactos no acredita validaci�n en Archi, etiquetas ni cierre de homologaci�n. Los textos de las nueve observaciones todav�a deben obtenerse y contrastarse.
