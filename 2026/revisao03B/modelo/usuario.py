from flask_login import UserMixin

class Usuario(UserMixin):
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

usuarios = [
    Usuario(1, "Ednaldo", "teste@teste.com", "1234"),
    Usuario(2, "Teste", "teste2@teste.com", "1234")
]


def user_loader(id):
    for usuario in usuarios:
        if usuario.id == id:
            return usuario
    return None

def buscar_por_email(email):
    for usuario in usuarios:
        if usuario.email == email:
            return usuario
    return None