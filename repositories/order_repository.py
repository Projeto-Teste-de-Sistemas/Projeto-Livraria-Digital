from entities.order import Order


class OrderRepository:
    def __init__(self) -> None:
        self.list_orders: list[Order] = []

    def add_order(self, pedido: Order) -> None:
        self.list_orders.append(pedido)

    def checa_se_pedido_existe(self, pedido: Order) -> bool:
        for item in self.list_orders:
            if (pedido.id == item.id):
                return True
        return False

    