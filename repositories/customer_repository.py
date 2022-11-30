from entities.customer import Customer


class CustomerRepository:
    def __init__(self) -> None:
        self.list_customers: list[Customer] = []

    def verify_exists_customer(self,customer_id:int) -> bool:
        for item in self.list_customers:
            if item.id == customer_id:
                return True
            else:
                return False

    def add_customer(self, customer: Customer) -> None:
        if not self.verify_exists_customer(customer.id):
            self.list_customers.append(customer)
            return("Cliente adicionado")
        return("Cliente já existente")

    def get_customer(self, customer_id:int):
         for item in self.list_customers:
            if item.id == customer_id: return item
            else: return False

    def __str__(self) -> str:
        formatText = "{0:<5} {1:<10}\n"
        str_customers = formatText.format("Id", "Nome")

        for item in self.list_customers:
            str_customers += formatText.format(item.id,item.name)

        return str_customers
