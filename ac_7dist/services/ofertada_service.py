from model.ofertada import Ofertada
from infra.log import Log
from services.professores_service import listar as lista_professor
from services.disciplina_service import resetar as reseta_disciplina

db_ofertada = []

class OfertadaJaExiste(Exception):
    pass

def resetar():
    db_ofertada.clear()

def listar():
    return db_ofertada

def localizar(id):
    for x in db_ofertada:
        if x.id == id:
            return x
    return None

def criar( id, ano,semestre,turma,data,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None):
    if localizar(id) != None:
        raise OfertadaJaExiste
    log = Log(None)
    criado = Ofertada( id, ano,semestre,turma,data,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None)
    professor_valido = False
    for professor in lista_professor():
        if professor.id == id_professor:
            professor_valido =True

    if professor_valido == False and id_professor!=None:
        return False
    db_ofertada.append(criado)
    log.finalizar(criado)
        
    return criado

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    db_ofertada.remove(existente)
    log.finalizar(existente)
    return existente

def atualizar(id_antigo, id_novo,ano,semestre,turma,data,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise OfertadaJaExiste()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    existente.atualizar(id_novo,ano,semestre,turma,data,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None)
    log.finalizar(existente)
    return existente
