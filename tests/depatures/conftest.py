import logging
import pytest

from py_rejseplan.api.departures import DeparturesAPIClient

_LOGGER = logging.getLogger(__name__)


@pytest.fixture
def departures_api_client(key):
    """Fixture to create a departures API client."""
    auth = key
    departures_api_client = DeparturesAPIClient(auth_key=auth)
    return departures_api_client