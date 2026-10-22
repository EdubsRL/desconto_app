import abc
from typing import Any

from src.app.entities.pedido import Pedido


class IPedidoGateway(abc.ABC):
    """Contrato: 'alguém capaz de salvar e listar pedidos'.

    O caso de uso não sabe (nem quer saber) se é memória, SQLite ou uma API.
    """

    @abc.abstractmethod
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        """Persiste um pedido junto com o tipo de desconto escolhido."""

    @abc.abstractmethod
    def listar(self) -> list[dict[str, Any]]:
        """Retorna os registros salvos: {"pedido": Pedido, "tipo_desconto": str}."""
