import requests
import logging

_LOGGER = logging.getLogger(__name__)

class baseAPIClient():
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

    def _get(self, service:str, params:dict) -> requests.Response:
        """Make a GET request to the specified service with the given parameters.

        Args:
            service (str): The API service endpoint.
            params (dict): The parameters to include in the request.
        """
        url = self.base_url + service
        _LOGGER.debug('Making request to %s with params: %s', url, params)
        try:
            response = requests.get(url, params=params, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()  # Raise an error for bad responses
        except requests.exceptions.RequestException as ex:
            _LOGGER.error('Request failed: %s', ex)
            raise ex
        if response.status_code == requests.codes['OK']:
            _LOGGER.debug('Request successful: %s', response.status_code)
            return response
        return None