from flask_login import UserMixin
import mysql
import mysql.connector

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]

DATABASE_CONFIG = {
    "host": "10.13.133.55",
    "user": "root",
    "password": "123456",
    "database":"chamados"
}

proximo_id = 6

def get_db():
    db = mysql.connector.connect(**DATABASE_CONFIG)
    return db

def init_db():
    conexao = get_db()
    print("Conectando ao bd")
    script = """
    CREATE TABLE IF NOT EXISTS chamados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(100) NOT NULL,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
"""
    try:
        cursor = conexao.cursor()
        cursor.execute(script)
    except mysql.connector.Error as err:
        print("Erro de conexão com BD")
    finally:
        cursor.close()
        conexao.close()

class Usuario(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome