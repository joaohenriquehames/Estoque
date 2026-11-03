# papeis.py — os cargos do sistema e o que cada um pode fazer
# São os mesmos quatro papéis do sistema Almox. Uma pessoa pode ter mais de um:
# o supervisor, por exemplo, também abre as próprias solicitações.
PERMISSOES = {
    "solicitante": [
        "ver_produtos",
        "abrir_pedido",
    ],
    "supervisor": [
        "ver_produtos",
        "abrir_pedido",
        "aprovar_pedido",  # só os p    edidos em que ele é o supervisor
    ],
    "almoxarifado": [
        "ver_produto",
        "abrir_pedido",
        "cadastrar_produto",
        "movimentar_estoque",
        "andamento_pedido",  # solicitado -> recebido -> entregue
        "cancelar_pedido",  # qualquer um, mesmo depois de aprovado
        "aprovar_cadastro",
    ],
    "admin": [
        "ver_produtos",
        "cadastrar_usuario",
        "mudar_papeis",
        "aprovar_cadastro",
    ],
}


# Devolve a lista com os nomes dos papéis que existem
def papeis_validos():
    return list(PERMISSOES.keys())  # <- Adicionados 4 espaços de indentação