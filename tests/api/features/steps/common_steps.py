from behave import then, step
from main.utils.behave_helpers import replace_ids, fill_payload, validate_schema
from main.utils.json_model import JsonModel
import re

@step('I send a "{method}" request to "{endpoint}"')
def step_impl(context, method, endpoint):
    """This step will send a request to the Trello API, using the manager that's
    currently in the context, and the method and endpoint that are passed in.
    The response and status code will be stored in the context."""
    if method == 'DELETE':
        context.deleted_item = getattr(context, re.findall(r'\{(.*?)\}', endpoint)[0])
    endpoint = replace_ids(context, endpoint)
    context.payload = fill_payload(context, payload={})
    context.status_code, context.response = context.request_manager.do_request(method, endpoint, context.payload)


@then('I receive a list with at least "{quantity:d}" "{item}"')
def step_impl(context, quantity, item):
    """This step will validate that the response is a list, and that it has at least
    the given number of elements."""
    assert len(context.response) >= quantity, f'No {item}s were found'


@then('I receive a response with the "{item}" "{attribute}"')
def step_impl(context, item, attribute):
    """This step will validate that the response contains the same attribute
    as an item that's currently in the context."""
    item_id = getattr(context, item)[attribute]
    assert context.response[attribute] == item_id, f'{item} id does not match'


@step('the status code is "{status_code:d}"')
def step_impl(context, status_code):
    """This step will validate that the status code is the one that was passed in."""
    assert context.status_code == status_code, f'it was expected {status_code} but it was received {context.status_code} '


@then('the response contains the message "{error}"')
def step_impl(context, error):
    """This step will validate that the response contains an error message."""
    if type(context.response) is dict:
        assert error in context.response, 'No error message was found'
    else:
        assert error in context.response.lower(), 'No error message was found'


@then('I receive a response with the "{schema_name}" schema')
def step_impl(context, schema_name):
    """This step will validate that the response matches the given schema."""
    validate_schema(context, schema_name)


@ step('The item is updated')
def step_impl(context):
    '''
        This method checks if a response item has been updated
        by comparing its objetc properties from the response
        to the input values in the request
    '''
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value = context.response[key]
        assert value == actual_value, f"Response Object Error: Expected: {value}, Actual: {actual_value}"


@ step('The item "{item_url}" is deleted')
def step_impl(context, item_url):
    '''
        This method checks if item has been deleted by
        making a GET request to its URL
    '''
    endpoint = replace_ids(context, item_url)
    status_code, _ = context.request_manager.do_request("GET", endpoint)
    assert status_code == 404, f"Status code 404 was expected but {status_code} was found"


@ step('The item "{item_url}" is created')
def step_impl(context, item_url):
    '''
        This method checks if item has been created by
        making a GET request to its URL
    '''
    endpoint = replace_ids(context, item_url)
    status_code, _ = context.request_manager.do_request("GET", endpoint)
    assert status_code == 200, f"Status code 200 was expected but {status_code} was found"


@step('I check the data is')
def step_impl(context):
    expected_json = fill_payload(context, payload={})
    for key, value in expected_json.items():
        assert value == context.response[key], f'expected value for {key} is {value}, but actual is {context.response[key]}'
