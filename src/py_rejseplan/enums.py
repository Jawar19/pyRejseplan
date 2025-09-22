from enum import IntEnum

class TransportClass(IntEnum):
    """Transport class numbers from Rejseplanen XML."""

    IC = 1  # InterCity trains
    ICL = 2  # InterCity Lyn trains
    RE = 4  # Regional trains
    TOG = 8  # Long distance trains
    S_TOG = 16  # S-trains (Copenhagen suburban)
    BUS = 32  # Regular city buses
    EXPRESS_BUS = 64  # Express/long-distance buses (S-bus/E-bus)
    NIGHT_BUS = 128  # Night buses (N-bus)
    FLEXIBLE_BUS = 256  # Flexible transport (Divbus)
    FERRY = 512  # Ferry
    METRO = 1024  # Metro
    LETBANE = 2048  # Light rail
    FLIGHT = 4096  # Flight