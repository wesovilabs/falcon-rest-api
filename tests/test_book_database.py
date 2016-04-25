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
        book = Book('La Colmenta','Camilo José Cela')
        self.bookDatabaseClient.insert(book)
        assert self.bookDatabaseClient.books.__len__() is 3
        assert book.id == 3

    def test_one(self):
        book = self.bookDatabaseClient.one(1)
        assert book is not None
        assert book.id is 1
        assert book.author == 'Miguel de Cervantes'
        assert book.title == 'Don Quijote de la Mancha'
        newBook = Book('La Colmenta', 'Camilo José Cela')
        self.bookDatabaseClient.insert(newBook)
        book = self.bookDatabaseClient.one(newBook.id)
        assert newBook.id is book.id
        assert newBook.title == book.title
        assert newBook.author == book.author