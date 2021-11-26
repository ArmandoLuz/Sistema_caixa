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

    def add_produto(self, lista_produto):
        while True:
            print("Para parar de adicionar, digite 0.")
            id = int(input("Insira o id do produto: "))

            if id == 0:
                break

            if id in lista_produto.keys():
                print("Há ", lista_produto[id]._quantidade, "unidades desse produto.")
                quant = int(input("Insira a quantidade desejada: "))
                
                if lista_produto[id]._quantidade >= quant:
                    lista_produto[id]._quantidade -= quant
                    self._produtos[id] = lista_produto[id]
                    self._quant_carrinho[id] = quant
                    self._preco_total += self._produtos[id]._preco * self._quant_carrinho[id]
                else:
                    print("O estoque não contém a quantidade desejada!")
            else:
                print("O estoque não contém esse produto!")

    def exibir_produtos(self):
        for i in self._produtos.keys():
            print(self._quant_carrinho[i], self._produtos[i]._nome)
        
        print("Total:", self._preco_total)
    


