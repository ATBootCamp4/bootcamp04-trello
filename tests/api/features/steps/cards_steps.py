import jsonschema
import json
import os
from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager
from main.utils.json_model import JsonModel
request_manager = RequestManager()


@step('the card is updated')
def step_impl(context):
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
        context.model = model
    for key, value in model.json_data.items():
        actual_value = context.response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step('response of type "{json_type}" is validated')
def step_impl(context, json_type):
    json_file = f'main/schemas/{json_type}.json'

    with open(json_file) as file:
        data = json.load(file)
        jsonschema.validate(data, context.response)


@step('verify the comment has been added')
def step_impl(context):
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
        context.model = model
    for key, value in model.json_data.items():
        actual_value = context.response['data'][key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step('I verify the card is deleted')
def step_impl(context):
    _, status_code = request_manager.do_request(
        'GET', 'cards/'+context.card['id'])
    assert status_code == 404, f"Status code 404 was expected but {status_code} was found"
