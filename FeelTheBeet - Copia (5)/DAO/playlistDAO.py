from database import db
class Playlist:
    #consulta pelo id
    @staticmethod
    def get_id(id): # função que busca no db o id da playlist
        return Playlist.query.get(id)
    #create
    @staticmethod
    def addPlaylist(nome): #função q adiciona uma Playlist no db
        playlist = Playlist(nome = nome) #possivel validação, para melhorar se ja existe uma playlist com esse nome
        db.session.add(playlist)  #linha 9: playlist ta recebendo um novo objeto criado da classe playlist
        db.session.commit() #nn se esqueça do commit
        return playlist
    
    #read
    @staticmethod
    def getPlaylist(id): #pega o id da playlist
        if id:
            return Playlist.query.filter_by(id = id).all() #consulta no db, filtrando pelo id
        return id

    #update
    @staticmethod #função estatica, ja q esta se relacionando com o db
    def atualizarPlaylist(id,nome): #recebe como parametro o id e nome 
        playlist = Playlist.get_id(id) #pegando o id no db q foi passado
        if playlist :
            playlist.nome = nome #se a playlist existir, na tabela playlist, de id tal, o nome é modificado
            db.session.commit()
            return playlist
    
    #delete
    @staticmethod
    def deletarPlaylist(id):
        playlist = Playlist.get_id(id)
        if playlist:
            db.session.delete(playlist) #mesma coisa do atualizar
            db.session.commit()
            return playlist