from datetime import date 
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

class UserInterface:
    def __init__(
        self,bookRepository:BookRepository,
        customerRepository:CustomerRepository,
        orderRepository:OrderRepository
                ) -> None:

        self.bookRepository = bookRepository
        self.customerRepository = customerRepository
        self.orderRepository = orderRepository


    def principal_menu(self) -> int:
        try:
            print("1 - Cadastrar cliente\n2 - Fazer pedido\n3 - Relatório de Pedidos\n4 - Relatório de Clientes\n5 - Relatório de Livros\n0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0

    def run(self):    
        while True:

            menu_option = self.principal_menu()
            if (menu_option == 0):
                break

            print("\n")

            if menu_option == 1: #CADASTRA CLIENTE
                id = int(input("Informe o código do cliente: "))
                name = input("Informe o nome do cliente: ")
                customer = Customer(id, name)
                print(self.customerRepository.add_customer(customer))
                

            if menu_option == 2: #fAZ PEDIDO
                id = int(input("Informe o código do pedido: "))
                customer_id = int(input("Informe o código do cliente: "))
                today = date.today()
                
                if (not self.customerRepository.verify_exists_customer(customer_id)):
                    print("Cliente não existe!")
                    
                customer = self.customerRepository.get_customer(customer_id)

                book_id = int(input("Informe o código do livro: "))
                if (not self.bookRepository.verify_exists_book(book_id)):
                    print("Livro não existe!")
                    

                book = self.bookRepository.get_book(book_id)
                order = Order(id, customer, today)
                order.purchased_book = book

                print(self.orderRepository.add_order(order))
                

            if menu_option == 3: #RELATÓRIO PEDIDOS
                print("\n***** Relatório de pedidos *****\n")
                print(self.orderRepository)

            if menu_option == 4: #RELATÓRIO CLIENTES
                print("\n***** Relatório de cliente *****\n")
                print(self.customerRepository)

            if menu_option == 5: #RELATÓRIO LIVROS
                print("\n***** Relatório de livros *****\n")
                print(self.bookRepository)
