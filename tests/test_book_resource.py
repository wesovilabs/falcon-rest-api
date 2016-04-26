import json

import falcon
from resources.books import BookResource
import falcon.testing as testing
from falcon import Request,API


class TestBookResource(testing.TestBase):

    def before(self):
        self.resource = testing.TestResource()
        book_resource = BookResource()
        self.api.add_route('/books', book_resource)

    def test_on_get_one(self):
        query_string = "id=1"
        result = self.simulate_request('/books', query_string=query_string, decode='utf-8',method='GET',headers={'X-MyHeader':'AB'})
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertEqual(json.loads(result).get('title'),'Don Quijote de la Mancha')
        self.assertEqual(json.loads(result).get('author'),'Miguel de Cervantes')
        self.assertEqual(json.loads(result).get('id'),1)

    def test_on_get_one_with_no_secret_token(self):
        query_string = "id=1"
        result = self.simulate_request('/books', query_string=query_string, decode='utf-8', method='GET')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)
        self.assertEqual(json.loads(result).get('title'), 'Bad request')
        self.assertEqual(json.loads(result).get('description'), 'No valid')

    def test_on_get_all(self):
        result = self.simulate_request('/books', decode='utf-8', method='GET',headers={'X-MyHeader':'AB'})
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        books = json.loads(result)
        self.assertEqual(books.__len__(), 2)
        book_0 = books[0]
        self.assertEqual(book_0.get('title'), 'Don Quijote de la Mancha')
        self.assertEqual(book_0.get('author'), 'Miguel de Cervantes')
        self.assertEqual(book_0.get('id'), 1)
        book_1 = books[1]
        self.assertEqual(book_1.get('title'), 'Romeo y Julieta')
        self.assertEqual(book_1.get('author'), 'William Shakespeare')
        self.assertEqual(book_1.get('id'), 2)

    def test_on_get_all_with_no_secret_token(self):
        result = self.simulate_request('/books', decode='utf-8', method='GET')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)
        self.assertEqual(json.loads(result).get('title'), 'Bad request')
        self.assertEqual(json.loads(result).get('description'), 'No valid')

