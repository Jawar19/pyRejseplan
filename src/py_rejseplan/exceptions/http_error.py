"""Exception class for HTTP errors during REST API calls."""

from .base_error import RejseplanError


class HTTPError(RejseplanError):
    """Raised when the HTTP response code is not 200."""
    pass
