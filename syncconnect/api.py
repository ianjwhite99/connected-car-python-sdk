from . import const, requester

class Api(object):

    def __init__(self, access_token):
        self.access_token = access_token
        self.auth = {
            'Content-Type': 'application/json',
            'application-id': const.APP_ID,
            'auth-token': access_token
        }

    def _format(self, endpoint, context):
        return '{}/{}'.format(endpoint, context)

    def get(self, endpoint, context):
        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('GET', url, headers=headers)

    def post(self, endpoint, context, data):
        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('POST', url, headers=headers, data=data)

    def put(self, endpoint, context, data):
        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('PUT', url, headers=headers, data=data)

    def delete(self, endpoint, context):
        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call('DELETE', url, headers=headers)

    def action(self, method, endpoint, context):
        url = self._format(endpoint, context)
        headers = self.auth

        return requester.call(method, url, headers=headers)
