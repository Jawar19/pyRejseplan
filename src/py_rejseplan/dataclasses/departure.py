import datetime
import logging
from typing import Optional
from pydantic_xml import BaseXmlModel, attr, element

import py_rejseplan.dataclasses.constants as constants

from .product_type import ProductType
from .journey_detail_ref import JourneyDetailRef
from .note import Notes
from .enums import JourneyStatusType, PrognosisType, DepartureType, RealtimeDataSourceType

_LOGGER = logging.getLogger(__name__)


class Departure(
    BaseXmlModel,
    tag='Departure',
    ns="",
    nsmap=constants.NSMAP,
    search_mode='unordered',
    ):
    """Departure class for parsing XML data from the Rejseplanen API.
    This class is used to represent the departure data returned by the API.
    It extends the BaseXmlModel from pydantic_xml to provide XML parsing capabilities.
    """
    name: str = attr()
    type: DepartureType = attr(default=None, tag='type',)
    stop: str = attr()
    stopid: str = attr()
    stopExtId: int = attr()
    lon: Optional[float] = attr(default=None)
    lat: Optional[float] = attr(default=None)
    isMainMast: Optional[bool] = attr(default=False)
    hasMainMast: Optional[bool] = attr(default=False)
    mainMastId: Optional[str] = attr(default=None, tag='mainMastId')
    mainMastExtId: Optional[str] = attr(default=None, tag='mainMastExtId')
    mainMastLon: Optional[float] = attr(default=None, tag='mainMastLon')
    mainMastLat: Optional[float] = attr(default=None, tag='mainMastLat')
    mainMastAlt: Optional[int] = attr(default=None, tag='mainMastAlt')
    prognosisType: Optional[PrognosisType] = attr(default=None,tag='prognosisType')
    time: datetime.time = attr()
    scheduledTimeChanged: Optional[bool] = attr(default=False, tag='scheduledTimeChanged')
    date: datetime.date = attr()
    tz: Optional[int] = attr(default=0, tag='tz')
    track: Optional[str] = attr(default=None)
    trackHidden: bool = attr(default=False, tag='trackHidden')

    rtTime: Optional[datetime.time] = attr(tag='rtTime', default=None)
    rtDate: Optional[datetime.date] = attr(tag='rtDate', default=None)
    rtTz: Optional[int] = attr(tag='rtTz', default=0)
    rtTrack: Optional[str] = attr(tag='rtTrack', default=None)
    rttrackHidden: bool = attr(default=False, tag='rtTrackHidden')
    cancelled: Optional[bool] = attr(default=False)
    partCancelled: Optional[bool] = attr(default=False, tag='partCancelled')
    reachable: Optional[bool] = attr(default=True)
    redirected: Optional[bool] = attr(default=False)
    direction: Optional[str] = attr(default=None)
    directionFlag: Optional[int] = attr(default=None, tag='directionFlag')
    directionExtId: Optional[str] = attr(default=None, tag='directionExtId')
    timeAtArrival: Optional[datetime.time] = attr(default=None, tag='timeAtArrival')
    dateAtArrival: Optional[datetime.date] = attr(default=None, tag='dateAtArrival')
    rtTimeAtArrival: Optional[datetime.time] = attr(default=None, tag='rtTimeAtArrival')
    rtDateAtArrival: Optional[datetime.date] = attr(default=None, tag='rtDateAtArrival')
    isFastest: Optional[bool] = attr(default=False, tag='isFastest')
    isBorderStop: Optional[bool] = attr(default=False, tag='isBorderStop')
    isTurningPoint: Optional[bool] = attr(default=False, tag='isTurningPoint')
    entry: Optional[bool] = attr(default=None)
    rtCnclDataSourceType: Optional[RealtimeDataSourceType] = attr(default=None, tag='rtCnclDataSourceType')
    uncertainDelay: Optional[bool] = attr(default=False, tag='uncertainDelay')

    # Subelements
    originStop: Optional['Departure'] = element(
        default=None,
        tag='OriginStop'
    )
    destinationStop: Optional['Departure'] = element(
        default=None,
        tag='DestinationStop'
    )
    journeyDetailRef: JourneyDetailRef = element(
        default_factory=None,
        tag='JourneyDetailRef'
    )
    journeyStatus: JourneyStatusType = element(
        default_factory=None,
        tag='JourneyStatus'
    )
    productAtStop: ProductType = element(
        default_factory=list,
        tag='ProductAtStop'
    )
    product: ProductType = element(
        default_factory=list,
        tag='Product'
    )
    notes: Notes = element(
        tag='Notes',  # This navigates through the Notes container
    )

    messages: list[str] = element(
        default_factory=list,
        tag='Messages'
    )

    directions: list[str] = element(
        default_factory=list,
        tag='Directions'
    )

    platform: dict[str, str] = element(
        default_factory=dict,
        tag='platform'
    )
    rtPlatform: dict[str, str] = element(
        default_factory=dict,
        tag='rtPlatform'
    )


