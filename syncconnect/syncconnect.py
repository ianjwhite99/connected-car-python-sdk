from . import api, const, requester, vehicle, user

class AuthClient(object):
    
    def __init__(self, client_id, client_secret, redirect_uri, scope=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_access_token(self, username, password, auth_code):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        response = requester.call('POST', const.TOKEN_URL, headers=headers, data=data).json()
        return response

    def exchange_refresh_token(self, refresh_token):

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }

        response = requester.call('POST', const.TOKEN_URL, headers=headers, data=data).json()
        return response
