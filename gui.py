from tkinter import *
from supermercado import Supermercado

sp = Supermercado()

root = Tk()

#Definição de fontes padrão
fonteTitlePadrao = ("Arial", 10, "bold")
fonteButtonPadrao = ("Arial", 10,)

#Declaração de conteiners
primeiroConteiner = Frame(root, pady=30)
primeiroConteiner.pack()

segundoConteiner = Frame(root, padx=20, pady=2)
segundoConteiner.pack()

terceiroConteiner = Frame(root, pady=2, padx=20)
terceiroConteiner.pack()

quartoConteiner = Frame(root, pady=2, padx=20)
quartoConteiner.pack()

quintoConteiner = Frame(root, pady=2, padx=20)
quintoConteiner.pack()

sextoConteiner = Frame(root, pady=2, padx=20)
sextoConteiner.pack()

setimoConteiner = Frame(root, pady=2, padx=20)
setimoConteiner.pack()

oitavoConteiner = Frame(root, padx=20, pady=2)
oitavoConteiner.pack()


#Declaração dos Labels
title = Label(primeiroConteiner, text="Sistema de caixa", font=("Arial", "20", "bold"))
title.pack()

titleOg = Label(segundoConteiner, text="Operações de gerência", font=fonteTitlePadrao, padx=45)
titleOg.pack(side=LEFT)

titleOpCa = Label(segundoConteiner, text="Operações de Caixa", font=fonteTitlePadrao, padx=45)
titleOpCa.pack(side=LEFT)

titleOe = Label(segundoConteiner, text="Operações de estoque", font=fonteTitlePadrao, padx=45)
titleOe.pack(side=LEFT)

#--------------------Declaração dos botões--------------------
#Declaração dos botões do terceiro conteiner
btAf = Button(terceiroConteiner, text="Adicionar funcionário", font=fonteButtonPadrao, width=25, command=sp.add_funcionario)
btAf.pack(side=LEFT, padx=20)

btCc = Button(terceiroConteiner, text="Criar carrinho", font=fonteButtonPadrao, width=25, command=sp.criar_carrinho)
btCc.pack(side=LEFT, padx=20)

btApe = Button(terceiroConteiner, text="Adicionar produto ao estoque", font=fonteButtonPadrao, width=25, command=sp.add_produto_estoque)
btApe.pack(side=LEFT, padx=20)

#Declaração dos botões do quarto conteiner
btAcli = Button(quartoConteiner, text="Adicionar cliente", font=fonteButtonPadrao, width=25, command=sp.add_cliente)
btAcli.pack(side=LEFT, padx=20)

btAc = Button(quartoConteiner, text="Adicionar produto ao carrinho", font=fonteButtonPadrao, width=25, command=sp.add_produto_carrinho)
btAc.pack(side=LEFT, padx=20)

btEe = Button(quartoConteiner, text="Exibir estoque", font=fonteButtonPadrao, width=25, command=sp.exibir_estoque)
btEe.pack(side=LEFT, padx=20)

#Declaração dos botões do quinto conteiner
btElf = Button(quintoConteiner, text="Exibir lista de funcionários", font=fonteButtonPadrao, width=25, command=sp.exibir_lista_funcionarios)
btElf.pack(side=LEFT, padx=20)

btPg = Button(quintoConteiner, text="Pagar Carrinho", font=fonteButtonPadrao, width=25, command=sp.pagar)
btPg.pack(side=LEFT, padx=20)

btAqe = Button(quintoConteiner, text="Atualizar estoque", font=fonteButtonPadrao, width=25, command=sp.atualiza_quant)
btAqe.pack(side=LEFT, padx=20)

#Declaração dos botões do sexto conteiner
btElc = Button(sextoConteiner, text="Exibir lista de clientes", font=fonteButtonPadrao, width=25, command=sp.exibir_lista_clientes)
btElc.pack(side=LEFT, padx=20)

btEic = Button(sextoConteiner, text="Exibir itens do carrinho", font=fonteButtonPadrao, width=25, command=sp.exibir_itens_carrinho)
btEic.pack(side=LEFT, padx=20)

btApe = Button(sextoConteiner, text="Atualizar preço do estoque", font=fonteButtonPadrao, width=25, command=sp.atualiza_preco)
btApe.pack(side=LEFT, padx=20)

#Declaração dos botões do sétimo conteiner
btIc = Button(setimoConteiner, text="Imprimir informações do cliente", font=fonteButtonPadrao, width=25, command=sp.imprimir_pessoa)
btIc.pack(side=LEFT, padx=20)

btRpc = Button(setimoConteiner, text="Remover item do carrinho", font=fonteButtonPadrao, width=25, command=sp.remover_produto_carrinho)
btRpc.pack(side=LEFT, padx=20)

titleAut = Label(setimoConteiner, text="Autor: Armando Luz Borges", width=25, font=fonteTitlePadrao, anchor=CENTER)
titleAut.pack(side=LEFT, padx=22)

#Declaração dos botões do sétimo conteiner
btIf = Button(oitavoConteiner, text="Imprimir informações do funcionário", font=fonteButtonPadrao, width=25, command=sp.imprimir_funcionario)
btIf.pack(side=LEFT, padx=20)

titleCop = Label(oitavoConteiner, text="Open Source", width=25, font=fonteTitlePadrao, anchor=CENTER)
titleCop.pack(side=LEFT, padx=22)

titleVersion = Label(oitavoConteiner, text="Versão: 1.1", width=25, font=fonteTitlePadrao, anchor=CENTER)
titleVersion.pack(side=LEFT, padx=22)

root.mainloop()