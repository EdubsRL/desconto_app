from src.app.use_cases.criar_pedido import CriarPedido

if __name__ == "__main__":
    criar_pedido = CriarPedido()

    pedido = criar_pedido.executar("Leonardo", 100.0, "vip")
    print(f"Cliente: {pedido.cliente}")
    print(f"Valor final: {pedido.valor_final()}")
