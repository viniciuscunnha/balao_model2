from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista = [
        ['Refrigerante', 4.50],
        ['Pizza', 2.50],
        ['Suco', 24.90],
        ['Salgados', 5.50],
        ['Lanche', 18.50]
    ]
    return render_template(
        'index.html', 
        titulo ='index',
        lista = lista
    )
if __name__ == '__main__':
    app.run()