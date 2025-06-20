import logging
from typing import Optional
from pydantic_xml import BaseXmlModel, attr, element
import py_rejseplan.dataclasses.constants as constants

class ProductAtStop(
    BaseXmlModel,
    tag='ProductAtStop',
    ns="",
    nsmap=constants.NSMAP
):
    """ProductAtStop class for parsing XML data from the Rejseplanen API.
    This class is used to represent the product at stop data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """

    name: Optional[str] = attr()
    internalName: Optional[str] = attr()
    addName: Optional[str] = attr(default="", tag='addName')
    displayNumber: Optional[str] = attr(default="", tag='displayNumber')
    num: Optional[int] = attr()
    line: Optional[str] = attr()
    lineId: Optional[str] = attr()
    lineHidden: bool = attr(default=False, tag='lineHidden')
    catOut: Optional[str] = attr()
    catIn: Optional[str] = attr()
    catCode: Optional[str] = attr()
    cls: Optional[str] = attr()
    catOutS: Optional[str] = attr()
    catOutL: Optional[str] = attr()
    operatorCode: Optional[str] = attr()
    operator: Optional[str] = attr()
    admin: Optional[str] = attr()
    routeIdxFrom: int = attr(default=-1, tag='routeIdxFrom')
    routeIdxTo: int = attr(default=-1, tag='routeIdxTo')
    matchId: Optional[str] = attr()

    icon: dict[str, str] = element(
        default_factory=dict,
        tag='icon'
    )

    operatorInfo: dict[str, str] = element(
        default_factory=dict,
        tag='operatorInfo'
    )


# - name: str, optional
# - internalName: str, optional
# - addName: str, optional
# - displayNumber: str, optional
# - num: str, optional
# - line: str, optional
# - lineId: str, optional
# - lineHidden: bool, default="false"
# - catOut: str, optional
# - catIn: str, optional
# - catCode: str, optional
# - cls: str, optional
# - catOutS: str, optional
# - catOutL: str, optional
# - operatorCode: str, optional
# - operator: str, optional
# - admin: str, optional
# - routeIdxFrom: int, default="-1"
# - routeIdxTo: int, default="-1"
# - matchId: str, optional