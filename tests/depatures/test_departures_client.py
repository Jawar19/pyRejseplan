import logging

from py_rejseplan.api.departures import departuresAPIClient

_LOGGER = logging.getLogger(__name__)

def test_get_departures(departures_api_client: departuresAPIClient):
    """Test the request method of departuresAPIClient."""

    _LOGGER.debug('Testing request method')
    # Call the request method with a sample stop ID
    stop_id = [8600617]
    departures, response = departures_api_client.get_departures(stop_id)
    assert response is not None, "Response should not be None"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"