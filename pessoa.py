import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, cpf, data_nas):
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nas

    @abc.abstractmethod
    def imprimir_pessoa(self):
        pass
        