import pytest
from requests import Response
from utils.ApiHipo import ApiHipo

"""
Execute API call with valid required parameters

Verify that HTTP headers are as expected, including content-type, connection, cache-control, expires,
access-control-allow-origin, keep-alive, HSTS, and other standard header fields – according to spec.

Verify that information is NOT leaked via headers (e.g. X-Powered-By header is not sent to user). 
"""

basic_headers = {'Content-Type': 'application/json'}
expected_response_headers = {'Date': '', 'Content-Type': 'application/json', 'Content-Length': '180', 'Connection': 'close'}


def test_get_search_check_expected_headers():
    result: Response = ApiHipo.get_search(headers=basic_headers, name='Marywood', country='United States')
    for header in result.headers.keys():
        assert header in expected_response_headers.keys(), f'Unexpected header: {header}'