# <xs:element name="OriginStop" type="StopType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="DestinationStop" type="StopType" minOccurs="0" maxOccurs="1"/>
# <xs:element ref="JourneyDetailRef"/>
# <xs:element name="JourneyStatus" type="JourneyStatusType" minOccurs="0"/>
# <xs:element name="ProductAtStop" type="ProductType" minOccurs="0" maxOccurs="1">
# <xs:element name="Product" type="ProductType" minOccurs="0" maxOccurs="unbounded">
# <xs:documentation>Product information from requested departure stop to the last stop of the service. In case of product information changes along, multiple entries are possible.</xs:documentation>
# <xs:element ref="Notes" minOccurs="0"/>
# <xs:element ref="Messages" minOccurs="0"/>
# <xs:element ref="Directions" minOccurs="0"/>
# <xs:element name="altId" type="xs:string" minOccurs="0" maxOccurs="unbounded">
# <xs:element name="mainMastAltId" type="xs:string" minOccurs="0" maxOccurs="unbounded">
# <xs:element ref="Stops" minOccurs="0"/>
# <xs:element name="Occupancy" type="OccupancyType" minOccurs="0" maxOccurs="unbounded"/>
# <xs:element name="ParallelJourneyRef" type="ParallelJourneyRefType" minOccurs="0" maxOccurs="unbounded"/>
# <xs:element name="referencedJourney" type="ReferencedJourneyType" minOccurs="0" maxOccurs="unbounded">
# <xs:element name="platform" type="PlatformType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="rtPlatform" type="PlatformType" minOccurs="0" maxOccurs="1"/>
# <xs:element name="mainMast" type="StopLocation" minOccurs="0">
# <xs:attributeGroup ref="attlist.Departure"/>

# ==== ATTLIST DEPARTURE ====

# <xs:attribute name="name" use="required">  # DONE
# <xs:documentation>Specifies the name of the departing journey (e.g. "Bus 100") as used for display. </xs:documentation>  

# <xs:attribute name="type" use="required">  # DONE
# <xs:documentation>The attribute type specifies the type of departs location. Valid values are ST (stop/station), ADR (address), POI (point of interest), CRD (coordinate), MCP (mode change point) or HL (hailing point). </xs:documentation>

# <xs:simpleType>
#     <xs:restriction base="xs:string">
#         <xs:enumeration value="ST"/>
#         <xs:enumeration value="ADR"/>
#         <xs:enumeration value="POI"/>
#         <xs:enumeration value="CRD"/>
#         <xs:enumeration value="MCP"/>
#         <xs:enumeration value="HL"/>
#     </xs:restriction>
# </xs:simpleType>

# <xs:attribute name="stop" type="xs:string" use="required">  # DONE
# <xs:documentation>Contains the name of the stop/station.</xs:documentation>

# <xs:attribute name="stopid" type="xs:string" use="required">
# <xs:documentation>Contains the ID of the stop/station.</xs:documentation>  # DONE

# <xs:attribute name="stopExtId" type="xs:string" use="optional">
# <xs:documentation>External ID of this stop/station</xs:documentation>  # DONE

# <xs:attribute name="lon" type="xs:decimal" use="optional">  # DONE
# <xs:documentation>The WGS84 longitude of the geographical position of this stop/station.</xs:documentation>

# <xs:attribute name="lat" type="xs:decimal" use="optional">  # DONE    
# <xs:documentation>The WGS84 latitude of the geographical position of this stop/station.</xs:documentation>

# <xs:attribute name="alt" type="xs:int" use="optional">  # DONE
# <xs:documentation>The altitude of the geographical position of this stop/station.</xs:documentation>

# <xs:attribute name="isMainMast" type="xs:boolean"> # DONE
# <xs:documentation>True if this stop is a main mast.</xs:documentation>

# <xs:attribute name="hasMainMast" type="xs:boolean">  # DONE
# <xs:documentation>True if this stop belongs to a main mast.</xs:documentation>

# <xs:attribute name="mainMastId" type="xs:string">  # DONE
# <xs:documentation>Deprecated. Use mainMast structure instead. ID of the main mast this stop belongs to.</xs:documentation>

# <xs:attribute name="mainMastExtId" type="xs:string" use="optional">  # DONE
# <xs:documentation>Deprecated. Use mainMast structure instead. External ID of the main mast this stop belongs to.</xs:documentation>

# <xs:attribute name="mainMastLon" type="xs:decimal" use="optional">  # DONE
# <xs:documentation>Deprecated. Use mainMast structure instead. The WGS84 longitude of the geographical position of the main mast this stop/station. </xs:documentation>

# <xs:attribute name="mainMastLat" type="xs:decimal" use="optional">  # DONE
# <xs:documentation>Deprecated. Use mainMast structure instead. The WGS84 latitude of the geographical position of the main mast this stop/station. </xs:documentation>

# <xs:attribute name="mainMastAlt" type="xs:int" use="optional">  # DONE
# <xs:documentation>Deprecated. Use mainMast structure instead. The altitude of the geographical position of the main mast this stop/station.</xs:documentation>

# <xs:attribute name="prognosisType" type="PrognosisType" use="optional">  # DONE
# <xs:documentation>Prognosis type of departure date and time.</xs:documentation>

