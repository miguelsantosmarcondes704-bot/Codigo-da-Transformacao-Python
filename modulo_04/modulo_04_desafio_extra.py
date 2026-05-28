agenda = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Remover contato")
    print("0 - Sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        agenda[nome] = telefone

    elif op == "2":
        nome = input("Nome: ")
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado!")

    elif op == "3":
        nome = input("Nome: ")
        if nome in agenda:
            del agenda[nome]
            print(f"Contato {nome} removido.")
        else:
            print("Contato não encontrado!")

    elif op == "0":
        break