from src_antigo.models.pedido import Pedido
from src_antigo.services.pedido_service import PedidoService


class PedidoController:
    """Porta de entrada: recebe as requisições e delega para o serviço."""

    def __init__(self, service: PedidoService) -> None:
        """Recebe o serviço que contém as regras de negócio."""
        self.service = service

    def adicionar_pedido(self, pedido: Pedido) -> None:
        """Encaminha o pedido para o serviço."""
        self.service.adicionar_pedido(pedido)

    def processar_pedidos(self) -> None:
        """Encaminha o processamento para o serviço."""
        self.service.processar_pedidos()
