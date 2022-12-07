from repositories.order_repository import OrderRepository
from repositories.book_repository import BookRepository
from entities.book import Book
from entities.order import Order
from entities.customer import Customer
from datetime import date


def test_verify_exists_order():
    # Arrange
    order_repository = OrderRepository()
    book = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)
    customer = Customer(1,"customer1")
    order = Order(1,customer, date.today)
    order.purchased_book = book

    # Act
    order_repository.list_orders.append(order)

    # Assert
    assert order_repository.verify_exists_order(1) == True
   
def test_add_order():
    # Arrange
    order_repository = OrderRepository()
    book = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)
    customer = Customer(1,"customer1")
    order = Order(1,customer, date.today)
    order.purchased_book = book

    # Act
    order_repository.add_order(order)

    # Assert
    assert len(order_repository.list_orders) == 1
    assert order.id == 1

