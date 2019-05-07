from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
disciplina_app = Blueprint('disciplina_app', __name__, template_folder='templates')
from services.disciplina_service import (
    listar as service_listar, 
    localizar as service_localizar, 
    criar as service_criar, 
    remover as service_remover, 
    atualizar as service_atualizar,
    DisciplinaJaExiste)



campos = ["id", "nome",'status','plano_ensino','carga_horaria']
tipos = {"id":int, "nome": str,'status':int,'plano_ensino':str,'carga_horaria':int}
campos_n_obj = ['id_coordenador']


@disciplina_app.route('/disciplinas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@disciplina_app.route('/disciplinas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None: 
        return jsonify(to_dict(x))
    return jsonify({'erro':'disciplina nao encontrada'}), 404

@disciplina_app.route('/disciplinas', methods=['POST'])
def criar():
    dados = request.json
    coodernador=None
    validar=validar_campos(dados, campos, tipos)
    if 'id_coordenador' in dados.keys():
       validar = validar_campos(dados, campos, tipos,campos_n_obj)
       coodernador = dados['id_coordenador']
    if not validar:
        print(validar)
        print(dados)
        print(campos)
        print(tipos)
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        criado = service_criar(dados['id'],dados['nome'],dados['status'],dados['plano_ensino'],dados['carga_horaria'],coodernador)
        return jsonify(to_dict(criado))
    except DisciplinaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409


@disciplina_app.route('/disciplinas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'disciplina nao encontrada'}), 404

@disciplina_app.route('/disciplinas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    coodernador=None
    if 'id_cooodernador' in dados.keys():
        campos.append('id_coodernador')
        tipos['id_coodernador'] = int
        coodernador = dados['id_coodernador']
    index = 0
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        atualizado = service_atualizar(id,dados['id'],dados['nome'],dados['status'],dados['plano_ensino'],dados['carga_horaria'],coodernador)
    except DisciplinaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'disciplina nao encontrada'}), 404
