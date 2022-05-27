from behave import when, then, step
from main.utils.behave_helpers import replace_ids, fill_payload, validate_schema
from main.utils.json_model import JsonModel


@step('I send a "{method}" request to "{endpoint}"')
def step_impl(context, method, endpoint):
    endpoint = replace_ids(context, endpoint)
    context.payload = fill_payload(context, payload={})
    context.status_code, context.response = context.request_manager.do_request(
        method, endpoint, context.payload)


@then('I receive a list with at least "{quantity:d}" "{item}"')
def step_impl(context, quantity, item):
    assert len(context.response) >= quantity, f'No {item}s were found'


@then('I receive a response with the "{item}" id')
def step_impl(context, item):
    item_id = getattr(context, item)['id']
    assert context.response['id'] == item_id, f'{item} id does not match'


@step('the status code is "{status_code:d}"')
def step_impl(context, status_code):
    assert context.status_code == status_code, f'it was expected {status_code} but it was received {context.status_code} '



@ then('I receive a response with the "{schema_name}" schema')
def step_impl(context, schema_name):
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