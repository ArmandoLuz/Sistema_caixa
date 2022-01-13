import abc

class Produtos(abc.ABC):

    def __init__(self, id , nome, preco, quant):
        self._id = id
        self._nome = nome
        self._preco = float(preco)
        self._quantidade = int(quant)

    @abc.abstractmethod
    def atualiza_preco(self, valor):
        pass
    
    @abc.abstractmethod
    def atualiza_quantidade(self, valor):
        pass