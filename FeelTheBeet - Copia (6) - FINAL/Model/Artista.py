from database import db

# Classe que representa o modelo da tabela "artistas" no banco de dados
class Artista(db.Model):  
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True)  
    # Coluna "id", do tipo inteiro, que funciona como chave primária

    nome = db.Column(db.String(80), nullable=False)  
    # Coluna "nome", do tipo string

    nacionalidade = db.Column(db.String(80), nullable=False)  
    # Coluna "nacionalidade", do tipo string

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)  
    # Coluna "categoria_id", que referencia a chave primária da tabela "categorias"
    # Define a relação com outra tabela usando uma chave estrangeira (ForeignKey)

    categoria = db.relationship('Categorias', back_populates='artistas')  
    # Cria uma relação bidirecional com a tabela "categorias"
    # Permite acessar os artistas a partir de uma categoria

