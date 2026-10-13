from typing import List, Optional
from pydantic_xml import BaseXmlModel, attr, element
import py_rejseplan.dataclasses.constants as constants

class Note(BaseXmlModel, tag='Note', nsmap=constants.NSMAP):
    key: str = attr()
    type: str = attr()
    priority: Optional[int] = attr(default=None)
    routeIdxFrom: Optional[int] = attr(default=None)
    routeIdxTo: Optional[int] = attr(default=None)
    txtN: Optional[str] = attr(default=None)

    value: Optional[str] = element(tag='value', default=None)
    children: list['Note'] = element(tag='Note', default_factory=list)

    @property
    def text(self) -> Optional[str]:
        return self.value if self.value is not None else self.txtN

class Notes(BaseXmlModel, tag='Notes', nsmap=constants.NSMAP):
    note: List[Note] = element(tag='Note', default_factory=list)