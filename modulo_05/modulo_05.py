def saudacao(nome):
    print(f"Olá, {nome}!")


def calcular_media(notas):
    media = sum(notas) / len(notas)
    if media >= 7:
        print(f"Média: {media:.1f} - Aprovado")
    else:
        print(f"Média: {media:.1f} - Reprovado")


def maior_menor(lista):
    return (max(lista), min(lista)) if lista else (None, None)


usuarios_cadastrados = {"admin": "1234", "aluno": "python2026"}

def validar_login(usuario, senha):
    return usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha


if __name__ == "__main__":
    saudacao("Carlos")
    
    calcular_media([8.5, 6.0, 7.5])
    
    maior, menor = maior_menor([12, 45, 2, 89, 23, 7])
    print(f"Maior: {maior}, Menor: {menor}")
    
    user = input("Usuário: ")
    password = input("Senha: ")
    if validar_login(user, password):
        print("Acesso concedido")
    else:
        print("Acesso negado")