from flask import Flask, render_template

app = Flask(__name__)

dados = [
    {
        "id": 1,
        "nome": "Mynd Linux",
        "idade": 13.5,
    },
    {
        "id": 2,
        "nome": "Lucas",
        "idade": 27,
    },
    {
        "id": 3,
        "nome": "Vitória",
        "idade": 14,
    },
    {
        "id": 4,
        "nome": "Fátima",
        "idade": 15,
    }
]

@app.route("/")
def index():
    return render_template("index.html", alunos=dados)

app.run()