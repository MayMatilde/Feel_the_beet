from database import db

class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

    artistas = db.relationship('Artista', back_populates='categoria', lazy=True)
