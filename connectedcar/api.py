from . import const, requester


class Api(object):

    def __init__(self, access_token, region):
        """ Initialize a new Api object to directly make requests to Ford.

        Args:
            access_token (str): Ford access token
            region (str): Define your region. Default is US.
        """
        
        regions = {
            "US": "71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592", # United States
            "CA": "71A3AD0A-CF46-4CCF-B473-FC7FE5BC4592", # Canada
            "EU": "1E8C7794-FF5F-49BC-9596-A1E0C86C5B19", # Europe
            "AU": "5C80A6BB-CF0D-4A30-BDBF-FC804B5C1A98", # Australia
        }

        self.access_token = access_token
        self.auth = {
            'auth-token': access_token,
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'User-Agent': 'FordPass/5 CFNetwork/1333.0.4 Darwin/21.5.0',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Application-Id': regions[region]
        }

    def _format(self, endpoint, context):
        """ Generates the formated URL

        Args:
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context

        Returns:
            str: formatted url
        """

        return '{}/{}'.format(endpoint, context)

    def get(self, endpoint, context):
        """ Sends GET requests to Ford

        Args:
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context

        Returns:
            Response: response from the request to the Ford API
        """

        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('GET', url, headers=headers)

    def post(self, endpoint, context, data):
        """ Sends POST requests to Ford

        Args:
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context
            data (array): data to be sent with request

        Returns:
            Response: response from the request to the Ford API
        """

        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('POST', url, headers=headers, data=data)

    def put(self, endpoint, context, data):
        """ Sends PUT requests to Ford

        Args:
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context
            data (array): data to be sent with request

        Returns:
            Response: response from the request to the Ford API
        """

        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('PUT', url, headers=headers, data=data)

    def delete(self, endpoint, context):
        """ Sends DELETE requests to Ford

        Args:
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context

        Returns:
            Response: response from the request to the Ford API
        """

        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('DELETE', url, headers=headers)

    def action(self, method, endpoint, context):
        """ Sends universal requests to Ford

        Args:
            method (str): the request type
            endpoint (str): the Ford endpoint of interest
            context (str): the API endpoint context

        Returns:
            Response: response from the request to the Ford API
        """

        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call(method, url, headers=headers)
