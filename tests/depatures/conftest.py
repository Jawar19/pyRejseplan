"""Pytest configuration for departures tests."""
import logging
import pytest

from py_rejseplan.api.departures import DeparturesAPIClient

_LOGGER = logging.getLogger(__name__)


@pytest.fixture
def departures_api_client(key):
    """Fixture to create a departures API client with real API key."""
    auth = key
    departures_api_client = DeparturesAPIClient(auth_key=auth)
    return departures_api_client


@pytest.fixture
def sample_valid_xml():
    """Fixture for valid XML response."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
    <DepartureBoard serverVersion="1.0" dialectVersion="1.0" 
                   planRtTs="2024-11-03T10:30:00Z" requestId="test123"
                   xmlns="http://hacon.de/hafas/proxy/hafas-proxy">
        <TechnicalMessages></TechnicalMessages>
    </DepartureBoard>'''


@pytest.fixture
def sample_malformed_xml():
    """Fixture for malformed XML response."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
    <DepartureBoard serverVersion="1.0" dialectVersion="1.0" 
                   planRtTs="2024-11-03T10:30:00Z" requestId="malformed123"
                   xmlns="http://hacon.de/hafas/proxy/hafas-proxy">
        <TechnicalMessages></TechnicalMessages>
        <Departure name="Bus 100" stop="Station A" stopid="123" stopExtId="456" 
                  type="ST" date="2024-11-03" time="10:35:00">
            <!-- Missing required fields like JourneyDetailRef -->
        </Departure>
        <Departure name="Train 200" stop="Station B" stopid="INVALID_ID" 
                  type="ST" date="INVALID_DATE" time="INVALID_TIME">
            <!-- Invalid data -->
        </Departure>
    </DepartureBoard>'''


@pytest.fixture
def sample_empty_xml():
    """Fixture for empty XML response."""
    return '''<?xml version="1.0" encoding="UTF-8"?>
    <DepartureBoard serverVersion="1.0" dialectVersion="1.0" 
                   planRtTs="2024-11-03T10:30:00Z" requestId="empty123"
                   xmlns="http://hacon.de/hafas/proxy/hafas-proxy">
        <TechnicalMessages></TechnicalMessages>
    </DepartureBoard>'''