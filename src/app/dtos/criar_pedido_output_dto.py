class CriarPedidoOutputDTO:
    """DTO (Data Transfer Object) de SAÍDA.

    É o que o caso de uso devolve: dados prontos (já calculados) em vez da
    entidade Pedido. Assim as camadas de fora (controller/presenter) não
    dependem da entidade.
    """

    def __init__(
        self,
        cliente: str,
        valor_original: float,
        valor_desconto: float,
        valor_final: float,
        tipo_desconto: str,
    ) -> None:
        """Guarda o resultado do pedido."""
        self.cliente = cliente
        self.valor_original = valor_original
        self.valor_desconto = valor_desconto
        self.valor_final = valor_final
        self.tipo_desconto = tipo_desconto
