"""Genera el modelo nativo de Archi y tres vistas de revision.

Las vistas PNG son previsualizaciones del mismo catalogo; no se declaran
exportaciones de Archi. Abrir el .archimate en Archi y exportar las vistas
tras validar semantica y presentacion. Requiere Pillow para las PNG.
"""
from pathlib import Path
from xml.etree import ElementTree as E
import csv
import json
import textwrap
from PIL import Image, ImageDraw, ImageFont

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
    element(state+'_B01','BusinessObject','Politica de seguridad revisada y difundida' if propuesto else 'Politica de seguridad 2022 sin revision','business',base+' FICHA B.')
    for i,(name,typ) in enumerate([('Cliente minero','BusinessActor'),('Gerencia de Operaciones','BusinessRole'),('Superintendencia de TI','BusinessRole'),('Superintendencia de Mantenimiento','BusinessRole')],1):
        element(f'{state}_R{i:02}',typ,name,'business',base+' FICHA A B; inventario 5.')
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
    if propuesto:
        for did in ['D05','D06']: rel('Access','TB_A01','TB_'+did)
    tech=[('T01','Node','Nube privada del ERP','Nube privada del ERP'),('T02','TechnologyService','Enlace principal sin respaldo efectivo','Conectividad redundante con conmutacion probada'),('T03','Node','Servidor de control en campamento','Servidor de control con recuperacion probada'),('T04','Node','90 estaciones Tacna y 40 campamento','Estaciones registradas y administradas'),('T05','Device','Disco externo conectado al servidor','Copia aislada o inmutable con restauracion probada'),('T06','TechnologyService','MFA solo en correo','MFA en servicios criticos compatibles')]
    for id,typ,actual,objetivo in tech: element(state+'_'+id,typ,objetivo if propuesto else actual,'technology',base+' FICHA C F G; inventario 6.')
    element(state+'_T07','CommunicationNetwork','Red Tacna y red campamento','technology',base+' Inventario 6; se abstraen detalles sensibles.')
    element(state+'_T08','Node','Plataforma SaaS de SSO','technology',base+' Inventario 6.')
    for tid,aid in [('T01','A01'),('T03','A03'),('T08','A02')]:rel('Association',state+'_'+tid,state+'_'+aid,'ubicacion documentada' if not propuesto else 'ubicacion propuesta')
    for aid in ['A01','A03']:rel('Serving',state+'_T02',state+'_'+aid)
    rel('Association',state+'_T07',state+'_T02')

def view(id,name,items):
    v=E.SubElement(folders['diagrams'],'element',{'{'+XSI+'}type':'archimate:ArchimateDiagramModel','id':id,'name':name})
    object_nodes={}
    for ix,(eid,x,y,w,h) in enumerate(items):
        obid=id+'-ob-'+str(ix)
        n=E.SubElement(v,'child',{'{'+XSI+'}type':'archimate:DiagramObject','id':obid,'archimateElement':eid})
        E.SubElement(n,'bounds',{'x':str(x),'y':str(y),'width':str(w),'height':str(h)})
        object_nodes[eid]=(obid,n)
    targets={}
    for rid,src,dst,typ in relations:
        if src in object_nodes and dst in object_nodes:
            source,node=object_nodes[src];target,_=object_nodes[dst]
            cid=id+'-con-'+rid
            E.SubElement(node,'sourceConnection',{'{'+XSI+'}type':'archimate:Connection','id':cid,'source':source,'target':target,'archimateRelationship':rid})
            targets.setdefault(dst,[]).append(cid)
    for eid,cons in targets.items():object_nodes[eid][1].set('targetConnections',' '.join(cons))

