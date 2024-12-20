from DAO.categoriaDAO import CategoriaDAO

class CategoriaRepository:
    def __init__(self) -> None:
        self.categoria = CategoriaDAO()

    def get_id_repository(self,id): # pega o id la no dao
        return self.categoria.get_id_dao(id)

    def addCategoria_repository(self,nome): # add categoria, vi pro dao
        return self.categoria.addCategoria_dao(nome)

    def atualizarCategoria_repository(self,id,nome): #att a categoria, tbm vai pro dao
        return self.categoria.atualizarCategoria_dao(id,nome)

    def deletarCategoria_repository(self,id): #deleta categoria
        return self.categoria.deletarCategoria_dao(id)