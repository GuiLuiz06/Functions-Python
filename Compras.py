## Gerenciador de compras
lista_de_compras = []
def lista_compras_programa():

    print("Seja bem vindo ao gerenciador de compras")

    while True:
        print("\n-------Menu-------")
        print("1. Adicionar itens à lista")
        print("2. Visualizar lista completa")
        print("3. Remover um item da lista")
        print("4. Sair do programa")
        print()
        escolha_usuario = input("Digite o número para onde você deseja ir: ")

        if escolha_usuario == "1":
            ##entrada de dados do item que o usuario deseja adicionar
            item = input("Qual item você deseja adicionar: ")
            ## adiciona item do usuario à lista
            lista_de_compras.append(item)
            ## informativo que o item foi adicionado
            print(f"item '{item}' adicionado com sucesso!")
        elif escolha_usuario == "2":
            if not lista_de_compras:
                ## informativo sobre a lista vazia
                print("A lista de compras está vazia.")
            else:
                ## informativo da lista de itens
                print("Segue a lista atual dos seus itens: ")
                for compra in lista_de_compras:
                    print(compra)
        elif escolha_usuario == "3":
            ## Entrada de dados do item que o usuario deseja remover
            item_remove = str(input("Escolha um item para remover da lista: "))
            ## remove o item escolhido
            if item_remove in lista_de_compras:
                lista_de_compras.remove(item_remove)
                print(f"item {item_remove} removido com sucesso!")
            else:
                print(f"O item {item_remove} não está na lista. Verifique a lista e remova o item correto")
        elif escolha_usuario > "4":
            ## informativo caso o usuario digite um numero invalido
            print("Por gentiliza, digite um número válido.")
        else:
            ## encerramento do programa
            print("Saindo do programa...")
            break

if __name__ == "__main__":
    lista_compras_programa()