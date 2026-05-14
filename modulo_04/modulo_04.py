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

    elif opcao == "2":
        item = input("Item para remover: ")
        if item in lista:
            lista.remove(item)

    elif opcao == "3":
        print(lista)

    elif opcao == "0":
        break

aluno = {
    "nome": "Miguel",
    "idade": 16,
    "nota": 8
}

print(aluno)

numeros = [1, 2, 3, 4, 5, 6]

print("Pares:")
for n in numeros:
    if n % 2 == 0:
        print(n)

print("Ímpares:")
for n in numeros:
    if n % 2 != 0:
        print(n)

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
            print(agenda[nome])

    elif op == "3":
        nome = input("Nome: ")
        if nome in agenda:
            del agenda[nome]

    elif op == "0":
        break