import requests


class SyncException(Exception):

    def __init__(self, response):
        self.message = 'Unknown error'
        if isinstance(response, requests.models.Response):
            json = response.json()
            if 'message' in json:
                self.message = json['message']
            elif 'error_description' in json:
                self.message = json['error_description']
        elif isinstance(response, str):
            self.message = response

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


class RateLimitingException(SyncException):
    pass


class ServerException(SyncException):
    pass


class GatewayTimeoutException(SyncException):
    def __init__(self, response):
        self.message = response.text

    def __str__(self):
        return self.message
