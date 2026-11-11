# solicitacoes/solicitacao.py
# A classe SolicitacaoCompra: o pedido que vai para o setor de compras

AGUARDANDO = "aguardando_aprovacao"
REPROVADO = "sem_aprovacao_gestor"
SOLICITADO = "solicitado"
RECEBIDO = "recebido"
ENTREGUE = "entregue"
CANCELADO = "cancelado"

# A ordem que o almoxarifado segue depois da aprovação
ANDAMENTO = [SOLICITADO, RECEBIDO, ENTREGUE]
ENCERRADOS = [ENTREGUE, CANCELADO]


class SolicitacaoCompra:
    # Construtor: o pedido nasce com número, unidade, quem pediu e quem aprova
    def __init__(self, numero, unidade, solicitante, supervisor):
        self.numero = numero
        self.unidade = unidade
        self.solicitante = solicitante  # matrícula de quem abriu
        self.supervisor = supervisor    # matrícula de quem aprova
        self.itens = []
        self.status = AGUARDANDO
        self.historico = []
        self._registrar(solicitante, "Solicitação aberta")

    # Guarda cada mudança: quem fez, para qual status e por quê
    def _registrar(self, quem, nota):
        self.historico.append({"status": self.status, "quem": quem, "nota": nota})

    # Acrescenta um item; só enquanto ninguém aprovou
    def adicionar_item(self, codigo, nome, quantidade):
        if self.status != AGUARDANDO:
            return "Depois de aprovada, a solicitação não recebe itens novos."
        if quantidade <= 0:
            return "A quantidade precisa ser maior que zero."
        self.itens.append({"codigo": codigo, "nome": nome, "quantidade": quantidade})
        return None

    # Só o supervisor DESTE pedido aprova, e só se estiver aguardando
    def aprovar(self, usuario):
        if not usuario.pode("aprovar_pedido") or usuario.matricula != self.supervisor:
            return "Só o supervisor desta solicitação pode aprová-la."
        if self.status != AGUARDANDO:
            return "Só dá para aprovar o que está aguardando aprovação."
        if len(self.itens) == 0:
            return "A solicitação não tem itens."
        self.status = SOLICITADO
        self._registrar(usuario.matricula, "Aprovada")
        return None

    # Reprova o pedido (apenas supervisor do pedido e se estiver aguardando)
    def reprovar(self, usuario, motivo):
        if not usuario.pode("aprovar_pedido") or usuario.matricula != self.supervisor:
            return "Só o supervisor desta solicitação pode reprová-la."
        if self.status != AGUARDANDO:
            return "Só dá para reprovar o que está aguardando aprovação."
        if not motivo or motivo.strip() == "":
            return "Informe o motivo da reprovação."
        self.status = REPROVADO
        self._registrar(usuario.matricula, motivo)
        return None

    # Avança a etapa no almoxarifado
    def avancar(self, usuario):
        if not usuario.pode("andamento_pedido"):
            return "Só o almoxarifado mexe no andamento da compra."
        if self.status not in ANDAMENTO or self.status == ENTREGUE:
            return "Esta solicitação não está em andamento."
        posicao = ANDAMENTO.index(self.status)
        self.status = ANDAMENTO[posicao + 1]
        self._registrar(usuario.matricula, "Etapa concluída")
        return None

    # Cancela o pedido
    def cancelar(self, usuario, motivo):
        if self.status in ENCERRADOS:
            return "Esta solicitação já está encerrada."
        if usuario.pode("cancelar_pedido"):
            pass
        elif usuario.matricula != self.solicitante:
            return "Só quem abriu ou o almoxarifado pode cancelar."
        elif self.status != AGUARDANDO and self.status != REPROVADO:
            return "Depois de aprovada, só o almoxarifado pode cancelar."
        self.status = CANCELADO
        self._registrar(usuario.matricula, motivo)
        return None

    # Retorna o dicionário representativo
    def para_dicionario(self):
        return {
            "numero": self.numero,
            "unidade": self.unidade,
            "solicitante": self.solicitante,
            "supervisor": self.supervisor,
            "status": self.status,
            "itens": self.itens,
            "historico": self.historico,
        }