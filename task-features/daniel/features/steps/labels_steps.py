from behave import given,when,then,step
from main.trello.api.label_manager import LabelsManager
from jsonschema import validate
import json


label_manager=LabelsManager()
#SCENARIO I
# ID='62852469f333e5117e262c83'
# @given('the user does a GET request to /labels/id endpoint')
# def step_impl(context):
#     context.endpoint=ID
#     pass


# @when('the user sends the request')
# def step_impl(context):
#     status_code,body=label_manager.get_label(context.endpoint)
#     context.status_code=status_code
#     context.id=body['id']
#     context.response=body


# @then('verify the status code is 200')
# def step_impl(context):
#     assert context.status_code==200,f"it was expected status code 200 but was {context.status_code}"

# @step('that the given label exists')
# def step_impl(context):
#     assert context.id==ID

# @step('validate the schema')
# def step_impl(context):
#     json_schema='./main/schemas/label_schema.json'
#     with open (json_schema) as file_schema:
#         data=json.load(file_schema)
#     validate(context.response,data)




 # SCENARIO II
# @given('the user wants to create new "{color}" label named "{name}"')
# def step_impl(context, name,color):
#     context.name=name
#     context.color=color

# @when('the user sends a POST request with the data')
# def step_impl(context):
#     status_code,body=label_manager.create_label('QI9piQFl',context.name,context.color)
#     context.status_code=status_code
#     context.retrieved_id=body['id']


# @then('verify the status code is 200')
# def step_impl(context):
#     assert context.status_code==200,f"it was expected status code 200 but was {context.status_code}"

# @step('verify that the new label named "{name}" is "{color}"')
# def step_impl(context,name, color):
#     status_code,body=label_manager.get_label(context.retrieved_id)
#     assert body['id']==context.retrieved_id
#     assert body['name']==name 
#     assert body['color']==color 

# # SCENARIO III
# #ID_DELETE='62850da3acbdbe54297cf023'
# @given('the user wants to DELETE a label')
# def step_impl(context):
#     context.endpoint=ID_DELETE
#     pass

# @when('the user sends DELETE request')
# def step_impl(context):
#     status_code,body=label_manager.delete_label_board(context.endpoint)
#     context.status_code=status_code


# @then('verify the status code is "{code:d}"')
# def step_impl(context,code):
#     assert context.status_code==code,"it was expected status code 200 but was {context.status_code}"

# @step('verify that label dont exists anymore in board')
# def step_impl(context):
#     status_code,body=label_manager.get_labels('QI9piQFl')
#     exists=False
#     for i in body:
#         if ID_DELETE in i.values():
#             exists=True
#     assert exists==False

# #SCENARIO IV
# ID='628530d07c4dcd1b4ff267d0'
# @given('the user wants to change the data in a label')
# def step_impl(context):
#     context.id=ID
#     pass

# @when('the user sends PUT request with "{name}" and "{color}"')
# def step_impl(context,name,color):
#     status_code,body=label_manager.update_label(context.id,name,color)
#     print(status_code)
#     context.status_code=status_code
#     context.body=body


# @then('verify the status code is "{code:d}"')
# def step_impl(context, code):
#     assert context.status_code==code,f"it was expected status code 200 but was {context.status_code}"

# @step('verify that the label is named "{name}" and is "{color}"')
# def step_impl(context,name, color):
#     status_code,body=label_manager.get_label(context.id)
#     assert body['id']==context.id
#     assert body['name']==name
#     assert body['color']==color  

# #SCENARIO V    

# @given('the user wants to create a label')
# def step_impl(context):
#     model=JsonModel()
#     for row in context.table:
#         model.build_json(row['key'], row['value'])
#     status_code,body=label_manager.create_label(model.json_data['board'],
#             model.json_data['name'],
#             model.json_data['color'])
#     context.id=body['id']
#     context.old_name=body['name']
#     context.old_color=body['color']


# @when('the user modifies the label with')
# def step_impl(context):
#     model=JsonModel()
#     for row in context.table:
#         model.build_json(row['key'], row['value'])
#     status_code,body=label_manager.update_label(context.id, 
#                                 model.json_data['name'],
#                                 model.json_data['color'])
#     context.new_name=body['name']
#     context.new_color=body['color']
#     assert context.old_name != context.new_name
#     assert context.old_color != context.new_color

# @then('verifies the data to be correct')
# def step_impl(context):
#     status_code,body=label_manager.get_label(context.id)
#     assert body['id']==context.id
#     assert body['name']==context.new_name
#     assert body['color']==context.new_color 


#SCENARIO VI
@given('the user creates labels in a card with different "{names}" and "{colors}"')
def step_impl(context, names,colors):
    context.name=names
    context.color=colors


@when('the user do the request')
def step_impl(context):
    status_code,body=label_manager.create_label_card("628264cf49d65c88ae11443d",context.name,context.color)
    context.status_code=status_code



@then('verify the status code is "{http_response:d}"')
def step_impl(context,http_response):
    assert context.status_code==http_response,f"it was expected status code 200 but was {context.status_code}"




class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
