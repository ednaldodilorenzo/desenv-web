from flask_login import UserMixin

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]

proximo_id = 6

class Usuario(UserMixin):
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome