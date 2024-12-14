from database import db

class Musica(db.Model):
    __tablename__ = 'musicas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)  
    artista = db.Column(db.String(80), nullable=False) 
    categoria = db.Column(db.String(80), nullable=False)  
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)

    playlists = db.relationship('Playlist', secondary='playlist_musicas', back_populates='musicas')
