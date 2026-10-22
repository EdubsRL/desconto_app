# desconto_app

Sistema de pedidos de um e-commerce com diferentes tipos de desconto (normal, VIP e premium) —
disciplina **Alta Qualidade de Software**, SENAI CIMATEC.

O projeto foi construído em duas etapas:

1. **Arquitetura em camadas** (`src_antigo/`): models → repositories/database → services → controllers.
2. **Arquitetura limpa** (`src/app/`): entities → use cases → gateways → adapters → frameworks,
   com DTOs de entrada/saída e presenter (Aula 12).

## Como rodar

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements-dev.txt
python main.py                 # arquitetura limpa
python -m src_antigo.main      # versão em camadas (antiga)
```

## Arquitetura limpa

```
src/app/
├── entities/            # regras de negócio puras (Pedido, IDesconto e descontos)
├── use_cases/           # CriarPedido: coordena o fluxo, depende só de abstrações
├── gateways/            # IPedidoGateway: contrato de persistência
├── adapters/
│   ├── controllers/     # PedidoController: porta de entrada
│   └── repositories/    # MemoryPedidoRepository: implementa o gateway
├── frameworks/database/ # MemoryDatabase: detalhe de infraestrutura
├── dtos/                # CriarPedidoInputDTO (entrada) e CriarPedidoOutputDTO (saída)
└── presenters/          # PedidoPresenter: transforma o DTO de saída em dicionário (formato de exibição)
```

Regra de dependência: as setas apontam **para dentro**. `entities` não conhece ninguém;
`use_cases` conhece `entities` e o contrato `gateways`; banco e controller ficam nas bordas.

> "Gateway é o contrato. Repository é a implementação."

Fluxo de uma requisição:

```
main → PedidoController.criar_pedido(cliente, valor, tipo)
         → CriarPedidoInputDTO
         → CriarPedido.executar(input_dto) → Pedido (entity) → gateway.salvar(pedido, tipo)
         ← CriarPedidoOutputDTO
       ← PedidoPresenter.apresentar(output_dto)  →  dict pronto para exibir
```

## Qualidade

```powershell
ruff check .
ruff format .
mypy --strict src main.py
pytest -v
coverage run -m pytest ; coverage report
```

## Branches

- `main` — versão estável
- `develop` — integração
- `feature/architecture-layers` — arquitetura em camadas
- `feature/clean-architecture` — arquitetura limpa
