import abc

from src.app.entities.pedido import Pedido


class IPedidoGateway(abc.ABC):
    """Contrato: 'alguém capaz de salvar e listar pedidos'.

    O caso de uso não sabe (nem quer saber) se é memória, SQLite ou uma API.
    """

    @abc.abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        """Persiste um pedido."""

    @abc.abstractmethod
    def listar(self) -> list[Pedido]:
        """Retorna todos os pedidos persistidos."""
