"""Genera el modelo nativo. Las PNG se exportan con Archi, no con Pillow.
Ejecutar AR03_brechas.py antes y validar/exportar con Archi.
"""
from pathlib import Path
from xml.etree import ElementTree as E
import csv
import json

ROOT=Path(__file__).resolve().parent
XSI='http://www.w3.org/2001/XMLSchema-instance'
NS='http://www.archimatetool.com/archimate'
E.register_namespace('xsi',XSI)
E.register_namespace('archimate',NS)
model=E.Element('{'+NS+'}model',{'name':'Caso 09 Servicios Mineros Cordillera Grupo 1','id':'id-cordillera-s10-g1','version':'5.0.0'})
folders={}
for typ,name in [('strategy','Strategy'),('business','Business'),('application','Application'),('technology','Technology and Physical'),('motivation','Motivation'),('implementation_migration','Implementation and Migration'),('other','Other'),('relations','Relations'),('diagrams','Views')]:
    folders[typ]=E.SubElement(model,'folder',{'id':'id-folder-'+typ,'name':name,'type':typ})
catalog={}
relations=[]

def element(id,typ,name,layer,doc):
    e=E.SubElement(folders[layer],'element',{'{'+XSI+'}type':'archimate:'+typ,'id':id,'name':name})
    E.SubElement(e,'documentation').text=doc
    catalog[id]={'id':id,'type':typ,'name':name,'layer':layer,'documentation':doc}
    return id

def rel(typ,source,target,name=''):
    assert source in catalog and target in catalog
    id='id-rel-'+str(len(relations)+1)
    attrs={'{'+XSI+'}type':'archimate:'+typ+'Relationship','id':id,'source':source,'target':target}
    if name: attrs['name']=name
    E.SubElement(folders['relations'],'element',attrs)
    relations.append((id,source,target,typ))

