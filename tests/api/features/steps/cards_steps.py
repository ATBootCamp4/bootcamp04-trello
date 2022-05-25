from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager

request_manager = RequestManager()


@step('the card is updated')
def step_impl(context):
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
        context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "

@step('verify the comment has been added')
def step_impl(context):
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
        context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.response['data'][key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "

class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
