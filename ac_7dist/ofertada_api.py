from flask import Blueprint, jsonify, request
from infra.validacao import validar_campos
from infra.to_dict import to_dict, to_dict_list
ofertada_app = Blueprint('ofertada_app', __name__, template_folder='templates')
from services.ofertada_service import (
    listar as service_listar, 
    localizar as service_localizar, 
    criar as service_criar, 
    remover as service_remover, 
    atualizar as service_atualizar,
     OfertadaJaExiste)


campos = ["id", "ano",'semestre','turma','data']
tipos = {"id":int, "ano": int,'semestre':int,'turma':str,'data':str}
campos_n_obj = []


@ofertada_app.route('/ofertadas', methods=['GET'])
def listar():
    lista = service_listar()
    return jsonify(to_dict_list(lista))

@ofertada_app.route('/ofertadas/<int:id>', methods=['GET'])
def localizar(id):
    x = service_localizar(id)
    if x != None:
        return jsonify(to_dict(x))
    return jsonify({'erro':'ofertada nao encontrada'}), 404

@ofertada_app.route('/ofertadas', methods=['POST'])
def criar():
    dados = request.json
    coodernador=None
    disciplina=None
    curso=None
    professor = None
    validar = validar_campos(dados, campos, tipos)
    validado = False
    if 'id_coordenador' in dados.keys():
        campos_n_obj.append('id_coordenador')
        coodernador = dados['id_coordenador']
        validado = True
    if 'id_disciplina' in dados.keys():
        campos_n_obj.append('id_disciplina')
        disciplina = dados['id_disciplina']
        validado = True
    if 'id_curso' in dados.keys():
        campos_n_obj.append('id_curso')
        curso = dados['id_curso']
        validado = True
    if 'id_professor' in dados.keys():
        campos_n_obj.append('id_professor')
        professor = dados['id_professor']
        validado = True
    if validado:
        validar=validar_campos(dados, campos, tipos,campos_n_obj)
        campos_n_obj.clear()
    if not  validar:
       print(campos)
       print(dados)
       print(tipos)
       return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        criado = service_criar(dados['id'],dados['ano'],dados['semestre'],dados['turma'],dados['data'],coodernador,disciplina,curso,professor)
        if not criado:
            return jsonify({'erro':'id professor invalido '}),400
        return jsonify(to_dict(criado))
    except OfertadaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409


@ofertada_app.route('/ofertadas/<int:id>', methods=['DELETE'])
def remover(id):
    removido = service_remover(id)
    if removido != None:
        return jsonify(to_dict(removido))
    return jsonify({'erro':'ofertada nao encontrada'}), 404

@ofertada_app.route('/ofertadas/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.json
    coodernador=None
    disciplina=None
    curso=None
    professor = None
    if 'id_cooodernador' in dados.keys():
        campos.append('id_coodernador')
        tipos['id_coodernador'] = int
        coodernador = dados['id_coodernador']
    if 'id_disciplina' in dados.keys():
        campos.append('id_disciplina')
        tipos['id_disciplina'] = int
        disciplina = dados['id_disciplina']
    if 'id_curso' in dados.keys():
        campos.append('id_curso')
        tipos['id_curso'] = int
        curso = dados['id_curso']
    if 'id_professor' in dados.keys():
        campos.append('id_professor')
        tipos['id_professor'] = int
        professor = dados['id_professor']
    index = 0
    if not validar_campos(dados, campos, tipos):
        return jsonify({'erro':'campo faltando ou valor invalido'}), 422
    try:
        atualizado = service_atualizar(id,dados['id'],dados['ano'],dados['semestre'],dados['turma'],dados['data'],coodernador,disciplina,curso,professor)
    except OfertadaJaExiste:
        return jsonify({'erro':'id ja utilizada'}), 409
    if atualizado != None:
        return jsonify(to_dict(atualizado))
    return jsonify({'erro':'ofertada nao encontrada'}), 404
