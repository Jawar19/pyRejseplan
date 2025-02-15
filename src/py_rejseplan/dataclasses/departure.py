"""Module containing representation of a departures from Rejseplanen
"""
from dataclasses import dataclass, field
from datetime import datetime, date as dt_date, time as dt_time
import enum

class PrognosisType(enum.Enum):
    """Enum to describe prognosis type from the REST API
    """
    PROGNOSED = "PROGNOSED"
    UNKNOWN = "UNKNOWN"

class LocationType(enum.Enum):
    """Location type enum

    ### From documentation:
    The attribute type specifies the type of the departure location. 
    Valid values are ST (stop/station), ADR(address), POI (point of interest), 
    CRD (coordinate), MCP (mode change point) or HL (hailing point)
    """
    ST =    "stop/station"
    ADR =   "address"
    POI =   "point of interest"
    CRD =   "coordinate"
    MCP =   "mode change point"
    HL  =   "hailing point"
    UNKNOWN = "UNKNOWN"


@dataclass
class Departure:
    """Simple departure dataclass

    A list of dictionaries, each containing departure name, time, direction and type.
        The results from all stops are mixed, but can be filtered by stop.
    """
    # pylint: disable=too-many-instance-attributes, C0103
    # These are all essential parameters from the REST API, names are created
    # with same names as in the REST API from Rejseplanen
    name: str = "Unknown"
    type: LocationType = LocationType.UNKNOWN
    stop: str = "Unknown"
    stopid: str = "Unknown"
    stopExtId: int = 0
    lon: float = 0.0
    lat: float = 0.0
    isMainMast: bool = False
    prognosisType: PrognosisType = PrognosisType.UNKNOWN
    time: dt_time = field(default_factory=lambda: dt_time(0, 0, 0))
    date: dt_date = field(default_factory=dt_date.today)
    track: int = -1
    rtTrack: int = -1
    reachable: bool = False
    direction: str = "Unknown"
    directionFlag: int = -1

def parse_departure(data: dict) -> Departure:
    """Convert dictionary to Departure dataclass.
    
    TODO: This needs to be robust enough to handle missing dict values. 
    """
    return Departure(
        name=data.get("name", "Unknown"),
        type=LocationType[data["type"]]
            if data.get("type") in LocationType.__members__
            else LocationType.UNKNOWN,
        stop=data.get("stop", "Unknown"),
        stopid=data.get("stopid", "Unknown"),
        stopExtId=int(data.get("stopExtId", 0)),
        lon=float(data.get("lon", 0.0)),
        lat=float(data.get("lat", 0.0)),
        isMainMast=data.get("isMainMast", "false").lower() == "true",  # Convert to bool
        prognosisType=PrognosisType[data.get("prognosisType")]
            if data.get("prognosisType") in PrognosisType.__members__
            else PrognosisType.UNKNOWN,
        time=datetime.strptime(data.get("time", "00:00:00"), "%H:%M:%S").time(),
        date=datetime.strptime(data.get("date", "1970-01-01"), "%Y-%m-%d").date(),
        track=int(data.get("track", -1)),
        rtTrack=int(data.get("rtTrack", -1)),
        reachable=data.get("reachable", "false").lower() == "true",  # Convert to bool
        direction=data.get("direction", "Unknown"),
        directionFlag=int(data.get("directionFlag", -1))
    )
