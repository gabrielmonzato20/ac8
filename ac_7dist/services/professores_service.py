from model.professor import Professor
from infra.log import Log,to_dict

professores_db = []
import sqlite3
from wrap_connection import transact
aluno_db = []
class ProfessorJaExiste(Exception):
    pass
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
def make_connection():
    connection = sqlite3.connect("lms.db")
    connection.row_factory = dict_factory
    return connection

@transact(make_connection)   
def criar_db():
    create_sql = """CREATE TABLE IF NOT EXISTS Professor (id INTEGER PRIMARY KEY,nome TEXT NOT NULL)"""
    cursor.execute(create_sql)
criar_db()


@transact(make_connection)   
def resetar():
    delete_sql="""DELETE  FROM Professor """
    # aluno_db.clear()
    cursor.execute(delete_sql)
    connection.commit()
    return 'resetado'

@transact(make_connection) 
def listar():
    show_sql = """ SELECT * FROM Professor"""
    cursor.execute(show_sql)
    lista = cursor.fetchall()
    print('oi')
    print(to_dict(lista))
    return to_dict(lista)
@transact(make_connection) 
def localizar(id):
    sql_localizar = "SELECT id, nome FROM Professor WHERE id = ?"
    cursor.execute(sql_localizar, (id,))
    x = cursor.fetchone()
    if x == None:
        return None
    return x
@transact(make_connection) 
def criar(id,nome):
    sql_criar = "INSERT INTO Professor (id, nome) VALUES (?, ?)"
    if localizar(id) != None:
        raise ProfessorJaExiste
    log = Log(None)
    criado = Professor(id, nome)
    cursor.execute(sql_criar, (criado.id, criado.nome))
    connection.commit()

    log.finalizar(criado)
    return criado
@transact(make_connection) 
def remover(id):
    existente = localizar(id)
    if existente == None:
        return None
    log = Log(existente)
    delete_sql="""DELETE  FROM Professor where id = ? """
    # aluno_db.clear()
    cursor.execute(delete_sql,(id,))
    connection.commit()
    log.finalizar(None)
    return existente
@transact(make_connection) 
def atualizar(id_antigo, id_novo, nome):
    if id_antigo != id_novo:
        colisao = localizar(id_novo)
        if colisao != None:
            raise ProfessorJaExiste()
    existente = localizar(id_antigo)
    if existente == None:
        return None
    log = Log(existente)
    atualizar_sql="""UPDATE Professor SET id = ?, nome= ? where id = ?   """
    # aluno_db.clear()
    cursor.execute(atualizar_sql,(id_novo,nome,id_antigo))
    connection.commit()
    log.finalizar(existente)
    return existente


