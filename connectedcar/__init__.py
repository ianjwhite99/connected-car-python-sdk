"""
The Python package `connectedcar` provides a SDK to interact with
Ford Sync Connect enabled vehicles. With this package you will
be able to make requests on behalf of a Ford Pass user to: authorize
new vehicles, edit current vehicles, return vehicle information, send
vehicle commands and return user information.
"""

from .connectedcar import (AuthClient)
from .user import User
from .vehicle import Vehicle
from .exceptions import (
    SyncException,
    ValidationException,
    AuthenticationException,
    PermissionException,
    ResourceNotFoundException,
    RateLimitingException,
    ServerException,
    GatewayTimeoutException)
