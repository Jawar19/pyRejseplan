from pydantic_xml import BaseXmlModel, attr
import py_rejseplan.dataclasses.constants as constants
import logging

_LOGGER = logging.getLogger(__name__)

class TechnicalMessage(
    BaseXmlModel,
    tag='TechnicalMessage',
    ns="",
    nsmap=constants.NSMAP
):
    """Technical message class for parsing XML data from the Rejseplanen API.
    This class is used to represent the technical message data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    key: str = attr()
    text: str