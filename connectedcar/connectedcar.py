from . import const, requester


class AuthClient(object):

    def __init__(self, client_id, client_secret,
                 redirect_uri=None, scope=None):
        """ A client for accessing the Ford API

        Args:
            client_id (str): The application id, provided in the application
                dashboard
            client_secret (str): The application secret, provided in the
                application dashboard
            redirect_uri (str, optional): The URL to redirect to after the user accepts
                or declines the application's permissions.
            scope (list, optional): A list of permissions requested by the application

        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def get_user_access_token(self, username, password):
        """ Exchange a username and password for a new access dictionary

        Args:
            username (str): Ford pass username
            password (str): Ford pass password

        Returns:
            Response: response containing access and refresh token

        Raises:
            SyncException
        """

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'fordpass-na/353 CFNetwork/1121.2.2 Darwin/19.3.0',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        response = requester.call(
            'POST', const.TOKEN_URL, headers=headers, data=data).json()
        return response

    def exchange_refresh_token(self, refresh_token):
        """ Exchange a refresh token for a new access dictionary

        Args:
            refresh_token (str): A valid refresh token from a previously retrieved
                access object

        Returns:
            Response: response containing access and refresh token

        Raises:
            SyncException
        """

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'fordpass-na/353 CFNetwork/1121.2.2 Darwin/19.3.0',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token
        }

        response = requester.call(
            'POST', const.TOKEN_URL, headers=headers, data=data).json()
        return response
