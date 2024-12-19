from flask import Blueprint, session, render_template, request, redirect, url_for, flash
from json import load, dump
from datetime import datetime
from pathlib import Path
from database import db
from Model import Usuario
from Repository.usuarioRepository import UsuarioRepository

# Blueprint 
music = Blueprint('music', __name__)
UsuarioRepository = UsuarioRepository()

#Caminho para o Json
log_path = Path("Model/log.json")

# página inicial:
@music.route('/')
def index():
    if 'nome' in session:
        nome_usuario = session.get('nome')
        return render_template('inicio.html', nome_usuario=nome_usuario)
    return render_template('inicio.html')

# rota da página de login
@music.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['username']
        email = request.form['email']
        senha = request.form['password']

        #busca o nome e o email do usuario:
        usuario = UsuarioRepository.getUsuario(nome,email)

        # o usuario existir, então ele retorna a função playmusic
        if usuario and usuario.senha == senha:
            session['nome'] = usuario.nome
            if not log_path.exists() or log_path.stat().st_size == 0:  # Verifica existência ou arquivo vazio
                with open(log_path, "w") as f:
                    dump({}, f)  # Cria um JSON vazio
            return redirect(url_for('music.playmusic'))
        
        
        #se o usuario não existir, ele adiciona ao banco de dados
        elif not usuario:
            novo_usuario = UsuarioRepository.addUsuário(nome, email,senha)
            session['nome'] = novo_usuario.nome
            log = load(open(log_path, "r"))
            log[novo_usuario.email] = datetime.now().isoformat()
            dump(log, open(log_path, "w"), sort_keys=True, indent=4)
            return redirect(url_for('music.playmusic'))  

        else:
            flash('Usuário ou senha inválidos!', 'error')
    return render_template('login.html')

#rota da playlist do usuário
@music.route('/MinhaPlaylist', methods=['GET', 'POST'])
def playmusic():
    return render_template('playlistUser.html')

 #rota logout
@music.route('/logout')
def logout():
    session.pop('nome')
    return redirect(url_for('music.index'))
    # render_template('inicio.html')
