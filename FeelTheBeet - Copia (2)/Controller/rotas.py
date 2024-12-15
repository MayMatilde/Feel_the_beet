from flask import Blueprint, session, render_template, request, redirect, url_for, flash
from Model import db, Usuario  # Certifique-se de que 'db' está sendo importado corretamente

# Blueprint 
music = Blueprint('music', __name__)

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
        usuario = Usuario.query.filter_by(nome=nome, email=email).first()

        #se o usuario existir, então ele retorna a função playmusic
        if usuario and usuario.senha == senha:
            session['nome'] = usuario.nome
            return redirect(url_for('music.playmusic'))  
        
        #se o usuario não existir, ele adiciona ao banco de dados
        elif not usuario:
            novo_usuario = Usuario(nome=nome, email=email, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            session['nome'] = novo_usuario.nome
            return redirect(url_for('music.playmusic'))  

        else:
            flash('Usuário ou senha inválidos!', 'erro')

    return render_template('login.html')

# rota da playlist do usuário
@music.route('/MinhaPlaylist', methods=['GET', 'POST'])
def playmusic():
    return render_template('playlistUser.html')

# rota logout
@music.route('/logout')
def logout():
    session.pop('nome', None)
    return redirect(url_for('music.index'))
