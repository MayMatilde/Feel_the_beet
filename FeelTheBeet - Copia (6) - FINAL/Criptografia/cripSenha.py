# Importando o algoritmo SHA-256 da biblioteca hashlib
from hashlib import sha256

# Função para criptografar uma senha usando o algoritmo SHA-256
def CriptograSenha(senha):
    # A função 'encode()' converte a senha (que é uma string) para bytes
    # O método 'hexdigest()' converte o hash em uma string hexadecimal legível
    criptoSenha = sha256(senha.encode()).hexdigest()

    # Retorna a senha criptografada
    return criptoSenha
