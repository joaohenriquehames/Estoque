

class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 4:
            return "Repor"
        else:
            return "OK"

    def listar_produtos(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "situacao": self.situacao()
        }

    def entrada(self, qtd):
        self.quantidade = self.quantidade + qtd

    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = self.quantidade - qtd
            return True
        return False
