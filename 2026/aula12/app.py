from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "chave_secreta_para_flash_messages"

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]
proximo_id = 0

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    
    usuario = request.form["login"]
    senha = request.form["senha"]

    if usuario == "aluno" and senha == "123456":
        session["usuario_logado"] = True
        return redirect(url_for("index"))
    
    flash("Usuário ou senha inválida!")
    return render_template("login.html")
    

@app.route("/logout")
def logout():
    del session["usuario_logado"]
    return redirect(url_for("login"))

@app.route("/", methods=["GET", "POST"])
def index():
    
    if not session.get("usuario_logado"):
        flash("É necessário fazer login para acessar essa tela!")
        return redirect(url_for("login"))

    valor = {
        "descricao": "Informática",
        "ano": 2026,
        "serie": "3ª Série",
    }
    return render_template("index.html", detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)
   


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():    
    if not session.get("usuario_logado"):
        flash("É necessário fazer login para acessar essa tela!")
        return redirect(url_for("login"))

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
