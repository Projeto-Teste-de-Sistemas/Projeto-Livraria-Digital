from repositories.order_repository import OrderRepository
from entities.book import Book

def verify_exists_order():
    # Arrange
    order_repository = OrderRepository()
    pedido1 = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)

    # Act
    order_repository.add_order(pedido1)
    resultOK = order_repository.verify_exists_order(1)
    resultNOK = order_repository.verify_exists_order(2)

    # Assert
    assert len(order_repository.list_orders) == 1
    assert resultOK == True
    assert resultNOK == False

def add_order():
    # Arrange
    order_repository = OrderRepository()
    pedido1 = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)
    
    # Act
    order_repository.add_order(pedido1)

    # Assert
    assert len(order_repository.list_orders) == 1
    assert pedido1.id == 1

