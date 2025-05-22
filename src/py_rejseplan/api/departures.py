import logging
from .base import baseAPIClient

from py_rejseplan.constants import RESOURCE as BASE_URL

_LOGGER = logging.getLogger(__name__)

class departuresAPIClient(baseAPIClient):
    """Client for the departures API.
    This class extends the baseAPIClient to provide specific functionality for the departures API.
    """
    def __init__(self, auth_key: str, timeout: int = 10) -> None:
        """Initialize the departures API client with the provided authorization key and optional timeout.

        Args:
            auth_key (str): The authorization key to be used in headers.
            timeout (int, optional): Timeout for API requests in seconds. Defaults to 10.
        """
        _LOGGER.debug('Initializing departuresAPIClient')
        super().__init__(BASE_URL, auth_key, timeout)

    def get_departures(
            self,
            stop_ids: list[int],
            max_results: int = -1,
            use_bus: bool = True,
            use_train: bool = True,
            use_metro: bool = True,
        ) -> dict:
        """Get departures for the given stop IDs.
        Args:
            stop_ids (list[int]): List of stop IDs to get departures for.
            max_results (int, optional): Maximum number of results to return. Defaults to 10.
            use_bus (bool, optional): Whether to include bus departures. Defaults to True.
            use_train (bool, optional): Whether to include train departures. Defaults to True.
            use_metro (bool, optional): Whether to include metro departures. Defaults to True.
        
        Returns:
            dict: Dictionary containing the departures data.
        """
        _LOGGER.debug('Getting departures for stop IDs: %s', stop_ids)
        if len(stop_ids) < 1:
            raise ValueError('Stop IDs must be provided')
        params = {
            'idList': stop_ids,
            'maxResults': max_results,
            'useBus': use_bus,
            'useTrain': use_train,
            'useMetro': use_metro,
        }
        _LOGGER.debug('Requesting departures with params: %s', params)
        response = self._get( 'multiDepartureBoard', params=params)
        if response is None:
            _LOGGER.error('Failed to get departures')
            return None
        return response