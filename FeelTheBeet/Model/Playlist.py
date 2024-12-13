from database import db

class Playlist(db.Model):
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)
    nome_da_musica = db.Column(db.String(80), nullable=False)
    usuarios_id = db.Column(db.String(80), db.ForeignKey('usuarios.id'), nullable=False)
    artista_id = db.Column(db.String(80), db.ForeignKey('artista.id'), nullable=False)
    categoria_id = db.Column(db.String(80), db.ForeignKey('categorias.id'), nullable=False)

# relacionamento entre o usuario

    users = db.relationship('Usuario', back_populates='playlists')

