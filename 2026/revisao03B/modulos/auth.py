from flask import Blueprint, request, render_template, redirect, url_for
from modelo.usuario import buscar_por_email
from flask_login import login_user

auth_bp = Blueprint("auth", __file__)

@auth_bp.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")

    email = request.form.get("email")
    senha = request.form.get("senha")

    usuario = buscar_por_email(email)
    if usuario and usuario.senha == senha:
        login_user(usuario)
        redirect(url_for("chamados.chamados"))
    else:
       return render_template("auth/login.html") 