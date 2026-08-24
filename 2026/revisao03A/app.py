from flask import Flask
from auth import auth_bp
from chamado import chamado_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(chamado_bp, url_prefix="/chamados")

if __name__ == "__main__":
    app.run()