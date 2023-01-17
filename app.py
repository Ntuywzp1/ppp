from flask import Flask

app = Flask(__name__)

# olá rota
@app.route('/ola')
def ola_mundo():
    return "Olá,mundo"


@app.route('/ola/<nome>')
def ola_mundo1(nome="mundo"):
    return "Olá, " + nome


if __name__ == '__main__':
    app.run()
