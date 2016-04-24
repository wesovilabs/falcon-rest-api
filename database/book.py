
from models.model import Book

class BookDB:

    ID = 0

    def __init__(self):
        self.books = []
        self.insert(Book(None,'Don Quijote de la Mancha', 'Miguel de Cervantes'))
        self.insert(Book(None, 'Romeo y Julieta', 'William Shakespeare'))

    def insert(self,book):
        self.ID+=1
        book.id = self.ID
        self.books.append(book)

    def all(self):
        return self.books

    def byId(self,book,bookId):
        return book.id == bookId


    def one(self,bookId):
        result = next(filter(lambda book: book.id == bookId,self.books),None)
        return result
