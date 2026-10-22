from src.models.desconto import DescontoNormal, DescontoPremium, DescontoVIP
from src.models.pedido import Pedido
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    # Configuração do repositório e do serviço
    repo = PedidoRepository()
    service = PedidoService(repo)

    # Criando pedidos com desconto
    pedido1 = Pedido(cliente="Leonardo", desconto=DescontoNormal())
    pedido1.valor_original = 100.0

    pedido2 = Pedido(cliente="Cardia", desconto=DescontoVIP())
    pedido2.valor_original = 100.0

    pedido3 = Pedido(cliente="Da Cruz", desconto=DescontoPremium())
    pedido3.valor_original = 100.0

    # Salvando os pedidos (o serviço usa o repositório)
    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    # Processando os pedidos
    service.processar_pedidos()
