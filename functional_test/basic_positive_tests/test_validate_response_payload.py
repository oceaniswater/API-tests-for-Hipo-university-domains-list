import pytest
from cerberus import Validator
from requests import Response
from utils.ApiHipo import ApiHipo

"""
Execute API call with valid required parameters

1. Response is a well-formed JSON object

2. Response structure is according to data model (schema validation: field names and field types are as expected, 
including nested objects; field values are as expected; non-nullable fields are not null, etc.) 

PS: I have reached the goal using cerberus 
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


def test_get_search_validate_response():
    result: Response = ApiHipo.get_search(headers=basic_headers)
    validator = Validator(test_schema, require_all=True)
    entities = result.json()
    for entity in entities:
        is_valid = validator.validate(entity)
        assert is_valid is True, validator.errors
