class SaldoInsuficienteError(Exception):
    pass

saldo = 100

try:
    saque = float(input("Digite o valor do saque: "))

    if saque > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para saque.")

    saldo -= saque

    print(f"Saque realizado. Saldo atual: R$ {saldo}")

except SaldoInsuficienteError as erro:
    print(erro)

except ValueError:
    print("Digite um valor válido.")