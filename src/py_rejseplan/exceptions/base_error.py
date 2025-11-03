"""Base exception for all pyRejseplan errors."""


class RejseplanError(Exception):
    """Base exception for all pyRejseplan errors."""

    def __init__(self, message: str, status_code: int | None = None, response=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response

    def __str__(self):
        if self.status_code:
            return f'{self.__class__.__name__} (status code: {self.status_code}): {self.message}'
        return f'{self.__class__.__name__}: {self.message}'

    def __repr__(self):
        return f'{self.__class__.__name__}(message="{self.message}", status_code={self.status_code})'