from src.app.entities.pedido import Pedido


class MemoryDatabase:
    """'Banco de dados' em memória (detalhe de infraestrutura)."""

    def __init__(self) -> None:
        """Cria a 'tabela' de pedidos."""
        self.pedidos: list[Pedido] = []
