from flask import Flask, render_template

app = Flask(__name__)

@app.route('/usuarios/listar')
def listar_usuarios():
    return render_template('listar_usuarios.html')

@app.route('/usuarios/cadastrar', methods=['GET', 'POST'])
def cadastrar_usuario():
    return render_template('cadastrar_usuario.html')

@app.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    return render_template('editar_usuario.html', id=id)

@app.route('/administradores/listar')
def listar_administradores():
    return render_template('listar_administradores.html')

@app.route('/administradores/cadastrar', methods=['GET', 'POST'])
def cadastrar_administrador():
    return render_template('cadastrar_administrador.html')

@app.route('/administradores/editar/<int:id>', methods=['GET', 'POST'])
def editar_administrador(id):
    return render_template('editar_administrador.html', id=id)

if __name__ == '__main__':
    app.run(debug=True)