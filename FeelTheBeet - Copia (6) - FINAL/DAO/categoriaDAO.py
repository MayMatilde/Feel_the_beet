from database import db
from Model.Categoria import Categorias

class CategoriaDAO:
    #consulta pelo id
    @staticmethod
    def get_id_dao(id): # função que busca no db o id da categoria
        return Categorias.query.get(id)
    #create
    @staticmethod
    def addCategoria_dao(nome): #função q adiciona uma categoria no db
        categoria = Categorias(nome = nome) #possivel validação, para melhorar se ja existe uma categoria com esse nome
        db.session.add(categoria)  #linha 9: categoria ta recebendo um novo objeto criado da classe categoria
        db.session.commit() #nn se esqueça do commit
        return categoria

    #update
    @staticmethod #função estatica, ja q esta se relacionando com o db
    def atualizarCategoria_dao(id,nome): #recebe como parametro o id e nome 
        categoria = Categorias.get_id_dao(id) #pegando o id no db q foi passado
        if categoria:
            categoria.nome = nome #se a categoria existir, na tabela categoria, de id tal, o nome é modificado
            db.session.commit()
            return categoria
    
    #delete
    @staticmethod
    def deletarCategoria_dao(id):
        categoria = Categorias.get_id_dao(id)
        if categoria:
            db.session.delete(categoria) #mesma coisa do atualizar
            db.session.commit()
            return categoria
        
#melhorias, adicionar validação em cada metodo com aviso de flash messages