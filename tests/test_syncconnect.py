import os
import unittest
import syncconnect
from dotenv import load_dotenv

class TestSyncConnect(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.access_token = None
        self.client_id = '9fb503e0-715b-47e8-adfd-ad4b7770f73b'
        self.client_secret = None # Unused at this time
        self.redirect_uri = None  # Unused at this time
        self.scope = None  # Unused at this time
        
        if not os.environ.get('TEST_USER') and not os.environ.get('TEST_PASS'):
            raise Exception(
                'Please provide a username and password in your .env')
        else:
            self.username = os.environ.get('TEST_USER')
            self.password = os.environ.get('TEST_PASS')
        
        self.client = syncconnect.AuthClient(self.client_id, self.client_secret, self.redirect_uri, self.scope)

    def test_get_access_token(self):
        actual = self.client.get_user_access_token(self.username, self.password)
        self.assertIn("access_token", actual)
        self.assertIn("refresh_token", actual)
        self.assertIn("grant_id", actual)

    def test_get_exchange_token(self):
        access_token = self.client.get_user_access_token(self.username, self.password)
        actual = self.client.exchange_refresh_token(access_token['refresh_token'])
        self.assertIn("access_token", actual)
        self.assertIn("refresh_token", actual)
        self.assertIn("grant_id", actual)
