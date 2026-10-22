class CriarPedidoInputDTO:
    """DTO (Data Transfer Object) de ENTRADA.

    Objeto usado apenas para transportar dados entre camadas: leva o que veio
    de fora (controller) até o caso de uso, de forma organizada, previsível e
    desacoplada. Não tem regra de negócio.
    """

    def __init__(self, cliente: str, valor_original: float, tipo_desconto: str) -> None:
        """Guarda os dados necessários para criar um pedido."""
        self.cliente = cliente
        self.valor_original = valor_original
        self.tipo_desconto = tipo_desconto
