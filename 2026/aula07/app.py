from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/professores')
def professores():
    return render_template('professores.html')

if __name__ == '__main__':
    app.run(debug=True)