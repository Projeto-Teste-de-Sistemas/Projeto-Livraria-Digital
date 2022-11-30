from entities.order import Order


class OrderRepository:

    def __init__(self) -> None:
        self.list_orders: list[Order] = []


    def add_order(self, order: Order) -> str:
        if not self.verify_exists_order(order.id):
            self.list_orders.append(order)
            return "Adicionado com sucesso"
        return"Código de pedido já existente"


    def verify_exists_order(self, order_id) -> bool:
        for item in self.list_orders:
            if (order_id == item.id):
                return True
        return False

    def __str__(self) -> str:
        for order in self.list_orders:
            return f"Código do Pedido: {order.id}\nCliente: {order.customer.name}\nData do pedido: {order.date_order}\nLivro escolhido: {order.purchased_book.name} \n"
