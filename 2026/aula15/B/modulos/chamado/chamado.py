from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from banco import chamados, proximo_id 
from modulos.chamado.chamador_form import ChamadoForm

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
    formulario = ChamadoForm()
    global proximo_id

    if formulario.validate_on_submit():
        chamados.append({
            "id": proximo_id,
            "nome": formulario.nome.data,
            "descricao": formulario.titulo.data
        })
        
        proximo_id += 1
        return redirect(url_for("chamado.index"))

    return render_template("chamado-add.html", form=formulario)
