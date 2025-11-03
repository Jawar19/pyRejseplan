import requests
import logging

from py_rejseplan.exceptions import HTTPError, ConnectionError, APIError

_LOGGER = logging.getLogger(__name__)

class BaseAPIClient():
    """Base class for API clients.
    This class provides a method to construct headers for API requests.
    """
    def __init__(self, base_url:str, auth_key: str, timeout:int = 10) -> None:
        """Initialize the base API client with the provided base URL, authorization key, and optional timeout.

        Args:
            base_url (str): The base URL for the API.
            auth_key (str): The authorization key to be used in headers.
            timeout (int, optional): Timeout for API requests in seconds. Defaults to 10.
        """
        _LOGGER.debug('Initializing baseAPIClient')
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {auth_key}'}
        self.timeout = timeout

    def _get(self, service: str, params: dict) -> requests.Response:
        """Make a GET request to the specified service with the given parameters."""
        url = self.base_url + service
        _LOGGER.debug('Making request to %s with params: %s', url, params)
        
        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()  # This handles 4xx, 5xx errors
            _LOGGER.debug('Request successful: %s', response.status_code)
            return response
            
        except requests.exceptions.HTTPError as e:
            # Convert requests HTTPError to our HTTPError
            status_code = e.response.status_code if e.response else None
            error_msg = f'HTTP {status_code}: {e}'
            _LOGGER.error('HTTP error: %s', error_msg)
            raise HTTPError(error_msg, status_code=status_code, response=e.response) from e
            
        except requests.exceptions.Timeout as e:
            error_msg = f'Request timeout after {self.timeout} seconds'
            _LOGGER.error('Connection timeout: %s', error_msg)
            raise ConnectionError(error_msg) from e
            
        except requests.exceptions.ConnectionError as e:
            error_msg = f'Connection failed to {url}'
            _LOGGER.error('Connection error: %s', error_msg)
            raise ConnectionError(error_msg) from e
            
        except requests.exceptions.RequestException as e:
            error_msg = f'Request failed: {e}'
            _LOGGER.error('Request exception: %s', error_msg)
            raise APIError(error_msg) from e
    
    def validate_auth_key(self) -> bool:
        """Validate the authorization key by making a simple request to the API.

        Returns:
            bool: True if the authorization key is valid, False otherwise.
        """
        try:
            self._get('datainfo', params={})
            _LOGGER.debug('Authorization key is valid')
            return True
            
        except HTTPError as e:
            if e.status_code == 401:
                _LOGGER.error('Unauthorized: Invalid authorization key')
            else:
                _LOGGER.error('HTTP error during auth validation: %s', e)
            return False
            
        except (ConnectionError, APIError) as e:
            _LOGGER.error('Error during auth validation: %s', e)
            return False