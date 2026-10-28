class Almoxarifado:

    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None

    def entrada(self, codigo, qtd):
        p = self.buscar(codigo)

        if p is None:
            return False

        p.entrada(qtd)
        return True

    def saida(self, codigo, qtd):
        p = self.buscar(codigo)

        if p is None:
            return False

        return p.saida(qtd)
    
    def listar(self):
        lista = []

        for p in self.produtos:
            lista.append(p.listar_produtos())

        return lista

    def solicitacao_compra(self):
        pedido = []

        for p in self.produtos:
            if p.situacao() != "OK":
                pedido.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": p.situacao()
                })

        return pedido

    def valor_estoque(self):
        total = 0

        for p in self.produtos:
            total = total + (p.quantidade * p.preco)

        return total

    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }
