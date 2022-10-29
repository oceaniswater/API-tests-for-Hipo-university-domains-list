import pytest
from requests import Response
from utils.ApiHipo import ApiHipo

"""
Execute API call with valid required parameters AND valid optional parameters

Run same tests as in #1, this time including the endpoint’s optional parameters (e.g., filter, sort, limit, skip, etc.)
"""

basic_headers = {'Content-Type': 'application/json'}


@pytest.mark.parametrize("skip", ["1", "100"])
def test_get_search_with_optional_parameters_filter(skip):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', offset=skip)
    assert result.status_code == 200


@pytest.mark.parametrize("sort", ["1", "100"])
def test_get_search_with_optional_parameters_sort(sort):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', sort=sort)
    assert result.status_code == 200


@pytest.mark.parametrize("limit", ["1", "100"])
def test_get_search_with_optional_parameters_limit(limit):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', limit=limit)
    assert result.status_code == 200

