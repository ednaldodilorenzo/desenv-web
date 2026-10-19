from flask import g
import mysql.connector

DATABASE_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "chamados"
}

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    return g.db

def init_db():
    print("Conectando no banco de dados...")
    conexao = mysql.connector.connect(**DATABASE_CONFIG)
    cursor = conexao.cursor()
    script = """
    CREATE TABLE IF NOT EXISTS chamados (
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(100) NOT NULL,
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

    try:
        cursor.execute(script)
        conexao.commit()
    except mysql.connector.Error as err:
        print("Falha de conexão com banco de dados.")
    finally:
        cursor.close()
        conexao.close()