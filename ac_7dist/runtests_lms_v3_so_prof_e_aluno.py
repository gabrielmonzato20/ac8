import requests
import unittest

class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5002/alunos')
        self.assertEqual(type(r.json()),type([]))

    def test_001_adiciona_alunos(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        r = requests.post('http://localhost:5002/alunos',json={'nome':'roberto','id':2})
        r_lista = requests.get('http://localhost:5002/alunos')
        achei_fernando = False
        achei_roberto = False
        for aluno in r_lista.json():
            if aluno['nome'] == 'fernando':
                achei_fernando = True
            if aluno['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_roberto:
            self.fail('aluno roberto nao apareceu na lista de alunos')

    def test_002_aluno_por_id(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'mario','id':20})
        r_id = requests.get('http://localhost:5002/alunos/20')
        self.assertEqual(r_id.json()['nome'],'mario')


    
    def test_003_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/alunos',json={'nome':'cicero','id':29})
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_004_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/alunos',json={'nome':'cicero','id':29})
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/alunos/28')
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_005_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        r_antes = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_antes.json()['nome'],'lucas')
        requests.put('http://localhost:5002/alunos/28', json={'nome':'lucas mendes', 'id':28})
        r_depois = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_depois.json()['nome'],'lucas mendes')

    def test_006_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/alunos/15',json={'nome':'bowser','id':15})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
        r = requests.get('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')
        r = requests.delete('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'aluno nao encontrado')

    def test_007_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'bond','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'james','id':7})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_008_post_ou_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'id':8})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'maximus','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/alunos/7',json={'id':7})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
    

    def test_100_professores_retorna_lista(self):
        r = requests.get('http://localhost:5002/professores')
        self.assertEqual(type(r.json()),type([]))
    
    def test_100b_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/alunos',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),0)
        r_lista_alunos = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_alunos.json()),2)

    def test_101_adiciona_professores(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'fernando','id':1})
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        r_lista = requests.get('http://localhost:5002/professores')
        achei_fernando = False
        achei_roberto = False
        for professor in r_lista.json():
            if professor['nome'] == 'fernando':
                achei_fernando = True
            if professor['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('professor fernando nao apareceu na lista de professores')
        if not achei_roberto:
            self.fail('professor roberto nao apareceu na lista de professores')

    def test_102_professores_por_id(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'mario','id':20})
        r_lista = requests.get('http://localhost:5002/professores/20')
        self.assertEqual(r_lista.json()['nome'],'mario')


    
    def test_103_adiciona_e_reseta(self):
        r = requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r_lista_depois = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista_depois.json()),0)

    def test_104_adiciona_e_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':28})
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),2)
        requests.delete('http://localhost:5002/professores/28')
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),1)
    
    def test_105_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':28})
        r_antes = requests.get('http://localhost:5002/professores/28')
        self.assertEqual(r_antes.json()['nome'],'lucas')
        requests.put('http://localhost:5002/professores/28', json={'nome':'lucas mendes', 'id':28})
        r_depois = requests.get('http://localhost:5002/professores/28')
        self.assertEqual(r_depois.json()['nome'],'lucas mendes')

    def test_106_id_inexistente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/professores/15',json={'nome':'bowser','id':15})
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')
        r = requests.get('http://localhost:5002/professores/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')
        r = requests.delete('http://localhost:5002/professores/15')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'professor nao encontrado')

    def test_107_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'bond','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'james','id':7})
        self.assertIn(r.status_code,[400,409])
        self.assertEqual(r.json()['erro'],'id ja utilizada')

    def test_108_post_ou_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'id':8})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':'maximus','id':7})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/professores/7',json={'id':7})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro',r.json())

    def test_109_nao_confundir_professor_e_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        r = requests.post('http://localhost:5002/professores',json={'nome':'fernando','id':1})
        self.assertEqual(r.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'roberto','id':2})
        self.assertEqual(r.status_code,200)
        r_lista = requests.get('http://localhost:5002/professores')
        self.assertEqual(len(r_lista.json()),2)
        r_lista_alunos = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_alunos.json()),0)
    
    '''
    def test_400_professor_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':'500'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':12,'id':501})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':502})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/professores/500',json={'nome':'lucas','id':'503'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_400a_professor_com_banana(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/professores',json={'nome':'lucas','id':504, 'banana':'madura'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
    
    def test_401_aluno_com_tipos_errados(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':'500'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':12,'id':500})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':501})
        self.assertEqual(r.status_code,200)
        r = requests.put('http://localhost:5002/alunos/500',json={'nome':'lucas','id':'503'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())

    def test_401a_aluno_com_frutas(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'abacate':'verde'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'melao':'de redinha'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':504, 'pera':'para deputada'})
        self.assertIn(r.status_code,[400,422])
        self.assertIn('erro', r.json())

   

    def test_500_log_professor(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/professores',json={'nome':'cicero','id':29})
        if 'cicero' not in open('sala_aula.log').read():
            self.fail('log incompleto')
    
    def test_501_log_aluno(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code,200)
        self.limpa_logs()
        r = requests.post('http://localhost:5002/alunos',json={'nome':'lucas','id':28})
        if 'lucas' not in open('sala_aula.log').read():
            self.fail('log incompleto')

        
    def limpa_logs(self):
       open('sala_aula.log', 'w').close()
    '''



    

    


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()
