from flask import Flask

app = Flask(__name__)

@app.route('/usuarios/listar')
def listar_usuarios():
    return 'Listando usuários...'

@app.route('/usuarios/cadastrar')
def cadastrar_usuario():
    return 'Cadastrando usuário...'

@app.route('/usuarios/editar')
def editar_usuario():
    return 'Editando usuário...'

@app.route('/administradores/listar')
def listar_administradores():
    return 'Listando administradores...'

@app.route('/administradores/cadastrar')
def cadastrar_administrador():
    return 'Cadastrando administrador...'

@app.route('/administradores/editar')
def editar_administrador():
    return 'Editando administrador...'

if __name__ == '__main__':
    app.run(debug=True)