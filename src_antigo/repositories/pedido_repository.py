from src_antigo.database.connection import DatabaseConnection
from src_antigo.models.pedido import Pedido


class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""

    def __init__(self, database: DatabaseConnection) -> None:
        """Recebe a conexão com o banco de dados."""
        self.database = database

    def adicionar_pedido(self, pedido: Pedido) -> None:
        """Salva um pedido no banco."""
        self.database.pedidos.append(pedido)

    def listar_pedidos(self) -> list[Pedido]:
        """Retorna todos os pedidos do banco."""
        return self.database.pedidos
