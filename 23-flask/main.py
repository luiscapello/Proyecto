from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return"Aprendiendo"

@app.route('/informacion')
def informacion():
    return "<h1>Pagina de información</h1>"

@app.route('/contacto')
def contacto():
    return "<h1>Pagina de contacto</h1>"

@app.route('/lenguajes-de-programacion')
def lenguajes():
    return "<h1>Pagina de lenguajes</h1>"

if __name__ == '__main__':
    app.run(debug=True)