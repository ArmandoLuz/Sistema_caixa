from supermercado import Supermercado

supermercado = Supermercado()

while True:
    print("-=-=-=-=-MENU-=-=-=-=-")
    print("1 - Adicionar funcionário")
    print("2 - Adicionar cliente")
    print("3 - Criar carrinho de compras")
    print("4 - Adicionar produto ao carrinho")
    print("5 - Adicionar produto ao estoque")
    print("6 - Fazer pagamento do carrinho")
    print("7 - Exibir produtos do estoque")
    print("8 - Atualizar o estoque de um produto")
    print("9 - Atualizar o preço de um produto")
    print("10 - Exibir lista de funcionários")
    print("11 - Exibir lista de clientes")
    print("12 - Exibir itens de um carrinho ")
    print("13 - Remover produto de um carrinho")
    print("14 - Imprimir cliente")
    print("15 - Imprimir funcionário")
    print("0 - Sair")

    opc = input("Insira a operação que deseja realizar: ")

    try:
        opc = int(opc)
    except ValueError:
        print("Opção inválida.")

    if opc == 0:
        break
    elif opc == 1:
        supermercado.add_funcionario()
    elif opc == 2:
        supermercado.add_cliente()
    elif opc == 3:
        supermercado.criar_carrinho()
    elif opc == 4:
        supermercado.add_produto_carrinho()
    elif opc == 5:
        supermercado.add_produto_estoque()
    elif opc == 6:
        supermercado.pagar()
    elif opc == 7:
        supermercado.exibir_estoque()
    elif opc == 8:
        supermercado.atualiza_quant()
    elif opc == 9:
        supermercado.atualiza_preco()
    elif opc == 10:
        supermercado.exibir_lista_funcionarios()
    elif opc == 11:
        supermercado.exibir_lista_clientes()
    elif opc == 12:
        supermercado.exibir_itens_carrinho()
    elif opc == 13:
        supermercado.remover_produto_carrinho()
    elif opc == 14:
        supermercado.imprimir_pessoa()
    elif opc == 15:
        supermercado.imprimir_funcionario()
    else:
        print("Opção inválida.")
