import json
from jsonschema import validate
from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager
from main.utils.common_globals import DEFAULT_SCHEMAS
from tests.api.features.steps.json_model import JsonModel


request_manager = RequestManager()
BOARD_ID = '6281405050ec165192c2f521'

@given('the user defines a "{http_method}" request to "{endpoint}"')
def step_impl(context, http_method, endpoint):
    context.endpoint = endpoint
    context.http_method = http_method
    model = None
    if context.table:
        model = JsonModel()
        for row in context.table:
            model.build_json(row['Key'], row['Value'])
    context.model = model
    

@when('the user sends the request')
def step_impl(context):
    if context.model:
        status_code, api_response = request_manager.do_request(context.http_method, context.endpoint,
                                                              payload=context.model.json_data)
    else:
        status_code, api_response = request_manager.do_request(context.http_method, context.endpoint)
    context.status_code = status_code
    context.api_response = api_response

@then('verify the status code is "{code:d}"')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"

@step('verify there is at least 1 member')
def step_impl(context):    
    assert len(context.api_response), f"cound't retrieve members from board {BOARD_ID}"


@step('verify the new object contains the following info')
def step_impl(context):    
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.api_response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step('the user sets "{field}" to be "{value}"')
def step_impl(context, field, value):
    if not context.model:
        context.model = JsonModel()

    context.model.build_json(field, value)

@step('validate the schema of "{endpoint}"')
def step_impl(context, endpoint):

    json_schema = DEFAULT_SCHEMAS.get(endpoint)

    with open(json_schema) as file_schema:
        data = json.load(file_schema)
    
    validate(context.api_response, data)