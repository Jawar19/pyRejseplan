from datetime import datetime
from pydantic_xml import BaseXmlModel, attr, element
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