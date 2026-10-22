from src_antigo.models.pedido import Pedido


class DatabaseConnection:
    """Classe de conexão com o banco de dados (por enquanto, em memória)."""

    def __init__(self) -> None:
        """Cria a 'tabela' de pedidos."""
        self.pedidos: list[Pedido] = []
