from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from modulos.chamado import chamado_bp
from modulos.auth import auth_bp
from banco import Usuario

app = Flask(__name__)
app.secret_key = "chave_secreta_para_flash_messages"
app.register_blueprint(chamado_bp, url_prefix="/chamados")
app.register_blueprint(auth_bp, url_prefix="/auth")

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id: int) -> Usuario:
    return Usuario(1, "Aluno")

if __name__ == "__main__":
    app.run()
