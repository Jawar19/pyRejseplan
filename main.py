import logging
import os, sys, argparse
from xml.etree import ElementTree
import pickle as pkl
import json

from pyRejseplan import LocationHandler, DepartureBoard

DEBUG = False
JSON = False

log_lvl = logging.INFO

rootlogger:logging.Logger = logging.getLogger()
rootlogger.setLevel(log_lvl)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
rootlogger.addHandler(ch)

parser = argparse.ArgumentParser(description="Test script for testing location functionality for Rejseplanen API")
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')
parser.add_argument('-j', '--json', action='store_true', help='Enable JSON mode')

args = parser.parse_args()

if args.debug:
    rootlogger.info("DEBUG flag set")
    log_lvl = logging.DEBUG
    rootlogger.setLevel(log_lvl)
    ch.setLevel(log_lvl) 
    DEBUG = True

if args.json:
    rootlogger.info("JSON flag set")
    JSON = True

KEY = None
with open(os.path.join(os.getcwd(), "rejseplan.key"), encoding='utf-8') as keyfile:
    for line in keyfile.readlines():
        if line.startswith("KEY:"):
            KEY = line.strip("KEY:").strip()
if not KEY:
    print("Auth key not found")
    sys.exit(1)
rootlogger.info("Auth key found")

if args.debug:
    departure_board = DepartureBoard(KEY, r'requestData\mdbRoskildeSt.pkl', JSON)
else:
    departure_board = DepartureBoard(KEY, None, JSON)

departure_board._stop_ids = [8600617, 8600794]
response = departure_board.update()

if JSON:
    with open(os.path.join(os.getcwd(), r'requestData/mdbRoskildeSt.json'), 'w', encoding='utf-8') as file:
        file.write(json.dumps(response.json(), indent=2))
else:
    xmlroot: ElementTree.Element = ElementTree.fromstring(response.content)
    xmltree = ElementTree.ElementTree(xmlroot)
    ElementTree.indent(xmltree)
    with open(os.path.join(os.getcwd(), r'requestData/mdbRoskildeSt.xml'), 'wb') as file:
        xmltree.write(file, encoding='utf-8', xml_declaration=True)

with open(os.path.join(os.getcwd(), r'requestData/mdbRoskildeSt.pkl'), 'wb') as file:
    pkl.dump(response, file)
