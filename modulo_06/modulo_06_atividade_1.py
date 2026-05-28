# Escrevendo no arquivo TXT
arquivo = open("dados.txt", "w")
arquivo.write("Nome: Miguel\n")
arquivo.write("Idade: 16")
arquivo.close()

# Lendo o arquivo TXT
arquivo = open("dados.txt", "r")
print("\nConteúdo do TXT:")
print(arquivo.read())
arquivo.close()