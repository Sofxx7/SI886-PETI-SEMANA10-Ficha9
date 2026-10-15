"""Caso 09. Ejecutar: python AR03_brechas.py. Requiere pandas.

Esfuerzo es una estimacion ordinal; no representa soles ni dias.
Las dependencias se resuelven por niveles topologicos y no con una secuencia fija.
"""
from pathlib import Path
from graphlib import TopologicalSorter, CycleError
import json
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parent
# id,capa,actual,objetivo,tipo,esfuerzo,paquete,origen,elemento_as_is,elemento_to_be
DATOS = [
('BR01','Negocio','Control de vencimientos en hoja; contrato satelital vencido','Control contractual con responsable y alertas','Modificar','Medio','PT01','FICHA F G H; inventario 2 5','AS_P07','TB_P07'),
('BR02','Tecnologia','Respaldo satelital inoperativo','Redundancia operativa con contrato y conmutacion probada','Modificar','Alto','PT03','FICHA G H; inventario 6','AS_T02','TB_T02'),
('BR03','Aplicacion','Integracion de personal mantenida por correo con exempleado','Integracion documentada y soportada por responsable formal','Reemplazar','Alto','PT04','Inventario 4','AS_A03','TB_A03'),
('BR04','Aplicacion','Transferencia mensual de personal al ERP','Transferencia validada con frecuencia aprobada segun necesidad','Modificar','Medio','PT04','Inventario 4; PA02 PA03','AS_S04','TB_S04'),
('BR05','Aplicacion','SSO aislado del ERP','Intercambio minimo necesario de personal y habilitaciones','Nuevo','Medio','PT04','Inventario 4; PA03 PA06','AS_A02','TB_S05'),
('BR06','Datos','Personal sin fuente autoritativa; responsable de hecho','Maestro validado con fuente y dueno formalizados','Modificar','Medio','PT02','Inventario 5','AS_D01','TB_D01'),
('BR07','Datos','Contratos sin fuente autoritativa ni dueno','Registro contractual con fuente dueno y calidad','Modificar','Medio','PT02','Inventario 5','AS_D03','TB_D03'),
('BR08','Aplicacion','Programacion en hoja de calculo sin soporte','Programacion integrada y conciliada con ERP','Migrar','Medio','PT04','Inventario 2 5; PA07','AS_A05','TB_A05'),
('BR09','Negocio','Administracion con cuentas compartidas','Administracion con identidad individual y trazabilidad','Modificar','Medio','PT05','FICHA F; PA04','AS_P08','TB_P08'),
('BR10','Tecnologia','MFA solo en correo corporativo','MFA en servicios criticos compatibles y excepciones controladas','Ampliar','Medio','PT05','FICHA F; PA04','AS_T06','TB_T06'),
('BR11','Tecnologia','Respaldo en disco conectado al servidor','Copias aisladas o inmutables con restauracion probada','Modificar','Medio','PT03','FICHA F; PA01','AS_T05','TB_T05'),
('BR12','Negocio','Soporte sin registro de incidentes','Gestion de incidentes con registro prioridad y cierre','Nuevo','Bajo','PT06','FICHA F; PA05','AS_P09','TB_P09'),
('BR13','Negocio','Formato de cambio completado despues de ejecutar','Cambio evaluado aprobado y verificable antes de aplicar','Modificar','Bajo','PT06','FICHA F; PA05','AS_P10','TB_P10'),
('BR14','Aplicacion','Soporte sin inventario de activos TI','Inventario y registro de configuracion con responsable','Nuevo','Medio','PT06','FICHA F; PA05','AS_P09','TB_A08'),
('BR15','Negocio','Homologacion con nueve observaciones abiertas','Registro de observaciones con evidencia y validacion de cierre','Modificar','Medio','PT01','FICHA C H; PA05','AS_P11','TB_P11'),
('BR16','Negocio','Politica de seguridad 2022 sin difusion ni revision','Politica revisada difundida y con capacitacion registrada','Modificar','Bajo','PT01','FICHA B F; PA06','AS_B01','TB_B01'),
('BR17','Datos','Horas de equipo diferentes entre ERP y libro','Horas de equipo conciliadas con reglas de aceptacion','Modificar','Medio','PT02','Inventario 5; PA02','AS_D02','TB_D02'),
]
COLUMNAS=['id','capa','actual','objetivo','tipo_brecha','esfuerzo','paquete','origen','elemento_as_is','elemento_to_be']
PAQUETES={
 'PT01':('Gobierno contractual y evidencia',[]),
 'PT02':('Gobierno y conciliacion del dato',['PT01']),
 'PT03':('Continuidad de enlace y respaldos',['PT01']),
 'PT04':('Integracion y programacion operativa',['PT02','PT03','PT05','PT06']),
 'PT05':('Identidad y control de acceso',['PT01']),
 'PT06':('Gestion de servicios cambios y activos',['PT01']),
}

