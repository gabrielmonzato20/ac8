class Ofertada():
    def __init__(self, id, ano,semestre,turma,data,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None):
        self.__id = id
        self.__ano = ano
        self.__semestre = semestre
        self.__turma= turma
        self.__data = data
        self.__id_coodernador = id_coodernador
        self.__id_disciplina = id_disciplina
        self.__id_curso = id_curso
        self.__id_professor = id_professor

    def atualizar(self, id=None, ano=None,semestre=None,turma=None,data=None,id_coodernador=None,id_disciplina=None,id_curso=None,id_professor=None):
        if id == None:
            pass
        else:
            self.__id = id
        if ano == None:
            pass
        else:
            self.__ano = ano
        if semestre == None:
            pass
        else:
            self.__semestre = semestre
        if turma == None:
            pass
        else:
             self.__turma= turma
        if data == None:
            pass
        else:
            self.__data = data
        if id_coodernador == None:
            pass
        else:
            self.__id_coodernador = id_coodernador
        if id_disciplina == None:
            pass
        else:
            self.__id_disciplina = id_disciplina
        if id_curso == None:
            pass
        else:
            self.__id_curso = id_curso
        if id_professor == None:
            pass
        else:
            self.__id_professor = id_professor
        
        
        return self

    @property
    def id(self):
        return self.__id 
    @property
    def ano(self):
       return self.__ano
  

    @property
    def semestre(self):
        return self.__semestre
    @property
    def turma(self):
        return self.__turma

    @property
    def data(self):
        return self.__data
    @property
    def coodernador(self):
        if self.__id_coodernador == None:
            pass
        else:
            return self.__id_coodernador
    @property
    def curso(self):
        if self.__id_curso == None:
            pass
        else:
            return self.__id_curso
    @property
    def professor(self):
        if self.__id_professor == None:
            pass
        else:
            return self.__id_professor
    @property
    def disciplina(self):
        if self.__id_disciplina == None:
            pass
        else:
            return self.__id_disciplina