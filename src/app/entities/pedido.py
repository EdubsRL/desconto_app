from src.app.entities.desconto import IDesconto


class Pedido:
    """Entidade Pedido: não depende de banco, framework ou tela."""

    def __init__(self, cliente: str, valor_original: float, desconto: IDesconto) -> None:
        """Cria o pedido já com o valor e o tipo de desconto."""
        self.cliente = cliente
        self.valor_original = valor_original
        self.desconto = desconto

    def valor_desconto(self) -> float:
        """Quanto será descontado."""
        return self.desconto.calcular(self.valor_original)

    def valor_final(self) -> float:
        """Valor a pagar depois do desconto."""
        return self.valor_original - self.valor_desconto()
