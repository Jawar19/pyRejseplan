# -*- coding: utf-8 -*-
"""Test the DepartureBoard class."""
import logging

import datetime

import pytest
from py_rejseplan.dataclasses.departure import Departure
from py_rejseplan.dataclasses.departure_board import DepartureBoard


_LOGGER = logging.getLogger(__name__)

def test_basic_attributes(departure_board: DepartureBoard):
    """Test the basic attributes of the DepartureBoard."""
    assert departure_board.serverVersion == '2.49.1'
    assert departure_board.dialectVersion == "2.45-Rejseplanen"
    assert departure_board.requestId == "e22kxq84ic8ypg8x"

def test_timestamp_parsing(departure_board: DepartureBoard):
    """Test that timestamp is correctly parsed."""
    assert isinstance(departure_board.planRtTs, datetime.datetime)
    assert departure_board.planRtTs == datetime.datetime.fromisoformat("2025-05-23T11:12:39+02:00")

def test_technical_messages(departure_board: DepartureBoard):
    """Test the technical messages in the DepartureBoard."""
    assert hasattr(departure_board, 'technicalMessages')
    tech_messages = departure_board.technicalMessages.technicalMessages
    assert len(tech_messages) > 0
    
    # Test specific message if it exists
    request_time_msg = next((msg for msg in tech_messages if msg.key == "requestTime"), None)
    if request_time_msg:
        assert "2025-05-23" in request_time_msg.text, "Expected date in requestTime message"

def test_departures_list(departure_board: DepartureBoard):
    """Test that departures are correctly parsed."""
    assert hasattr(departure_board, 'departures')
    assert len(departure_board.departures) > 0

def test_first_departure_details(departure_board: DepartureBoard):
    """Test details of the first departure."""
    # Skip if no departures
    if not departure_board.departures:
        pytest.skip("No departures in test data")
        
    first_departure: Departure = departure_board.departures[0]
    assert first_departure.name is not None
    assert first_departure.stop == "Roskilde St."
    assert isinstance(first_departure.time, datetime.time)
    assert isinstance(first_departure.date, datetime.date)