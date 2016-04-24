# books.py

__author__ = "Iván Corrales Solera <developer@wesovi.com>"
__written_date = "24/04/2016"

import falcon
import json
from database.book import BookDB


class BookResource(object):

    def __init__(self):
        self.props = ''
        self.bookDB = BookDB()

    def on_get(self,req,resp):
        if req.get_param("id"):
            book = self.bookDB.one(int(req.get_param("id")))
            if book == None:
                raise falcon.HTTPError(falcon.HTTP_404,'Invalid ID','There is not a book with this id')
            else:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(book.__dict__)
        else:
            books = self.bookDB.all()
            resp.status = falcon.HTTP_200
            resp.body = json.dumps([book.__dict__ for book in books])


    def delete_mode_enabled(req, resp, resource, params):
        raise falcon.HTTPBadRequest('Bad request', 'No valid')

    @falcon.before(delete_mode_enabled)
    def on_delete(self,req,resp):
        resp.status = falcon.HTTP_200


    def on_post(self,req,resp):
        try:
            raw_json = req.stream.read()
        except Exception as ex:
            raise falcon.HTTPError(falcon.HTTP_400, 'Error', ex.message)

        book = json.loads(raw_json, encoding='utf-8')
        print(book)
        resp.status = falcon.HTTP_201
        resp.body = book





