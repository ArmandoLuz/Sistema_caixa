import abc

class SistemaInterno(abc.ABC):
    """Classe que contém operações de um objeto autenticável
    
    As subclasses concretas devem sobrescrever o método login."""

    @abc.abstractmethod
    def login(self, senha):
        """Faz login em um usuário cadastrado como funcionário no sistema."""
        pass