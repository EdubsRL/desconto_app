from src.app.entities.pedido import Pedido
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.gateways.pedido_gateway import IPedidoGateway


class MemoryPedidoRepository(IPedidoGateway):
    """Repository Adapter: implementa o contrato do gateway usando memória.

    "Gateway é o contrato. Repository é a implementação."
    Para trocar por SQLite, basta criar outro adapter (ex.: SqlitePedidoRepository).
    """

    def __init__(self, database: MemoryDatabase) -> None:
        """Recebe o banco em memória."""
        self.database = database

    def salvar(self, pedido: Pedido) -> None:
        """Guarda o pedido no banco em memória."""
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        """Retorna os pedidos do banco em memória."""
        return self.database.pedidos
