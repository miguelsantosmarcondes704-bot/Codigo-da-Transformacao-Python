import json
import csv
import shutil

# 1 - Arquivo TXT

arquivo = open("dados.txt", "w")
arquivo.write("Nome: Miguel\n")
arquivo.write("Idade: 16")
arquivo.close()

arquivo = open("dados.txt", "r")
print("\nConteúdo do TXT:")
print(arquivo.read())
arquivo.close()

# 2 - Arquivo JSON

clientes = {
    "nome": "Miguel",
    "idade": 16,
    "cidade": "São Paulo"
}

with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo)

with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)

print("\nConteúdo do JSON:")
print(dados)

# 3 - Arquivo CSV

with open("notas.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)

    escritor.writerow(["Nome", "Nota"])
    escritor.writerow(["Miguel", 9])
    escritor.writerow(["João", 8])

with open("notas.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)

    print("\nConteúdo do CSV:")
    for linha in leitor:
        print(linha)

# 4 - Backup automático

shutil.copy("dados.txt", "backup_dados.txt")

print("\nBackup realizado com sucesso!")