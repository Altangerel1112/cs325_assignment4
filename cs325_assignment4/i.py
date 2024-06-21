from abc import ABC, abstractmethod

class Searchable(ABC):
    @abstractmethod
    def search_books(self, query):
        pass

class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, user, book_id):
        pass

    @abstractmethod
    def return_book(self, user, book_id):
        pass

class Reportable(ABC):
    @abstractmethod
    def generate_report(self):
        pass

class Library(Searchable, Borrowable, Reportable):
    def __init__(self):
        self.catalog = []
        self.borrowed_books = {}

    def search_books(self, query):
        return [book for book in self.catalog if query in book['title']]

    def borrow_book(self, user, book_id):
        self.borrowed_books[book_id] = user

    def return_book(self, user, book_id):
        if book_id in self.borrowed_books:
            del self.borrowed_books[book_id]

    def generate_report(self):
        return "Report Data"
