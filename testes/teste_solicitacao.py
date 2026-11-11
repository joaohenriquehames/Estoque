# testes/teste_solicitacao.py
# Confere o caminho de uma solicitação de compra

from solicitacoes.solicitacao import SolicitacaoCompra
from usuarios.usuario import Usuario

ana = Usuario("1001", "Ana Souza", "senai123", ["solicitante"], supervisor="1002")
bruno = Usuario("1002", "Bruno Lima", "senai123", ["supervisor", "solicitante"])
carla = Usuario("1003", "Carla Mendes", "senai123", ["almoxarifado"])
eva = Usuario("1005", "Eva Ramos", "senai123", ["supervisor"])

pedido = SolicitacaoCompra("2026-0001", "Lages", ana.matricula, ana.supervisor)
print("Status inicial:", pedido.status)
print("=== Itens ===")
print(pedido.adicionar_item("P002", "Óculos de proteção", 20))
print(pedido.adicionar_item("P003", "Broca 8 mm", 0))
print("Itens:", len(pedido.itens))
print("=== Aprovação ===")
print("Ana:", pedido.aprovar(ana))
print("Eva:", pedido.aprovar(eva))
print("Bruno:", pedido.aprovar(bruno))
print("Status:", pedido.status)
print("Bruno de novo:", pedido.aprovar(bruno))
print("=== Andamento ===")
print("Ana cancela:", pedido.cancelar(ana, "Desisti"))
print("Bruno avança:", pedido.avancar(bruno))
print("Carla avança:", pedido.avancar(carla), " ", pedido.status)
print("Carla avança:", pedido.avancar(carla), "|", pedido.status)
print("Carla avança:", pedido.avancar(carla))
print("=== Histórico ===")
for h in pedido.historico:
    print(h["status"], "|", h["quem"], " ", h["nota"])
print("=== Outra solicitação ===")
outro = SolicitacaoCompra("2026-0002", "Lages", ana.matricula, ana.supervisor)
outro.adicionar_item("P001", "Luva de vaqueta", 10)
print("Sem motivo:", outro.reprovar(bruno, ""))
print("Com motivo:", outro.reprovar(bruno, "Já temos luvas"), "|", outro.status)
print("Ana cancela:", outro.cancelar(ana, "Não precisa mais"), "|", outro.status)
print(outro.para_dicionario()["status"], len(outro.para_dicionario()["historico"]))