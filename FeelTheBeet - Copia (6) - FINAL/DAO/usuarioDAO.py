from database import db
from Model.Usuario import Usuario
from hashlib import sha256  
from Criptografia.cripSenha import CriptograSenha # importando a função paracriptografia

class UsuarioDAO:
    #consulta pelo id
    @classmethod
    def get_id_dao(cls,id): # função que busca no db o id da usuario
        return Usuario.query.get(id)
    
    #create
    @classmethod
    def addUsuario_dao(cls,nome, email, senha): #função q adiciona uma usuario no db
        criptoSenha = CriptograSenha(senha) #TEMOS CRIPTOGRAFIA, E TA FUNCIONANDO
        usuario = Usuario(nome = nome, email = email, senha = criptoSenha) #possivel validação, para melhorar se ja existe uma usuario com esse nome
        print(f'{senha}')
        # print(f'{cr}')
        db.session.add(usuario)  #linha 9: usuario ta recebendo um novo objeto criado da classe usuario
        db.session.commit() #nn se esqueça do commit
        return usuario, criptoSenha
    
    #read
    @classmethod
    def get_usuario_dao(cls,nome,email): #pega o nome e email da usuario
        if email:
           return Usuario.query.filter_by(nome=nome, email=email).first() #consulta no db, filtrando pelo id
        return email

    #update
    @classmethod #função estatica, ja q esta se relacionando com o db
    def atualizarUsuario_dao(cls,id,nome): #recebe como parametro o id e nome 
        usuario = Usuario.get_id(id) #pegando o id no db q foi passado
        if usuario :
            usuario.nome = nome #se a usuario existir, na tabela usuario, de id tal, o nome é modificado
            db.session.commit()
            return usuario
    
    #delete
    @classmethod
    def deletarUsuario_dao(cls,id):
        usuario = Usuario.get_id(id)
        if usuario:
            db.session.delete(usuario) #mesma coisa do atualizar
            db.session.commit()
            return usuario