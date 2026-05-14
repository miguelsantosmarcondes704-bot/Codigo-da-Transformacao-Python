n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("Soma:", n1 + n2)
print("Subtração:", n1 - n2)
print("Multiplicação:", n1 * n2)
print("Divisão:", n1 / n2)

if n1 > n2:
    print(n1, "é maior")
else:
    print(n2, "é maior")

idade = int(input("Digite sua idade: "))

if idade <= 12:
    print("Criança")

elif idade <= 17:
    print("Adolescente")

elif idade <= 59:
    print("Adulto")

else:
    print("Idoso")

opcao = ""

while opcao != "0":

    print("\n1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        a = int(input("Número: "))
        b = int(input("Número: "))
        print("Resultado:", a + b)

    elif opcao == "2":
        a = int(input("Número: "))
        b = int(input("Número: "))
        print("Resultado:", a - b)

    elif opcao == "0":
        print("Programa encerrado")

    else:
        print("Opção inválida")