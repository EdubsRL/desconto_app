from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto
from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway


class CriarPedido:
    """Caso de uso: criar (e salvar) um pedido aplicando o desconto conforme o tipo.

    Depende da abstração ``IPedidoGateway`` e não conhece ``MemoryPedidoRepository``.
    """

    def __init__(self, pedido_gateway: IPedidoGateway) -> None:
        """Recebe o gateway (injeção de dependência)."""
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        """Escolhe o desconto, cria o pedido, salva e devolve."""
        desconto: IDesconto
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido)

        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        """Retorna os pedidos salvos."""
        return self.pedido_gateway.listar()
