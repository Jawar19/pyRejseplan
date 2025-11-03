"""Connection error exceptions."""

from .base_error import RejseplanError


class ConnectionError(RejseplanError):
    """Raised when connection to the API fails."""
    pass
