"""Validation error for invalid data."""

from .base_error import RejseplanError


class ValidationError(RejseplanError):
    """Raised when data validation fails."""
    
    def __init__(self, message: str, status_code: int | None = None, response=None, field: str | None = None, value=None):
        super().__init__(message, status_code, response)
        self.field = field
        self.value = value

    def __str__(self):
        base_str = super().__str__()
        if self.field:
            return f'{base_str} (field: {self.field}, value: {self.value})'
        return base_str

    def __repr__(self):
        return f'{self.__class__.__name__}(message="{self.message}", field="{self.field}", value={self.value})'