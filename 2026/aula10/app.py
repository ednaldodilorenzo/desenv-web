from flask import Flask, render_template, request, redirect

app = Flask(__name__)

chamados = [
    {"id": 1, "descricao": "Computador não liga"},
    {"id": 2, "descricao": "Impressora sem tinta"},
    {"id": 3, "descricao": "Internet lenta"},
    {"id": 4, "descricao": "Tela azul no Windows"},
    {"id": 5, "descricao": "Problema com o mouse"},
]
proximo_id = 0

@app.route("/", methods=["GET", "POST"])
def index():
    valor = {
        "descricao": "Informática",
        "ano": 2026,
        "serie": "3ª Série",
    }
    return render_template("index.html", detalhe="Detalhe dos Alunos", exibeDetalhe=False, turma=valor, chamados=chamados)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if (request.method == "GET"):
        return render_template("cadastro.html")
    else:
        print(request.form["nome"])
        print(request.form["cidade"])
        chamados.append({
            "ID": proximo_id + 1,
            "nome": request.form["nome"],
            "cidade": request.form["cidade"]
        })
        proximo_id += 1
        return redirect("/")    

if __name__ == "__main__":
    app.run()
