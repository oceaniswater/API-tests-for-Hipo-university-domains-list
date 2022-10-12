import pytest
from requests import Response
from utils.ApiHipo import ApiHipo

"""
Execute API call with valid required parameters

1. All requests should return 2XX HTTP status code

2. Returned status code is according to spec: 
– 200 OK for GET requests
– 201 for POST or PUT requests creating a new resource 
– 200, 202, or 204 for a DELETE operation and so o
"""

basic_headers = {'Content-Type': 'application/json'}


def test_get_search_all():
    result: Response = ApiHipo.get_search(headers=basic_headers)
    assert result.status_code == 200


def test_get_search_with_valid_name():
    result: Response = ApiHipo.get_search(headers=basic_headers, name='Marywood')
    assert result.status_code == 200


def test_get_search_with_valid_country():
    result: Response = ApiHipo.get_search(headers=basic_headers, country='United States')
    assert result.status_code == 200


def test_get_search_with_valid_name_and_country():
    result: Response = ApiHipo.get_search(headers=basic_headers, name='Marywood', country='United States')
    assert result.status_code == 200