procesos=['Licitacion y contratacion','Planificacion y ejecucion','Seguridad y salud ocupacional','Control de personal y campamento','Mantenimiento de equipos','Facturacion y valorizaciones']
for state in ['AS','TB']:
    propuesto=state=='TB'
    base='Propuesta de arquitectura objetivo; requiere validacion y aprobacion.' if propuesto else 'Estado actual documentado en FICHA D y arquitectura-actual 3.'
    for i,name in enumerate(procesos,1):
        element(f'{state}_P{i:02}','BusinessProcess',name,'business',base)
    aux=[('P07','Control contractual con alertas' if propuesto else 'Control contractual en hoja'),('P08','Administracion con identidad individual' if propuesto else 'Administracion con cuentas compartidas'),('P09','Soporte con registro de incidentes' if propuesto else 'Soporte reactivo sin registro'),('P10','Cambios aprobados antes de ejecutar' if propuesto else 'Cambios documentados despues de ejecutar'),('P11','Homologacion con evidencia y cierre validado' if propuesto else 'Homologacion con nueve observaciones abiertas')]
    for id,name in aux: element(state+'_'+id,'BusinessProcess',name,'business',base+' Fuentes FICHA C F H y PA05.')
    for i,name in enumerate(['Atención contractual al cliente','Ejecución del servicio minero','Aseguramiento de SSO','Control de acceso y asistencia','Disponibilidad de equipos','Valorización del servicio'],1):
        element(f'{state}_BS{i:02}','BusinessService',name,'business','Servicio abstraído de FICHA D; no implica un SLA medido.')
        rel('Realization',f'{state}_P{i:02}',f'{state}_BS{i:02}')
    for i,name in enumerate(['Personal','Equipo','Contrato','Servicio'],1):
        element(f'{state}_BO{i:02}','BusinessObject',name,'business','Concepto de negocio del inventario 5.')
    element(state+'_B01','BusinessObject','Politica de seguridad revisada y difundida' if propuesto else 'Politica de seguridad 2022 sin revision','business',base+' FICHA B.')
    for i,(name,typ) in enumerate([('Cliente minero','BusinessActor'),('Gerencia de Operaciones','BusinessRole'),('Superintendencia de TI','BusinessRole'),('Superintendencia de Mantenimiento','BusinessRole')],1):
        element(f'{state}_R{i:02}',typ,name,'business',base+' FICHA A B; inventario 5.')
    rel('Serving',state+'_BS01',state+'_R01')
    rel('Serving',state+'_BS06',state+'_R01')
    rel('Assignment',state+'_R02',state+'_P02')
    rel('Assignment',state+'_R04',state+'_P05')
    rel('Assignment',state+'_R03',state+'_P09')
    apps=[('A01','ERP corporativo','ERP corporativo'),('A02','SaaS SSO','SaaS SSO'),('A03','Control de personal e integracion dependiente de exempleado','Control de personal con integracion soportada'),('A04','Modulo ERP mantenimiento','Modulo ERP mantenimiento'),('A05','Hoja de programacion de servicios','Programacion integrada en ERP'),('A06','Hoja de vencimiento de contratos','Registro contractual con alertas'),('A07','Hoja de reportes de asistencia','Reporte de asistencia conciliado')]
    for id,actual,objetivo in apps:
        element(state+'_'+id,'ApplicationComponent',objetivo if propuesto else actual,'application',base+' Inventario 2 y 4. En TB se verifica capacidad del producto antes de adquirir o ampliar.')
    if propuesto:
        element('TB_A08','ApplicationComponent','Registro de activos configuracion e incidentes','application',base+' FICHA F; BR12 BR13 BR14. Producto por evaluar.')
    servicios=[('S01','Gestion de proyectos y finanzas','Gestion de proyectos y finanzas'),('S02','Gestion SSO','Gestion SSO'),('S03','Registro de personal y asistencia','Registro de personal conciliado'),('S04','Transferencia mensual de personal','Transferencia de personal con validacion'),('S06','Gestion de mantenimiento','Gestion de mantenimiento')]
    if propuesto: servicios.append(('S05','','Intercambio minimo SSO ERP'))
    for id,actual,objetivo in servicios:
        element(state+'_'+id,'ApplicationService',objetivo if propuesto else actual,'application',base+' Inventario 2 4 y PA03.')
    for aid,sid in [('A01','S01'),('A02','S02'),('A03','S03'),('A03','S04'),('A04','S06')]: rel('Realization',state+'_'+aid,state+'_'+sid)
    if propuesto: rel('Realization','TB_A02','TB_S05')
    for sid,pid in [('S01','P01'),('S01','P02'),('S02','P03'),('S03','P04'),('S06','P05'),('S01','P06')]: rel('Serving',state+'_'+sid,state+'_'+pid)
    rel('Serving',state+'_S04',state+'_A01')
    if propuesto: rel('Serving','TB_S05','TB_A01')
    datos=[('Personal en campamento','Sin fuente autoritativa; Operaciones como responsable de hecho. Conteos 420, hasta 700, 480, 420.'),('Equipo','ERP autoritativo; Superintendente de Mantenimiento; 310,310,290. Horas discrepantes.'),('Contrato','Sin fuente ni dueno; 140 en cada ubicacion, sin control efectivo de vigencia.'),('Servicio','ERP autoritativo; Gerente de Operaciones; 36 por anio, sin desglose por sistema.'),('Proveedor','Dataset entregado proveedores.csv con 210 registros. Sistema origen y dueno no documentados.'),('Pago','Dataset entregado pagos.csv con 25185 registros. Sistema origen y dueno no documentados.')]
    for i,(name,doc) in enumerate(datos,1):
        element(f'{state}_D{i:02}','DataObject',name+(' con gobierno propuesto' if propuesto else ''),'application',base+' '+('Fuente y dueno propuestos en AR02; validar.' if propuesto else doc))
    for aid,did in [('A01','D01'),('A03','D01'),('A02','D01'),('A04','D02'),('A01','D03'),('A06','D03'),('A01','D04'),('A05','D04')]: rel('Access',state+'_'+aid,state+'_'+did)
    for i in range(1,5): rel('Realization',f'{state}_D{i:02}',f'{state}_BO{i:02}')
    for aid,pid in [('A05','P02'),('A06','P07'),('A07','P04')]: rel('Serving',state+'_'+aid,state+'_'+pid)
    if propuesto:
        for did in ['D05','D06']: rel('Access','TB_A01','TB_'+did)
    tech=[('T01','Node','Nube privada del ERP','Nube privada del ERP'),('T02','TechnologyService','Enlace principal sin respaldo efectivo','Conectividad redundante con conmutacion probada'),('T03','Node','Servidor de control en campamento','Servidor de control con recuperacion probada'),('T04','Node','90 estaciones Tacna y 40 campamento','Estaciones registradas y administradas'),('T05','Device','Disco externo conectado al servidor','Copia aislada o inmutable con restauracion probada'),('T06','TechnologyService','MFA solo en correo','MFA en servicios criticos compatibles')]
    for id,typ,actual,objetivo in tech: element(state+'_'+id,typ,objetivo if propuesto else actual,'technology',base+' FICHA C F G; inventario 6.')
    element(state+'_T07','CommunicationNetwork','Red Tacna y red campamento','technology',base+' Inventario 6; se abstraen detalles sensibles.')
    element(state+'_T08','Node','Plataforma SaaS de SSO','technology',base+' Inventario 6.')
    rel('Association',state+'_T03',state+'_T05','respaldo actual' if not propuesto else 'recuperación propuesta')
    rel('Association',state+'_T06',state+'_P08','alcance de autenticación')
    for tid,aid in [('T01','A01'),('T03','A03'),('T08','A02')]:rel('Association',state+'_'+tid,state+'_'+aid,'ubicacion documentada' if not propuesto else 'ubicacion propuesta')
    for aid in ['A01','A03']:rel('Serving',state+'_T02',state+'_'+aid)
    rel('Association',state+'_T07',state+'_T02')

