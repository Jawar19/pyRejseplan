"""API error when Rejseplanen API v2.0 returns an error."""

from .base_error import RejseplanError


class APIError(RejseplanError):
    """Raised when the API returns an error response."""
    pass
