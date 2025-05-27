from typing import List, Optional
from pydantic_xml import BaseXmlModel, attr, element
import py_rejseplan.dataclasses.constants as constants

class Note(BaseXmlModel, tag='Note', nsmap=constants.NSMAP):
    key: str = attr()
    type: str = attr()
    priority: Optional[int] = attr(default=None)
    routeIdxFrom: Optional[int] = attr(default=None)
    routeIdxTo: Optional[int] = attr(default=None)
    txtN: Optional[str] = attr()
    content: Optional[str] = element(tag='', default=None) # Captures the text content


class Notes(BaseXmlModel, tag='Notes', nsmap=constants.NSMAP):
    note: List[Note] = element(tag='Note', default_factory=list)