import json

from behave import step

from back_test.api_bdd.steps.bdd_utils import (
    convert_object_to_json_schema,
    validate_with_datetime,
)


@step("the response code is {code:d}")
def check_response_code(context, code):
    response = context.response
    context.test.assertEqual(response.status_code, code)


@step('the response "{field}" is equal to')
def check_response_data(context, field):
    response = context.response
    expected_data = json.loads(context.text)
    expected_schema = convert_object_to_json_schema(expected_data)
    response_data = response.json()
    if field != "data":
        response_data = _get_data_helper(field, response_data)
    validate_with_datetime(expected_schema, response_data)


def _get_data_helper(field, data):
    """
    adds support nested objects using '.' access notation, e.g. 'data.getModules'
    """
    key = field.split(".", 1)
    if len(key) > 1:
        return _get_data_helper(key[1], data[key[0]])
    else:
        return data[key[0]]


@step('the response has the header "{header}" with value "{value}"')
def response_header(context, header, value):
    response_headers = context.response.headers
    context.test.assertIn(header, response_headers)
    context.test.assertEqual(response_headers.get(header), value)
