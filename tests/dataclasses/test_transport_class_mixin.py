import pytest

from py_rejseplan.dataclasses.mixins import TransportClassMixin
from py_rejseplan.enums import TransportClass
from py_rejseplan.dataclasses.transport_mappings import DEPARTURE_TYPE_TO_CLASS, CATOUT_TO_CLASS

@pytest.mark.parametrize("transport_type,expected_class", [
    (TransportClass.BUS, "bus"),
    (TransportClass.IC, "IC"),
    (TransportClass.METRO, "metro"),
    (TransportClass.ICL, "ICL"),
])
def test_transport_class_mixin_get_transport_class_int(transport_type: TransportClass, expected_class: str):
    """Test TransportClassMixin.get_transport_class returns correct class for known transport types."""
    mixin = TransportClassMixin()
    mixin.cls = transport_type.value
    assert mixin.get_transport_class() == transport_type

@pytest.mark.parametrize("transport_type,expected_class", [
    ("EC", TransportClass.TOG),
    ("IR", TransportClass.TOG),
    ("IP", TransportClass.TOG),
    ("Bus", TransportClass.BUS),
    ("Bybus", TransportClass.BUS),
    ("E-Bus", TransportClass.BUS),
    ("ServiceB", TransportClass.BUS),
    ("R-net", TransportClass.BUS),
])
def test_transport_class_mixin_get_transport_class_str(transport_type: str, expected_class: TransportClass):
    """Test TransportClassMixin.get_transport_class returns correct class for known transport types."""
    mixin = TransportClassMixin()
    mixin.catOut = transport_type 
    assert mixin.get_transport_class() == expected_class

@pytest.mark.parametrize("transport_type", [
    "spaceship",
    "",
    None,
])
def test_transport_class_mixin_get_transport_class_unknown(transport_type: str):
    """Test TransportClassMixin.get_transport_class returns 'unknown' for unknown transport types."""
    mixin = TransportClassMixin()
    mixin.catOut = transport_type
    assert mixin.get_transport_class() is None

