from src.app.entities.pedido import Pedido
from src.app.use_cases.criar_pedido import CriarPedido


class PedidoController:
    """Porta de entrada da aplicação.

    Recebe ações externas (usuário, API, botão, formulário, CLI) e traduz essas
    entradas para o Use Case correto. O controller NÃO decide regra de negócio:
    ele apenas direciona/encaminha.
    """

    def __init__(self, criar_pedido_use_case: CriarPedido) -> None:
        """Recebe o caso de uso que será acionado."""
        self.criar_pedido_use_case = criar_pedido_use_case

    def criar_pedido(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        """Encaminha os dados para o caso de uso criar o pedido."""
        return self.criar_pedido_use_case.executar(cliente, valor_original, tipo_desconto)

    def listar_pedidos(self) -> list[Pedido]:
        """Encaminha a listagem para o caso de uso."""
        return self.criar_pedido_use_case.listar_pedidos()
