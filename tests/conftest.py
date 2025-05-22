"""Conftest document containing setup of fixtures for pytest"""

import os
import pytest


@pytest.fixture(name='key')
def fixture_key():
    """Reading authkey from auth file in root

    Returns:
        auth key: str
    """
    _key = None
    try:
        with open(
            os.path.join(os.getcwd(), 'rejseplan.key'), encoding='utf-8'
        ) as keyfile:
            for line in keyfile.readlines():
                if line.startswith('KEY:'):
                    _key = line.strip('KEY:').strip()
    except FileNotFoundError as err:
        print(f'{err.filename} not found, using dummy key')
        _key = 'DUMMY_KEY'
    if not _key:
        print('Auth key not found, using dummy')
        _key = 'DUMMY_KEY'
    return _key
