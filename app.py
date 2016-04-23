# app.py

__author__ = "Iván Corrales Solera <developer@wesovi.com>"
__written_date = "23/04/2016"
__title__ =""


import falcon

class BookResource(object):

    def on_get(self,req,resp):

        resp.status= falcon.HTTP_200
        resp.body = '[' \
                    '{"title":"Don Quijote de la Mancha", "author":"Miguel de Cervantes"},' \
                    '{"title":"Romeo y Julieta", "author":"Shackespeare"}' \
                    ']'


wsgi_app = api = falcon.API()
bookResource = BookResource()
api.add_route('/books', bookResource)