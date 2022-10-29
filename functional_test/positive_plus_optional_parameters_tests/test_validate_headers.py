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
# for example:
expected_response_headers = ['Date', 'Content-Type', 'Content-Length', 'Connection']


def test_get_search_check_expected_headers():
    result: Response = ApiHipo.get_search(headers=basic_headers, name='Marywood', country='United States', skip=10)
    for header in result.headers.keys():
        assert header in expected_response_headers, f'unexpected header: {header}'


def test_get_search_check_imortant_headers():
    result: Response = ApiHipo.get_search(headers=basic_headers, name='Marywood', country='United States', limit=1)
    assert 'application/json' == result.headers['Content-Type'], 'wrong header value'
    assert 'close' == result.headers['Connection'], 'wrong header value'
