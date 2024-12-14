from flask import Flask
from database import init_db
from Model import *

app = Flask(__name__)
init_db(app)

@app.route('/')
def index():
      return 'Olá, mundo'

if __name__ == "__main__":
      app.run()