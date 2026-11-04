import secrets
from usuarios.papeis import papeis_validos

CREDENCIAL_INVALIDA = "Matrícula ou senha inválida."


class ControleAcesso:
    def __init__(self):
        self.usuarios = []
        self.sessoes = {}  # guarda {token: matricula}

    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u
        return None

    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)
        if achado is not None:
            return False
        self.usuarios.append(usuario)
        return True

    def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)
        if usuario is None or not usuario.conferir_senha(senha) or usuario.situacao != "ativo":
            return None
        
        token = secrets.token_hex(16)
        self.sessoes[token] = matricula
        return token

    def usuario_logado(self, token):
        matricula = self.sessoes.get(token)
        if matricula is None:
            return None
        return self.buscar(matricula)

    def sair(self, token):
        if token in self.sessoes:
            del self.sessoes[token]
            return True
        return False

    def mudar_papeis(self, quem, matricula, papeis):
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."
        
        alvo = self.buscar(matricula)
        if alvo is None:
            return "Usuário não encontrado."
        
        if not papeis:
            return "Escolha pelo menos um papel."
        
        validos = papeis_validos()
        for papel in papeis:
            if papel not in validos:
                return f"Papel inválido: {papel}"
        
        alvo.papeis = papeis
        return None
