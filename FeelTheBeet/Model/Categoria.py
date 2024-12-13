from database import db

class Categorias(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    artista_id = db.Column(db.String(80), db.ForeignKey('artista.id'), nullable=False)
    