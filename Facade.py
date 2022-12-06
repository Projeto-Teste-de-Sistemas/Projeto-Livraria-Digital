from datetime import date 
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository

class Facade:
    def __init__(
        self,bookRepository:BookRepository,
        customerRepository:CustomerRepository,
        orderRepository:OrderRepository
                ) -> None:

        self.bookRepository = bookRepository
        self.customerRepository = customerRepository
        self.orderRepository = orderRepository

    def get_customer_by_user(self)->str:
        id = int(input("Informe o código do cliente: "))
        name = input("Informe o nome do cliente: ")
        customer = Customer(id, name)
                    
        return(self.customerRepository.add_customer(customer))
                

    def get_order_by_user(self)->str:
                id = int(input("Informe o código do pedido: "))
                if (self.orderRepository.verify_exists_order(id)):
                    return("O pedido já existe existe!")

                customer_id = int(input("Informe o código do cliente: "))
                today = date.today()
                
                if (not self.customerRepository.verify_exists_customer(customer_id)):
                    return("Cliente não existe!")
                    
                customer = self.customerRepository.get_customer(customer_id)

                book_id = int(input("Informe o código do livro: "))
                if (not self.bookRepository.verify_exists_book(book_id)):
                    return("Livro não existe!")


                book = self.bookRepository.get_book(book_id)
                if(book.stock == 0):
                    return("Livro sem estoque")

                book.stock = 0
                order = Order(id, customer, today)
                order.purchased_book = book


                return(self.orderRepository.add_order(order))


            
