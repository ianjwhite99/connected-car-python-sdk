from base64 import urlsafe_b64encode
import hashlib
import json
import random
import re
import string
from . import const, requester
import requests


class AuthClient(object):

    session = requests.session()

    regions = {
        'US': '71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592',
        'CA': '71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592',
        'EU': '1E8C7794-FF5F-49BC-9596-A1E0C86C5B19',
        'AU': '5C80A6BB-CF0D-4A30-BDBF-FC804B5C1A98',
    }

    defaultHeaders = {
        "Accept": "*/*",
        "Accept-Language": "en-us",
        "User-Agent": "FordPass/5 CFNetwork/1197 Darwin/20.0.0",
        "Accept-Encoding": "gzip, deflate, br",
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

        pkce_code = ''.join(random.choice(string.ascii_lowercase) for i in range(43))

        # Fetch the Auth URL
        authURL = self.web_session(pkce_code)

        # Attempt to login
        codeURL = self.attemptLogin(authURL, username, password)

        # Fetch the auth codes
        codes = self.fetch_auth_codes(codeURL)

        headers = {
            **self.defaultHeaders,
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = {
            'client_id': self.client_id,
            'grant_type': 'authorization_code',
            "redirect_uri": 'fordapp://userauthorized',
            "grant_id": codes["grant_id"],
            "code": codes["code"], 
            "code_verifier": pkce_code
        }

        response = self.session.post(const.TOKEN_URL, headers=headers, data=data)

        if response.status_code == 200:
            result = response.json()
            if result["access_token"]:
                access_token = result["access_token"]
        else:
            raise Exception("Error Fetching Access Token with PKCE Code")

        if (access_token):

            headers['Content-Type'] = 'application/json'
            headers['Application-Id'] = self.region

            data = {
                'ciToken': access_token
            }        

            response = self.session.post('https://api.mps.ford.com/api/token/v2/cat-with-ci-access-token', headers=headers, data=json.dumps(data)).json()

            return response
        
        else:
            raise Exception("Access Token was not returned")

    def web_session(self, pkce_code):
        headers = {
            **self.defaultHeaders,
            'Content-Type': 'application/json',
        }
        code_verifier = self.generate_hash(pkce_code)
        response = self.session.get("https://sso.ci.ford.com/v1.0/endpoint/default/authorize?redirect_uri=fordapp://userauthorized&response_type=code&scope=openid&max_age=3600&client_id=9fb503e0-715b-47e8-adfd-ad4b7770f73b&code_challenge=" + code_verifier + "&code_challenge_method=S256", headers=headers)

        authURL = re.findall('data-ibm-login-url="(.*)"\s', response.text)[0]
        if (authURL):
            return "https://sso.ci.ford.com" + authURL
        raise Exception("Missing AuthURL")

    def attemptLogin(self, authURL, username, password):
        headers = {
            **self.defaultHeaders,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        data = {
            "operation": "verify",
            "login-form-type": "password",
            "username" : username,
            "password" : password
        }

        response = self.session.post(authURL, headers=headers, data=data, allow_redirects=False)

        if response.status_code == 302:
            return response.headers["Location"]
        raise Exception("Unable to login, missing location redirect")

    def fetch_auth_codes(self, codeURL):
        headers = {
            **self.defaultHeaders,
            'Content-Type': 'application/json',
        }

        response = self.session.get(codeURL, headers=headers, allow_redirects=False)

        if response.status_code == 302:
            nextUrl = response.headers["Location"]
            query = requests.utils.urlparse(nextUrl).query
            params = dict(x.split('=') for x in query.split('&'))
            code = params["code"]
            grant_id = params["grant_id"]

            return {
                "code": code,
                "grant_id": grant_id
            }
        raise Exception("Unable to Fetch Code & Grant ID")
            
    def base64UrlEncode(self,data):
        return urlsafe_b64encode(data).rstrip(b'=')
        
    def generate_hash(self, code):
        m = hashlib.sha256()
        m.update(code.encode('utf-8'))
        return self.base64UrlEncode(m.digest()).decode('utf-8')
        
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
