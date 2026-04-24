from datetime import datetime
from typing import Optional
from pydantic_xml import BaseXmlModel, attr, element
from pydantic import field_validator, ValidationError as PydanticValidationError
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
    technicalMessages: Optional[TechnicalMessages] = element(
        tag='TechnicalMessages'
    )
    departures: list[Departure] = element(
        default_factory=list,
        tag='Departure'
    )

    @field_validator('departures', mode='before')
    @classmethod
    def  validate_departures(cls, value):
        """
        Validate departures list, filtering out invalid entries.
        This allows partial success when some departures are malformed.
        """
        if not value:
            return []
        
        if not isinstance(value, list):
            _LOGGER.warning("Expected list for departures, got %s", type(value))
            return []
        valid_departures: list[Departure] = []

        for index, item in enumerate(value):
            try:
                if isinstance(item, Departure):
                    valid_departures.append(item)
                elif isinstance(item, dict):
                    valid_departures.append(Departure.model_validate(item))
                else:
                    _LOGGER.warning("Skipping departure at index %d: unexpected type %s", index, type(item))
            except PydanticValidationError as e:
                _LOGGER.warning("Skipping invalid departure at index %d: %s", index, e)
        
        _LOGGER.info("Validated %d departures (skipped %d invalid)", 
             len(valid_departures), len(value) - len(valid_departures))
        return valid_departures

    @field_validator('technicalMessages', mode='before')
    @classmethod
    def validate_technical_messages(cls, v):
        """Validate technical messages, providing empty fallback if invalid."""
        if not v:
            return TechnicalMessages(technicalMessages=[])
        
        # If already a TechnicalMessages instance, return it
        if isinstance(v, TechnicalMessages):
            return v
        
        # For other types, pass through and let pydantic's field validation handle it
        return v