# <xs:attribute name="time" type="xs:string" use="required">    # DONE
# <xs:documentation>Time in format hh:mm[:ss]</xs:documentation>

# <xs:attribute name="scheduledTimeChanged" type="xs:boolean" use="optional" default="false">   # DONE
# <xs:documentation>Scheduled time changed.</xs:documentation>

# <xs:attribute name="date" type="xs:string" use="required"> # DONE
# <xs:documentation>Date in format YYYY-MM-DD.</xs:documentation>

# <xs:attribute name="tz" type="xs:int" use="optional" default="0"> # DONE
# <xs:documentation>Time zone information in the format +/- minutes</xs:documentation>

# <xs:attribute name="track" type="xs:string" use="optional">
# <xs:documentation>Track information, if available.</xs:documentation>

# <xs:attribute name="trackHidden" type="xs:boolean" default="false">
# <xs:documentation>True if track information is hidden by data.</xs:documentation>

# <xs:attribute name="rtTime" type="xs:string" use="optional">
# <xs:documentation>Realtime time in format hh:mm[:ss] if available.</xs:documentation>

# <xs:attribute name="rtDate" type="xs:string" use="optional">
# <xs:documentation>Realtime date in format YYYY-MM-DD, if available.</xs:documentation>

# <xs:attribute name="rtTz" type="xs:int" use="optional" default="0">
# <xs:documentation>Realtime time zone information in the format +/- minutes, if available.</xs:documentation>

# <xs:attribute name="rtTrack" type="xs:string" use="optional">
# <xs:documentation>Realtime track information, if available.</xs:documentation>

# <xs:attribute name="rtTrackHidden" type="xs:boolean" default="false">
# <xs:documentation>True if track information is hidden by realtime data.</xs:documentation>

# <xs:attribute name="cancelled" type="xs:boolean" use="optional" default="false">
# <xs:documentation>Will be true if this journey is cancelled</xs:documentation>

# <xs:attribute name="partCancelled" type="xs:boolean" use="optional" default="false">
# <xs:documentation>Will be true if this journey is partially cancelled.</xs:documentation>

# <xs:attribute name="reachable" type="xs:boolean" use="optional" default="true">
# <xs:documentation>Will be true if this journey is reachable. A journey is considered reachable if either the follow-up journey is reachable based on the scheduled time (default without realtime) or the followup journey is not reachable regarding realtime situation but reported as reachable explicitly.</xs:documentation>

# <xs:attribute name="redirected" type="xs:boolean" use="optional" default="false">
# <xs:documentation>Will be true if this journey is redirected. A journey is considered as redirected if structural changes (e.g. additional/removed stop, change of scheduled times, ...) have been made.</xs:documentation>

# <xs:attribute name="direction" type="xs:string" use="optional">
# <xs:documentation>Direction information. This is the last stop of the journey. Get the full journey of the train or bus with the JourneyDetails service. </xs:documentation>

# <xs:attribute name="directionFlag" type="xs:string">
# <xs:documentation>Direction flag of the journey.</xs:documentation>

# <xs:attribute name="directionExtId" type="xs:string" use="optional">
# <xs:documentation>External ID of direction stop/station</xs:documentation>

# <xs:attribute name="timeAtArrival" type="xs:string" use="optional">
# <xs:documentation>Time in format hh:mm[:ss] the services arrives at the destination.</xs:documentation>

# <xs:attribute name="dateAtArrival" type="xs:string" use="optional">
# <xs:documentation>Date in format YYYY-MM-DD the services arrives at the destination.</xs:documentation>

# <xs:attribute name="rtTimeAtArrival" type="xs:string" use="optional">
# <xs:documentation>Realtime time in format hh:mm[:ss] the services arrives at the destination.</xs:documentation>

# <xs:attribute name="rtDateAtArrival" type="xs:string" use="optional">
# <xs:documentation>Realtime date in format YYYY-MM-DD the services arrives at the destination. </xs:documentation>

# <xs:attribute name="isFastest" type="xs:boolean" use="optional">
# <xs:documentation>Services is 'fastest service to' location.</xs:documentation>

# <xs:attribute name="isBorderStop" type="xs:boolean" use="optional" default="false">
# <xs:documentation>Will be true if this stop is a border stop</xs:documentation>

# <xs:attribute name="isTurningPoint" type="xs:boolean" use="optional" default="false">
# <xs:documentation>Will be true if this stop is a turning point</xs:documentation>

# <xs:attribute name="entry" type="xs:boolean" use="optional">
# <xs:documentation>True, if the stop is an entry point.</xs:documentation>

# <xs:attribute name="rtCnclDataSourceType" type="RealtimeDataSourceType" use="optional">
# <xs:documentation>Realtime data source that the stop cancellation originates from</xs:documentation>

# <xs:attribute name="uncertainDelay" type="xs:boolean" use="optional" default="false">
# <xs:documentation>The journey stopped or is waiting somewhere along its path and some journey stops contain an uncertain delay.</xs:documentation>
