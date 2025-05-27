from enum import Enum

class PrognosisType(str, Enum):
    """Types of prognosis for departure times.
    
    Indicates how the prognosis was determined:
    - PROGNOSED: Reported from external provider as future prognosis
    - MANUAL: Manually entered by external provider
    - REPORTED: Reported delay from previously passed stations
    - CORRECTED: System-corrected to ensure journey consistency
    - CALCULATED: System-calculated for upcoming or gap-filling stations
    """
    PROGNOSED = "PROGNOSED"
    MANUAL = "MANUAL"
    REPORTED = "REPORTED"
    CORRECTED = "CORRECTED"
    CALCULATED = "CALCULATED"

class DepartureType(str, Enum):
    """The attribute type specifies the type of departs location. 
    Valid values are: 
        ST (stop/station), 
        ADR (address), 
        POI (point of interest), 
        CRD (coordinate), 
        MCP (mode change point) 
        HL (hailing point).
    """
    ST = "ST"
    ADR = "ADR"
    POI = "POI"
    CRD = "CRD"
    MCP = "MCP"
    HL = "HL"