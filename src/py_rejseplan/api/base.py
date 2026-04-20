import asyncio
from dataclasses import dataclass
import requests
import aiohttp
import logging

from py_rejseplan.exceptions import HTTPError, ConnectionError, APIError

_LOGGER = logging.getLogger(__name__)


@dataclass
class AsyncHTTPResponse:
    """Lightweight async response payload detached from aiohttp response lifecycle."""

    status_code: int
    headers: dict[str, str]
    content: bytes

class BaseAPIClient():
    """Base class for API clients.
    This class provides a method to construct headers for API requests.
    """
    def __init__(
        self,
        base_url: str,
        auth_key: str,
        timeout: int = 10,
        session: aiohttp.ClientSession | None = None,
    ) -> None:
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
        self._session = session
        self._owns_session = session is None

    async def _get_async(self, service: str, params: dict) -> AsyncHTTPResponse:
        """Make an async GET request to the specified service with the given parameters."""
        url = self.base_url + service
        _LOGGER.debug('Making async request to %s with params: %s', url, params)

        try:
            if self._session is None:
                self._session = aiohttp.ClientSession()

            async with self._session.get(
                url,
                params=params,
                headers=self.headers,
                timeout=aiohttp.ClientTimeout(total=self.timeout),
            ) as response:
                response.raise_for_status()
                content = await response.read()
                _LOGGER.debug('Async request successful: %s', response.status)
                return AsyncHTTPResponse(
                    status_code=response.status,
                    headers=dict(response.headers),
                    content=content,
                )

        except aiohttp.ClientResponseError as e:
            status_code = e.status
            error_msg = f'HTTP {status_code}: {e}'
            _LOGGER.error('HTTP error (async): %s', error_msg)
            raise HTTPError(error_msg, status_code=status_code) from e

        except (
            asyncio.TimeoutError,
            aiohttp.ServerTimeoutError,
            aiohttp.ClientConnectionError,
            aiohttp.ClientConnectorError,
        ) as e:
            error_msg = f'Request timeout/connection error after {self.timeout} seconds'
            _LOGGER.error('Connection timeout/error (async): %s', error_msg)
            raise ConnectionError(error_msg) from e

        except aiohttp.ClientError as e:
            error_msg = f'Request failed (async): {e}'
            _LOGGER.error('Request exception (async): %s', error_msg)
            raise APIError(error_msg) from e

    async def close(self) -> None:
        """Close internally managed aiohttp session."""
        if self._owns_session and self._session and not self._session.closed:
            await self._session.close()

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

    async def validate_auth_key_async(self) -> bool:
        """Validate the authorization key using async HTTP call."""
        try:
            await self._get_async('datainfo', params={})
            _LOGGER.debug('Authorization key is valid (async)')
            return True

        except HTTPError as e:
            if e.status_code == 401:
                _LOGGER.error('Unauthorized: Invalid authorization key (async)')
            else:
                _LOGGER.error('HTTP error during auth validation (async): %s', e)
            return False

        except (ConnectionError, APIError) as e:
            _LOGGER.error('Error during auth validation (async): %s', e)
            return False