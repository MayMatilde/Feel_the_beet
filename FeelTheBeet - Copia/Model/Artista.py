from database import db

class Artista(db.Model):
    __tablename__ = 'artistas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    nacionalidade = db.Column(db.String(80), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)

    categoria = db.relationship('Categorias', back_populates='artistas')
