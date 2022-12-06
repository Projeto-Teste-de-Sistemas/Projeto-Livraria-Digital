from pytest import MonkeyPatch
from Facade import Facade
from datetime import date 
from entities.book import Book
from entities.customer import Customer
from entities.order import Order
from repositories.book_repository import BookRepository
from repositories.customer_repository import CustomerRepository
from repositories.order_repository import OrderRepository



def test_adicionar_ordem(monkeypatch):
    # Arrange
    book_repository = BookRepository()
    customer_repository = CustomerRepository()
    order_repository = OrderRepository()
    book_repository.add_books("books.csv")
    facade = Facade(book_repository,customer_repository,order_repository)
    custumer1=Customer(1,"Adm")
    facade.customerRepository.add_customer(custumer1)


    # Act
    responses = iter([1,1,1])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    result = facade.get_order_by_user()

    #Assert
    assert result == "Adicionado com sucesso"


def test_adicionar_ordem_existente(monkeypatch):
    # Arrange
    book_repository = BookRepository()
    customer_repository = CustomerRepository()
    order_repository = OrderRepository()
    book_repository.add_books("books.csv")
    facade = Facade(book_repository,customer_repository,order_repository)
    custumer1=Customer(1,"Adm")
    facade.customerRepository.add_customer(custumer1)


    # Act
    responses = iter([1,1,1,1])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    facade.get_order_by_user()
    result = facade.get_order_by_user()

    #Assert
    assert result == "O pedido já existe existe!"


def test_adicionar_ordem_sem_estoque(monkeypatch):
    # Arrange
    book_repository = BookRepository()
    customer_repository = CustomerRepository()
    order_repository = OrderRepository()
    book_repository.add_books("books.csv")
    facade = Facade(book_repository,customer_repository,order_repository)
    custumer1=Customer(1,"Adm")
    facade.customerRepository.add_customer(custumer1)


    # Act
    responses = iter([1,1,1,2,1,1])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    facade.get_order_by_user()
    result = facade.get_order_by_user()

    #Assert
    assert result == "Livro sem estoque"