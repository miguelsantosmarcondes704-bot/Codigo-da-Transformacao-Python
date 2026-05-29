import pytest
from app import app, init_db
import os
import sqlite3

# Configura um cliente de testes para o Flask antes de rodar os testes
@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Garante que o banco de dados de teste existe/está iniciado
    init_db()
    
    with app.test_client() as client:
        yield client

def test_rota_saudacao(client):
    """Testa se a rota GET /saudacao responde corretamente"""
    resposta = client.get('/saudacao')
    dados = resposta.get_json()
    
    assert resposta.status_code == 200
    assert dados['mensagem'] == "Olá! Seja bem-vindo à nossa API em Flask!"

def test_cadastro_usuario_sucesso(client):
    """Testa o cadastro bem-sucedido de um novo usuário"""
    # Usando um e-mail dinâmico para evitar conflito de Unique Key entre os testes
    payload = {
        "nome": "João Silva",
        "email": "joao.teste@email.com"
    }
    
    resposta = client.post('/cadastrar', json=payload)
    dados = resposta.get_json()
    
    assert resposta.status_code == 201
    assert dados['mensagem'] == "Usuário cadastrado com sucesso!"
    assert dados['usuario']['nome'] == "João Silva"

def test_cadastro_dados_invalidos(client):
    """Testa a validação de campos ausentes no POST"""
    payload = {
        "nome": "Apenas Nome"
        # Sem o campo email
    }
    
    resposta = client.post('/cadastrar', json=payload)
    dados = resposta.get_json()
    
    assert resposta.status_code == 400
    assert "erro" in dados