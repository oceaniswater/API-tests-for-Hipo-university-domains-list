import pytest
from requests import Response
from utils.ApiHipo import ApiHipo
from cerberus import Validator

"""
Verify response structure and content.  

In addition, check the following parameters:
– filter: ensure the response is filtered on the specified value. 
– sort: specify field on which to sort, test ascending and descending options. Ensure the response is sorted according to selected field and sort direction.
– skip: ensure the specified number of results from the start of the dataset is skipped
– limit: ensure dataset size is bounded by specified limit. 
– limit + skip: Test pagination

Check combinations of all optional fields (fields + sort + limit + skip) and verify expected response.  
"""

basic_headers = {'Content-Type': 'application/json'}
test_schema = schema = {
    "state-province": {'nullable': True, 'type': 'string'},
    "alpha_two_code": {'type': 'string'},
    "web_pages": {'type': 'list', 'schema': {'type': 'string'}},
    "country": {'type': 'string'},
    "name": {'type': 'string'},
    "domains": {'type': 'list', 'schema': {'type': 'string'}}
}



@pytest.mark.parametrize("skip", ["1", "100"])
def test_get_search_with_optional_parameters_filter(skip):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', skip=skip)
    validator = Validator(test_schema, require_all=True)
    entities = result.json()
    for entity in entities:
        is_valid = validator.validate(entity)
        assert is_valid is True, validator.errors


@pytest.mark.parametrize("sort", ["1", "100"])
def test_get_search_with_optional_parameters_sort(sort):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', sort=sort)
    validator = Validator(test_schema, require_all=True)
    entities = result.json()
    for entity in entities:
        is_valid = validator.validate(entity)
        assert is_valid is True, validator.errors


@pytest.mark.parametrize("limit", ["1", "100"])
def test_get_search_with_optional_parameters_limit(limit):
    result: Response = ApiHipo.get_search(headers=basic_headers, country='India', limit=limit)
    validator = Validator(test_schema, require_all=True)
    entities = result.json()
    for entity in entities:
        is_valid = validator.validate(entity)
        assert is_valid is True, validator.errors

@pytest.mark.parametrize("limit", ["1", "2"])
def test_get_search_check_limit(limit):
    result: Response = ApiHipo.get_search(headers=basic_headers, limit=limit)
    entities = result.json()
    assert len(entities) == limit

def test_get_search_check_pagination():
    result: Response = ApiHipo.get_search(headers=basic_headers)
    entitiesFull = result.json()
    result: Response = ApiHipo.get_search(headers=basic_headers, limit=2, skip=0)
    entitiesFirstPage = result.json()
    result: Response = ApiHipo.get_search(headers=basic_headers, limit=2, skip=2)
    entitiesSecondPage = result.json()
    assert entitiesFirstPage == entitiesFull[0:2]
    assert entitiesSecondPage == entitiesFull[2:4]