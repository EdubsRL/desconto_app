from src.models.pedido import Pedido


class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self) -> None:
        """Começa sem pedidos armazenados."""
        self.pedidos: list[Pedido] = []

    def adicionar_pedido(self, pedido: Pedido) -> None:
        """Salva um pedido."""
        self.pedidos.append(pedido)

    def listar_pedidos(self) -> list[Pedido]:
        """Retorna todos os pedidos salvos."""
        return self.pedidos
