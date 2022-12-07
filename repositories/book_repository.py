from datetime import date
from entities.book import Book


class BookRepository:

    def __init__(self) -> None:
        self.list_books: list[Book] = []


    def format_str_price_to_float(self,price: str) -> float:
        try:
            return float(price.replace("R$ ", "").replace(",", "."))
        except:
            return 0

    def add_books(self, address: str) -> None:
        file_book = list(open(address, "r", encoding="utf-8"))

        for book in file_book[1:]:
            list_book = book.split(";")
            book = Book(int(list_book[0]), list_book[1], list_book[2],
            list_book[3],list_book[4], self.format_str_price_to_float(list_book[5]))

            self.list_books.append(book)
        
    def verify_exists_book(self,book_id:int) -> bool:
        for item in self.list_books:
            if item.id == book_id:
                return True

        return False

    def verify_book_price_more_than_zero(self,book_id:int) -> bool:
        book = self.get_book(book_id)
        if book.price == 0:
            return False

        return True

    def book_stock_down(self,book_id:int) -> bool:
        book = self.get_book(book_id)
        book.stock = 0

    def get_book(self, book_id:int) -> Book:
        for item in self.list_books:
            if item.id == book_id:
                return item

        return False

    def __str__(self) -> str:
        formatText = "{0:<5} {1:<25} {2:<20} {3:<20} {4:<5} {5:<10}\n"
        str_books = formatText.format("Id", "Título","Autor", "Assunto", "Valor", "Estoque")

        for item in self.list_books:
            str_books += formatText.format(item.id, item.name,item.author,item.category,item.price,item.stock)

        return str_books

    


        