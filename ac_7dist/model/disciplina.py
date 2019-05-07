class Disciplina():
    def __init__(self, id, nome,status,plano_ensino,carga_horaria,id_coodernador=None):
        self.__id = id
        self.__nome = nome
        self.__status = status
        self.__plano_ensino = plano_ensino
        self.__carga_horaria = carga_horaria
        self.__id_coodernador = id_coodernador

    def atualizar(self, id=None, nome=None,status=None,plano_ensino=None,carga_horaria=None,id_coodernador=None):
        if id == None:
            pass
        else:
            self.__id = id
        if self.__nome == None:
            pass
        else:
            self.__nome = nome
        if status == None:
            pass
        else:
            self.__status = status
        if plano_ensino == None:
            pass
        else:
            self.__plano_ensino == plano_ensino
        if carga_horaria == None:
            pass
        else:
            self.__carga_horaria = carga_horaria
        if id_coodernador == None:
            pass
        else:
            self.__id_coodernador = id_coodernador
        
        
        return self

    @property
    def id(self):
        return self.__id 
    @property
    def nome(self):
       return self.__nome 
  

    @property
    def status(self):
        return self.__status
    @property
    def plano_ensino(self):
        return self.__plano_ensino

    @property
    def carga_horaria(self):
        return self.__carga_horaria
    @property
    def coodernador(self):
        if self.__id_coodernador == None:
            pass
        else:
            return self.__id_coodernador
