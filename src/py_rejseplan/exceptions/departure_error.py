"""Departure API error when departure API calls fail."""

from .api_error import APIError


class DepartureError(APIError):
    """Raised when departure API operations fail."""
    pass