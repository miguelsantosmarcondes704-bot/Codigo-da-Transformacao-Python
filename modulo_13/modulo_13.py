import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/saudacao", methods=["GET"])
def saudacao():
    return (
        jsonify({"mensagem": "Olá! Seja bem-vindo à nossa API em Flask!"}),
        200,
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return (
            jsonify(
                {
                    "erro": "Dados inválidos. Certifique-se de enviar 'nome' e 'email'."
                }
            ),
            400,
        )

    nome = dados["nome"]
    email = dados["email"]

    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email)
        )
        conn.commit()
        conn.close()

        return (
            jsonify(
                {
                    "mensagem": "Usuário cadastrado com sucesso!",
                    "usuario": {"nome": nome, "email": email},
                }
            ),
            201,
        )

    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este e-mail já está cadastrado."}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro interno no servidor: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)