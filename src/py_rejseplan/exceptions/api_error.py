"""API error when Rejseplanen API v2.0 returns an error."""


class RPAPIError(BaseException):
    """Raised when the API returned an error."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        if self.status_code:
            return f'RPAPIError (status code: {self.status_code}): {self.message}'
        return f'RPAPIError: {self.message}'
