"""Comprobaciones reproducibles; --archi-home permite usar la matriz oficial instalada."""
from pathlib import Path
import argparse
import csv
import json
import unittest
from xml.etree import ElementTree as E
from AR03_brechas import niveles_topologicos
from graphlib import CycleError

ROOT = Path(__file__).resolve().parent
TYPE = '{http://www.w3.org/2001/XMLSchema-instance}type'

class DependenciasTest(unittest.TestCase):
    def test_niveles(self):
        self.assertEqual(niveles_topologicos({'a': [], 'b': ['a'], 'c': ['a']}), [['a'], ['b', 'c']])
    def test_desconocida(self):
        with self.assertRaises(ValueError): niveles_topologicos({'a': ['inexistente']})
    def test_ciclo(self):
        with self.assertRaises(CycleError): niveles_topologicos({'a': ['b'], 'b': ['a']})

def validar(archi_home=None):
    root = E.parse(ROOT/'AR05_Cordillera.archimate').getroot()
    ids = [n.get('id') for n in root.iter() if n.get('id')]
    assert len(ids) == len(set(ids)), 'IDs duplicados'
    concepts = {n.get('id'): n for n in root.iter('element') if n.get(TYPE)}
    for n in root.iter():
        for attr in ['source', 'target', 'archimateElement', 'archimateRelationship']:
            if n.get(attr): assert n.get(attr) in ids, (attr, n.get(attr))
    views = [n for n in concepts.values() if n.get(TYPE).endswith('ArchimateDiagramModel')]
    assert len(views) == 7
    visible = {n.get('archimateElement') for v in views for n in v.findall('child')}
    with (ROOT/'AR03_brechas.csv').open(encoding='utf-8-sig') as f: gaps = list(csv.DictReader(f))
    with (ROOT/'AR07_trazabilidad.csv').open(encoding='utf-8-sig') as f: trace = list(csv.DictReader(f))
    assert {g['id'] for g in gaps} == {g['brecha'] for g in trace}
    for g in gaps:
        assert g['elemento_as_is'].startswith('AS_') and g['elemento_to_be'].startswith('TB_')
        assert g['elemento_as_is'] in visible and g['elemento_to_be'] in visible, g['id']
    assert sum(n.get(TYPE).endswith(':BusinessService') for n in concepts.values()) == 12
    assert all('AS_A'+str(i).zfill(2) in visible for i in [5, 6, 7])
    seq = json.loads((ROOT/'AR03_secuencia.json').read_text())
    assert niveles_topologicos(seq['dependencias']) == seq['niveles']
    for f in ROOT.parent.rglob('*.md'):
        assert '\ufffd' not in f.read_text(encoding='utf-8'), f
    relations = [n for n in concepts.values() if n.get(TYPE).endswith('Relationship')]
    if archi_home:
        folder = next((Path(archi_home)/'plugins').glob('com.archimatetool.model_*/model'))
        matrix = E.parse(folder/'relationships.xml').getroot()
        keys = {k.get('relationship'): k.get('char') for k in E.parse(folder/'relationships-keys.xml').getroot()}
        allowed = {(s.get('concept'), t.get('concept')): t.get('relations').lower() for s in matrix for t in s}
        for r in relations:
            src, dst = [concepts[r.get(a)].get(TYPE).split(':')[-1] for a in ['source','target']]
            typ = r.get(TYPE).split(':')[-1]
            assert keys[typ] in allowed.get((src, dst), ''), (r.get('id'),src,typ,dst)
        print(f'Matriz oficial de Archi: {len(relations)} relaciones permitidas; 0 inválidas.')
    print(f'7 vistas; 17 brechas visibles AS/TB; 12 servicios de negocio; 3 hojas actuales; IDs y referencias válidos; UTF-8 sin U+FFFD.')
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(DependenciasTest))
    assert result.wasSuccessful()

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--archi-home', type=Path)
    validar(parser.parse_args().archi_home)
