from flask import Blueprint, session, render_template, request,redirect, url_for, flash, abort
import json
from datetime import datetime
from pathlib import Path
from Repository.init import *
from Repository.usuarioRepository import UsuarioRepository
from Repository.playlistRepository import PlaylistRepository
from Criptografia.cripSenha import CriptograSenha

# Blueprint 
music = Blueprint('music', __name__)
usuario_repository = UsuarioRepository()  # nomes diferentes = sem confusões
playlist_repository = PlaylistRepository()
#Middleware
rotas_livres = ["music.inicio", "music.login", "music.cadastro"]

#@music.playmusic
#Middleware com o tipo before_request. Antes da requisição 
# @music.before_request
# def sessaoVerifica():
#     if request.endpoint in rotas_livres and 'nome' in session:
#          flash('Usuário logado!', 'success')
#          return rotas_livres and session
#     if 'nome' not in session:
#          # abort(401)
#          return redirect(url_for('music.index'))


# Caminho para o arquivo JSON de log
log_path = Path("Model/log.json")


# Página inicial
@music.route('/')
def index():
    if 'nome' in session: #pra passar pro html o nome_usuario
        nome_usuario = session.get('nome')
        return render_template('inicio.html', nome_usuario=nome_usuario)
    return render_template('inicio.html')

# Rota da página de login
@music.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']
        senhacripto = CriptograSenha(senha) # a senha do form é criptografa para comparar com a senha no banco de dados que ja esta criptpgrafada

        # Busca o usuário pelo nome e e-mail
        usuario = None
        usuario = usuario_repository.getUsuario_repository(nome, email)

            
        # Se o usuário existir, verifica a senha
        if usuario != None and usuario.senha == senhacripto:#compara a senha do user com a senha criptografada
            session['nome'] = usuario.nome
            #PARTE DO LOG
            if not log_path.exists() or log_path.stat().st_size == 0:
                data = [{
                    "nome": nome,
                    "email": email,
                    "timestamp": datetime.now().isoformat()
                }]
                with open(log_path, "w") as f:
                        json.dump(data, f, indent=4)
            else:
                with open(log_path, "r") as f:
                    try:
                        file_data = json.load(f)
                        if isinstance(file_data, dict):
                            file_data = [file_data]
                    except json.JSONDecodeError:
                        file_data = []

                new_entry = {
                    "nome": nome,
                    "email": email,
                    "timestamp": datetime.now().isoformat()
                }
                file_data.append(new_entry)

                with open(log_path, "w") as f:
                    json.dump(file_data, f, indent=4)
                        
            return redirect(url_for('music.playmusic'))
        
        # Se o usuário não existir, adiciona ao banco de dados
        elif not usuario:
            return redirect(url_for('music.cadastro')) 

        # Caso de erro: usuário ou senha inválidos
        else:
            flash('Usuário ou senha inválidos!', 'error')
    return render_template('login.html')

# Rota da playlist do usuário
@music.route('/MinhaPlaylist/playlist/<int:id>' , methods=['GET'])
def playmusic_playlist(id):
    playlist = playlist_repository.get_id_playlist__repository(id) # vendo se existe playlist
    if playlist: #se existir, eu mostro minha playlist
        playlist = playlist_repository.getPlaylist_repository(id)
    else:
        return render_template('playlistUser.html')
    
@music.route('/MinhaPlaylist' , methods=['GET'])
def playmusic(): #mostra so o html de playlist
    return render_template('playlistUser.html')

# @music.route('/criarPlaylist' , methods=['GET'])
# def criar_playlist():
#    return render_template('playlistUser.html')
        
#rota de cadastro
@music.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'GET': #so mostrar no cadastro
        return render_template('cadastro.html')
    else: #post
        nome = request.form.get('username')
        email = request.form.get('email')
        senha = request.form.get('password') 
        #recebo do form, e passo pro repository fazer a magica
        novo_usuario = usuario_repository.addUsuario_repository(nome, email, senha)
        session['nome'] = novo_usuario.nome
        return redirect(url_for('music.login')) #vai fazer o login

# Rota de logout
@music.route('/logout')
def logout():
    session.pop('nome', None)  # Remoção segura da sessão
    return redirect(url_for('music.index'))
