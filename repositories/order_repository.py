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
        formatText = "{0:<9} {1:<10} {2:<18} {3:<25}\n"
        str_orders = formatText.format("Código", "Cliente", "Data do pedido", "Livro")

        for order in self.list_orders:
            str_orders += formatText.format(order.id, order.customer.name, str(order.date_order), order.purchased_book.name)

        return str_orders
