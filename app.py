# app.py

__author__ = "Iván Corrales Solera <developer@wesovi.com>"
__written_date = "23/04/2016"


import falcon

from resources.books import BookResource



wsgi_app = api = falcon.API()

api.add_route('/books', BookResource())