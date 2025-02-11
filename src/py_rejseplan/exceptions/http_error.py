"""Exception class for HTTP errors during REST api calls
"""
class RPHTTPError(Exception):
    """Raised when the HTTP response code is not 200."""
