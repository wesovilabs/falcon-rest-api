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
        resp.status= falcon.HTTP_200
        books = self.bookDB.all()
        print ([book.title for book in books])
        resp.body = json.dumps([book.__dict__ for book in books])

