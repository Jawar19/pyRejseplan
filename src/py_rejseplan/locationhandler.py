from . import constants, utils
import logging

import requests
from xml.etree import ElementTree

DEBUG = False

class LocationHandler():
    
    headers: dict
    _logger = logging.getLogger(__name__)

    def __init__(self, auth_key: str) -> None:
        self._logger.debug("Initializing LocationHandler")
        self.headers = {
            "Authorization": f"Bearer {auth_key}"
        }

    




# def request_location(auth_key:str, location):
#     service = "location.name"
#     headers = {
#         "Authorization": f"Bearer {auth_key}"
#     }
#     url = constants.RESOURCE + service

#     if DEBUG:
#         request = requests.Request('GET', url, headers=headers, params={"input": location})
#         prepared_request = request.prepare()
#         utils.dump_prepared_request(prepared_request)
#         # TODO read stored debug values
#         with open(os.path.join(os.getcwd(), r"requestData\dLocation.xml"), "r", encoding="UTF-8") as xml_file:
#             xml_elem = ElementTree.parse(xml_file)
#         xml_data = xml_elem.getroot()
#         for location in xml_data.findall("ns0:StopLocation",NS):
#             print(location.get("name"), location.get("name"))
#             products = [product.get('name') for product in location.findall("ns0:productAtStop", NS)]
#             print('\t', end='')
#             print(*products, sep='\n\t')
#             print()


#     else:
#         response: requests.Response = requests.get(url, headers=headers, params={"input": location})
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



