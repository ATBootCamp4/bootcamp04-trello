import re
import json
from jsonschema import validate
from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager
from main.utils.common_globals import DEFAULT_BOARD, DEFAULT_GET_REQUESTS, DEFAULT_SCHEMAS
from tests.api.features.steps.json_model import JsonModel


request_manager = RequestManager()


@step('the user defines a "{http_method}" request to "{endpoint}"')
def step_impl(context, http_method, endpoint):
    context.endpoint = validate_endpoint(context, endpoint)
    context.http_method = http_method
    model = None
    if context.table:
        model = JsonModel()
        for row in context.table:
            model.build_json(row['Key'], row['Value'])
    context.model = model

@step('the user sends the request')
def step_impl(context):
    if context.model:
        status_code, api_response = request_manager.do_request(context.http_method, context.endpoint,
                                                               payload=context.model.json_data)
        #replacements = re.findall(r'(?:[^/]|//)+', endpoint) 
        str_list = context.endpoint.split('/')
        obj_name = str_list[-1] if '?' not in str_list[-1] else str_list[-2]
        setattr(context, obj_name, api_response)
    else:
        status_code, api_response = request_manager.do_request(context.http_method, context.endpoint)
    context.status_code = status_code
    context.api_response = api_response

@step('verify the status code is "{code:d}"')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"


@step('verify the new object contains the following info')
def step_impl(context):    
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.api_response[key]
        assert value in actual_value, f"Expected: {value}, Actual: {actual_value} "


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

def validate_endpoint(context, endpoint):
    replacements = re.findall(r'\{(.*?)\}', endpoint)
    
    for replacement in replacements:
        if hasattr(context, replacement):
            endpoint = endpoint.replace("{" + replacement + "}", getattr(context, replacement)['id'])
        else:
            _endpoint, default_name = DEFAULT_GET_REQUESTS.get(replacement)
            _, response = request_manager.do_request('GET', _endpoint, fields='name')
            _object = [obj for obj in response if default_name == obj['name']]
            endpoint = endpoint.replace("{" + replacement + "}", _object[0]['id'])
    return endpoint
