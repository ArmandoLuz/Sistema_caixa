from tkinter import *
from tokenize import String
from typing import Sized
from supermercado import Supermercado

class aplicacao:
    def __init__(self, root):
        self.root = root
        
        self.sp = Supermercado()

        #Definição de fontes padrão
        self.fonteTitlePadrao = ("Arial", 10, "bold")
        self.fonteButtonPadrao = ("Arial", 10,)

        #Declaração de conteiners
        self.primeiroConteiner = Frame(self.root, pady=30)
        self.primeiroConteiner.pack()

        self.segundoConteiner = Frame(self.root, padx=20, pady=2)
        self.segundoConteiner.pack()

        self.terceiroConteiner = Frame(self.root, pady=2, padx=20)
        self.terceiroConteiner.pack()

        self.quartoConteiner = Frame(self.root, pady=2, padx=20)
        self.quartoConteiner.pack()

        self.quintoConteiner = Frame(self.root, pady=2, padx=20)
        self.quintoConteiner.pack()

        self.sextoConteiner = Frame(self.root, pady=2, padx=20)
        self.sextoConteiner.pack()

        self.setimoConteiner = Frame(self.root, pady=2, padx=20)
        self.setimoConteiner.pack()

        self.oitavoConteiner = Frame(self.root, padx=20, pady=2)
        self.oitavoConteiner.pack()


        #Declaração dos Labels
        self.title = Label(self.primeiroConteiner, text="Sistema de caixa", font=("Arial", "20", "bold"))
        self.title.pack()

        self.titleOg = Label(self.segundoConteiner, text="Operações de gerência", font=self.fonteTitlePadrao, padx=45)
        self.titleOg.pack(side=LEFT)

        self.titleOpCa = Label(self.segundoConteiner, text="Operações de Caixa", font=self.fonteTitlePadrao, padx=45)
        self.titleOpCa.pack(side=LEFT)

        self.titleOe = Label(self.segundoConteiner, text="Operações de estoque", font=self.fonteTitlePadrao, padx=45)
        self.titleOe.pack(side=LEFT)

        #--------------------Declaração dos botões--------------------
        #Declaração dos botões do terceiro conteiner
        self.btAf = Button(self.terceiroConteiner, text="Adicionar funcionário", font=self.fonteButtonPadrao, width=25, command=self.add_fun)
        self.btAf.pack(side=LEFT, padx=20)

        self.btCc = Button(self.terceiroConteiner, text="Criar carrinho", font=self.fonteButtonPadrao, width=25, command=self.criar_car)
        self.btCc.pack(side=LEFT, padx=20)

        self.btApe = Button(self.terceiroConteiner, text="Adicionar produto ao estoque", font=self.fonteButtonPadrao, width=25, command=self.add_prod_estoq)
        self.btApe.pack(side=LEFT, padx=20)

        #Declaração dos botões do quarto conteiner
        self.btAcli = Button(self.quartoConteiner, text="Adicionar cliente", font=self.fonteButtonPadrao, width=25, command=self.add_cli)
        self.btAcli.pack(side=LEFT, padx=20)

        self.btAc = Button(self.quartoConteiner, text="Adicionar produto ao carrinho", font=self.fonteButtonPadrao, width=25, command=self.add_prod_car)
        self.btAc.pack(side=LEFT, padx=20)

        self.btEe = Button(self.quartoConteiner, text="Exibir estoque", font=self.fonteButtonPadrao, width=25, command=lambda: self.sp.exibir_estoque(root))
        self.btEe.pack(side=LEFT, padx=20)

        #Declaração dos botões do quinto conteiner
        self.btElf = Button(self.quintoConteiner, text="Exibir lista de funcionários", font=self.fonteButtonPadrao, width=25, command=lambda: self.sp.exibir_lista_funcionarios(root))
        self.btElf.pack(side=LEFT, padx=20)

        self.btPg = Button(self.quintoConteiner, text="Pagar Carrinho", font=self.fonteButtonPadrao, width=25, command=self.pagar)
        self.btPg.pack(side=LEFT, padx=20)

        self.btAqe = Button(self.quintoConteiner, text="Atualizar estoque", font=self.fonteButtonPadrao, width=25, command=self.atualiza_estoq)
        self.btAqe.pack(side=LEFT, padx=20)

        #Declaração dos botões do sexto conteiner
        self.btElc = Button(self.sextoConteiner, text="Exibir lista de clientes", font=self.fonteButtonPadrao, width=25, command=lambda: self.sp.exibir_lista_clientes(root))
        self.btElc.pack(side=LEFT, padx=20)

        self.btEic = Button(self.sextoConteiner, text="Exibir itens do carrinho", font=self.fonteButtonPadrao, width=25, command=self.exibir_itens_carrinho)
        self.btEic.pack(side=LEFT, padx=20)

        self.btApe = Button(self.sextoConteiner, text="Atualizar preço do estoque", font=self.fonteButtonPadrao, width=25, command=self.atualiza_preco)
        self.btApe.pack(side=LEFT, padx=20)

        #Declaração dos botões do sétimo conteiner
        self.btIc = Button(self.setimoConteiner, text="Imprimir informações do cliente", font=self.fonteButtonPadrao, width=25, command=self.sp.imprimir_pessoa)
        self.btIc.pack(side=LEFT, padx=20)

        self.btRpc = Button(self.setimoConteiner, text="Remover item do carrinho", font=self.fonteButtonPadrao, width=25, command=self.remover_produto_carrinho)
        self.btRpc.pack(side=LEFT, padx=20)

        self.titleAut = Label(self.setimoConteiner, text="Autor: Armando Luz Borges", width=25, font=self.fonteTitlePadrao, anchor=CENTER)
        self.titleAut.pack(side=LEFT, padx=22)

        #Declaração dos botões do sétimo conteiner
        self.btIf = Button(self.oitavoConteiner, text="Imprimir informações do funcionário", font=self.fonteButtonPadrao, width=25, command=self.sp.imprimir_funcionario)
        self.btIf.pack(side=LEFT, padx=20)

        self.titleCop = Label(self.oitavoConteiner, text="Open Source", width=25, font=self.fonteTitlePadrao, anchor=CENTER)
        self.titleCop.pack(side=LEFT, padx=22)

        self.titleVersion = Label(self.oitavoConteiner, text="Versão: 1.2", width=25, font=self.fonteTitlePadrao, anchor=CENTER)
        self.titleVersion.pack(side=LEFT, padx=22)
    #GUI da função adicionar funcionário
    def add_fun(self):

        root2 = Toplevel(self.root)
        root2.title("Adicionar funcionário")
        root2.geometry("300x140")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root2)
        primeirConteiner.pack()

        segundConteiner = Frame(root2)
        segundConteiner.pack()

        terceirConteiner = Frame(root2)
        terceirConteiner.pack()

        quartConteiner = Frame(root2)
        quartConteiner.pack()

        quintConteiner = Frame(root2)
        quintConteiner.pack()

        sextConteiner = Frame(root2)
        sextConteiner.pack()

        #Definição dos campos, textos e botões
        titleNm = Label(primeirConteiner, text="Nome")
        titleNm.pack(side=LEFT, padx=46)
        
        nm = StringVar()
        nmEntry = Entry(primeirConteiner, width=25, textvariable=nm)
        nmEntry.pack(side=LEFT)

        titleCpf = Label(segundConteiner, text="CPF")
        titleCpf.pack(side=LEFT, padx=52)

        cpf = StringVar()
        cpfEntry = Entry(segundConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        titleNas = Label(terceirConteiner, text="Nascimento")
        titleNas.pack(side=LEFT, padx=30)

        nas = StringVar()
        nasEntry = Entry(terceirConteiner, width=25, textvariable=nas)
        nasEntry.pack(side=LEFT, padx=1)

        titleSal = Label(quartConteiner, text="Salário")
        titleSal.pack(side=LEFT, padx=45)

        sal = StringVar()
        salEntry = Entry(quartConteiner, width=25, textvariable=sal)
        salEntry.pack(side=LEFT)

        titleSen = Label(quintConteiner, text="Senha")
        titleSen.pack(side=LEFT, padx=46)

        sen = StringVar()
        senEntry = Entry(quintConteiner, width=25, textvariable=sen)
        senEntry.pack(side=LEFT)

        cadBt = Button(sextConteiner, text="Cadastrar",width=25, command=lambda: self.sp.add_funcionario(self.root, root2,nm.get(), cpf.get(), nas.get(), sal.get(), sen.get()))
        cadBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI da função adicionar cliente
    def add_cli(self):
        
        root2 = Toplevel(self.root)
        root2.title("Adicionar cliente")
        root2.geometry("300x100")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root2)
        primeirConteiner.pack()

        segundConteiner = Frame(root2)
        segundConteiner.pack()

        terceirConteiner = Frame(root2)
        terceirConteiner.pack()

        quartConteiner = Frame(root2)
        quartConteiner.pack()

        #Definição dos campos, textos e botões
        titleNm = Label(primeirConteiner, text="Nome")
        titleNm.pack(side=LEFT, padx=46)
        
        nm = StringVar()
        nmEntry = Entry(primeirConteiner, width=25, textvariable=nm)
        nmEntry.pack(side=LEFT)

        titleCpf = Label(segundConteiner, text="CPF")
        titleCpf.pack(side=LEFT, padx=52)

        cpf = StringVar()
        cpfEntry = Entry(segundConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        titleNas = Label(terceirConteiner, text="Nascimento")
        titleNas.pack(side=LEFT, padx=30)

        nas = StringVar()
        nasEntry = Entry(terceirConteiner, width=25, textvariable=nas)
        nasEntry.pack(side=LEFT, padx=1)

        cadBt = Button(quartConteiner, text="Cadastrar",width=25, command=lambda: self.sp.add_cliente(self.root, root2,nm.get(), cpf.get(), nas.get()))
        cadBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI da função criar carrinho
    def criar_car(self):

        root2 = Toplevel(self.root)
        root2.title("Criar carrinho")
        root2.geometry("300x60")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeirConteiner = Frame(root2)
        primeirConteiner.pack()

        segundConteiner = Frame(root2)
        segundConteiner.pack()

        #Definição dos campos, textos e botões
        titleCpf = Label(primeirConteiner, text="CPF")
        titleCpf.pack(side=LEFT, padx=52)

        cpf = StringVar()
        cpfEntry = Entry(primeirConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        criBt = Button(segundConteiner, text="Criar",width=25, command=lambda: self.sp.criar_carrinho(self.root, root2,cpf.get()))
        criBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI adicionar produto ao carrinho
    def add_prod_car(self):

        root2 = Toplevel(self.root)
        root2.title("Adicionar produto")
        root2.geometry("300x100")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        terceiroConteiner = Frame(root2)
        terceiroConteiner.pack()

        quartoConteiner = Frame(root2)
        quartoConteiner.pack()

        #Definição dos campos, textos e botões
        titleCpf = Label(primeiroConteiner, text="CPF")
        titleCpf.pack(side=LEFT, padx=52)

        cpf = StringVar()
        cpfEntry = Entry(primeiroConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        titleId = Label(segundoConteiner, text="ID")
        titleId.pack(side=LEFT, padx=57)

        id = StringVar()
        idEntry = Entry(segundoConteiner, width=25, textvariable=id)
        idEntry.pack(side=LEFT)

        titleQuant = Label(terceiroConteiner, text="Quantidade")
        titleQuant.pack(side=LEFT, padx=31)

        quant = StringVar()
        quantEntry = Entry(terceiroConteiner, width=25, textvariable=quant)
        quantEntry.pack(side=LEFT)

        addBt = Button(quartoConteiner, text="Adicionar", width=25, command=lambda: self.sp.add_produto_carrinho(self.root, root2, cpf.get(), id.get(), quant.get()))
        addBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI adicionar produto ao estoque
    def add_prod_estoq(self):

        root2 = Toplevel(self.root)
        root2.title("Adicionar produto ao estoque")
        root2.geometry("310x100")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        terceiroConteiner = Frame(root2)
        terceiroConteiner.pack()

        quartoConteiner = Frame(root2)
        quartoConteiner.pack()

        #Definição dos campos, textos e botões
        titleNm = Label(primeiroConteiner, text="Nome",)
        titleNm.pack(side=LEFT, padx=52)

        nm = StringVar()
        nmEntry = Entry(primeiroConteiner, width=25, textvariable=nm)
        nmEntry.pack(side=LEFT)

        titlePr = Label(segundoConteiner, text="Preço",)
        titlePr.pack(side=LEFT, padx=53)

        pr = StringVar()
        prEntry = Entry(segundoConteiner, width=25, textvariable=pr)
        prEntry.pack(side=LEFT)

        titleQuant = Label(terceiroConteiner, text="Quantidade",)
        titleQuant.pack(side=LEFT, padx=37)

        quant = StringVar()
        quantEntry = Entry(terceiroConteiner, width=25, textvariable=quant)
        quantEntry.pack(side=LEFT)

        addBt = Button(quartoConteiner, width=25, text="Adicionar", command=lambda: self.sp.add_produto_estoque(self.root, root2, nm.get(), pr.get(), quant.get()))
        addBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI de pagamento de um carrinho
    def pagar(self):

        root2 = Toplevel(self.root)
        root2.title("Login")
        root2.geometry("300x125")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        terceiroConteiner = Frame(root2)
        terceiroConteiner.pack()

        quartoConteiner = Frame(root2)
        quartoConteiner.pack()

        quintoConteiner = Frame(root2)
        quintoConteiner.pack()

        #Definição dos campos, botões e textos
        title = Label(primeiroConteiner, text="Logue como funcionário", font=("Arial", 10, "bold"))
        title.pack(pady=10)

        titleCpf = Label(segundoConteiner, text="CPF")
        titleCpf.pack(side=LEFT, padx=52)

        cpf = StringVar()
        cpfEntry = Entry(segundoConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        titleSen = Label(terceiroConteiner, text="Senha")
        titleSen.pack(side=LEFT, padx=46)

        sen = StringVar()
        senEntry = Entry(terceiroConteiner, width=25, textvariable=sen)
        senEntry.pack(side=LEFT)

        LogBt = Button(quintoConteiner, text="Logar", width=25, command=lambda: self.sp.login(self.root, root2, cpf.get(), sen.get()))
        LogBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI de atualização de estoque
    def atualiza_estoq(self):

        root2 = Toplevel(self.root)
        root2.title("Atualizar estoque")
        root2.geometry("300x80")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        terceiroConteiner = Frame(root2)
        terceiroConteiner.pack()

        #Definição dos campos, botões e textos
        titleId = Label(primeiroConteiner, text="ID")
        titleId.pack(side=LEFT, padx=52)

        Id = StringVar()
        IdEntry = Entry(primeiroConteiner, width=25, textvariable=Id)
        IdEntry.pack(side=LEFT)

        titleQuant = Label(segundoConteiner, text="Quantidade")
        titleQuant.pack(side=LEFT, padx=26)

        quant = StringVar()
        quantEntry = Entry(segundoConteiner, width=25, textvariable=quant)
        quantEntry.pack(side=LEFT)

        atuBt = Button(terceiroConteiner, text="Atualizar", width=25, command=lambda: self.sp.atualiza_quant(self.root, Id.get(), quant.get()))
        atuBt.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI de atualização de preço
    def atualiza_preco(self):

        root2 = Toplevel(self.root)
        root2.title("Atualizar preço")
        root2.geometry("300x80")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        terceiroConteiner = Frame(root2)
        terceiroConteiner.pack()

        #Definição dos campos, botões e textos
        idLabel = Label(primeiroConteiner, text='ID')
        idLabel.pack(side=LEFT, padx=58)

        id = StringVar()
        idEntry = Entry(primeiroConteiner, width=25, textvariable=id)
        idEntry.pack(side=LEFT)

        prLabel = Label(segundoConteiner, text='Preço')
        prLabel.pack(side=LEFT, padx=48)

        preco = StringVar()
        prEntry = Entry(segundoConteiner, width=25, textvariable=preco)
        prEntry.pack(side=LEFT)

        atuButton = Button(terceiroConteiner, width=25, text='Atualizar', command= lambda: self.sp.atualiza_preco(self.root, id.get(), preco.get()))
        atuButton.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI de exibição dos itens de um carrinho
    def exibir_itens_carrinho(self):
        root2 = Toplevel(self.root)
        root2.title("Exibir itens do carrinho")
        root2.geometry("300x60")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        #Definição dos campos, botões e textos
        cpfLabel = Label(primeiroConteiner, text="CPF")
        cpfLabel.pack(side=LEFT, padx=58)

        cpf = StringVar()
        cpfEntry = Entry(primeiroConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        exiButton = Button(segundoConteiner, width=25, text="Exibir", command=lambda: self.sp.exibir_itens_carrinho(self.root, root2, cpf.get()))
        exiButton.pack(pady=5)


        root2.focus_force()
        root2.grab_set()
        root2.mainloop()
    #GUI de remoção de um produto de um carrinho
    def remover_produto_carrinho(self):
        root2 = Toplevel(self.root)
        root2.title("Remover produto do carrinho")
        root2.geometry("300x60")
        root2.resizable(False, False)

        #Definição dos conteiners
        primeiroConteiner = Frame(root2)
        primeiroConteiner.pack()

        segundoConteiner = Frame(root2)
        segundoConteiner.pack()

        #Definição dos campos, botões e textos
        cpfLabel = Label(primeiroConteiner, text="CPF")
        cpfLabel.pack(side=LEFT, padx=58)

        cpf = StringVar()
        cpfEntry = Entry(primeiroConteiner, width=25, textvariable=cpf)
        cpfEntry.pack(side=LEFT)

        remButton = Button(segundoConteiner, width=25, text="OK", command=lambda: self.sp.remover_produto_carrinho(self.root, root2, cpf.get()))
        remButton.pack(pady=5)

        root2.focus_force()
        root2.grab_set()
        root2.mainloop()


root = Tk()
root.title("Sistema de caixa")
aplicacao(root)
root.mainloop()
