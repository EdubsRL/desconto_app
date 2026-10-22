import pytest

from src.app.entities.desconto import DescontoNormal, DescontoPremium, DescontoVIP, IDesconto
from src.app.entities.pedido import Pedido


@pytest.mark.parametrize(
    ("desconto", "esperado"),
    [(DescontoNormal(), 90.0), (DescontoVIP(), 80.0), (DescontoPremium(), 70.0)],
)
def test_valor_final_por_tipo_de_desconto(desconto: IDesconto, esperado: float) -> None:
    pedido = Pedido("Cliente", 100.0, desconto)
    assert pedido.valor_final() == pytest.approx(esperado)


def test_valor_desconto() -> None:
    pedido = Pedido("Cliente", 200.0, DescontoVIP())
    assert pedido.valor_desconto() == pytest.approx(40.0)
