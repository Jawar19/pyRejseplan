"""Exception for issues related to connection to Rejseplanen REST API"""


class RPConnectionError(BaseException):
    """Raised in the event of a network problem."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

    def __str__(self):
        if self.status_code:
            return (
                f'RPConnectionError (status code: {self.status_code}): {self.message}'
            )
        return f'RPConnectionError: {self.message}'
