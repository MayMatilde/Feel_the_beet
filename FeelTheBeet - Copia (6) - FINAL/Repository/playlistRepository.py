from DAO.playlistDAO import PlaylistDAO

class PlaylistRepository:
    def __init__(self) -> None:
        self.playlist_repository = PlaylistDAO() #instanciando

    def get_id_playlist__repository(self,id): #pega o id no dao
        return self.playlist_repository.get_id_dao(id)

    def addPlaylist_repository(self,nome): #pega no dao pra add
        return self.playlist_repository.addPlaylist_dao(nome)
    
    def getPlaylist_repository(self,id): #pega no dao a playlist
        return self.playlist_repository.getPlaylist_dao(id)

    def atualizarPlaylist_repository(self,id,nome): #pega no dao pra att
        return self.playlist_repository.atualizarPlaylist_dao(id,nome)

    def deletarPlaylist_repository(self,id): #pega no dao pra del
        return self.playlist_repository.deletarPlaylist_dao(id)