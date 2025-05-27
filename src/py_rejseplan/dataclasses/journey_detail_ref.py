import logging
from pydantic_xml import BaseXmlModel, attr

_LOGGER = logging.getLogger(__name__)

class JourneyDetailRef(
    BaseXmlModel,
    tag='JourneyDetailRef',
    ns="",
    nsmap=None
):
    """JourneyDetailRef class for parsing XML data from the Rejseplanen API.
    This class is used to represent the journey detail reference data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    ref: str = attr()