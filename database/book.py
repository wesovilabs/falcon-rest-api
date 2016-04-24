
from models.model import Book

class BookDB:

    def __init__(self):
        self.books = []
        self.books.append(Book('Don Quijote de la Mancha', 'Miguel de Cervantes'))
        self.books.append(Book('Romeo y Julieta', 'William Shakespeare'))

    def all(self):
        return self.books
