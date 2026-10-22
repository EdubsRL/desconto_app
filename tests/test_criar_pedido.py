import pytest
from pytest_mock import MockerFixture

from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.dtos.criar_pedido_output_dto import CriarPedidoOutputDTO
from src.app.entities.desconto import DescontoPremium
from src.app.use_cases.criar_pedido import CriarPedido
from tests.doubles import StubPedidoGateway


def test_executar_devolve_output_dto_com_valores_calculados() -> None:
    use_case = CriarPedido(StubPedidoGateway())

    output = use_case.executar(CriarPedidoInputDTO("Ana", 100.0, "premium"))

    assert isinstance(output, CriarPedidoOutputDTO)
    assert output.cliente == "Ana"
    assert output.valor_desconto == pytest.approx(30.0)
    assert output.valor_final == pytest.approx(70.0)


def test_executar_salva_pedido_e_tipo_no_gateway() -> None:
    gateway = StubPedidoGateway()
    use_case = CriarPedido(gateway)

    use_case.executar(CriarPedidoInputDTO("Ana", 100.0, "premium"))

    registro = gateway.listar()[0]
    assert isinstance(registro["pedido"].desconto, DescontoPremium)
    assert registro["tipo_desconto"] == "premium"


def test_tipo_de_desconto_ignora_maiusculas_e_espacos() -> None:
    use_case = CriarPedido(StubPedidoGateway())
    output = use_case.executar(CriarPedidoInputDTO("Ana", 100.0, "  VIP "))
    assert output.valor_final == pytest.approx(80.0)


def test_tipo_invalido_levanta_erro() -> None:
    use_case = CriarPedido(StubPedidoGateway())
    with pytest.raises(ValueError, match="Tipo de desconto inválido"):
        use_case.executar(CriarPedidoInputDTO("Ana", 100.0, "black-friday"))


def test_listar_pedidos_converte_registros_em_dtos() -> None:
    use_case = CriarPedido(StubPedidoGateway())
    use_case.executar(CriarPedidoInputDTO("Ana", 100.0, "normal"))
    use_case.executar(CriarPedidoInputDTO("Bia", 200.0, "vip"))

    lista = use_case.listar_pedidos()

    assert [dto.cliente for dto in lista] == ["Ana", "Bia"]
    assert [dto.tipo_desconto for dto in lista] == ["normal", "vip"]


def test_use_case_chama_salvar_uma_vez(mocker: MockerFixture) -> None:
    """Mock: verificamos a interação com o gateway."""
    mock_gateway = mocker.Mock()
    use_case = CriarPedido(mock_gateway)

    use_case.executar(CriarPedidoInputDTO("Ana", 50.0, "normal"))

    mock_gateway.salvar.assert_called_once()
    _, tipo_salvo = mock_gateway.salvar.call_args.args
    assert tipo_salvo == "normal"
