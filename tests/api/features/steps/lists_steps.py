import json
from multiprocessing import context
from jsonschema import validate
from behave import *
from main.trello.api.lists_manager import ListsManager
from main.utils.behave_helpers import fill_payload

manager = ListsManager()

@given('I created a board')
def step_impl(context):
    pass

@step('I created a list on the board with name "{list_name}"')
def step_impl(context, list_name):
    if not getattr(context, 'list'):
        context.status_code, context.list = manager.create_list(list_name, context.board["id"])

@step('I check the data is')
def step_impl(context):
    expected_json = fill_payload(context, payload={})
    for key, value in expected_json.items():
        assert value==context.response[key], \
        'expected value for {key} is {value},but actual is {context.response[key]}'
