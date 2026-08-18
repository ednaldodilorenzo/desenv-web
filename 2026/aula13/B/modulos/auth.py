from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, flash, logout_user
from banco import Usuario

auth_bp = Blueprint("auth", __file__, template_folder="templates")

@auth_bp.route("/login", methods=["GET", "POST"])
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

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))