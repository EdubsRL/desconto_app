from typing import Any


class MemoryDatabase:
    """'Banco de dados' em memória (detalhe de infraestrutura).

    Cada registro é um dicionário: {"pedido": Pedido, "tipo_desconto": str}.
    """

    def __init__(self) -> None:
        """Cria a 'tabela' de pedidos."""
        self.pedidos: list[dict[str, Any]] = []
