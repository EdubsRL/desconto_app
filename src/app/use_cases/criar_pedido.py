from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto
from src.app.entities.pedido import Pedido


class CriarPedido:
    """Caso de uso: criar um pedido aplicando o desconto conforme o tipo."""

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        """Escolhe o desconto e devolve o pedido criado."""
        desconto: IDesconto
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        return Pedido(cliente, valor_original, desconto)
