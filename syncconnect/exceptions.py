class SyncException(Exception):

    def __init__(self, response):
        json = response.json()
        if 'error' in json:
            self.message = json['error']
        elif 'message' in json:
            self.message = json['message']
        else:
            self.message = 'Unknown Error'

    def __str__(self):
        return self.message


class ValidationException(SyncException):
    pass


class AuthenticationException(SyncException):
    pass


class PermissionException(SyncException):
    pass


class ResourceNotFoundException(SyncException):
    pass


class StateException(SyncException):
    def __init__(self, response):
        super(StateException, self).__init__(response)
        json = response.json()
        self.code = json['code']

    def __str__(self):
        return self.code + ': ' + self.message


class RateLimitingException(SyncException):
    pass


class MonthlyLimitExceeded(SyncException):
    pass


class ServerException(SyncException):
    pass


class VehicleNotCapableException(SyncException):
    pass


class GatewayTimeoutException(SyncException):
    def __init__(self, response):
        self.message = response.text

    def __str__(self):
        return self.message
