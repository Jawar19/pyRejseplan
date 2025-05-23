import datetime
import logging
from pydantic_xml import BaseXmlModel, attr, element

import py_rejseplan.dataclasses.constants as constants

from .product_at_stop import ProductAtStop
from .product import Product
from .journey_detail_ref import JourneyDetailRef
from .note import Notes

_LOGGER = logging.getLogger(__name__)


class Departure(
    BaseXmlModel,
    tag='Departure',
    ns="",
    nsmap=constants.NSMAP,
    search_mode='ordered',
    ):
    """Departure class for parsing XML data from the Rejseplanen API.
    This class is used to represent the departure data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    name: str = attr()
    type: str = attr()
    stop: str = attr()
    stopid: str = attr()
    stopExtId: int = attr()
    lon: float = attr()
    lat: float = attr()
    isMainMast: bool = attr()
    prognosisType: str = attr()
    time: datetime.time = attr()
    date: datetime.date = attr()
    track: int = attr()
    rtTime: datetime.time = attr()
    rtDate: datetime.date = attr()
    rtTrack: int = attr()
    reachable: bool = attr()
    direction: str = attr()
    directionFlag: int = attr()

    # Subelements
    journeyDetailRef: JourneyDetailRef = element(
        default_factory=JourneyDetailRef,
        tag='JourneyDetailRef'
    )
    journeyStatus: str = element(
        default_factory=str,
        tag='JourneyStatus'
    )
    productAtStop: ProductAtStop = element(
        default_factory=list,
        tag='ProductAtStop'
    )
    product: Product = element(
        default_factory=list,
        tag='Product'
    )
    notes: Notes = element(
        tag='Notes',  # This navigates through the Notes container
    )
    platform: dict[str, str] = element(
        default_factory=dict,
        tag='platform'
    )
    rtPlatform: dict[str, str] = element(
        default_factory=dict,
        tag='rtPlatform'
    )