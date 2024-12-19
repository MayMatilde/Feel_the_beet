from database import db

# Classe que representa o modelo da tabela "playlist" no banco de dados
class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    categoria = db.Column(db.String(80), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='playlists')
    musicas = db.relationship('Musica', secondary='playlist_musicas', back_populates='playlists')
    # Cria uma relação bidirecional com a tabela "musicas" e outra com a tabela "usuario"
