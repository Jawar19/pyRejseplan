"""Module containing representation of a departures from Rejseplanen
"""
from dataclasses import dataclass
from datetime import date, time


@dataclass
class Departure:
    """Simple departure dataclass
    """
    departure_date: date
    departure_time: time
    direction: str
    name: str
    prognosis_type: str
    departure_track: int
    departure_type: str
