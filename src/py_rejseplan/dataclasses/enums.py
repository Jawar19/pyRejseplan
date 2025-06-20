from enum import Enum

class PrognosisType(str, Enum):
    """Types of prognosis for departure times."""
    PROGNOSED = "PROGNOSED"
    MANUAL = "MANUAL"
    REPORTED = "REPORTED"
    CORRECTED = "CORRECTED"
    CALCULATED = "CALCULATED"

class DepartureType(str, Enum):
    """The attribute type specifies the type of departs location."""
    ST = "ST"
    ADR = "ADR"
    POI = "POI"
    CRD = "CRD"
    MCP = "MCP"
    HL = "HL"

class RealtimeDataSourceType(str, Enum):
    """Realtime data source types."""
    DEFAULT = "DEFAULT"           # Default source (undefined)
    VDV = "VDV"
    HIM = "HIM"
    HRC = "HRC"
    SIRI = "SIRI"
    UIC = "UIC"
    HRX = "HRX"
    GTFS = "GTFS"
    FIS = "FIS"
    DDS = "DDS"                  # Datendrehscheiben
    PAISA = "PAISA"              # PA-ISA
    FE = "FE"                    # FahrtenEditor
    BLACKLIST = "BLACKLIST"      # List of blacklisted trains
    ARAMIS = "ARAMIS"            # ARAMIS data source
    RTABO2 = "RTABO2"            # RTABO2 data source

class JourneyStatusType(str, Enum):
    """Contains the status of the journey."""
    P = "P"  # Planned: A planned journey. This is also the default value.
    R = "R"  # Replacement: The journey was added as a replacement for a planned journey.
    A = "A"  # Additional: The journey is an additional journey to the planned journeys.
    S = "S"  # Special: This is a special journey. The exact definition which journeys are considered special is up to the customer.
