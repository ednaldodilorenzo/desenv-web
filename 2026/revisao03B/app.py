from flask import Flask
from modulos.auth import auth_bp
from modulos.chamados import chamados_bp
from flask_login import LoginManager

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chamados_bp, url_prefix="/chamados")

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

if __name__ == "__main__":
    app.run()