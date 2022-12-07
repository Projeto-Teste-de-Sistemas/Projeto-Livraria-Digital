from repositories.book_repository import BookRepository
from entities.book import Book

def test_add_books():
    # Arrange
    book_repository = BookRepository()
    book = Book(1,"Achados e Perdidos","9788543805900","Stephen King","Suspense", 32.08)
    
    # Act
    book_repository.add_books("books.csv")

    # Assert
    assert book_repository.list_books != 0


def test_format_str_price_to_float():
    # Arrange
    book_repository = BookRepository()
    book_str = "015;Alongamento;85-7480-264-6;Sérgio Medeiros;Literatura brasileira, Poesia;62,00"
    list_book = book.split(";")

    # Act
    book = Book(int(list_book[0]), list_book[1], list_book[2],list_book[3],list_book[4], book_repository.format_str_price_to_float(list_book[5]))

    assert book.price == 0


    
