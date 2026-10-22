import abc


class IDesconto(abc.ABC):
    """Contrato de qualquer tipo de desconto."""

    @abc.abstractmethod
    def calcular(self, valor: float) -> float:
        """Retorna o valor do desconto sobre ``valor``."""


class DescontoNormal(IDesconto):
    """Cliente normal: 10%."""

    def calcular(self, valor: float) -> float:
        """Retorna 10% do valor."""
        return valor * 0.1


class DescontoVIP(IDesconto):
    """Cliente VIP: 20%."""

    def calcular(self, valor: float) -> float:
        """Retorna 20% do valor."""
        return valor * 0.2


class DescontoPremium(IDesconto):
    """Cliente Premium: 30%."""

    def calcular(self, valor: float) -> float:
        """Retorna 30% do valor."""
        return valor * 0.3
