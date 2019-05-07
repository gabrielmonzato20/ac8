from model.disciplina import Disciplina
from infra.log import Log

disciplina_db = []

class DisciplinaJaExiste(Exception):
    pass

def resetar():
    disciplina_db.clear()

def listar():
    return disciplina_db

def localizar(id):
    for x in disciplina_db:
        if x.id == id:
            return x
    return None

def criar(id, nome,status,plano_ensino,carga_horaria,id_coodernador=None):
    if localizar(id) != None:
        raise DisciplinaJaExiste
    log = Log(None)
    criado = Disciplina(id, nome,status,plano_ensino,carga_horaria,id_coodernador=None)
    disciplina_db.append(criado)
    log.finalizar(criado)
    return criado  

def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    disciplina_db.remove(existente)
    log.finalizar(existente)
    return existente

def atualizar(id_antigo, id_novo, nome,status,plano_ensino,carga_horaria,id_coodernador=None):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise DisciplinaJaExiste()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    existente.atualizar(id_novo, nome)
    log.finalizar(existente)
    return existente
