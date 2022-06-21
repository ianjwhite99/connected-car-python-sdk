import json
from . import const, requester
import requests


class AuthClient(object):

    regions = {
        'US': '71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592',
        'CA': '71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592',
        'EU': '1E8C7794-FF5F-49BC-9596-A1E0C86C5B19',
        'AU': '5C80A6BB-CF0D-4A30-BDBF-FC804B5C1A98',
    }

    def __init__(self, client_id, client_secret,
                 redirect_uri=None, scope=None, region='US'):
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
        self.region = self.regions[region]

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
            'User-Agent': 'FordPass/5 CFNetwork/1333.0.4 Darwin/21.5.0',
            'Accept-Encoding': 'gzip, deflate, br',
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        response = requester.call(
            'POST', const.TOKEN_URL, headers=headers, data=data).json()

        if (response['access_token']):

            headers['Content-Type'] = 'application/json'
            headers['Application-Id'] = self.region

            data = {
                'ciToken': response['access_token']
            }        

            response = requester.call(
                'POST', 'https://api.mps.ford.com/api/token/v2/cat-with-ci-access-token', headers=headers, data=json.dumps(data)).json()

            return response
        
        else:
            raise Exception("Access Token was not returned")
            

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
            'Content-Type': 'application/json',
            'User-Agent': 'FordPass/5 CFNetwork/1333.0.4 Darwin/21.5.0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Application-Id': self.region
        }

        data = {
            'refresh_token': refresh_token
        }

        response = requester.call(
            'POST', 'https://api.mps.ford.com/api/token/v2/cat-with-refresh-token', headers=headers, data=json.dumps(data)).json()
        return response
