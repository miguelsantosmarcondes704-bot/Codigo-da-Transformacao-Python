usuarios_cadastrados = {"admin": "1234", "aluno": "python2026"}

def validar_login(usuario, senha):
    return usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha

# Testando a função:
if __name__ == "__main__":
    user = input("Usuário: ")
    password = input("Senha: ")
    
    if validar_login(user, password):
        print("Acesso concedido")
    else:
        print("Acesso negado")