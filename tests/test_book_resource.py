

from mock import Mock
from resources.books import BookResource
from mock import patch

class TestBookResource:

    def setup(self):
        self.bookResource = BookResource()


    def test_on_get(self):
        mock_request = {}
        mock = Mock(return_value=None)
        mock(mock_request.get_param("id"),"1")
        bookResponse = self.bookResource.on_get(mock_request,None)




 