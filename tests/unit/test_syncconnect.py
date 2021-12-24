import unittest
import responses
from connectedcar import connectedcar, const


class Testconnectedcar(unittest.TestCase):

    def setUp(self):
        self.client_id = 'apiKey'
        self.client_secret = "clientSecret"
        self.redirect_uri = "redirectUri"
        self.scope = ['profile']

        self.client = connectedcar.AuthClient(
            self.client_id, self.client_secret, self.redirect_uri, self.scope)

    @responses.activate
    def test_get_access_token(self):
        data = {
            "access_token": "v6574b42-a5bc-4574-a87f-5c9d1202e316",
            "expires_in": "308874923",
            "token_type": "Bearer"
        }
        responses.add('POST', const.TOKEN_URL, json=data)
        actual = self.client.get_user_access_token('username', 'password')
        self.assertEqual("v6574b42-a5bc-4574-a87f-5c9d1202e316",
                         actual['access_token'])

    @responses.activate
    def test_get_exchange_token(self):
        data = {
            "access_token": "v6574b42-a5bc-4574-a87f-5c9d1202e316",
            "expires_in": "308874923",
            "token_type": "Bearer"
        }
        responses.add('POST', const.TOKEN_URL, json=data)
        actual = self.client.exchange_refresh_token('access_token')
        self.assertEqual("v6574b42-a5bc-4574-a87f-5c9d1202e316",
                         actual['access_token'])
