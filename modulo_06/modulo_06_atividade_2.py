import json

clientes = {
    "nome": "Miguel",
    "idade": 16,
    "cidade": "São Paulo"
}

# Salvando o dicionário em JSON
with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo)

# Carregando e exibindo o JSON
with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)

print("\nConteúdo do JSON:")
print(dados)