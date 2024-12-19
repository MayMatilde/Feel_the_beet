from DAO.usuarioDAO import Usuario

class UsuarioRepository:
    def __init__(self) -> None:
        self.usuario = Usuario()

    def get_id(self,id):
        return self.usuario.get_id(id)

    def addUsuário(self,nome):
        return self.usuario.addUsuário(nome)
    
    def getUsuario(self,nome,email):
        return self.usuario.getUsuario(nome,email)
    
    def atualizarUsuário(self,id,nome):
        return self.usuario.atualizarUsuário(id,nome)

    def deletarUsuário(self,id):
        return self.usuario.deletarUsuário(id)