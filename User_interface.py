from Facade import Facade
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
facade = Facade(book_repository,customer_repository,order_repository)


def principal_menu() -> int:
        try:
            print("1 - Cadastrar cliente\n2 - Fazer pedido\n3 - Relatório de Pedidos\n4 - Relatório de Clientes\n5 - Relatório de Livros\n0 - Sair")
            return int(input("Informe a opção do menu: "))
        except:
            print("A opção informada é inválida, o programa vai ser encerrado...")
            return 0


def run() -> None:    
    while True:

        menu_option = principal_menu()
        if (menu_option == 0):
            break

        print("\n")

        if menu_option == 1: #CADASTRA CLIENTE
            print(facade.get_customer_by_user())

        if menu_option == 2: #fAZ PEDIDO
            print(facade.get_order_by_user())

        if menu_option == 3: #RELATÓRIO PEDIDOS
            print("\n***** Relatório de pedidos *****\n")
            print(facade.orderRepository)

        if menu_option == 4: #RELATÓRIO CLIENTES
            print("\n***** Relatório de cliente *****\n")
            print(facade.customerRepository)

        if menu_option == 5: #RELATÓRIO LIVROS
            print("\n***** Relatório de livros *****\n")
            print(facade.bookRepository)


if __name__ == "__main__":
    run()

