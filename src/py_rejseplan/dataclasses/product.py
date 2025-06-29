# -*- coding: utf-8 -*-
"""Product class for parsing XML data from the Rejseplanen API."""
from typing import Optional
from pydantic_xml import BaseXmlModel, attr, element
import py_rejseplan.dataclasses.constants as constants


class Product(
    BaseXmlModel,
    tag='Product',
    ns="",
    nsmap=constants.NSMAP
):
    """Product class for parsing XML data from the Rejseplanen API.
    This class is used to represent the product data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    name: str = attr()
    internalName: str = attr()
    displayNumber: str = attr()
    num: str = attr()
    catOut: str = attr()
    catIn: str = attr()
    catCode: str = attr()
    cls: str = attr()
    catOutS: str = attr()
    catOutL: str = attr()
    operatorCode: Optional[str] = attr(default="")
    operator: Optional[str] = attr(default="")
    admin: str = attr()
    routeIdxFrom: int = attr()
    routeIdxTo: int = attr()
    matchId: str = attr()
    icon: dict[str, str] = element(
        default_factory=dict,
        tag='icon'
    )
    operatorInfo: dict[str, str] = element(
        default_factory=dict,
        tag='operatorInfo'
    )

# <Product name="Re 54541" internalName="Re 54541" displayNumber="54541" num="54541"
#     catOut="Re" catIn="004" catCode="2" cls="4" catOutS="004" catOutL="Re"
#     operatorCode="DSB" operator="DSB" admin="000002" routeIdxFrom="19" routeIdxTo="24"
#     matchId="54541">
#     <icon res="prod_ic" />
#     <operatorInfo name="DSB" nameS="DSB" nameN="DSB" nameL="DSB" />
# </Product>