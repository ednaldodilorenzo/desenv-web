from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from banco import chamados, proximo_id 

chamado_bp = Blueprint("chamado", __file__)

@chamado_bp.route("/listagem", methods=["GET", "POST"])
@login_required
def index():
    valor = {
        "descricao": "Informática",
        "ano": 2026,
        "serie": "3ª Série",
    }
    return render_template("index.html",usuario_logado=current_user.nome, detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)

@chamado_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():
    if (request.method == "GET"):
        return render_template("cadastro.html")
    else:
        print(request.form["nome"])
        print(request.form["cidade"])
        chamados.append({
            "ID": proximo_id,
            "nome": request.form["nome"],
            "cidade": request.form["cidade"]
        })
        proximo_id += 1
        return redirect(url_for("index"))