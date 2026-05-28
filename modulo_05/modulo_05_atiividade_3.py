def maior_menor(lista):
    return (max(lista), min(lista)) if lista else (None, None)

# Testando a função:
if __name__ == "__main__":
    maior, menor = maior_menor([12, 45, 2, 89, 23, 7])
    print(f"Maior: {maior}, Menor: {menor}")