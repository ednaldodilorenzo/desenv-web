class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

usuarios = [
    Usuario(1, "Ednaldo", "ed@teste.com", "1234"),
    Usuario(2, "Teste", "teste@teste.com", "1234")
]

def buscar_pelo_email(email):
    for usuario in usuarios:
        if usuario.email == email:
            return usuario

    return None