import pytest
from pytest_mock import MockerFixture

from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO
from src.app.entities.desconto import DescontoNormal
from src.app.entities.pedido import Pedido
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido


def test_memory_repository_salva_e_lista() -> None:
    repo = MemoryPedidoRepository(MemoryDatabase())
    pedido = Pedido("Ana", 100.0, DescontoNormal())

    repo.salvar(pedido, "normal")

    assert repo.listar() == [{"pedido": pedido, "tipo_desconto": "normal"}]


def test_presenter_apresentar() -> None:
    dto = CriarPedidoOutputDTO("Ana", 100.0, 10.0, 90.0, "normal")
    assert PedidoPresenter().apresentar(dto) == {
        "cliente": "Ana",
        "valor_original": 100.0,
        "valor_desconto": 10.0,
        "valor_final": 90.0,
        "tipo_desconto": "normal",
    }


def test_presenter_apresentar_lista() -> None:
    dtos = [
        CriarPedidoOutputDTO("Ana", 100.0, 10.0, 90.0, "normal"),
        CriarPedidoOutputDTO("Bia", 100.0, 20.0, 80.0, "vip"),
    ]
    lista = PedidoPresenter().apresentar_lista(dtos)
    assert [item["cliente"] for item in lista] == ["Ana", "Bia"]


def test_controller_monta_input_dto_e_usa_o_presenter(mocker: MockerFixture) -> None:
    """Mocks: use case e presenter falsos para verificar só o encaminhamento."""
    mock_use_case = mocker.Mock()
    mock_presenter = mocker.Mock()
    controller = PedidoController(mock_use_case, mock_presenter)

    controller.criar_pedido("Ana", 100.0, "vip")

    (input_dto,) = mock_use_case.executar.call_args.args
    assert isinstance(input_dto, CriarPedidoInputDTO)
    assert (input_dto.cliente, input_dto.valor_original, input_dto.tipo_desconto) == (
        "Ana",
        100.0,
        "vip",
    )
    mock_presenter.apresentar.assert_called_once_with(mock_use_case.executar.return_value)


def test_fluxo_completo_controller_ate_banco() -> None:
    database = MemoryDatabase()
    controller = PedidoController(CriarPedido(MemoryPedidoRepository(database)), PedidoPresenter())

    criado = controller.criar_pedido("Ana", 100.0, "normal")
    lista = controller.listar_pedidos()

    assert criado["valor_final"] == pytest.approx(90.0)
    assert len(database.pedidos) == 1
    assert lista == [criado]
