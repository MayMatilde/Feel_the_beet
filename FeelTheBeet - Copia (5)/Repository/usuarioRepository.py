from DAO.usuarioDAO import Usuario

class UsuarioRepository:
    
    def __init__(self) -> None:
        self.usuario = Usuario()

    def get_id(self,id):
        return self.usuario.get_id(id)

    def addUsuario(self,nome):
        return self.usuario.addUsuario(nome)
    
    def getUsuario(self,nome,email):
        return self.usuario.getUsuario(nome,email)
    
    def atualizarUsuario(self,id,nome):
        return self.usuario.atualizarUsuario(id,nome)

    def deletarUsuario(self,id):
        return self.usuario.deletarUsuario(id)