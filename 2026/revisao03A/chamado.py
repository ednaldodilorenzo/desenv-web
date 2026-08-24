from flask import Blueprint, render_template

chamado_bp = Blueprint("chamado", __file__)

@chamado_bp.route("")
def index():
    return render_template("chamados.html")