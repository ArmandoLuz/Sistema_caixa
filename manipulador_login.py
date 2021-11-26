from sistema_interno import SistemaInterno

class Manipulador_de_login:
    
    def login(self, usuario, senha):
        if isinstance(usuario, SistemaInterno):
            if senha == usuario.login():
                return True
            else:
                return False
        else:
            print(usuario.__repr__(), "não é atenticável.")
