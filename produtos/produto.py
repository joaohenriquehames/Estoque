# produto.py — a classe Produto do back-end do almoxarifado
# Aqui ficam só os dados e as regras. Nada de print: quem mostra é quem chama.
 
class Produto:
    # Construtor: o produto já nasce com os quatro dados
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco
 
    # Em falta, Repor ou OK (o zero é testado primeiro)
    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 4:
            return "Repor"
        else:
            return "OK"
 
    # Devolve os dados em um dicionário: é isso que a API vai enviar
    def listar_produtos(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "situacao": self.situacao(),
        }
 
    # Entrada: soma a quantidade que chegou
    def entrada(self, qtd):
        self.quantidade = self.quantidade + qtd
 
    # Saída: só tira se houver estoque
    # Devolve True quando deu certo e False quando foi recusada
    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = self.quantidade - qtd
            return True
        return False
