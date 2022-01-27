import requests
from . import exceptions as E


def call(method, url, **kwargs):
    """ Attachs the kwargs into the headers, sends the request to the Ford API's
        and handles all error cases.

    Args:
        method (str): HTTP method
        url (str): url of the request
        **kwargs: parameters for the request

    Returns:
        Response: response from the request to the Ford API's
    """

    if "headers" not in kwargs:
        kwargs["headers"] = {}
    kwargs['headers']['User-Agent'] = 'FordPass/5 CFNetwork/1327.0.4 Darwin/21.2.0'

    try:
        response = requests.request(method, url, timeout=310, **kwargs)
        code = response.status_code

        if response.ok:
            return response
        elif code == 400:
            raise E.ValidationException(response)
        elif code == 401:
            raise E.AuthenticationException(response)
        elif code == 403:
            raise E.PermissionException(response)
        elif code == 404:
            raise E.ResourceNotFoundException(response)
        elif code == 429:
            raise E.RateLimitingException(response)
        elif code == 500:
            raise E.ServerException(response)
        elif code == 504:
            raise E.GatewayTimeoutException(response)
        else:
            response.raise_for_status()

    except Exception as e:
        if isinstance(e, E.SyncException):
            raise e
        else:
            raise E.SyncException("Unexpected error") from e
