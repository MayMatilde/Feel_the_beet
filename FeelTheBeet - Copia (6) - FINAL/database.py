from flask_sqlalchemy import SQLAlchemy

# Criando uma instância de SQLAlchemy, que será usada para gerenciar o banco de dados
db = SQLAlchemy()

# Função que inicializa o banco de dados com a aplicação Flask
def init_db(app):

    # Configurando a URI do banco de dados. Neste caso, estamos usando SQLite com um arquivo chamado 'dadinho.db'.
    # SQLAlchemy usará essa URI para se conectar ao banco de dados.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dadinho.db'

    # Desativando o recurso de monitoramento de modificações no banco de dados, o que economiza recursos.
    # Esse recurso envia um sinal sempre que ocorre uma mudança no banco de dados.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializando o objeto db com a aplicação Flask
    db.init_app(app)

    # Usando o contexto da aplicação para garantir que o banco de dados seja criado quando a aplicação for inicializada
    # O método 'create_all()' cria todas as tabelas definidas nas classes de modelos (com base nas classes SQLAlchemy)
    with app.app_context(): 
        db.create_all()
