from datetime import datetime
import logging

from pydantic import ValidationError as PydanticValidationError
import requests

from py_rejseplan.enums import TransportClass
from .base import BaseAPIClient

from py_rejseplan.constants import RESOURCE as BASE_URL
from py_rejseplan.dataclasses.departure_board import DepartureBoard
from py_rejseplan.exceptions import DepartureError

_LOGGER = logging.getLogger(__name__)

class DeparturesAPIClient(BaseAPIClient):
    """Client for the departures API.
    This class extends the BaseAPIClient to provide specific functionality for the departures API.
    """
    def __init__(self, auth_key: str, timeout: int = 10) -> None:
        """Initialize the departures API client with the provided authorization key and optional timeout.

        Args:
            auth_key (str): The authorization key to be used in headers.
            timeout (int, optional): Timeout for API requests in seconds. Defaults to 10.
        """
        _LOGGER.debug('Initializing departuresAPIClient')
        super().__init__(BASE_URL, auth_key, timeout)

    def _create_empty_departure_board(self) -> DepartureBoard:
        """Create an empty departure board for fallback scenarios."""
        from py_rejseplan.dataclasses.technical_messages import TechnicalMessages
        return DepartureBoard(
            serverVersion="unknown",
            dialectVersion="1.0",
            planRtTs=datetime.now(),
            requestId="fallback",
            departures=[],
            technicalMessages=TechnicalMessages(technicalMessages=[])
        )

    def parse_response(self, response: bytes | str | None) -> DepartureBoard:
        """
        Parse the XML response from the API and return a DepartureBoard.
        Always returns a valid DepartureBoard object for successful API calls.
        
        Args:
            response: The XML response from the API.

        Returns:
            DepartureBoard: Parsed departure board with valid departures.
                           Returns empty board for parsing failures only.
                           
        Raises:
            DepartureError: When response is None (indicates API/network failure)
        """
        if response is None:
            _LOGGER.error('Response is None - indicates complete API failure')
            raise DepartureError('Failed to get response from departure API')
        
        try:
            # Parse using pydantic-xml with built-in validation
            departure_board = DepartureBoard.from_xml(response)
            _LOGGER.debug('Successfully parsed departure board with %d departures', 
                         len(departure_board.departures))
            return departure_board
            
        except PydanticValidationError as ve:
            # Check if this is a critical structural error or just invalid departures
            critical_errors = [
                error for error in ve.errors() 
                if not any(field in str(error.get('loc', [])) for field in ['departures', 'technicalMessages'])
            ]
            
            if critical_errors:
                _LOGGER.error('Critical validation errors, returning empty departure board: %s', critical_errors)
                return self._create_empty_departure_board()
            else:
                # Only departure/technical message validation errors - these are handled by field validators
                _LOGGER.warning('Non-critical validation errors handled by field validators: %s', ve)
                try:
                    return DepartureBoard.from_xml(response)
                except Exception as retry_error:
                    _LOGGER.error('Failed to parse even with field validation, returning empty board: %s', retry_error)
                    return self._create_empty_departure_board()
                
        except Exception as e:
            _LOGGER.error('Unexpected error parsing response, returning empty board: %s', e)
            return self._create_empty_departure_board()

    def get_departures(
            self,
            stop_ids: list[int],
            max_results: int = -1,
            use_bus: bool = True,
            use_train: bool = True,
            use_metro: bool = True,
        ) -> tuple[DepartureBoard, requests.Response]:
        """Get departures for the given stop IDs.
        
        Args:
            stop_ids: List of stop IDs to get departures for.
            max_results: Maximum number of results to return. Defaults to -1.
            use_bus: Whether to include bus departures. Defaults to True.
            use_train: Whether to include train departures. Defaults to True.
            use_metro: Whether to include metro departures. Defaults to True.

        Returns:
            tuple: (DepartureBoard, response object)
            
        Raises:
            ValueError: When stop_ids is empty
            DepartureError: When API request fails completely
        """
        _LOGGER.debug('Getting departures for stop IDs: %s', stop_ids)
        if len(stop_ids) < 1:
            raise ValueError('Stop IDs must be provided')
            
        prep_id_list = "|".join(map(str, stop_ids))
        params = {
            'idList': prep_id_list,
            'maxResults': max_results,
            'useBus': use_bus,
            'useTrain': use_train,
            'useMetro': use_metro,
        }
        
        _LOGGER.debug('Requesting departures with params: %s', params)
        response = self._get('multiDepartureBoard', params=params)        
        # This will raise DepartureError if response.content is None
        # or return valid DepartureBoard (possibly empty) for parsing issues
        departure_board = self.parse_response(response.content)
        
        return departure_board, response
    
    def calculate_departure_type_bitflag(self, departure_types: list) -> int | None:
        """Calculate bitflag from departure type list."""
        if not departure_types:
            return None

        bitflag = 0
        for transport_class in departure_types:
            if isinstance(transport_class, int):
                # If already an int (TransportClass enum value)
                bitflag |= transport_class
            elif isinstance(transport_class, TransportClass):
                # If TransportClass enum instance
                bitflag |= transport_class.value
            elif isinstance(transport_class, str):
                # If string, try to convert to TransportClass enum
                try:
                    enum_value = TransportClass[transport_class.upper()]
                    bitflag |= enum_value.value
                except KeyError:
                    _LOGGER.warning("Unknown departure type: %s", transport_class)
            else:
                _LOGGER.warning("Invalid departure type format: %s", transport_class)

        return bitflag if bitflag > 0 else None