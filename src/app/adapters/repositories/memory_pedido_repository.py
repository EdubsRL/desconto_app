from typing import Any

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

    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        """Guarda o pedido e o tipo de desconto no banco em memória."""
        self.database.pedidos.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

    def listar(self) -> list[dict[str, Any]]:
        """Retorna os registros do banco em memória."""
        return self.database.pedidos
