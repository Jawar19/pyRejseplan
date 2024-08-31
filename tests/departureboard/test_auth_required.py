import pytest


def test_connection(t_departureboard, key):
    """test connection to Rejseplanen API

    Arguments:
        t_departureboard -- Fixture
        key -- Fixture
    """
    if key == "DUMMY_KEY":
        pytest.skip("API key is DUMMY_KEY")
    assert True
    