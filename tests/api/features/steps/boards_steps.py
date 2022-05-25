from logging import exception
from behave import given, when, then, step
from jsonschema import validate
from main.core.rest.request_manager import RequestManager

from main.trello.api.boards_manager import BoardsManager


request_manager = RequestManager()
boards_manager = BoardsManager()



@step('verify there is at least 1 member')
def step_impl(context):    
    assert len(context.response), f"cound't retrieve members from board "

@step('verify the new object contains the following info')
def step_impl(context):    
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step ('the user creates a board with "{field}" to be "{value}"')
def step_impl(context, field, value ): 
    context.model = JsonModel()
    context.model.build_json(field, value)

    name = context.model.json_data["name"] 
    status_code, response =  boards_manager.create_board(name )
    context.status_code = status_code
    context.response = response


@step ('the user deletes the board "{name}"')
def step_impl(context, name): 
    if (context.response["name"] == name):
        context.status_code, context.response = boards_manager.delete_board(context.response["id"])







class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
