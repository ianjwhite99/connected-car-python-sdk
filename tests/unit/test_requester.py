import connectedcar
import responses
import unittest


class TestRequester(unittest.TestCase):

    EXPECTED = 'expected'
    URL = 'http://ford.url'

    def queue(self, status_code, **kwargs):
        """ queue fake responses with passed status code """
        if not kwargs:
            json = {'message': self.EXPECTED}
        else:
            json = kwargs

        responses.add('GET', self.URL, status=status_code, json=json)

    def check(self, exception):

        self.assertRaisesRegexp(
            exception,
            self.EXPECTED,
            connectedcar.requester.call,
            'GET',
            self.URL)

    @responses.activate
    def test_user_agent(self):
        self.queue(200)
        connectedcar.requester.call('GET', self.URL)
        self.assertEqual(
            responses.calls[0].request.headers['User-Agent'],
            'FordPass/24 CFNetwork/1399 Darwin/22.1.0',
        )

    @responses.activate
    def test_oauth_error(self):
        self.queue(401, error_description='unauthorized')
        try:
            connectedcar.requester.call('GET', self.URL)
        except connectedcar.AuthenticationException as err:
            self.assertEqual(err.message, 'unauthorized')

    @responses.activate
    def test_unknown_error(self):
        self.queue(401, error_description='unknown error')
        try:
            connectedcar.requester.call('GET', self.URL)
        except connectedcar.AuthenticationException as err:
            self.assertEqual(err.message, 'unknown error')

    @responses.activate
    def test_400(self):
        self.queue(400)
        self.check(connectedcar.ValidationException)

    @responses.activate
    def test_401(self):
        self.queue(401)
        self.check(connectedcar.AuthenticationException)

    @responses.activate
    def test_403(self):
        self.queue(403)
        self.check(connectedcar.PermissionException)

    @responses.activate
    def test_404(self):
        self.queue(404)
        self.check(connectedcar.ResourceNotFoundException)

    @responses.activate
    def test_429(self):
        self.queue(429)
        self.check(connectedcar.RateLimitingException)

    @responses.activate
    def test_429(self):
        self.queue(429)
        self.check(connectedcar.RateLimitingException)

    @responses.activate
    def test_500(self):
        self.queue(500)
        self.check(connectedcar.ServerException)

    @responses.activate
    def test_504(self):
        responses.add('GET', self.URL, status=504, json={
                      'error': 'some error', 'message': self.EXPECTED})
        self.check(connectedcar.GatewayTimeoutException)

    @responses.activate
    def test_other(self):
        self.queue(503)
        with self.assertRaises(connectedcar.SyncException) as se:
            connectedcar.requester.call('GET', self.URL)
        self.assertEquals(se.exception.message, 'Unexpected error')
