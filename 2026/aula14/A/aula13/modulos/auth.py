from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from modelo.usuario import Usuario

auth_bp = Blueprint("auth", __file__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    
    usuario = request.form["login"]
    senha = request.form["senha"]

    if usuario == "aluno" and senha == "123456":
        usuario_login = Usuario(1, "Aluno")
        login_user(usuario_login)
        return redirect(url_for("chamado.listagem"))
    
    flash("Usuário ou senha inválida!")
    return render_template("login.html")
    

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))