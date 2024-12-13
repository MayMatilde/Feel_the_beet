from database import db

class Artistas(db.Model):
    __tablename__ = 'artista'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    nacionalidade = db.Column(db.String(80), nullable=False)
    categoria_id = db.Column(db.String(80), db.ForeignKey('categorias.id'), nullable=False)

    
