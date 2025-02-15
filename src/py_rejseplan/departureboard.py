"""This module represents Rejseplanens multideparture board"""
import logging
import pickle as pkl
from xml.etree import ElementTree

import requests

from py_rejseplan import constants
from py_rejseplan.dataclasses import departure

_logger = logging.getLogger(__name__)

class DepartureBoard:
    """Multidepartureboard wrapping class. latest request is stored in the
    class and translated into python dataclasses representing the data recieved
    from Rejseplanen API.
    """

    _sim: bool = False
    _response: requests.Response = None
    _header: dict
    _stop_ids: list = []
    _timeout: float = 10.0
    _use_bus: bool = True
    _use_train: bool = True
    _use_metro: bool = True

    def __init__(self, auth_key: str, filepath:str = None) -> None:
        """Initialize the departure board wrapper
        if filepath is provided the class will load the simulation data from

        Arguments:
            auth_key -- Private key for API requests

        Keyword Arguments:
            filepath -- path to simulation data (default: {None})
        """
        _logger.debug("initializing...")
        self._construct_header(auth_key)

        if filepath:
            _logger.warning("Simulation data loaded from path %s", filepath)
            with open(filepath, "rb") as pkl_file:
                self._response = pkl.load(pkl_file)
                self._sim = True

    @staticmethod
    def _request(service, headers, params, timeout):
        """Request function for the Rejseplanen API"""
        url = constants.RESOURCE + service
        try:
            response = requests.get(url, params, headers=headers, timeout=timeout)
        except requests.exceptions.RequestException as ex:
            print(ex)
            # NOTE Make custom exceptions
        if response.status_code == requests.codes["OK"]:
            return response
        return None

    def update(self) -> requests.Response:
        """Update multideparture board data

        Raises:
            ValueError: If id's are less than 1

        Returns:
            Valid XML response according to rejseplanen API
        """
        if self._sim:
            return self._response

        params: dict = {}
        if len(self._stop_ids) < 1:
            raise ValueError("Need at least one id.")
        params["idList"] = self._stop_ids

        if self._use_bus:
            params["useBus"] = self._use_bus
        if self._use_train:
            params["useTrain"] = self._use_train
        if self._use_metro:
            params["useMetro"] = self._use_metro

        self._response = self._request(
            "multiDepartureBoard", self._header, params, self._timeout
        )
        return self._response

    def get_departures(self):
        """Updates the internal list of departures from the ID's provided to
        the class.
        """
        response = self.update()
        xmlroot: ElementTree.Element = ElementTree.fromstring(response.text)
        namespace = "{http://hacon.de/hafas/proxy/hafas-proxy}"

        departures = xmlroot.findall(f".//{namespace}Departure")
        result = []
        for i, depart in enumerate(departures):
            _logger.debug("Departure %4d --> %15s @ %10s ==> %15s [%s]",
                          i, depart.attrib.get("name"), depart.attrib.get("time"),
                          depart.attrib.get("direction"), depart.attrib.get("prognosisType"))
            result.append(departure.parse_departure(depart.attrib))

        # Need to make a list of departure objects and return them.

        # iterate trough the response and create a list of departures, this
        # could be provides for later use as a generator or just returned as
        # a list.
        return result

    def _construct_header(self, auth_key) -> None:
        """Constructs the header for the API requests
        This is embedding the auth_key in the header"""
        self._header = {"Authorization": f"Bearer {auth_key}"}

    def add_stop_ids(self, ids:list) -> None:
        """Add stop ids to the internal list of stop ids
        """
        seen = set(self._stop_ids)
        # Only add elements that are not already in the set
        self._stop_ids.extend(x for x in ids if x not in seen and not seen.add(x))

    def remove_stop_ids(self, ids:list) -> None:
        """Remove the ids listed in the input list

        Arguments:
            ids -- _description_
        """
        to_remove = set(ids)
        # Filter out elements that are in the to_remove set
        self._stop_ids = [x for x in self._stop_ids if x not in to_remove]

    def clear_stop_ids(self) -> None:
        """Clears the class' list of stop id's
        """
        self._stop_ids.clear()

    @property
    def stop_ids(self) -> list[int]:
        """returns list of stopids stored in class

        Returns:
            list
        """
        return self._stop_ids

    @property
    def timeout(self) -> float:
        """timeout property in seconds

        Returns:
            float [s]
        """
        return self._timeout

    @timeout.setter
    def timeout(self, value: float) -> None:
        """Timeout property in seconds

        Arguments:
            value -- input value in seconds

        Raises:
            ValueError: negative value
            ValueError: non-zero value
        """
        if value < 0:
            raise ValueError("Timeout can not be negative number")
        if value == 0:
            raise ValueError("Timeout can not be zero")

        self._timeout = value

    @property
    def use_bus(self) -> bool:
        """Use bus property 

        Returns:
            bool
        """
        return self._use_bus

    @use_bus.setter
    def use_bus(self, value: bool) -> None:
        """Use bus property

        Arguments:
            value -- bool

        Raises:
            TypeError: If value not bool
        """
        if not isinstance(value, bool):
            raise TypeError(
                f"Value is of incorrect type {type(value)},"
                " it should be of type bool"
            )

        self._use_bus = value

    @property
    def use_train(self) -> bool:
        """Use train property 

        Returns:
            bool
        """
        return self._use_train

    @use_train.setter
    def use_train(self, value: bool) -> None:
        """Use train property

        Arguments:
            value -- bool

        Raises:
            TypeError: If value not bool
        """
        if not isinstance(value, bool):
            raise TypeError(
                f"Value is of incorrect type {type(value)},"
                " it should be of type bool"
            )

        self._use_train = value

    @property
    def use_metro(self) -> bool:
        """Use metro property 

        Returns:
            bool
        """
        return self._use_metro

    @use_metro.setter
    def use_metro(self, value: bool) -> None:
        """Use metro property

        Arguments:
            value -- bool

        Raises:
            TypeError: If value not bool
        """
        if not isinstance(value, bool):
            raise TypeError(
                f"Value is of incorrect type {type(value)},"
                " it should be of type bool"
            )

        self._use_metro = value
