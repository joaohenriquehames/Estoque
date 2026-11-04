from usuarios.usuario import Usuario

ana = Usuario("1001", "Ana Souza", "senai123", ["solicitante"], supervisor="1002")
bruno = Usuario("1002", "Bruno Lima", "senai123", ["supervisor", "solicitante"])
carla = Usuario("1003", "Carla Mendes", "senai123", ["almoxarifado"])

print("=== Senha ===")
print("Senha certa:", ana.conferir_senha("senai123"))
print("Senha errada:", ana.conferir_senha("123456"))
print("A senha aparece?", "senai123" in str(ana.para_dicionario()))

print("=== Papéis ===")
print("Bruno é supervisor?", bruno.tem_papel("supervisor"))
print("Ana é supervisor?", ana.tem_papel("supervisor"))

print("=== Permissões ===")
print("Ana abre pedido?", ana.pode("abrir_pedido"))
print("Ana aprova pedido?", ana.pode("aprovar_pedido"))
print("Bruno aprova pedido?", bruno.pode("aprovar_pedido"))
print("Carla movimenta estoque?", carla.pode("movimentar_estoque"))

print("=== Todas as permissões ===")
print("Ana:", ana.permissoes())
print("Bruno:", bruno.permissoes())

print("=== Cadastro inativo ===")
carla.situacao = "inativo"
print("Carla inativa movimenta estoque?", carla.pode("movimentar_estoque"))

print("=== Trocar senha ===")
print("Com a atual errada:", ana.trocar_senha("errada", "nova123"))
print("Com a atual certa:", ana.trocar_senha("senai123", "nova123"))
print("Senha nova vale?", ana.conferir_senha("nova123"))

print("=== Dicionário ===")
print(bruno.para_dicionario())