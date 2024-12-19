from database import db

class Musica:
    #consulta pelo id
    @staticmethod
    def get_id(id): # função que busca no db o id da musica
        return Musica.query.get(id)
    #create
    @staticmethod
    def addMusica(nome): #função q adiciona uma musica no db
        musica = Musica(nome = nome) #possivel validação, para melhorar se ja existe uma musica com esse nome
        db.session.add(musica)  #linha 9: musica ta recebendo um novo objeto criado da classe musica
        db.session.commit() #nn se esqueça do commit
        return musica
    
    #read
    @staticmethod
    def getMusica(id): #pega o id da musica
        if id:
            return Musica.query.filter_by(id = id).all() #consulta no db, filtrando pelo id
        return id
    
    #delete musica do sistema
    @staticmethod
    def deletarMusica(id):
        musica = Musica.get_id(id)
        if musica:
            db.session.delete(musica) #mesma coisa do atualizar
            db.session.commit()
            return musica