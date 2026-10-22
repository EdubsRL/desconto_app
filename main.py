"""Ponto de entrada: monta as dependências (de fora para dentro) e executa o fluxo."""

from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.presenters.pedido_presenter import PedidoPresenter
from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":
    # Frameworks & Drivers -> Adapters -> Use Cases (a dependência aponta para dentro)
    database = MemoryDatabase()
    repository = MemoryPedidoRepository(database)
    criar_pedido = CriarPedido(repository)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido, presenter)

    # Fluxo completo: criar pedidos e calcular o desconto
    print("=== Pedidos criados ===")
    print(controller.criar_pedido("Leonardo", 100.0, "normal"))
    print(controller.criar_pedido("Cardia", 200.0, "vip"))
    print(controller.criar_pedido("Da Cruz", 300.0, "premium"))

    # Listar todos os pedidos já realizados
    print("\n=== Todos os pedidos ===")
    for pedido in controller.listar_pedidos():
        print(
            f"{pedido['cliente']:<10} | {pedido['tipo_desconto']:<8} | "
            f"original: R$ {pedido['valor_original']:>7.2f} | "
            f"desconto: R$ {pedido['valor_desconto']:>6.2f} | "
            f"final: R$ {pedido['valor_final']:>7.2f}"
        )
