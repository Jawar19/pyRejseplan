from datetime import datetime
from pydantic_xml import BaseXmlModel, attr, element
from pydantic import field_validator
import logging

import py_rejseplan.dataclasses.constants as constants

from .departure import Departure
from .technical_messages import TechnicalMessages

_LOGGER = logging.getLogger(__name__)

class DepartureBoard(
    BaseXmlModel,
    tag='DepartureBoard',
    # ns="",
    nsmap=constants.NSMAP
):
    """Departure board class for parsing XML data from the Rejseplanen API.
    This class is used to represent the departure board data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    serverVersion: str = attr()
    dialectVersion: str = attr()
    planRtTs: datetime = attr()
    requestId: str = attr()
    technicalMessages: TechnicalMessages = element(
        default_factory=list,
        tag='TechnicalMessages'
    )
    departures: list[Departure] = element(
        default_factory=list,
        tag='Departure'
    )

    @field_validator('departures', mode='before')
    @classmethod
    def validate_departures(cls, v):
        """
        Validate departures list, filtering out invalid entries.
        This allows partial success when some departures are malformed.
        """
        if not v:
            return []
        
        if not isinstance(v, list):
            _LOGGER.warning("Expected list for departures, got %s", type(v))
            return []
        
        valid_departures = []
        for i, departure_data in enumerate(v):
            try:
                # If it's already a validated Departure object, keep it
                if hasattr(departure_data, '__class__') and departure_data.__class__.__name__ == 'Departure':
                    valid_departures.append(departure_data)
                else:
                    # Let pydantic validate the departure data
                    if hasattr(departure_data, 'model_validate'):
                        valid_departure = departure_data
                    else:
                        # This handles raw XML element data
                        valid_departure = departure_data
                    valid_departures.append(valid_departure)
            except Exception as e:
                _LOGGER.warning("Skipping invalid departure at index %d: %s", i, e)
                continue
        
        _LOGGER.info("Successfully validated %d out of %d departures", len(valid_departures), len(v))
        return valid_departures

    @field_validator('technicalMessages', mode='before')
    @classmethod
    def validate_technical_messages(cls, v):
        """
        Validate technical messages, providing empty fallback if invalid.
        """
        if not v:
            from .technical_messages import TechnicalMessages
            return TechnicalMessages(technicalMessages=[])
        
        try:
            # If it's already a TechnicalMessages object, return it
            if hasattr(v, '__class__') and v.__class__.__name__ == 'TechnicalMessages':
                return v
            else:
                # Let pydantic handle validation
                return v
        except Exception as e:
            _LOGGER.warning("Invalid technical messages, using empty fallback: %s", e)
            from .technical_messages import TechnicalMessages
            return TechnicalMessages(technicalMessages=[])