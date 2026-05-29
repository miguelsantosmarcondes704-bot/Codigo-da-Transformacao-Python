try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    resultado = numero1 / numero2

    print(f"Resultado: {resultado}")

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")

except ValueError:
    print("Erro: digite apenas números.")