def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.1f} - Aprovado")
    else:
        print(f"Média: {media:.1f} - Reprovado")

# Testando a função:
if __name__ == "__main__":
    calcular_media([8.5, 6.0, 7.5])