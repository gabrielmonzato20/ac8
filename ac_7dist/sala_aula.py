
from flask import Flask, jsonify, request
from alunos_api import aluno_app
from professores_api import professores_app
from disciplina_api import  disciplina_app
from ofertada_api import  ofertada_app


app = Flask(__name__)
app.register_blueprint(aluno_app)
app.register_blueprint(professores_app)
app.register_blueprint(disciplina_app)
app.register_blueprint(ofertada_app)

from services.professores_service import resetar as reseta_professores
from services.aluno_service import resetar as reseta_aluno
from services.disciplina_service import resetar as reseta_disciplina
from services.ofertada_service import resetar as reseta_ofertada
@app.route('/reseta', methods=['POST'])
def reseta():
    reseta_aluno()
    reseta_professores()
    reseta_disciplina()
    reseta_ofertada()
    return 'resetado'

from services.professores_service import listar as listar_professores
from services.aluno_service import listar as listar_aluno
from services.disciplina_service import listar as listar_disciplina
from services.ofertada_service import listar as listar_ofertada
@app.route('/')
def all():
    database = {
        "ALUNOS": listar_aluno(),
        "PROFESSORES": listar_professores(),
        'DISCIPLINA':listar_disciplina(),
        'OFERTADA':listar_ofertada(),
    }
    return jsonify(database)


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)


