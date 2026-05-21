import sqlite3

conexao = sqlite3.connect("sistema.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conexao.commit()

def inserir_cliente(nome, email):
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()

def consultar_clientes():
    cursor.execute("SELECT * FROM Clientes")
    return cursor.fetchall()

def atualizar_email(id_cliente, novo_email):
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()

def deletar_cliente(id_cliente):
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conexao.commit()

def consultar_por_inicial(letra):
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    return cursor.fetchall()


cursor.execute("""
CREATE TABLE IF NOT EXISTS Tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL
)
""")
conexao.commit()

def adicionar_tarefa(descricao):
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()

def visualizar_tarefas():
    cursor.execute("SELECT * FROM Tarefas")
    return cursor.fetchall()

def excluir_tarefa(id_tarefa):
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()


inserir_cliente("Ana Souza", "ana@email.com")
inserir_cliente("Carlos Lima", "carlos@email.com")
inserir_cliente("Amanda Costa", "amanda@email.com")

atualizar_email(2, "carlos.novo@email.com")
deletar_cliente(3)

print("--- Clientes cadastrados ---")
for cliente in consultar_clientes():
    print(cliente)

print("\n--- Clientes que começam com 'A' ---")
for cliente in consultar_por_inicial("A"):
    print(cliente)

adicionar_tarefa("Estudar SQLite")
adicionar_tarefa("Subir projeto no GitHub")
excluir_tarefa(1)

print("\n--- Sistema de Tarefas ---")
for tarefa in visualizar_tarefas():
    print(tarefa)

conexao.close()