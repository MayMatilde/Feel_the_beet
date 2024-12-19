from DAO.categoriaDAO import Categoria

class CategoriaRepository:
    def __init__(self) -> None:
        self.categoria = Categoria()

    def get_id(self,id):
        return self.categoria.get_id(id)

    def addCategoria(self,nome):
        return self.categoria.addCategoria(nome)

    def atualizarCategoria(self,id,nome):
        return self.categoria.atualizarCategoria(id,nome)

    def deletarCategoria(self,id):
        return self.categoria.deletarCategoria(id)