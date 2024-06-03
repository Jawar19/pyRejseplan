from dataclasses import dataclass, field

@dataclass
class StopLocation():
    id: str
    extId: int
    isMainMast: bool
    name: str
    longitude: float
    latitude: float
    weight: int
    products: list
