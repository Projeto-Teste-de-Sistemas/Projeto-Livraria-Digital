from repositories.order_repository import OrderRepository
from entities.book import Book

def test_checa_se_pedido_existe():
    # Arrange
    order_repository = OrderRepository()
    order_repository.list_orders = []
    pedido1 = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)

    # Act
    destino_repository.adicionar_destino(destino1)
    resultOK = destino_repository.checa_se_destino_existe(destino1)
    resultNOK = destino_repository.checa_se_destino_existe(destino2)

    # Assert
    assert len(destino_repository.lista_destino) == 1
    assert resultOK == True
    assert resultNOK == False
