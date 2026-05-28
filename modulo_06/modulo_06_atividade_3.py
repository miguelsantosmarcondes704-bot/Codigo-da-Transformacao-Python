import csv

# Gravando os dados no CSV
with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Miguel", 9])
    escritor.writerow(["João", 8])

# Carregando e exibindo o CSV
with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    print("\nConteúdo do CSV:")
    for linha in leitor:
        print(linha)