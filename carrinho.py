from tkinter import *

class Carrinho:

    def __init__(self, cpf_cliente):
        self._cpf_cliente = cpf_cliente
        self._produtos = {}
        self._quant_carrinho = {}
        self._preco_total = 0
        self._status = False

    def remover_produto(self, lista_produto):
        while True:
            print("Para parar de remover, digite 0")
            id = int(input("Insira o id do produto: "))

            if id == 0:
                break

            if id in self._produtos.keys():
                lista_produto[id]._quantidade += self._quant_carrinho[id]
                self._preco_total -= self._produtos[id]._preco * self._quant_carrinho[id]
                del(self._produtos[id])
                del(self._quant_carrinho[id])
            else:
                print("Item não está no seu carrinho.")
    #Adicionar produto ao carrinho
    def add_produto(self, lista_produto, root, root2, Id, Quant):
        id = int(Id)

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

        msg = "Produto adicionado com sucesso!"

        #Verifica se o id é chave de algum produto
        if id in lista_produto.keys():
            quant = int(Quant)
            
            #Verifica se a quantidade desejada está disponível
            if lista_produto[id]._quantidade >= quant:
                lista_produto[id]._quantidade -= quant
                self._produtos[id] = lista_produto[id]
                self._quant_carrinho[id] = quant
                self._preco_total += self._produtos[id]._preco * self._quant_carrinho[id]

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
            else:
                msg = "O estoque não contém a quantidade desejada!"

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
        else:
            msg = "O estoque não contém esse produto!"

            #Fecha a janela de cadastro
            root2.destroy()

            #Exibe a janela de alerta
            primeirConteiner.pack()
            segundConteiner.pack()

            msgLabel["text"] = msg

            msgLabel.pack(pady=10)
            btClose.pack()

            root3.focus_force()
            root3.grab_set()

    def exibir_produtos(self):
        for i in self._produtos.keys():
            print(self._quant_carrinho[i], self._produtos[i]._nome)
        
        print("Total:", self._preco_total)
    

