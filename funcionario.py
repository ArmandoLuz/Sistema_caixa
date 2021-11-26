from pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, data_nas, salario, senha):
        super().__init__(nome, cpf, data_nas)
        self._salario = salario
        self._senha = senha

    def imprimir_pessoa(self):
        print("Nome: ", self._nome)
        print("CPF: ", self._cpf)
        print("Data de nascimento: ", self._data_nascimento)

    def imprimir_funcionario(self):
        print("Nome:", self._nome)
        print("CPF:", self._cpf)
        print("Data de nascimento:", self._data_nascimento)
        print("Salário:", self._salario)

    def login(self):
        return str(self._senha)
