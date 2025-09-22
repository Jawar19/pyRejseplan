from typing import Optional
from py_rejseplan.enums import TransportClass
from py_rejseplan.dataclasses.transport_mappings import CATOUT_TO_CLASS

class TransportClassMixin:
    """Mixin to add transport class functionality to dataclasses."""

    cls: Optional[int] = None  # Placeholder for the cls attribute
    catOut: Optional[str] = None  # Placeholder for the catOut attribute
    
    def get_transport_class(self) -> Optional[TransportClass]:
        """Get the transport class based on the catOut attribute.
        Returns:
            Optional[TransportClass]: The transport class if found, else None.
        """
        if self.cls is not None:
            try:
                return TransportClass(self.cls)
            except ValueError:
                pass  # Invalid cls value, fall back to catOut

        if self.catOut:
            transport_class = CATOUT_TO_CLASS.get(self.catOut)
            if transport_class:
                return transport_class

        return None