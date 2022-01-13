from pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome, cpf, data_nas):
        super().__init__(nome, cpf, data_nas)

    def imprimir_pessoa(self):
        print("Nome:", self._nome)
        print("CPF:", self._cpf)
        print("Data de nascimento:", self._data_nascimento)