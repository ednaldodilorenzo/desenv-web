from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from banco import chamados, proximo_id
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms import StringField 

chamado_bp = Blueprint("chamado", __file__)

class ChamadoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired("Campo nome é obrigatório")])
    titulo = StringField("Título", validators=[
        DataRequired("Campo título é obrigatório"),
        Length(min=5, max=250, message="O título deve ter entre 5 e 100 caracteres")
        ])

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
    
    global proximo_id
    formulario = ChamadoForm()
    if formulario.validate_on_submit():
        chamados.append({
            "id": proximo_id,
            "nome": formulario.nome.data,
            "descricao": formulario.titulo.data
        })        
        
        proximo_id += 1
        return redirect(url_for("chamado.index"))
    else:
        return render_template("cadastro_chamado.html", form=formulario)
