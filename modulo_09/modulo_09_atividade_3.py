try:
    idade = int(input("Digite sua idade: "))

    if idade < 0:
        print("A idade não pode ser negativa.")

    else:
        print(f"Idade válida: {idade}")

except ValueError:
    print("Digite apenas números.")