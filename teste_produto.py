from produto import produto

p1 = produto("001", "Coca-Cola", 10.99, 10, "Alimento")
p1.codigo = "001"
p1.nome = "Coca-Cola"
p1.quantidade = 10
p1.preco = 10.99
p1.tipo = "Alimento"

p2 = produto("002", "lasanha", 18.99, 50, "Alimento")
p2.codigo = "002"
p2.nome = "Lasanha"
p2.quantidade = 50
p2.preco = 18.99
p2.tipo = "Alimento"

print(p1.listar_produtos())
print(p2.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos()) 

p1.saida(15)
print(p1.listar_produtos())

if p1.saida(100):
    print("Saída realizada com sucesso!")
else:
    print("Não foi possível realizar a saída. Quantidade insuficiente.")

print(p1.quantidade) 