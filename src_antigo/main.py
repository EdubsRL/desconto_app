"""Versão antiga (arquitetura em camadas). Rode com: python -m src_antigo.main."""

from src_antigo.controllers.pedido_controller import PedidoController
from src_antigo.database.connection import DatabaseConnection
from src_antigo.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src_antigo.models.pedido import Pedido
from src_antigo.repositories.pedido_repository import PedidoRepository
from src_antigo.services.pedido_service import PedidoService

if __name__ == "__main__":
    # Montando as camadas: database -> repository -> service -> controller
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    pedido1 = Pedido("Cliente 1", DescontoNormal())
    pedido1.valor_original = 100.0
    pedido2 = Pedido("Cliente 2", DescontoVIP())
    pedido2.valor_original = 100.0
    pedido3 = Pedido("Cliente 3", DescontoPremium())
    pedido3.valor_original = 100.0

    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()
