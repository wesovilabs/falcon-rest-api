from database.book import BookDB,Book


class TestBookDatabase:

    def setup(self):
        self.bookDatabaseClient = BookDB()

    def test_default_database_length(self):
        assert self.bookDatabaseClient.books.__len__() is 2

    def test_all(self):
        assert self.bookDatabaseClient.all().__len__() is 2
        self.bookDatabaseClient.books.clear()
        assert self.bookDatabaseClient.all().__len__() is 0

    def test_insert(self):
        assert self.bookDatabaseClient.books.__len__() is 2
        book = Book('La Colmena','Camilo José Cela')
        self.bookDatabaseClient.insert(book)
        assert self.bookDatabaseClient.books.__len__() is 3
        assert book.id == 3

    def test_one(self):
        book = self.bookDatabaseClient.one(1)
        assert book is not None
        assert book.id is 1
        assert book.author == 'Miguel de Cervantes'
        assert book.title == 'Don Quijote de la Mancha'
        new_book = Book('La Colmena', 'Camilo José Cela')
        self.bookDatabaseClient.insert(new_book)
        book = self.bookDatabaseClient.one(new_book.id)
        assert new_book.id is book.id
        assert new_book.title == book.title
        assert new_book.author == book.author