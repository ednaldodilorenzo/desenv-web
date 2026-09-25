from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_required

chamado_bp = Blueprint("chamado", __file__)

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]

proximo_id = 0

@chamado_bp.route("/listagem")
@login_required
def listagem():
    valor = {
            "descricao": "Informática",
            "ano": 2026,
            "serie": "3ª Série",
        }
    return render_template("index.html",usuario_logado=current_user.nome, detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)
    

@chamado_bp.route("/cadastro")
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