from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length
from database import get_db

chamado_bp = Blueprint("chamado", __file__)

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]

proximo_id = 0

class ChamadoForm(FlaskForm):
     nome = StringField("Nome", validators=[
         DataRequired("O campo nome deve ser preenchido."),
         Length(min=5, max=250, message="O campo nome deve ter entre 5 e 250 caracteres.")])
     titulo = StringField("Título", validators=[DataRequired("O campo título deve ser preenchido.")])

@chamado_bp.route("/listagem")
@login_required
def listagem():
    valor = {
            "descricao": "Informática",
            "ano": 2026,
            "serie": "3ª Série",
        }
    return render_template("index.html",usuario_logado=current_user.nome, detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)
    

@chamado_bp.route("/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():
    conexao = get_db()
    formulario = ChamadoForm()
    if formulario.validate_on_submit():
        conexao.cursor().execute(
            "INSERT INTO chamados (descricao) VALUES (%s)",
            (formulario.titulo.data,)
        )
        conexao.commit()
        return redirect(url_for("chamado.listagem"))
    
    return render_template("cadastro_chamado.html", form=formulario)

@chamado_bp.route("/cadastro/<int:id>", methods=["GET", "POST"])
@login_required
def editar(id):
    conexao = get_db()
    formulario = ChamadoForm()
    if formulario.validate_on_submit():
        conexao.cursor().execute(
            "UPDATE chamados SET descricao = %s WHERE id = %s",
            (formulario.titulo.data, id)
        )
        conexao.commit()
        return redirect(url_for("chamado.listagem"))
    return render_template("cadastro_chamado.html", form=formulario, id=id)