"""Module containing tests for rejseplanen which requires an API key
"""
import pytest
from requests import Response


def test_connection(t_departureboard, key):
    """test connection to Rejseplanen API

    Arguments:
        t_departureboard -- Fixture
        key -- Fixture
    """
    if key == "DUMMY_KEY":
        pytest.skip("API key is DUMMY_KEY")

    t_departureboard.add_stop_ids([8600617])
    response = t_departureboard.update()

    if not isinstance(response, Response):
        assert False, "Response from server is an unknown type"
