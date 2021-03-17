from syncconnect import api, const
import unittest

class TestAPI(unittest.TestCase):

    def test_format_default(self):
        a = api.Api('996b14c1-32e3-4753-b438-67ec719eca5c')
        url = a._format(const.API_URL, "users")
        self.assertEqual(url,"https://usapi.cv.ford.com/api/users")
