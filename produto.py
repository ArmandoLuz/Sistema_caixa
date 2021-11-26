from produtos import Produtos

class Produto(Produtos):

    def __init__(self, id ,nome, preco, quant):
        super().__init__(id, nome, preco, quant)
    
    def atualiza_preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
            print("O preço não pode ser igual ou inferior a zero.")

    def atualiza_quantidade(self, valor):
        if valor >= 0:
            self._quantidade = valor
        else:
            print("A quantidade não pode ser menor que zero.")