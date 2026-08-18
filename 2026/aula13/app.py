from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from modulos.chamado import chamado_bp

app = Flask(__name__)
app.secret_key = "chave_secreta_para_flash_messages"
app.register_blueprint(chamado_bp, url_prefix="/chamados")

login_manager = LoginManager(app)
login_manager.login_view = "login"

class Usuario(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

@login_manager.user_loader
def load_user(user_id: int) -> Usuario:
    return Usuario(1, "Aluno")

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    
    usuario = request.form["login"]
    senha = request.form["senha"]

    if usuario == "aluno" and senha == "123456":
        usuario_login = Usuario(1, "Aluno")
        login_user(usuario_login)
        return redirect(url_for("chamado.index"))
    
    flash("Usuário ou senha inválida!")
    return render_template("login.html")
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run()
