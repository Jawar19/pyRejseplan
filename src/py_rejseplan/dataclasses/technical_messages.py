from pydantic_xml import BaseXmlModel, attr, element
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