def view(id,name,items,notes=()):
    v=E.SubElement(folders['diagrams'],'element',{'{'+XSI+'}type':'archimate:ArchimateDiagramModel','id':id,'name':name})
    object_nodes={}
    for ix,(eid,x,y,w,h) in enumerate(items):
        obid=id+'-ob-'+str(ix)
        n=E.SubElement(v,'child',{'{'+XSI+'}type':'archimate:DiagramObject','id':obid,'archimateElement':eid})
        E.SubElement(n,'bounds',{'x':str(x),'y':str(y),'width':str(w),'height':str(h)})
        object_nodes.setdefault(eid,[]).append((obid,n,y))
    targets={}
    for rid,src,dst,typ in relations:
        if src in object_nodes and dst in object_nodes:
            for target,_,target_y in object_nodes[dst]:
                source,node,_=min(object_nodes[src],key=lambda ob:abs(ob[2]-target_y))
                cid=id+'-con-'+rid+'-'+target
                E.SubElement(node,'sourceConnection',{'{'+XSI+'}type':'archimate:Connection','id':cid,'source':source,'target':target,'archimateRelationship':rid})
                targets.setdefault(target,[]).append(cid)
    for objects in object_nodes.values():
        for obid,node,_ in objects:
            if obid in targets: node.set('targetConnections',' '.join(targets[obid]))
    for ix,(text,x,y,w,h) in enumerate(notes):
        n=E.SubElement(v,'child',{'{'+XSI+'}type':'archimate:Note','id':id+'-note-'+str(ix)})
        E.SubElement(n,'bounds',{'x':str(x),'y':str(y),'width':str(w),'height':str(h)})
        E.SubElement(n,'content').text=text
    return v

for st,nm in [('AS','01 Arquitectura actual'),('TB','02 Arquitectura objetivo')]:
    items=[]
    for i in range(1,7):
        x=40+(i-1)*270
        items += [(f'{st}_BS{i:02}',x,90,235,65),(f'{st}_P{i:02}',x,215,235,70)]
    for eid,x,y in [('S01',40,365),('S02',580,365),('S03',850,365),('S06',1120,365),('S04',1390,495),('A01',40,615),('A05',310,615),('A02',580,615),('A03',850,615),('A04',1120,615),('A07',1390,615),('T01',40,775),('T02',445,775),('T08',850,775),('T03',1120,775),('T04',1390,775),('T07',445,910),('T05',1120,910)]:
        items.append((st+'_'+eid,x,y,235,75))
    if st=='TB': items.append(('TB_S05',580,495,235,70))
    view('view-'+st,nm,items,[(nm+' | Caso 09 | Negocio → Aplicación → Tecnología. AS documentado; TB propuesto. Controles y brechas adicionales: vistas 04 a 07.',40,0,1585,60)])

with (ROOT/'AR04_proceso_aplicacion.csv').open(encoding='utf-8-sig') as f: coop=list(csv.DictReader(f))
items=[];notes=[]
for i,(sid,aid) in enumerate([('S01','A01'),('S01','A01'),('S02','A02'),('S03','A03'),('S06','A04'),('S01','A01')],1):
    y=80+i*170
    items += [(f'AS_P{i:02}',40,y,280,70),('AS_'+sid,380,y,270,70),('AS_'+aid,720,y,260,70)]
    notes.append((coop[i-1]['evaluacion']+': '+coop[i-1]['justificacion'],1040,y,470,95))
