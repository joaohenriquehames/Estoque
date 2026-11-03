import hashlib
import secrets
from usuarios.papeis import PERMISSOES


class Usuario:
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis
        self.supervisor = supervisor
        self.situacao = "ativo"

        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)

    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()

    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash

    def tem_papel(self, papel):
        return papel in self.papeis

    def pode(self, permissao):
        if self.situacao != "ativo":
            return False
        for papel in self.papeis:
            if papel in PERMISSOES and permissao in PERMISSOES[papel]:
                return True
        return False

    def permissoes(self):
        lista = []
        for papel in self.papeis:
            if papel in PERMISSOES:
                for permissao in PERMISSOES[papel]:
                    if permissao not in lista:
                        lista.append(permissao)
        return lista

    def trocar_senha(self, atual, nova):
        if self.conferir_senha(atual):
            self._senha_hash = self._resumir(nova)
            return True
        return False

    def para_dicionario(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "papeis": self.papeis,
            "permissoes": self.permissoes(),
            "supervisor": self.supervisor,
            "situacao": self.situacao,
        }