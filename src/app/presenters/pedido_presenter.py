from typing import Any

from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO


class PedidoPresenter:
    """Presenter: transforma o resultado do caso de uso em formato de exibição.

    Aqui o formato é um dicionário (parecido com um JSON de uma API). Desacopla a
    regra de negócio da forma como a informação é mostrada ao usuário.
    """

    def apresentar(self, output_dto: CriarPedidoOutputDTO) -> dict[str, Any]:
        """Formata UM pedido."""
        return {
            "cliente": output_dto.cliente,
            "valor_original": output_dto.valor_original,
            "valor_desconto": output_dto.valor_desconto,
            "valor_final": output_dto.valor_final,
            "tipo_desconto": output_dto.tipo_desconto,
        }

    def apresentar_lista(self, output_dtos: list[CriarPedidoOutputDTO]) -> list[dict[str, Any]]:
        """Formata uma lista de pedidos."""
        lista_formatada = []

        for output_dto in output_dtos:
            pedido_formatado = self.apresentar(output_dto)
            lista_formatada.append(pedido_formatado)

        return lista_formatada
