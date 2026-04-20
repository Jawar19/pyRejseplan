"""Async tests for departures API client using aiohttp transport."""

import pytest
from unittest.mock import AsyncMock

from py_rejseplan.api.base import AsyncHTTPResponse
from py_rejseplan.api.departures import DeparturesAPIClient
from py_rejseplan.dataclasses.departure_board import DepartureBoard
from py_rejseplan.exceptions import APIError, ConnectionError, HTTPError


@pytest.mark.asyncio
async def test_get_departures_async_empty_stop_ids_raises_value_error():
    """Validate async API input guard for empty stop IDs."""
    client = DeparturesAPIClient('test_key')

    with pytest.raises(ValueError) as exc_info:
        await client.get_departures_async([])

    assert 'Stop IDs must be provided' in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_departures_async_success(monkeypatch, sample_valid_xml):
    """Ensure async departures call returns parsed board and response metadata."""
    client = DeparturesAPIClient('test_key')

    expected = AsyncHTTPResponse(
        status_code=200,
        headers={'Content-Type': 'application/xml'},
        content=sample_valid_xml.encode('utf-8'),
    )
    mock_get_async = AsyncMock(return_value=expected)
    monkeypatch.setattr(client, '_get_async', mock_get_async)

    board, response = await client.get_departures_async([8600617])

    assert isinstance(board, DepartureBoard)
    assert response.status_code == 200
    assert response is expected
    mock_get_async.assert_awaited_once_with(
        'multiDepartureBoard',
        params={
            'idList': '8600617',
            'maxResults': -1,
            'useBus': True,
            'useTrain': True,
            'useMetro': True,
        },
    )


@pytest.mark.asyncio
async def test_validate_auth_key_async_valid(monkeypatch):
    """Async auth validation should return True on successful request."""
    client = DeparturesAPIClient('test_key')
    monkeypatch.setattr(client, '_get_async', AsyncMock(return_value=AsyncHTTPResponse(200, {}, b'')))

    assert await client.validate_auth_key_async() is True


@pytest.mark.asyncio
async def test_validate_auth_key_async_invalid_key(monkeypatch):
    """Async auth validation should return False when API returns 401."""
    client = DeparturesAPIClient('test_key')
    monkeypatch.setattr(
        client,
        '_get_async',
        AsyncMock(side_effect=HTTPError('HTTP 401: unauthorized', status_code=401)),
    )

    assert await client.validate_auth_key_async() is False


@pytest.mark.asyncio
async def test_validate_auth_key_async_connection_error(monkeypatch):
    """Async auth validation should return False on connection errors."""
    client = DeparturesAPIClient('test_key')
    monkeypatch.setattr(
        client,
        '_get_async',
        AsyncMock(side_effect=ConnectionError('connection failed')),
    )

    assert await client.validate_auth_key_async() is False


@pytest.mark.asyncio
async def test_validate_auth_key_async_api_error(monkeypatch):
    """Async auth validation should return False on generic API errors."""
    client = DeparturesAPIClient('test_key')
    monkeypatch.setattr(
        client,
        '_get_async',
        AsyncMock(side_effect=APIError('request failed')),
    )

    assert await client.validate_auth_key_async() is False
