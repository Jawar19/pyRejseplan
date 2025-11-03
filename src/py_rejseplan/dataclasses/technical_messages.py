from pydantic_xml import BaseXmlModel, element
from pydantic import field_validator
import py_rejseplan.dataclasses.constants as constants
import logging

from .technical_message import TechnicalMessage
_LOGGER = logging.getLogger(__name__)


class TechnicalMessages(
    BaseXmlModel,
    tag='TechnicalMessages',
    ns="",
    nsmap=constants.NSMAP
):
    """Technical message class for parsing XML data from the Rejseplanen API.
    This class is used to represent the technical message data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    technicalMessages: list[TechnicalMessage] = element(
        default_factory=list,
        tag='TechnicalMessage'
    )

    @field_validator('technicalMessages', mode='before')
    @classmethod
    def validate_technical_message_list(cls, v):
        """
        Validate technical messages list, filtering out invalid entries.
        """
        if not v:
            return []
        
        if not isinstance(v, list):
            _LOGGER.warning("Expected list for technicalMessages, got %s", type(v))
            return []
        
        valid_messages = []
        for i, message_data in enumerate(v):
            try:
                # If it's already a validated TechnicalMessage object, keep it
                if hasattr(message_data, '__class__') and message_data.__class__.__name__ == 'TechnicalMessage':
                    valid_messages.append(message_data)
                else:
                    # Let pydantic validate the message data
                    valid_messages.append(message_data)
            except Exception as e:
                _LOGGER.warning("Skipping invalid technical message at index %d: %s", i, e)
                continue
        
        return valid_messages