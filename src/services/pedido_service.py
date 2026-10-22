from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository


class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""

    def __init__(self, repository: PedidoRepository) -> None:
        """Recebe o repositório onde os pedidos ficam guardados."""
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido) -> None:
        """Salva o pedido através do repositório."""
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self) -> None:
        """Mostra cliente e valor final de cada pedido salvo."""
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {pedido.valor_final(pedido.valor_original)}")
