from typing import Any

from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


class PedidoController:
    """Porta de entrada da aplicação.

    Recebe ações externas (usuário, API, botão, formulário, CLI), monta o DTO de
    entrada, aciona o Use Case e entrega a resposta ao Presenter. O controller
    NÃO decide regra de negócio: ele apenas direciona/encaminha.
    """

    def __init__(self, criar_pedido_use_case: CriarPedido, presenter: PedidoPresenter) -> None:
        """Recebe o caso de uso e o presenter."""
        self.criar_pedido_use_case = criar_pedido_use_case
        self.presenter = presenter

    def criar_pedido(
        self, cliente: str, valor_original: float, tipo_desconto: str
    ) -> dict[str, Any]:
        """Cria um pedido e devolve o pedido já formatado pelo presenter."""
        input_dto = CriarPedidoInputDTO(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto,
        )

        output_dto = self.criar_pedido_use_case.executar(input_dto)

        return self.presenter.apresentar(output_dto)

    def listar_pedidos(self) -> list[dict[str, Any]]:
        """Lista todos os pedidos já realizados, formatados pelo presenter."""
        output_dtos = self.criar_pedido_use_case.listar_pedidos()

        return self.presenter.apresentar_lista(output_dtos)
