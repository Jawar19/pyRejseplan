import logging

import pytest

from py_rejseplan.api.departures import DeparturesAPIClient


_LOGGER = logging.getLogger(__name__)

def test_get_departures(departures_api_client: DeparturesAPIClient):
    """Test the request method of departuresAPIClient."""

    _LOGGER.debug('Testing request method')
    # Call the request method with a sample stop ID
    # stop_id = [8600617]
    stop_id = [8600695, 8600617]
    departures, response = departures_api_client.get_departures(stop_id)
    assert response is not None, "Response should not be None"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert departures is not None, "Departures should not be None"
 
def test_validate_auth_key(departures_api_client: DeparturesAPIClient):
    """Test the validate_auth_key method of departuresAPIClient."""

    _LOGGER.debug('Testing validate_auth_key method')
    # Call the validate_auth_key method
    is_valid = departures_api_client.validate_auth_key()
    assert is_valid, "Authorization key should be valid"

def test_validate_auth_key_invalid(departures_api_client: DeparturesAPIClient):
    """Test the validate_auth_key method with an invalid key.
    This test simulates an invalid authorization key and checks if the method correctly identifies it as invalid.
    should use xfail to indicate that this test is expected to fail.
    """

    _LOGGER.debug('Testing validate_auth_key with invalid key')
    # Set an invalid auth key
    departures_api_client.headers['Authorization'] = 'Bearer invalid_key'
    is_valid = departures_api_client.validate_auth_key()
    assert not is_valid, "Authorization key should be invalid"

