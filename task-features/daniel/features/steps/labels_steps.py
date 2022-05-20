from behave import given,when,then,step
from main.trello.api.label_manager import LabelsManager


label_manager=LabelsManager()

@given('the user wants to create a label')
def step_impl(context):
    model=JsonModel()
    for row in context.table:
        model.build_json(row['key'], row['value'])
    status_code,body=label_manager.create_label(model.json_data['board'],
            model.json_data['name'],
            model.json_data['color'])
    context.id=body['id']
    context.old_name=body['name']
    context.old_color=body['color']


@when('the user modifies the label with')
def step_impl(context):
    model=JsonModel()
    for row in context.table:
        model.build_json(row['key'], row['value'])
    status_code,body=label_manager.update_label(context.id, 
                                model.json_data['name'],
                                model.json_data['color'])
    context.new_name=body['name']
    context.new_color=body['color']
    assert context.old_name != context.new_name
    assert context.old_color != context.new_color

@then('verifies the data to be correct')
def step_impl(context):
    status_code,body=label_manager.get_label(context.id)
    assert body['id']==context.id
    assert body['name']==context.new_name
    assert body['color']==context.new_color 



class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
