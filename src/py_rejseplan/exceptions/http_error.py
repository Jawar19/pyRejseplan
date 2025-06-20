"""Exception class for HTTP errors during REST API calls"""


class RPHTTPError(BaseException):
    """Raised when the HTTP response code is not 200."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        if self.status_code:
            return f'RPHTTPError (status code: {self.status_code}): {self.message}'
        return f'RPHTTPError: {self.message}'
