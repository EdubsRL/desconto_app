"""Ponto de entrada: monta as dependências (de fora para dentro) e executa o fluxo."""

from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":
    # Frameworks & Drivers -> Adapters -> Use Cases (a dependência aponta para dentro)
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    criar_pedido = CriarPedido(repository)
    controller = PedidoController(criar_pedido)

    # Fluxo completo: criar um pedido e calcular o desconto
    pedido = controller.criar_pedido("Leonardo", 100.0, "vip")
    print(f"Cliente: {pedido.cliente}")
    print(f"Valor original: {pedido.valor_original}")
    print(f"Desconto: {pedido.valor_desconto()}")
    print(f"Valor final: {pedido.valor_final()}")
