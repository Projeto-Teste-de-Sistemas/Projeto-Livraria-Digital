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
book_repository.add_books("Aula_6/books.csv")

customer_repository.add_customer(Customer(0,"Administrador"))

user_interface = UserInterface(book_repository,customer_repository,order_repository)


user_interface.run()