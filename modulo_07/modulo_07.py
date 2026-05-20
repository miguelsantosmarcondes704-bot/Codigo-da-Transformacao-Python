import random
import math
from datetime import datetime

# 1 - Funções matemáticas

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def potencia(a, b):
    return a ** b

print("Soma:", soma(10, 5))
print("Subtração:", sub(10, 5))
print("Potência:", potencia(2, 3))

# 2 - Biblioteca datetime

agora = datetime.now()

print("\nData e hora atual:")
print(agora)

# 3 - Jogo de adivinhação

numero = random.randint(1, 10)

jogador = int(input("\nAdivinhe o número de 1 a 10: "))

if jogador == numero:
    print("Você acertou!")
else:
    print("Você errou!")
    print("O número era", numero)

print("\nRaiz quadrada de 81:", math.sqrt(81))