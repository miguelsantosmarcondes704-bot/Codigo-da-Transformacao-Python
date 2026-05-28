lista = []

while True:
    print("\n1 - Adicionar")
    print("2 - Remover")
    print("3 - Ver lista")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        item = input("Item: ")
        lista.append(item)

    if opcao == "2":
        item = input("Item para remover: ")
        if item in lista:
            lista.remove(item)
        else:
            print("Item não encontrado!")

    elif opcao == "3":
        print(lista)

    elif opcao == "0":
        break