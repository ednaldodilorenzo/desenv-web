from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")
    
    
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if (request.method == "GET"):
        return render_template("cadastro.html")
    else:
        print(request.form["nome"])
        print(request.form["cidade"])
        return redirect("/")    

if __name__ == "__main__":
    app.run()
