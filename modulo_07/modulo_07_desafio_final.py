import os
import random
import math
from datetime import datetime

# ==============================================================================
# EXERCÍCIO 1: Criar um módulo utilidades.py e importar no programa principal
# ==============================================================================
print("--- EXERCÍCIO 1 ---")

# Criando o arquivo utilidades.py via código para simular o módulo
conteudo_modulo = """def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def potencia(a, b):
    return a ** b
"""

with open("utilidades.py", "w", encoding="utf-8") as f:
    f.write(conteudo_modulo)

# Agora importamos o módulo que acabamos de criar
import utilidades

print("Soma:", utilidades.soma(10, 5))
print("Subtração:", utilidades.sub(10, 5))
print("Potência:", utilidades.potencia(2, 3))


# ==============================================================================
# EXERCÍCIO 2: Instale e utilize uma biblioteca externa (faker, datetime, etc.)
# ==============================================================================
print("\n--- EXERCÍCIO 2 ---")

agora = datetime.now()

print("Data e hora atual:")
print(agora)


# ==============================================================================
# EXERCÍCIO 3: Use math e random para criar um jogo de adivinhação
# ==============================================================================
print("\n--- EXERCÍCIO 3 ---")

numero_secreto = random.randint(1, 10)

jogador = int(input("Adivinhe o número de 1 a 10: "))

if jogador == numero_secreto:
    print("Você acertou!")
else:
    print(f"Você errou! O número era {numero_secreto}")

# Demonstração extra usando a biblioteca math
print("Raiz quadrada de 81:", math.sqrt(81))


# ==============================================================================
# DESAFIO EXTRA: Organize um projeto grande em pacotes
# ==============================================================================
print("\n--- DESAFIO EXTRA ---")

# Criando a estrutura de pastas (pacote) via código para simular o projeto
os.makedirs("meu_pacote", exist_ok=True)

# Criando o arquivo __init__.py (necessário para o Python reconhecer como pacote)
with open("meu_pacote/__init__.py", "w") as f:
    pass

# Criando o arquivo de funções dentro do pacote
conteudo_pacote = """def mensagem_sucesso():
    return "Pacote importado e executado com sucesso!"
"""

with open("meu_pacote/funcoes.py", "w", encoding="utf-8") as f:
    f.write(conteudo_pacote)

# Importando e utilizando a função do nosso pacote recém-criado
from meu_pacote.funcoes import mensagem_sucesso

print(mensagem_sucesso())