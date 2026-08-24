from flask import Blueprint, render_template

chamados_bp = Blueprint("chamados", __file__)

@chamados_bp.route("")
def chamados():
    return render_template("chamados/index.html")