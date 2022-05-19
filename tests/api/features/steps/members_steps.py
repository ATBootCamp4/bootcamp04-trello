from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager


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


class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
