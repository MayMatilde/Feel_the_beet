from database import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(64), nullable=False, unique=True)

    # relacionamento entre playlist

    playlists = db.relationship('Playlist', back_populates='users', uselist=False)
