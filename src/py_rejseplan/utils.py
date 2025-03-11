"""
This module provides utility functions for working with HTTP requests.
Functions:
    dump_prepared_request(prepared_request: PreparedRequest):
"""

from requests.models import PreparedRequest


def dump_prepared_request(prepared_request: PreparedRequest):
    """
    Dumps the details of a prepared HTTP request to the console.
    This function prints the request line, headers, and body of the given
    `PreparedRequest` object in a formatted manner.
    Args:
        prepared_request (PreparedRequest): The prepared HTTP request to be dumped.
    Returns:
        None
    """
    # Print the request line
    print(' REQUEST LINE '.center(50, '-'))
    print(f'{prepared_request.method} {prepared_request.url} HTTP/1.1')

    # Print the headers
    print(' HEADER '.center(50, '-'))
    for header, value in prepared_request.headers.items():
        print(f'{header}: {value}')

    # Print the body if it exists
    print(' BODY '.center(50, '-'))
    if prepared_request.body:
        print(f'\n{prepared_request.body}')
    print('-'.center(50, '-'))
