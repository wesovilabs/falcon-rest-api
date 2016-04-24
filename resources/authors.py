# authors.py

__author__ = "Iván Corrales Solera <developer@wesovi.com>"
__written_date = "24/04/2016"

import falcon


class AuthorResource(object):

    def __init__(self):
        self.props = ''

    def on_get(self,req,resp):

        resp.status= falcon.HTTP_200
        resp.body = '[' \
                    '{"fullName":"Miguel de Cervantes"},' \
                    '{"fullName":"William Shakespeare"},' \
                    ']'

