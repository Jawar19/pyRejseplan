"""Departure API error when departure API calls fail."""

from .api_error import RPAPIError


class DepartureAPIError(RPAPIError):
    """Raised when the departure API fails completely."""

    def __init__(self, message, status_code=None, response=None):
        super().__init__(message, status_code)
        self.response = response

    def __str__(self):
        if self.status_code:
            return f'DepartureAPIError (status code: {self.status_code}): {self.message}'
        return f'DepartureAPIError: {self.message}'