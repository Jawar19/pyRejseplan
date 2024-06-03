"""This module represents Rejseplanens multideparture board"""
from . import constants, utils
import logging

import requests
from xml.etree import ElementTree

class DepartureBoard():

    _logger = logging.getLogger(__name__)
    
    _header: dict
    _stop_ids: list
    _timeout: float = 10.0
    _useBus: bool = True
    _useTrain: bool = True
    _useMetro: bool = True


    def __init__(self, auth_key:str) -> None:
        self._logger.debug("__init__ called")
        self._construct_header(auth_key)

    @staticmethod
    def _request(service, headers, params, timeout):
        url = constants.RESOURCE + service
        try:
            response = requests.get(
                url,
                params,
                headers=headers,
                timeout=timeout
            )
        except requests.exceptions.RequestException as ex:
            # TODO Make custom exceptions
            pass
        if (response.status_code == requests.codes.ok):
            return response

    def update(self):
        params: dict = {}
        if len(self._stop_ids) < 1:
            raise ValueError("Need at least one id.")
        params["idList"] = self._stop_ids
        
        if self._useBus:
            params["useBus"] = self._useBus
        if self._useTrain:
            params["useTrain"] = self._useTrain
        if self._useMetro:
            params["useMetro"] = self._useMetro

        response = self._request(
            "multiDepartureBoard",
            self._header,
            params,
            self._timeout
            )
        return response

    def _construct_header(self, auth_key) -> None:
        self._header = {
            "Authorization": f"Bearer {auth_key}"
        }
    
    def add_stop_ids(self, *ids) -> None:
        pass

    def remove_stop_ids(self, *ids) -> None:
        pass

    def clear_stop_ids(self) -> None:
        self._stop_ids.clear()

    @property
    def timeout(self) -> float:
        return self._timeout
    
    @timeout.setter
    def timeout(self, value: float) -> None:
        if value < 0:
            raise ValueError("Timeout can not be negative number")
        elif value == 0:
            raise ValueError("Timeout can not be zero")
        
        self._timeout = value

    @property
    def useBus(self) -> bool:
        return self._useBus
    
    @useBus.setter
    def useBus(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"Value is of incorrect type {type(value)},"
                            " it should be of type bool")
        
        self._useBus = value
    
    @property
    def useTrain(self) -> bool:
        return self._useTrain
    
    @useTrain.setter
    def useTrain(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"Value is of incorrect type {type(value)},"
                            " it should be of type bool")
        
        self._useTrain = value
    
    @property
    def useMetro(self) -> bool:
        return self._useMetro
    
    @useMetro.setter
    def useMetro(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"Value is of incorrect type {type(value)},"
                            " it should be of type bool")
        
        self._useMetro = value