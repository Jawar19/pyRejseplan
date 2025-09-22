import logging
import os
import sys
import argparse

# from py_rejseplan.locationhandler import LocationHandler
from py_rejseplan.api.departures import DepartureBoard

DEBUG = False

log_lvl = logging.INFO

rootlogger: logging.Logger = logging.getLogger()
rootlogger.setLevel(log_lvl)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
rootlogger.addHandler(ch)

parser = argparse.ArgumentParser(
    description='Test script for testing location functionality for Rejseplanen API'
)
parser.add_argument('-d', '--debug', action='store_true', help='Enable debug mode')

args = parser.parse_args()

if args.debug:
    rootlogger.info('DEBUG flag set')
    log_lvl = logging.DEBUG
    rootlogger.setLevel(log_lvl)
    ch.setLevel(log_lvl)
    DEBUG = True

KEY = None
with open(os.path.join(os.getcwd(), 'rejseplan.key'), encoding='utf-8') as keyfile:
    for line in keyfile.readlines():
        if line.startswith('KEY:'):
            KEY = line.strip('KEY:').strip()
if not KEY:
    print('Auth key not found')
    sys.exit(1)
rootlogger.info('Auth key found')

# if args.debug:
#     departure_board = DepartureBoard(KEY, r'requestData\mdbRoskildeSt.pkl')
# else:
#     departure_board = DepartureBoard(KEY)

# departure_board._stop_ids = [8600617, 8600794]

# departure_board.get_departures()
