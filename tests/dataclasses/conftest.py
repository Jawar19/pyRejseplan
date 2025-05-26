import logging

import pytest

from py_rejseplan.api.departures import DepartureBoard

_LOGGER = logging.getLogger(__name__)

@pytest.fixture()
def roskilde_st_data() -> str:
    """Fixture for the Roskilde station data."""
    _LOGGER.debug("Loading Roskilde station data")
    # with open('./requestData/mdbRoskildeSt.xml', 'r', encoding='utf-8') as f:
    with open('./requestData/mdbRoskildeSt.xml', 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    return xml_content

@pytest.fixture
def departure_board(roskilde_st_data) -> DepartureBoard:
    """Fixture that parses the XML data once for all tests."""
    _LOGGER.debug('Creating DepartureBoard fixture from XML data')
    return DepartureBoard.from_xml(roskilde_st_data)