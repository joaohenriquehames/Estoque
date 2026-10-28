
class Almoxarifado:

    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []
 
    def adicionar(self, produto):
        self.produtos.append(produto)

    def contar_em_falta(self):
        total = 0                       # começa o contador
        for p in self.produtos:         # cada p é um objeto Produto
            if p.situacao() == "Em falta":
                total = total + 1
        return total                    # devolve, não mostra

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
            sit = p.situacao()
            if sit == "Repor" or sit == "Em falta":
                pedido.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": sit
                })
        return pedido

    def valor_estoque(self):
        total = 0.0
        for p in self.produtos:
            total = total + (p.quantidade * p.preco)
        return total

    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }