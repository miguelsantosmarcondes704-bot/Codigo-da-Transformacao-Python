import random
import math

# Gerando o número aleatório
numero = random.randint(1, 10)

jogador = int(input("\nAdivinhe o número de 1 a 10: "))

if jogador == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero)

# Exemplo de uso da biblioteca math
print("\nRaiz quadrada de 81:", math.sqrt(81))