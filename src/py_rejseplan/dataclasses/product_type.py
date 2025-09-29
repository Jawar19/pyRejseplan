from typing import Optional
from pydantic_xml import BaseXmlModel, attr, element
import py_rejseplan.dataclasses.constants as constants
from .mixins import TransportClassMixin

class ProductType(
    BaseXmlModel,
    TransportClassMixin,
    tag='ProductAtStop',
    ns="",
    nsmap=constants.NSMAP,
    search_mode='unordered',
):
    """ProductType class for parsing XML data from the Rejseplanen API.
    This class is used to represent the product at stop data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    # attributes
    name: Optional[str] = attr(default=str)
    internalName: Optional[str] = attr(default=str)
    addName: Optional[str] = attr(default="", tag='addName')
    displayNumber: Optional[str] = attr(default="", tag='displayNumber')
    num: Optional[int] = attr(default=str)
    line: Optional[str] = attr(default=str)
    lineId: Optional[str] = attr(default=str)
    lineHidden: bool = attr(default=False, tag='lineHidden')
    catOut: Optional[str] = attr(default=str)
    catIn: Optional[str] = attr(default=str)
    catCode: Optional[str] = attr(default=str)
    cls_id: Optional[int] = attr(default=int, tag='cls')
    catOutS: Optional[str] = attr(default=str)
    catOutL: Optional[str] = attr(default=str)
    operatorCode: Optional[str] = attr(default=str)
    operator: Optional[str] = attr(default=str)
    admin: Optional[str] = attr(default=str)
    routeIdxFrom: int = attr(default=-1, tag='routeIdxFrom')
    routeIdxTo: int = attr(default=-1, tag='routeIdxTo')
    matchId: Optional[str] = attr(default=str)

    #Customer specific attributes
    tarGr: Optional[str] = attr(default=str, tag='tarGr')
    surcharge: Optional[str] = attr(default=str, tag='surcharge')
    outCtrl: Optional[str] = attr(default=str, tag='outCtrl')
    locTraffic: Optional[str] = attr(default=str, tag='locTraffic')
    shipTraffic: Optional[str] = attr(default=str, tag='shipTraffic')

    icon: dict[str, str] = element(
        default_factory=dict,
        tag='icon'
    )

    status: dict[str, str] = element(
        default_factory=dict,
        tag='status'
    )

    fromLocation: dict[str, str] = element(
        default_factory=dict,
        tag='fromLocation'
    )

    toLocation: dict[str, str] = element(
        default_factory=dict,
        tag='toLocation'
    )

    operatorInfo: dict[str, str] = element(
        default_factory=dict,
        tag='operatorInfo'
    )

    Note: list[dict[str, str]] = element(
        default_factory=list,
        tag='Note'
    )

    Message: list[dict[str, str]] = element(
        default_factory=list,
        tag='Message'
    )
    LineInfo: dict[str, str] = element(
        default_factory=dict,
        tag='LineInfo'
    )



# <xs:element name="icon" type="IconType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="status" type="ProductStatusType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="fromLocation" type="StopType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="toLocation" type="StopType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="operatorInfo" type="OperatorType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="Note" type="Note" minOccurs="0" maxOccurs="unbounded"/>
# <xs:element name="Message" type="Message" minOccurs="0" maxOccurs="unbounded"/>
# <xs:element name="LineInfo" type="LineType" minOccurs="0" maxOccurs="1"/>

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

# <xs:attribute name="tarGr" type="xs:string" use="optional"/>
# <xs:attribute name="surcharge" type="xs:string" use="optional"/>
# <xs:attribute name="outCtrl" type="xs:string" use="optional"/>
# <xs:attribute name="locTraffic" type="xs:string" use="optional"/>
# <xs:attribute name="shipTraffic" type="xs:string" use="optional"/>


