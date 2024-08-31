"""This module represents a stop location
"""
from dataclasses import dataclass

@dataclass
class StopLocation():
    """Stop location
    """
    id: str
    extId: int
    isMainMast: bool
    name: str
    longitude: float
    latitude: float
    weight: int
    products: list
