from User_interface import UserInterface
from datetime import date 
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

book_repository = BookRepository()
customer_repository = CustomerRepository()
order_repository = OrderRepository()
book_repository.add_books("books.csv")




user_interface = UserInterface(book_repository,customer_repository,order_repository)

user_interface.run()

class Main:
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
                UserInterface.get_customer_by_user()

            
            if menu_option == 2: #fAZ PEDIDO
                UserInterface.get_order_by_user()

            if menu_option == 3: #RELATÓRIO PEDIDOS
                print("\n***** Relatório de pedidos *****\n")
                print(self.orderRepository)

            if menu_option == 4: #RELATÓRIO CLIENTES
                print("\n***** Relatório de cliente *****\n")
                print(self.customerRepository)

            if menu_option == 5: #RELATÓRIO LIVROS
                print("\n***** Relatório de livros *****\n")
                print(self.book_repository)