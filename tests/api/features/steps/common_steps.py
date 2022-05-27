from behave import given, when, then, step
from main.utils.behave_helpers import replace_ids, fill_payload, validate_schema


@given('I created a new card')
def step_impl(context):
    _, context.card = context.request_manager.post_request(
        'cards', payload={'name': 'Behave card', 'idList': context.list['id']})


@when('I send a "{method}" request to "{endpoint}"')
def step_impl(context, method, endpoint):
    """This step will send a request to the Trello API, using the manager that's
    currently in the context, and the method and endpoint that are passed in.
    The response and status code will be stored in the context."""
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
