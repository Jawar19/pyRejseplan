import logging
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

    name: str = attr()
    internalName: str = attr()
    displayNumber: int = attr()
    num: int = attr()
    catOut: str = attr()
    catIn: int = attr()
    catCode: int = attr()
    cls: int = attr()
    catOutS: int = attr()
    catOutL: str = attr()
    operatorCode: str = attr()
    operator: str = attr()
    admin: int = attr()
    matchId: int = attr()

    icon: dict[str, str] = element(
        default_factory=dict,
        tag='icon'
    )

    operatorInfo: dict[str, str] = element(
        default_factory=dict,
        tag='operatorInfo'
    )


# <ProductAtStop name="Re 54541" internalName="Re 54541" displayNumber="54541" num="54541"
#     catOut="Re" catIn="004" catCode="2" cls="4" catOutS="004" catOutL="Re"
#     operatorCode="DSB" operator="DSB" admin="000002" matchId="54541">
#     <icon res="prod_ic" />
#     <operatorInfo name="DSB" nameS="DSB" nameN="DSB" nameL="DSB" />
# </ProductAtStop>