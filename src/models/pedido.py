from src.models.desconto import IDesconto


class Pedido:
    """Representa um pedido de um cliente com um tipo de desconto."""

    def __init__(self, cliente: str, desconto: IDesconto) -> None:
        """Cria o pedido (o valor é informado depois)."""
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0

    def valor_final(self, valor: float) -> float:
        """Registra o valor original e retorna o valor com desconto."""
        self.valor_original = valor
        return self.valor_original - self.desconto.calcular(self.valor_original)
