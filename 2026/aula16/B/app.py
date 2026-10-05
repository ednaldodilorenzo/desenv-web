from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from modulos.chamado.chamado import chamado_bp
from modulos.auth import auth_bp
from banco import Usuario
import mysql.connector

app = Flask(__name__)
app.secret_key = "chave_secreta_para_flash_messages"
app.register_blueprint(chamado_bp, url_prefix="/chamados")
app.register_blueprint(auth_bp, url_prefix="/auth")
DATABASE_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database":"chamados"
}

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

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

@app.route("/")
def index():
    get_db()  # Conecta ao banco de dados
    return "conectou!"  

@login_manager.user_loader
def load_user(user_id: int) -> Usuario:
    return Usuario(1, "Aluno")

if __name__ == "__main__":
    init_db()
    app.run()
