from produtos.produto import Produto

p1 = Produto("001", "Coca-Cola", 10.99, 10)
p1.tipo = "Alimento"

p2 = Produto("002", "Lasanha", 18.99, 50)
p2.tipo = "Alimento"

print(p1.listar_produtos())
print(p2.listar_produtos())

p1.entrada(30)