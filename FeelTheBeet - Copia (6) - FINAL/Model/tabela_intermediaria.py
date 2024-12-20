# Importando o objeto db do arquivo 'database' para interagir com o banco de dados
from database import db

# Definindo uma tabela auxiliar (tabela de associação) para representar o relacionamento muitos-para-muitos
# entre playlists e músicas no banco de dados
playlist_musicas = db.Table(
    'playlist_musicas',  # Nome da tabela no banco de dados
    # Definindo a primeira coluna 'playlist_id', que é uma chave estrangeira referenciando a tabela 'playlists'
    db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), primary_key=True),
    # Definindo a segunda coluna 'musica_id', que é uma chave estrangeira referenciando a tabela 'musicas'
    db.Column('musica_id', db.Integer, db.ForeignKey('musicas.id'), primary_key=True)
)
