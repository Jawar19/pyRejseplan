"""
locationhandler.py
This module provides the LocationHandler class responsible for handling
location-related operations using the Rejseplanen API. It includes methods
for initializing the handler with an authorization key and making requests
to retrieve location data.

Classes:
    LocationHandler: Handles location-related operations and manages
    authorization headers.
    DEBUG (bool): A flag to enable or disable debug mode.

Usage:
    handler = LocationHandler(auth_key="your_auth_key")
    # Use handler to perform location-related operations
"""

import logging
# import requests
# from xml.etree import ElementTree

# from py_rejseplan import constants, utils

DEBUG = False
_logger = logging.getLogger(__name__)


class LocationHandler:
    """
    LocationHandler is responsible for handling location-related operations.
    Attributes:
        headers (dict): A dictionary containing the authorization header.
        _logger (logging.Logger): Logger instance for logging messages.
    Methods:
        __init__(auth_key: str) -> None:
            Initializes the LocationHandler with the provided authorization key.
            Args:
                auth_key (str): The authorization key to be used in headers.
    """

    headers: dict

    def __init__(self, auth_key: str) -> None:
        _logger.debug('Initializing LocationHandler')
        self.headers = {'Authorization': f'Bearer {auth_key}'}

    def address_lookup(self) -> list:
        """
        Retrieves a list of possible locations from an address string using the underlying API.
        Args:
            address (str): The address string to look up.
        Returns:
            list: A list of possible locations matching the given address string.
        """
        # Implementation goes here
        _logger.debug('Address lookup')

    def coordinate_lookup(self, latitude: float, longitude: float) -> list:
        """
        Looks up location information based on provided latitude and longitude coordinates.
        Args:
            latitude (float): The latitude of the location to look up.
            longitude (float): The longitude of the location to look up.
        Returns:
            list: A list containing location information corresponding to the provided coordinates.
        """
        _logger.debug('Geo location lookup')


# def request_location(auth_key:str, location):
#     service = "location.name"
#     headers = {
#         "Authorization": f"Bearer {auth_key}"
#     }
#     url = constants.RESOURCE + service

#     if DEBUG:
#         request = requests.Request('GET',
#                                     url,
#                                     headers=headers,
#                                     params={"input": location}
#                                     )
#         prepared_request = request.prepare()
#         utils.dump_prepared_request(prepared_request)
#         with open(os.path.join(os.getcwd(), r"requestData\dLocation.xml"),
#                   "r",
#                   encoding="UTF-8"
#                   ) as xml_file:
#             xml_elem = ElementTree.parse(xml_file)
#         xml_data = xml_elem.getroot()
#         for location in xml_data.findall("ns0:StopLocation",NS):
#             print(location.get("name"), location.get("name"))
#             products = [
#                 product.get('name') for product
#                 in location.findall("ns0:productAtStop", NS)
#                 ]
#             print('\t', end='')
#             print(*products, sep='\n\t')
#             print()


#     else:
# response: requests.Response = requests.get(url,
#                                            headers=headers,
#                                            params={"input": location}
#                                            )
#         xmlroot: ElementTree.Element = ElementTree.fromstring(response.content)
#         xmltree = ElementTree.ElementTree(xmlroot)

#         xml_bytes = ElementTree.tostring(xmlroot, encoding='utf-8', method='xml')

#         # Add the XML declaration manually
#         xml_declaration = b'<?xml version="1.0" encoding="utf-8"?>\n'
#         full_xml = xml_declaration + xml_bytes

#         # Print the resulting XML string
#         print(full_xml.decode('utf-8'))

#         # print("dumping xml...")
#         # with open(os.path.join(os.getcwd(), r"requestData\dLocation.xml"), "wb") as f:
#         #     xmltree.write(f, encoding='utf-8', xml_declaration=True)
