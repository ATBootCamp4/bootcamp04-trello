from behave import given,when,then,step
from main.trello.api.label_manager import LabelsManager
ID='62852469f333e5117e262c83'
label_manager=LabelsManager()

@given('the user does a GET request to /labels/id endpoint')
def step_impl(context):
    context.endpoint=ID
    pass


@when('the user sends the request')
def step_impl(context):
    status_code,body=label_manager.get_label(context.endpoint)
    context.status_code=status_code
    context.id=body['id']


@then('verify the status code is 200')
def step_impl(context):
    assert context.status_code==200,"it was expected status code 200 but was {context.status_code}"

@step('that the given label exists')
def step_impl(context):
    assert context.id==ID
