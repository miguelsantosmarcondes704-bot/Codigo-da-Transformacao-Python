importar biblioteca
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
