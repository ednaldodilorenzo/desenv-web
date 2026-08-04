from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "chave_secreta_para_flash_messages"

login_manager = LoginManager(app)
login_manager.login_view = "login"

class Usuario(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]
proximo_id = 0

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
        return redirect(url_for("index"))
    
    flash("Usuário ou senha inválida!")
    return render_template("login.html")
    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    valor = {
        "descricao": "Informática",
        "ano": 2026,
        "serie": "3ª Série",
    }
    return render_template("index.html",usuario_logado=current_user.nome, detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)
   


@app.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():
    if (request.method == "GET"):
        return render_template("cadastro.html")
    else:
        print(request.form["nome"])
        print(request.form["cidade"])
        chamados.append({
            "ID": proximo_id + 1,
            "nome": request.form["nome"],
            "cidade": request.form["cidade"]
        })
        proximo_id += 1
        return redirect("/")    

if __name__ == "__main__":
    app.run()
