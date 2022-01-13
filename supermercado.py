import random
from tkinter import *
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
        
    #Adiciona um funcionário a lista de funcionários
    def add_funcionario(self, root,root2, nm, Cpf, nas, sal, sen):
        nome = nm
        cpf = str(Cpf)
        data_nas = nas
        salario = sal
        senha = sen

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root3)
        segundoConteiner = Frame(root3)
        
        #Definição dos campos e botões
        msgLabel = Label(primeiroConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundoConteiner, text="OK", width=20, command=root3.destroy)

        msg = "Funcionário cadastrado com sucesso."

        #Verifica se o CPF está na lista de funcionários
        if cpf in self._lista_funcionario.keys():
            msg = "Funcionário já cadastrado no sistema."

            #Fecha a janela de cadastro
            root2.destroy()

            #Exibe a janela de alerta
            primeiroConteiner.pack()
            segundoConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()
            return 0

        #Adiciona o CPF a lista de funcionários
        self._lista_funcionario[cpf] = Funcionario(nome, cpf, data_nas, salario, senha)

        #Fecha a janela de cadastro
        root2.destroy()

        #Exibe a janela de alerta
        primeiroConteiner.pack()
        segundoConteiner.pack()

        msgLabel["text"] = msg

        msgLabel.pack(pady=10)
        btClose.pack()

        root3.focus_force()
        root3.grab_set()
    #Adiciona um cliente a lista de clientes
    def add_cliente(self,root, root2, nm, Cpf, nas):
        nome = nm
        cpf = Cpf
        data_nas = nas

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root3)
        segundoConteiner = Frame(root3)

        #Definição dos campos e botões
        msgLabel = Label(primeiroConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundoConteiner, text="OK", width=20, command=root3.destroy)

        msg = "Cliente cadastrado com sucesso."

        #Verifica se o CPF está na lista de Clientes
        if cpf in self._lista_cliente.keys():
            msg = "Cliente já cadastrado no sistema."

            #Fecha a janela de cadastro
            root2.destroy()

            #Exibe a janela de alerta
            primeiroConteiner.pack()
            segundoConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()
            return 0

        #Adiciona o CPF a lista de clientes
        self._lista_cliente[cpf] = Cliente(nome, cpf, data_nas)

        #Fecha a janela de cadastro
        root2.destroy()

        #Exibe a janela de alerta
        primeiroConteiner.pack()
        segundoConteiner.pack()

        msgLabel["text"] = msg

        msgLabel.pack(pady=10)
        btClose.pack()

        root3.focus_force()
        root3.grab_set()
    #Cria um carrinho de compras
    def criar_carrinho(self, root, root2, Cpf):

        cpf = Cpf

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root3)
        segundoConteiner = Frame(root3)

        #Definição dos campos e botões
        msgLabel = Label(primeiroConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundoConteiner, text="OK", width=20, command=root3.destroy)
        
        #Verifica se o CPF não está na lista de clientes
        if cpf not in self._lista_cliente.keys():
            msg = "Cliente não cadastrado no sistema."

            #Fecha a janela de criação
            root2.destroy()

            #Exibe a janela de alerta
            primeiroConteiner.pack()
            segundoConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()

            return 0
        
        #Verifica se o CPF está na lista de carrinhos
        if cpf in self._lista_carrinho.keys():
            msg = "O cliente já possui um carrinho de compras."

            #Fecha a janela de criação
            root2.destroy()

            #Exibe a janela de alerta
            primeiroConteiner.pack()
            segundoConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()

            return 0
        
        #Adiciona o CPF como chave de um carrinho de compras
        self._lista_carrinho[cpf] = Carrinho(cpf)
        msg = "Carrinho criado com sucesso."

        #Fecha a janela de criação
        root2.destroy()

        #Exibe a janela de alerta
        primeiroConteiner.pack()
        segundoConteiner.pack()

        msgLabel["text"] = msg

        msgLabel.pack(pady=10)
        btClose.pack()

        root3.focus_force()
        root3.grab_set()
    #Adiciona um produto ao carrinho
    def add_produto_carrinho(self, root, root2, Cpf, id, quant):

        cpf = Cpf

        #Verifica se o CPF não é uma chave do carrinho de compras
        if cpf not in self._lista_carrinho.keys():
            root3 = Toplevel(root)
            root3.title("Alerta")
            root3.geometry("300x80")
            root3.resizable(False, False)

            #Definição dos conteiners
            primeirConteiner = Frame(root3)
            segundConteiner = Frame(root3)

            #Definição dos campos, textos e botões
            msgLabel = Label(primeirConteiner, font=("Arial", 10, "bold"))
            btClose = Button(segundConteiner, text="OK", width=25, command=root3.destroy)

            msg = "O cliente não possui um carrinho de compras."

            #Fecha a janela de adicionar
            root2.destroy()

            #Exibe a janela de alerta
            primeirConteiner.pack()
            segundConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()
            return 0
        
        #Adiciona um produto ao carrinho de compras
        self._lista_carrinho[cpf].add_produto(self._lista_estoque, root, root2, id, quant)
    #Adiciona um produto ao estoque
    def add_produto_estoque(self, root, root2, nm, pr, quat):
        nome = nm
        preco = pr
        quant = quat

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root3)
  

        segundConteiner = Frame(root3)
        

        #Definição dos textos, campos e botões
        msgLabel = Label(primeirConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundConteiner, text="OK", width=25, command=root3.destroy)

        #Inserção do produto ao estoque com um id diferente dos que já existem
        while True:
            id = random.randint(100000, 999999)

            if id not in self._lista_estoque.keys():
                self._lista_estoque[id] = Produto(id, nome, preco, quant)
                msg = "Produto adicionado com sucesso."
                break

        #Fecha a janela de adicionar
        root2.destroy()

        #Exibe a janela de alerta
        msgLabel["text"] = msg

        primeirConteiner.pack()
        segundConteiner.pack()

        msgLabel.pack(pady=10)
        btClose.pack()

        root3.focus_force()
        root3.grab_set()
    #Faz o login de um funcionário           
    def login(self, root, root2, Cpf, sen):

        ml = Manipulador_de_login()
        SistemaInterno.register(Funcionario)

        cpf = Cpf
        senha = sen
        
        #Verifica se o CPF está na lista de funcionários
        if cpf in self._lista_funcionario.keys():

            #Realiza a verificação da senha
            if ml.login(self._lista_funcionario[cpf], senha):
                #Fecha a janela de login
                root2.destroy()

                root4 = Toplevel(root)
                root4.title("Dados do cliente")
                root4.geometry("350x100")
                root4.resizable(False, False)

                #Definição dos conteiners de alerta do cpf do cliente
                primeirConteinerCli = Frame(root4)
                primeirConteinerCli.pack()
                segundConteinerCli = Frame(root4)
                segundConteinerCli.pack()
                terceirConteinerCli = Frame(root4)
                terceirConteinerCli.pack()

                #Definição dos campos, textos e botões de alerta de cpf do cliente
                titletext = Label(primeirConteinerCli, text="Login feito com sucesso.", font=("Arial", 10, "bold"))
                titletext.pack(pady=5)
                CPF_cli = StringVar()
                titleCpf = Label(segundConteinerCli, text="CPF do cliente")
                titleCpf.pack(side=LEFT, padx=52)
                entryCli = Entry(segundConteinerCli, width=25, textvariable=CPF_cli)
                entryCli.pack(side=LEFT)
                btPg = Button(terceirConteinerCli, text="Pagar", width=25, command=lambda:self.pagar(root, root4, CPF_cli.get()))
                btPg.pack(pady=5)

                #Exibe a tela que pede o CPF do cliente
                root4.focus_force()
                root4.grab_set()

            else:
                
                root3 = Toplevel(root)
                root3.title("Alerta")
                root3.geometry("300x70")
                root3.resizable(False, False)

                #Definição dos conteiners de alerta de login
                primeirConteinerLog = Frame(root3)
                segundConteinerLog = Frame(root3)

                #Definição dos campos, textos e botões de alerta de login
                logtext = Label(primeirConteinerLog, font=("Arial", 10, "bold"))
                btCloseLog = Button(segundConteinerLog, text="OK", width=25, command=root3.destroy)

                #Fecha a janela de login
                root2.destroy()

                #Exibe a janela de Alerta de Login
                logtext["text"] = "Senha incorreta."

                primeirConteinerLog.pack()
                segundConteinerLog.pack()

                logtext.pack(pady=5)
                btCloseLog.pack()

                root3.focus_force()
                root3.grab_set()
                
        else:
            
            root3 = Toplevel(root)
            root3.title("Alerta")
            root3.geometry("300x70")
            root3.resizable(False, False)

            #Definição dos conteiners de alerta de login
            primeirConteinerLog = Frame(root3)
            segundConteinerLog = Frame(root3)

            #Definição dos campos, textos e botões de alerta de login
            logtext = Label(primeirConteinerLog, font=("Arial", 10, "bold"))
            btCloseLog = Button(segundConteinerLog, text="OK", width=25, command=root3.destroy)

            #Fecha a janela de login
            root2.destroy()

            #Exibe a janela de Alerta de Login
            logtext["text"] = "Funcionário não cadastrado no sistema."

            primeirConteinerLog.pack()
            segundConteinerLog.pack()

            logtext.pack(pady=5)
            btCloseLog.pack()

            root3.focus_force()
            root3.grab_set()
    #Faz o pagamento de um carrinho
    def pagar(self, root, root4, cpf_cli):

        if cpf_cli in self._lista_carrinho.keys():

            root4.destroy()

            self._lista_carrinho[cpf_cli]._status = True
            del(self._lista_carrinho[cpf_cli])
            
            root2 = Toplevel(root)
            root2.title("Alerta")
            root2.geometry("300x80")
            root2.resizable(False, False)

            #Definição dos conteiners de alerta do cpf do cliente
            primeirConteinerAle = Frame(root2)
            primeirConteinerAle.pack()
            segundConteinerAle = Frame(root2)
            segundConteinerAle.pack()

            #Definição dos campos, textos e botões de alerta de cpf do cliente
            alerttext = Label(primeirConteinerAle, text="Carrinho pago com sucesso.", font=("Arial", 10, "bold"))
            alerttext.pack(pady=5)
            okPg = Button(segundConteinerAle, text="OK", width=25, command=root2.destroy)
            okPg.pack()

            root2.focus_force()
            root2.grab_set()
            root2.mainloop()

        else:

            root2 = Toplevel(root)
            root2.title("Alerta")
            root2.geometry("500x70")
            root2.resizable(False, False)

            #Definição dos conteiners de alerta do cpf do cliente
            primeirConteinerAle = Frame(root2)
            primeirConteinerAle.pack()
            segundConteinerAle = Frame(root2)
            segundConteinerAle.pack()

            #Definição dos campos, textos e botões de alerta de cpf do cliente
            alerttext = Label(primeirConteinerAle, text="Cliente não cadastrado no sistema ou não possui carrinho de compras.", font=("Arial", 10, "bold"))
            alerttext.pack(pady=5)
            okPg = Button(segundConteinerAle, text="OK", width=25, command=root2.destroy)
            okPg.pack()

            root2.focus_force()
            root2.grab_set()
            root2.mainloop()
    #Exibe o estoque
    def exibir_estoque(self, root):

        root3 = Toplevel(root)
        root3.title("Estoque")
        root3.geometry("500x300")

        #Definição do listbox
        lista = Listbox(root3)
        lista.pack(side=LEFT, fill=BOTH, expand=1)

        #Definição da barra de rolagem
        scroll = Scrollbar(root3, orient=VERTICAL, command=lista.yview)
        scroll.pack(side=LEFT, fill=BOTH)

        #Configurando a barra de rolagem
        lista["yscrollcommand"] = scroll.set

        for i in self._lista_estoque.keys():
            lista.insert("end", f"ID: {self._lista_estoque[i]._id:<10} {'Nome:':<5} {self._lista_estoque[i]._nome:<100} {'Preço:':<6} {self._lista_estoque[i]._preco:<10} {'Quantidade:':<11} {self._lista_estoque[i]._quantidade:<10}")
        root3.mainloop()
    #Atualiza o estoque
    def atualiza_quant(self, root, Id, Quant):
        id = int(Id)
        quant = int(Quant)

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root3)
        segundConteiner = Frame(root3)

        #Definição dos textos, campos e botões
        msgLabel = Label(primeirConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundConteiner, text="OK", width=25, command=root3.destroy)


        if id in self._lista_estoque.keys():
            if quant > 0:
                self._lista_estoque[id]._quantidade = quant
                msg = "Estoque atualizado com sucesso!"
            else:
                msg = "Você não pode colocar valores negativos."
        else:
            msg = "Produto não encontrado no estoque."

        #Exibe a janela de alerta
        msgLabel["text"] = msg

        primeirConteiner.pack()
        segundConteiner.pack()

        msgLabel.pack()  
        btClose.pack(pady=10)

        root3.focus_force()
        root3.grab_set()
    #Atualiza a quantidade do estoque
    def atualiza_preco(self, root, Id, Preco):
        id = int(Id)
        preco = float(Preco)

        root3 = Toplevel(root)
        root3.title("Alerta")
        root3.geometry("300x80")
        root3.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root3)
        segundConteiner = Frame(root3)

        #Definição dos textos, campos e botões
        msgLabel = Label(primeirConteiner, font=("Arial", 10, "bold"))
        btClose = Button(segundConteiner, text="OK", width=25, command=root3.destroy)

        if id in self._lista_estoque.keys():
            if preco > 0:
                self._lista_estoque[id]._preco = preco
                msg = 'Preço atualizado com sucesso!'
            else:
                msg = "Não é possível inserir preços iguais ou menores que zero."
        else:
            msg = "Produto não está no estoque."
        
        #Exibe a janela de alerta
        msgLabel["text"] = msg

        primeirConteiner.pack()
        segundConteiner.pack()

        msgLabel.pack()  
        btClose.pack(pady=10)

        root3.focus_force()
        root3.grab_set()

    def exibir_lista_funcionarios(self, root):
        root3 = Toplevel(root)
        root3.title("Litsa de funcionários")
        root3.geometry("500x300")
        root3.resizable(False, False)

        #Definição do listbox
        lista = Listbox(root3)
        lista.pack(side=LEFT, fill=BOTH, expand=1)

        #Definição da barra de rolagem
        scroll = Scrollbar(root3, orient=VERTICAL, command=lista.yview)
        scroll.pack(side=LEFT, fill=BOTH)

        #Configurando a barra de rolagem
        lista["yscrollcommand"] = scroll.set

        count = 0

        for i in self._lista_funcionario.keys():
            count+=1
            lista.insert("end", str(count) + "-" + self._lista_funcionario[i]._nome)
        root3.mainloop()

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
