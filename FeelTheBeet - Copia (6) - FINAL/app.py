from flask import Flask
from database import init_db
from Model import *
from Controller import *
from Controller.rotas import music

app = Flask(__name__)
app.register_blueprint(music) # Registra o Music como template.
app.secret_key = 'VamosPassardeAno' # chave para acessar os cookies da sessão para que o user não modifique o cookie|CRIPTOGRAFIA
init_db(app)

if __name__ == "__main__":
    app.run()