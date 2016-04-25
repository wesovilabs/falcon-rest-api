
from database.book import BookDB,Book

class TestBookDatabase:

    def setup(self):
        self.bookDatabaseClient = BookDB()

    def test_default_database_length(self):
        assert self.bookDatabaseClient.books.__len__() == 2


    def test_all(self):
        assert self.bookDatabaseClient.all().__len__() == 2
        self.bookDatabaseClient.books.clear()
        assert self.bookDatabaseClient.all().__len__() == 0

    def test_insert(self):
        assert self.bookDatabaseClient.books.__len__() == 2
        book = Book('La Colmenta','Camilo José Cela')
        self.bookDatabaseClient.insert(book)
        assert self.bookDatabaseClient.books.__len__() == 3
        assert book.id == 3

