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
        self.expected_book_0 = {'title': 'Don Quijote de la Mancha', 'author': 'Miguel de Cervantes', 'id': 1}
        self.expected_book_1 = {'title': 'Romeo y Julieta', 'author': 'William Shakespeare', 'id': 2}


    def test_on_get_one(self):
        query_string = "id=1"
        result = self.simulate_request('/books', query_string=query_string, decode='utf-8',method='GET',headers={'X-MyHeader':'AB'})
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertEqual(json.loads(result),self.expected_book_0)

        query_string = "id=2"
        result = self.simulate_request('/books', query_string=query_string, decode='utf-8', method='GET',headers={'X-MyHeader': 'AB'})
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
        self.assertEqual(json.loads(result), self.expected_book_1)

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
        self.assertEqual(books[0], self.expected_book_0)
        self.assertEqual(books[1], self.expected_book_1)


    def test_on_get_all_with_no_secret_token(self):
        result = self.simulate_request('/books', decode='utf-8', method='GET')
        self.assertEqual(self.srmock.status, falcon.HTTP_400)
        self.assertEqual(json.loads(result).get('title'), 'Bad request')
        self.assertEqual(json.loads(result).get('description'), 'No valid')