for st,nm in [('AS','01 Arquitectura actual'),('TB','02 Arquitectura objetivo')]:
    items=[]
    for row,ids in enumerate([[f'{st}_P{i:02}' for i in range(1,7)],[f'{st}_A{i:02}' for i in range(1,8)],[f'{st}_T{i:02}' for i in range(1,7)]]):
        for j,eid in enumerate(ids):items.append((eid,40+(j%4)*245,30+row*220+(j//4)*90,220,65))
    view('view-'+st,nm,items)
view('view-coop','03 Cooperacion proceso aplicacion',[(f'AS_P{i:02}',30,30+(i-1)*100,250,65) for i in range(1,7)]+[(f'AS_{sid}',390,30+(i-1)*100,250,65) for i,sid in enumerate(['S01','S02','S03','S06'],1)])
view('view-data','04 Informacion actual y objetivo',[(f'{st}_D{i:02}',30+j*400,30+(i-1)*100,330,65) for j,st in enumerate(['AS','TB']) for i in range(1,7)])
E.SubElement(model,'purpose').text='Taller S10 Grupo 1. Organizacion ficticia del caso academico 09 publicado por OscarJimenezFlores/PETI en GitHub publico. No es infraestructura real. Estado actual derivado exclusivamente de ese material publico; objetivo propuesto. Sin IP credenciales rutas internas ni datos privados. Validacion en Archi pendiente. Ver PROCEDENCIA.md.'
E.indent(model,space='  ')
E.ElementTree(model).write(ROOT/'AR05_Cordillera.archimate',encoding='utf-8',xml_declaration=True)
with (ROOT/'AR05_catalogo.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['id','type','name','layer','documentation']);w.writeheader();w.writerows(catalog.values())

# Previsualizaciones de lectura, NO exportaciones de Archi.
G=ROOT.parent/'graficos';G.mkdir(exist_ok=True)
fontpath=Path('C:/Windows/Fonts/arial.ttf')
def font(n):return ImageFont.truetype(str(fontpath),n)
def preview(name,title,columns,rows,foot):
    width=1800; left=40; top=155; rowh=125
    height=top+len(rows)*rowh+130
    im=Image.new('RGB',(width,height),'white');d=ImageDraw.Draw(im)
    d.text((left,25),title,font=font(34),fill='#16285c')
    d.text((left,80),'Caso 09 | Grupo 1 | Vista de revision previa a validacion en Archi',font=font(22),fill='#555555')
    colw=(width-80)/len(columns)
    colors=['#fff3c9','#dceffc','#e0f2dd']
    for j,c in enumerate(columns):d.text((left+j*colw,top-40),c,font=font(24),fill='#16285c')
    for i,row in enumerate(rows):
        for j,txt in enumerate(row):
            x=left+j*colw;y=top+i*rowh
            d.rounded_rectangle((x,y,x+colw-18,y+rowh-18),radius=7,fill=colors[j%len(colors)],outline='#78869b',width=2)
            lines=textwrap.wrap(txt,width=int(colw/13))
            for k,line in enumerate(lines[:4]):d.text((x+15,y+14+k*23),line,font=font(21),fill='#172331')
    for k,line in enumerate(textwrap.wrap(foot,width=130)):d.text((left,height-95+k*25),line,font=font(20),fill='#555555')
    im.save(G/name)

preview('V01_actual_revision.png','Arquitectura actual de Servicios Mineros Cordillera',['Negocio','Aplicacion','Tecnologia'],[
('Licitacion y contratacion','ERP proyectos compras y finanzas','Nube privada del proveedor con SLA'),
('Planificacion y ejecucion','ERP mas hoja de programacion','Enlace Tacna campamento sin respaldo efectivo'),
('Seguridad y salud ocupacional','SaaS SSO sin integracion ERP','Plataforma SaaS del proveedor'),
('Control de personal y campamento','Biometrico sistema proveedor hoja de asistencia','Servidor de campamento'),
('Mantenimiento de equipos','Modulo del ERP y libro de operaciones','Nube privada del proveedor'),
('Facturacion y valorizaciones','ERP y contraste de horas con informe al cliente','90 estaciones en Tacna y 40 en campamento')],
'La tabla relaciona soportes documentados, no contratos de servicio medidos. Radioenlace y respaldo son tecnologia; no componentes de aplicacion. Fuentes: FICHA e inventario del caso.')
preview('V02_objetivo_revision.png','Arquitectura objetivo propuesta',['Negocio','Aplicacion','Tecnologia'],[
('Obligaciones y homologacion con evidencia','Registro contractual con alertas','Plataformas existentes con soporte validado'),
('Planificacion y horas conciliadas','Programacion integrada con ERP','Conectividad redundante con pruebas'),
('SSO con intercambio minimo necesario','Integracion documentada y controlada','Identidad reforzada en servicios compatibles'),
('Asistencia validada antes de reportar','Control de personal con soporte formal','Recuperacion probada en campamento'),
('Incidentes cambios y activos registrados','Registro de servicios y configuracion','Copias aisladas o inmutables'),
('Valorizaciones con horas aceptadas','ERP con maestros y reglas de conciliacion','Infraestructura inventariada y monitoreada')],
'Todos los cambios son propuestas. Capacidades de productos, frecuencias, RTO RPO y presupuesto deben validarse. La arquitectura no acredita ejecucion ni cierre de observaciones.')
preview('V03_cooperacion_revision.png','Cooperacion proceso aplicacion',['Proceso','Soporte actual','Evaluacion del soporte'],[
(procesos[0],'ERP corporativo','Adecuado segun inventario; sin prueba de SLA del proceso'),
(procesos[1],'ERP y hoja de programacion','Parcial; horas e informes discrepantes'),
(procesos[2],'SaaS SSO','Parcial; sin integracion al ERP'),
(procesos[3],'Biometrico proveedor y hoja de reporte','Deficiente; integracion dependiente de exempleado'),
(procesos[4],'ERP mantenimiento y libro','Parcial; horas por conciliar'),
(procesos[5],'ERP finanzas y proyectos','Parcial; validar horas antes de valorizar')],
'Seis procesos con algun soporte. Cinco presentan soporte parcial o deficiente; ninguno esta totalmente sin sistema segun la ficha. Evaluacion analitica, no medicion de disponibilidad.')

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
salida=f'XML nativo generado y parseable. Conceptos: {len(catalog)}. Relaciones: {len(relations)}. Vistas: 4. Brechas con identificadores en ambos estados: {len(gaps)}. IDs unicos y referencias internas validas.\nNo ejecutado: apertura y validacion semantica en Archi; exportacion PNG desde Archi.\n'
(ROOT.parent/'evidencias/S10/salidas/AR05_validacion_estructural.txt').write_text(salida,encoding='utf-8')
print(salida)
