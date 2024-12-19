from database import db

# Classe que representa o modelo da tabela "categorias" no banco de dados
class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    # Coluna "id", do tipo inteiro, que funciona como chave primária

    nome = db.Column(db.String(80), nullable=False)
    # Coluna "nome", do tipo string

    artistas = db.relationship('Artista', back_populates='categoria', lazy=True)
    # Cria uma relação bidirecional com a tabela "artistas"
    # Permite acessar as categorias a partir de um artista
