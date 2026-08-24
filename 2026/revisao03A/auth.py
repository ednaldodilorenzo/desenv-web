from flask import Blueprint, request, render_template, flash, redirect, url_for
from usuario import buscar_pelo_email

auth_bp = Blueprint("auth", __file__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        render_template("login.html")

    login = request.form.get("login")
    senha = request.form.get("senha")

    usuario = buscar_pelo_email(login)

    if usuario and usuario.senha == senha:
       redirect(url_for("chamado.index"))
    else:
        flash("Usuário ou senha inválida!")
        render_template("login.html") 