def niveles_topologicos(dependencias):
    faltantes={d for ds in dependencias.values() for d in ds}-set(dependencias)
    if faltantes:
        raise ValueError(f'Dependencias desconocidas: {faltantes}')
    ts=TopologicalSorter(dependencias)
    ts.prepare()  # CycleError si la secuencia es imposible
    niveles=[]
    while ts.is_active():
        listos=sorted(ts.get_ready())
        niveles.append(listos)
        ts.done(*listos)
    return niveles

def main():
    b=pd.DataFrame(DATOS,columns=COLUMNAS)
    assert b.id.is_unique and len(b)>=10
    assert set(b.paquete)<=set(PAQUETES)
    assert b[COLUMNAS].notna().all().all()
    dependencias={p:datos[1] for p,datos in PAQUETES.items()}
    niveles=niveles_topologicos(dependencias)
    nivel={p:i for i,ns in enumerate(niveles,1) for p in ns}
    escala={'Bajo':1,'Medio':2,'Alto':3}
    assert set(b.esfuerzo)<=set(escala)
    b['dependencias_paquete']=b.paquete.map(lambda p:';'.join(dependencias[p]) or 'Ninguna')
    b.to_csv(ROOT/'AR03_brechas.csv',index=False,encoding='utf-8-sig')
    filas=[]
    for p,(nombre,deps) in PAQUETES.items():
        sub=b[b.paquete==p]
        assert len(sub)>0
        maximo=int(sub.esfuerzo.map(escala).max())
        filas.append({'paquete':p,'nombre':nombre,'brechas':';'.join(sub.id),'numero_brechas':len(sub),'esfuerzo_maximo':{1:'Bajo',2:'Medio',3:'Alto'}[maximo],'dependencias':';'.join(deps) or 'Ninguna','nivel':nivel[p]})
    pd.DataFrame(filas).to_csv(ROOT/'AR03_paquetes.csv',index=False,encoding='utf-8-sig')
    (ROOT/'AR03_secuencia.json').write_text(json.dumps({'niveles':niveles,'dependencias':dependencias,'criterio':'Orden tecnico propuesto. Dentro del mismo nivel se puede trabajar en paralelo sujeto a recursos. No es cronograma ni autorizacion presupuestal.'},ensure_ascii=False,indent=2),encoding='utf-8')
    lineas=[f'Python {sys.version.split()[0]} | pandas {pd.__version__}',f'Brechas totales: {len(b)}',b.groupby(['capa','tipo_brecha']).size().to_string(),'Esfuerzo ordinal, no costo ni plazo:',b.esfuerzo.value_counts().to_string(),'PAQUETES',pd.DataFrame(filas).to_string(index=False),'SECUENCIA POR DEPENDENCIAS']
    lineas += [f'Nivel {i}: '+', '.join(ns) for i,ns in enumerate(niveles,1)]
    lineas += ['Dependencias referenciadas: validas. Ciclos: ninguno. Cada brecha pertenece a un paquete.','PT03 incluye continuidad provisional mientras se cierra integracion; no esperar PT04 para recuperar el respaldo.','El cierre de homologacion requiere conocer las nueve observaciones; este analisis no acredita su cierre.']
    salida='\n\n'.join(lineas)+'\n'
    out=ROOT.parent/'evidencias'/'S10'/'salidas'
    out.mkdir(parents=True,exist_ok=True)
    (out/'AR03_salida.txt').write_text(salida,encoding='utf-8')
    print(salida)

if __name__=='__main__':
    main()
