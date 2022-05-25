from behave import given,when,then,step
from main.trello.api.label_manager import LabelsManager
from jsonschema import validate
import json



label_manager=LabelsManager()

@step('I get the item info')
def step_impl(context):
    _,body=label_manager.get_label(context.response['id'])
    context.new_reponse=body

@then('I check data')
def step_impl(context):
   assert context.response['id']== context.new_reponse['id']
   assert context.response['name']== context.new_reponse['name']
   assert context.response['color']== context.new_reponse['color']


@when('the user sends PUT request with "{name}" and "{color}"')
def step_impl(context,name,color):
   _, context.new_response=label_manager.update_label(context.response['id'],name,color)
