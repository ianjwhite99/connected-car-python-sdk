from syncconnect import syncconnect, api
import unittest

class TestAPI(unittest.TestCase):
    def test_format_default(self):
        
        a = api.Api('996b14c1-32e3-4753-b438-67ec719eca5c')

        url = a._format("https://usapi.cv.ford.com/api", "users")

        self.assertEqual(
            url,
            "https://usapi.cv.ford.com/api/users"
        )
