
# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

cursor.execute('''
               
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
               
''')

conn.commit()

print("Atividade 1 concluída: Tabela criada.")

# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

conn.commit()

print('Atividade 2 concluída: Dados inseridos.')

importar biblioteca

import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

conn.commit()

# --- CONSULTAR (Read) ---
cursor.execute("SELECT * FROM clientes")
print("Clientes atuais:", cursor.fetchall())

# --- ATUALIZAR (Update) ---
# Vamos atualizar o email do Igor Freitas
cursor.execute("UPDATE clientes SET email = 'igor.freitas@mail.com' WHERE nome = 'Igor Freitas'")

# --- DELETAR (Delete) ---
# Vamos deletar o registro do Leticia Dorta
cursor.execute("DELETE FROM clientes WHERE nome = 'Leticia Dorta'")

conn.commit()
print("Atividade 2 concluída: Operações CRUD realizadas.")

print('Atividade 2 concluída: Dados inseridos.')

# importar biblioteca
import sqlite3

# conectar banco de dados
conn = sqlite3.connect('atividade_info_cliente.db')

# executar o sql
cursor = conn.cursor()

clientes = cursor.fetchall()


cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES
                
    ('Leticia Dorta', 'joao.silva@mail.com'),
               
    ('Ayla Sousa', 'maria.oliveira@mail.com'),
               
    ('Aurélio Dinis ', 'carlos.santos@mail.com'),
               
    ('Igor Freitas', 'joao.silva@mail.com'),
               
    ('Ana Cecília ', 'maria.oliveira@mail.com'),
               
    ('Ana Alves', 'carlos.santos@mail.com'),
    
    ('André Ramalho', 'joao.silva@mail.com'),
               
    ('Maria Helena', 'maria.oliveira@mail.com'),
               
    ('Antônio Fernandes', 'carlos.santos@mail.com'),
    
    ('Ana Clara Machado', 'joao.silva@mail.com'),
               
    ('Vitor Bispo Cruz', 'maria.oliveira@mail.com'),
               
    ('Pedro Henrique', 'carlos.santos@mail.com')
               

''')

conn.commit()

cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', clientes)
conn.commit()
print("Sucesso: Novos clientes inseridos na base de dados.")

# --- CONSULTAR (Read) ---
print("\n--- LISTA DE CLIENTES ATUAIS ---")
cursor.execute("SELECT * FROM clientes")
for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]}")



# --- CONSULTAR (Somente com a letra 'A') ---
print("\n--- Clientes com nome começando com 'A' ---")
# O símbolo % é um coringa que representa "qualquer coisa depois"
cursor.execute("SELECT * FROM clientes WHERE nome LIKE 'A%'")

for cliente in cursor.fetchall():
    print(f"ID: {cliente[0]} | Nome: {cliente[1]}")

'''

1.  **Crie sua primeira tabela:** Configure um banco de 
dados SQLite e crie uma tabela 
Clientes com id, nome e email.

2.  **Implemente operações CRUD:** 
Desenvolva um programa para inserir, consultar, 
atualizar e deletar dados na tabela Clientes.

3.  **Filtre dados com SQL:** Execute consultas 
para extrair informações específicas do banco de 
dados, como clientes com nome começando em "A".

**Desafio Extra:** Crie um sistema de 
gerenciamento de tarefas que permita adicionar, 
visualizar e excluir tarefas, usando o SQLite 
para armazenar os dados.

Antônio Alves 
Alexandra Augusta 
Ana Alves
Arthur Augusto 
Antônio Alves 
Alexandra Augusta 
Adriana Almeida
Alexandre Alves
Angélica Andrade
Adriano Alvin
Augusto Albuquerque
Adriano Amaral
Alberto Alexandre 
Alice Amaral 
Alison Andrade 
Adriana Silva;
Arthur Souza
Arthur Alexandre 
Matheus Albano
Maycon augusto
Paulo Paiva
Arthur Alexandre 
Matheus Albano
Guilherme Souza
Adriano Alvin
Augusto Albuquerque
Arthur Almeida
André Alves 
Jhonatan Oliveira
Alberto Augustos;
Adriano Almeida
Miguel Soares
Miguel Soares
Jhonatas Nascimento
Lucas Freitas
Matheus Hideo

'''

import sqlite3
import json

def menu():
    conn = sqlite3.connect('atividade_info_cliente.db')
    cursor = conn.cursor()

    # Criar a tabela se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT)''')

    while True:
        print("\n--- MENU DE GERENCIAMENTO ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Todos os Clientes")
        print("3. Buscar Clientes por Letra Inicial")
        print("4. Atualizar Email de Cliente")
        print("5. Excluir Cliente")
        print("6. Exportar para JSON")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
            conn.commit()
            print("Cliente cadastrado com sucesso!")

        elif opcao == '2':
            cursor.execute("SELECT * FROM clientes")
            for c in cursor.fetchall():
                print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

        elif opcao == '3':
            letra = input("Digite a letra inicial: ")
            cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", (letra + '%',))
            for c in cursor.fetchall():
                print(f"Encontrado: {c[1]}")

        elif opcao == '4':
            nome_alvo = input("Nome do cliente para atualizar: ")
            novo_email = input("Novo email: ")
            cursor.execute("UPDATE clientes SET email = ? WHERE nome = ?", (novo_email, nome_alvo))
            conn.commit()
            print("Dados atualizados!")

        elif opcao == '5':
            nome_del = input("Nome do cliente para excluir: ")
            cursor.execute("DELETE FROM clientes WHERE nome = ?", (nome_del,))
            conn.commit()
            print("Cliente removido!")

        elif opcao == '6':
            cursor.execute("SELECT * FROM clientes")
            dados = [{"id": c[0], "nome": c[1], "email": c[2]} for c in cursor.fetchall()]
            with open('clientes.json', 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4, ensure_ascii=False)
            print("Arquivo JSON gerado com sucesso!")

        elif opcao == '0':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

    conn.close()

if __name__ == "__main__":
    menu()
