from src.models.pedido import Pedido


class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self) -> None:
        """Começa sem pedidos."""
        self.pedidos: list[Pedido] = []

    def adicionar_pedido(self, pedido: Pedido) -> None:
        """Adiciona um pedido à lista."""
        self.pedidos.append(pedido)

    def processar_pedidos(self) -> None:
        """Mostra cliente e valor final de cada pedido."""
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
