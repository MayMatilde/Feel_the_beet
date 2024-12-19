from database import db

playlist_musicas = db.Table(
    'playlist_musicas',
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), primary_key=True),
    db.Column('musica_id', db.Integer, db.ForeignKey('musicas.id'), primary_key=True)
)
