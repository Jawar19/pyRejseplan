"""Exceptions for pyRejseplan."""

from .base_error import RejseplanError
from .api_error import APIError
from .http_error import HTTPError
from .connection_error import ConnectionError
from .departure_error import DepartureError
from .validation_error import ValidationError

# Maintain backward compatibility aliases
RPAPIError = APIError
RPHTTPError = HTTPError
RPConnectionError = ConnectionError
DepartureAPIError = DepartureError
RPValidationError = ValidationError

__all__ = [
    # New naming (recommended)
    'RejseplanError',
    'APIError', 
    'HTTPError',
    'ConnectionError',
    'DepartureError',
    'ValidationError',
    
    # Backward compatibility aliases (deprecated)
    'RPAPIError',
    'RPHTTPError', 
    'RPConnectionError',
    'DepartureAPIError',
    'RPValidationError',
]