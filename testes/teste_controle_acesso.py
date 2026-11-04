from usuarios.controle_acesso import ControleAcesso
from usuarios.usuario import Usuario

acesso = ControleAcesso()

print("Cadastrar Ana:", acesso.cadastrar(Usuario("1001", "Ana Souza", "senai123", ["solicitante"], supervisor="1002")))
print("Cadastrar Bruno:", acesso.cadastrar(Usuario("1002", "Bruno Lima", "senai123", ["supervisor", "solicitante"])))
print("Cadastrar Diego:", acesso.cadastrar(Usuario("1004", "Diego Rocha", "senai123", ["admin"])))
print("Repetir a 1001:", acesso.cadastrar(Usuario("1001", "Outra Pessoa", "abc", ["solicitante"])))

print("=== Login ===")
token = acesso.entrar("1001", "senai123")
print("Entrou?", token is not None)
print("Tamanho do token:", len(token))
print("Senha errada:", acesso.entrar("1001", "errada"))
print("Matrícula que não existe:", acesso.entrar("9999", "senai123"))

print("=== Quem está logado ===")
print(acesso.usuario_logado(token).nome)
print(acesso.usuario_logado("token-inventado"))

print("=== Papéis ===")
ana = acesso.buscar("1001")
diego = acesso.buscar("1004")

print("Ana tenta:", acesso.mudar_papeis(ana, "1001", ["admin"]))
print("Diego, papel inválido:", acesso.mudar_papeis(diego, "1001", ["chefe"]))
print("Diego, certo:", acesso.mudar_papeis(diego, "1001", ["solicitante", "almoxarifado"]))
print("Papéis da Ana:", ana.papeis)

print("=== Sair ===")
print("Saiu?", acesso.sair(token))
print("Token depois de sair:", acesso.usuario_logado(token))