from DAO.usuarioDAO import UsuarioDAO

class UsuarioRepository:
    
    def __init__(self) -> None:
        self.usuario_repository = UsuarioDAO() #instancia

    def get_id_repository(self,id): #pega o id no dao
        return self.usuario_repository.get_id_dao(id)

    def addUsuario_repository(self,nome,email,senha):#pega o id no dao pra add
        return self.usuario_repository.addUsuario_dao(nome,email,senha)
    
    def getUsuario_repository(self, nome, email):#pega o usuario no dao
        # Corrigido para buscar o usuário com nome e email no banco de dados
        return self.usuario_repository.get_usuario_dao(nome,email)
    
    def atualizarUsuario_repository(self,id,nome):#pega o id no dao pra att
        return self.usuario_repository.atualizarUsuario_dao(id,nome)

    def deletarUsuario_repository(self,id):#pega o id no dao pra del
        return self.usuario_repository.deletarUsuario_dao(id)