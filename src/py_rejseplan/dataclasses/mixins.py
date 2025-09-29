from typing import Optional
from py_rejseplan.enums import TransportClass
from py_rejseplan.dataclasses.transport_mappings import CATOUT_TO_CLASS

class TransportClassMixin():
    """Mixin to add transport class functionality to dataclasses."""
    
    def get_transport_class(self) -> Optional[TransportClass]:
        """Get the transport class based on the catOut attribute.
        Returns:
            Optional[TransportClass]: The transport class if found, else None.
        """
        cls_id = getattr(self, 'cls_id', None)
        if cls_id is not None:
            try:
                return TransportClass(cls_id)
            except ValueError:
                pass  # Invalid cls value, fall back to catOut

        cat_out = getattr(self, 'catOut', None)
        if cat_out:
            transport_class = CATOUT_TO_CLASS.get(cat_out)
            if transport_class:
                return transport_class

        return None