items += [('AS_A05',720,500,260,65),('AS_A07',720,840,260,65)]
view('view-coop','03 Cooperacion proceso aplicacion',items,[('Cooperación AS: 6 con soporte; 1 deficiente, 4 parciales, 1 adecuado según inventario. Evaluación analítica; no es medición de SLA.',40,20,1470,65)]+notes)

items=[];notes=[]
for j,st in enumerate(['AS','TB']):
    for i in range(1,7):
        items.append((f'{st}_D{i:02}',40+j*1000,130+(i-1)*190,300,80))
        info=catalog[f'{st}_D{i:02}']['documentation']
        notes.append((info,370+j*1000,130+(i-1)*190,600,125))
    for i,aid in enumerate(['A01','A02','A03','A04','A05','A06']): items.append((st+'_'+aid,40+j*1000,1320+i*100,300,65))
view('view-data','04 Informacion actual y objetivo',items,[('Información AS / TB: fuentes, dueños y límites documentados. Proveedor/Pago: origen actual desconocido; no se inventa un sistema operativo.',40,20,1930,70)]+notes)
for st,nm in [('AS','05 Gobierno actual'),('TB','06 Gobierno objetivo')]:
    keys=['R01','R02','R03','R04','P07','P08','P09','P10','P11','B01','A06','T06']
    if st=='TB': keys+=['A08']
    keys += [f'BO{i:02}' for i in range(1,5)]+[f'D{i:02}' for i in range(1,5)]
    items=[(st+'_'+eid,40+(i%4)*350,120+(i//4)*160,290,90) for i,eid in enumerate(keys)]
    view('view-'+st+'-gov',nm,items,[(nm+' | Roles, controles y objetos de negocio. Fuente: FICHA B/C/F/H e inventario. Propuestas TB no implantadas.',40,20,1340,60)])
with (ROOT/'AR03_brechas.csv').open(encoding='utf-8-sig') as f: gaps=list(csv.DictReader(f))
for g in gaps:
    rel('Association',g['elemento_as_is'],g['elemento_to_be'],g['id']+' / '+g['tipo_brecha'])
items=[]
for i,g in enumerate(gaps):
    for j,k in enumerate(['elemento_as_is','elemento_to_be']):
        eid=g[k]
        items.append((eid,40+j*740,140+i*150,500,95))
notes=[(g['id']+' | '+g['capa']+' | '+g['tipo_brecha']+' | '+g['paquete'],560,140+i*150,200,90) for i,g in enumerate(gaps)]
view('view-gaps','07 Brechas actual objetivo',items,[('Brechas AS → TB | Origen y criterios en AR03_brechas.csv y AR07_trazabilidad.csv. No representa migración ejecutada.',40,20,1240,70)]+notes)
E.SubElement(model,'purpose').text='Caso académico ficticio 09. AS basado en FICHA e inventario; TB propuesto. Sin IP, secretos ni registros personales. Mantener público fue decisión del equipo; requisito privado pendiente.'
E.indent(model,space='  ')
E.ElementTree(model).write(ROOT/'AR05_Cordillera.archimate',encoding='utf-8',xml_declaration=True)
with (ROOT/'AR05_catalogo.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','type','name','layer','documentation'],lineterminator='\n');w.writeheader();w.writerows(catalog.values())

# Comprobacion estructural, distinta de validacion semantica en Archi.
tree=E.parse(ROOT/'AR05_Cordillera.archimate')
ids=[n.get('id') for n in tree.iter() if n.get('id')]
assert len(ids)==len(set(ids)), 'IDs repetidos'
for n in tree.iter():
    for attr in ['source','target','archimateElement','archimateRelationship']:
        if n.get(attr):assert n.get(attr) in set(ids),(attr,n.get(attr))
with (ROOT/'AR03_brechas.csv').open(encoding='utf-8-sig') as f:
    gaps=list(csv.DictReader(f))
for g in gaps:
    assert g['elemento_as_is'] in catalog and g['elemento_to_be'] in catalog
    assert g['elemento_as_is'].startswith('AS_') and g['elemento_to_be'].startswith('TB_')
salida=f'XML nativo generado y parseable. Conceptos: {len(catalog)}. Relaciones: {len(relations)}. Vistas: 7. Brechas con identificadores en ambos estados: {len(gaps)}. IDs unicos y referencias internas validas.\nEsta salida comprueba estructura. La ejecución de Archi y revisión semántica se registran separadamente en AR08_validacion.md.\n'
(ROOT.parent/'evidencias/S10/salidas/AR05_validacion_estructural.txt').write_text(salida,encoding='utf-8')
print(salida)
