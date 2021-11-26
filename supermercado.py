import random
from cliente import Cliente
from produto import Produto
from carrinho import Carrinho
from funcionario import Funcionario
from sistema_interno import SistemaInterno
from manipulador_login import Manipulador_de_login


class Supermercado:

    def __init__(self):
        self._lista_funcionario = {}
        self._lista_cliente = {}
        self._lista_estoque = {}
        self._lista_carrinho = {}

    def add_funcionario(self):
        nome = input("Insira o nome: ")
        cpf = str(input("Insira o CPF: "))

        if cpf in self._lista_funcionario.keys():
            print("Funcionário já cadastrado no sistema.")
            return 0

        data_nas = input("Insira a data de nascimento: ")
        salario = input("Insira o salário: ")
        senha = input("Defina uma senha: ")

        self._lista_funcionario[cpf] = Funcionario(nome, cpf, data_nas, salario, senha)

    def add_cliente(self):
        nome = input("Insira o nome: ")
        cpf = str(input("Insira o CPF: "))

        if cpf in self._lista_cliente.keys():
            print("Cliente já cadastrado no sistema.")
            return 0

        data_nas = input("Insira a data de nascimento: ")

        self._lista_cliente[cpf] = Cliente(nome, cpf, data_nas)
    
    def criar_carrinho(self):
        cpf = input("Insira o CPF do cliente: ")
        
        if cpf not in self._lista_cliente.keys():
            print("Cliente não cadastrado no sistema.")
            return 0
        
        if cpf in self._lista_carrinho.keys():
            print("O cliente já possui um carrinho de compras.")
            return 0
        
        self._lista_carrinho[cpf] = Carrinho(cpf)
        print("Carrinho criado com sucesso.")

    def add_produto_carrinho(self):
        cpf = input("Insira o CPF do cliente: ")

        if cpf not in self._lista_carrinho.keys():
            print("O cliente não possui um carrinho de compras.")
            return 0
        
        self._lista_carrinho[cpf].add_produto(self._lista_estoque)

    def add_produto_estoque(self):
        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o preco do produto: "))
        quant = int(input("Insira a quantidade disponível: "))
        while True:
            id = random.randint(100000, 999999)

            if id not in self._lista_estoque.keys():
                self._lista_estoque[id] = Produto(id, nome, preco, quant)
                print("Produto adicionado com sucesso.")
                break
                
    def pagar(self):
        print("Logue como funcionário.")
        ml = Manipulador_de_login()
        SistemaInterno.register(Funcionario)

        cpf = input("Insira seu CPF: ")
        senha = input("Insira sua senha: ")
        
        if cpf in self._lista_funcionario.keys():

            if ml.login(self._lista_funcionario[cpf], senha):
                print("Login feito com sucesso.")
                cpf_cli = input("Insira o CPF do cliente: ")

                if cpf_cli in self._lista_carrinho.keys():
                    self._lista_carrinho[cpf]._status = True
                    del(self._lista_carrinho[cpf])
                    print("Carrinho pago com sucesso.")
                else:
                    print("Cliente não cadastrado no sistema ou não possui carrinho de compras.")
            else:
                print("Senha incorreta.")
        else:
            print("Funcionário não cadastrado no sistema.")
    
    def exibir_estoque(self):
        for i in self._lista_estoque.keys():
            print("ID:", self._lista_estoque[i]._id, "|", "Nome:",self._lista_estoque[i]._nome,"|", "Preço:", self._lista_estoque[i]._preco,"|", "Quantidade:", self._lista_estoque[i]._quantidade)

    def atualiza_quant(self):
        id = int(input("Insira o ID do produto: "))
        quant = int(input("Insira a quantidade: "))

        if id in self._lista_estoque.keys():
            if quant > 0:
                self._lista_estoque[id]._quantidade = quant
            else:
                print("Você não pode colocar valores negativos.")
        else:
            print("Produto não encontrado no estoque.")  

    def atualiza_preco(self):
        id = int(input("Insira o ID do produto: "))
        preco = int(input("Insira o novo preço: "))

        if id in self._lista_estoque.keys():
            if preco > 0:
                self._lista_estoque[id]._preco = preco
            else:
                print("Não é possível inserir preços iguais ou menores que zero.")
        else:
            print("Produto não está no estoque.")

    def exibir_lista_funcionarios(self):
        for i in self._lista_funcionario.keys():
            print(self._lista_funcionario[i]._nome)

    def exibir_lista_clientes(self):
        for i in self._lista_cliente.keys():
            print(self._lista_cliente[i]._nome)

    def exibir_itens_carrinho(self):
        cpf = input("Insira o CPF do cliente: ")

        if cpf not in self._lista_carrinho.keys():
            print("O cliente não possui carrinho de compras.")
            return 0
        
        self._lista_carrinho[cpf].exibir_produtos()
    
    def remover_produto_carrinho(self):
        cpf = input("Insira o CPF do cliente: ")

        if cpf not in self._lista_carrinho.keys():
            print("O cliente não possui um carrinho de compras.")
            return 0

        self._lista_carrinho[cpf].remover_produto(self._lista_estoque)

    def imprimir_pessoa(self):
        cpf = input("Insira o CPF do cliente: ")

        if cpf not in self._lista_cliente.keys():
            print("O cliente não está cadastrado no sistema.")
            return 0

        self._lista_cliente[cpf].imprimir_pessoa()

    def imprimir_funcionario(self):
        cpf = input("Insira o CPF do funcionário: ")

        if cpf not in self._lista_funcionario.keys():
            print("O funcionário não está cadastrado no sistema.")
            return 0

        self._lista_funcionario[cpf].imprimir_funcionario()