"""Dublês de teste para a arquitetura limpa."""

from typing import Any

from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway


class StubPedidoGateway(IPedidoGateway):
    """Stub/fake do gateway: guarda os registros numa lista, sem banco nenhum."""

    def __init__(self) -> None:
        self.registros: list[dict[str, Any]] = []

    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        self.registros.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

    def listar(self) -> list[dict[str, Any]]:
        return self.registros
