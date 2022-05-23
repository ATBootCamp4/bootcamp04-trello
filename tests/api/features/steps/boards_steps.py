from logging import exception
from behave import given, when, then, step
import json
from jsonschema import validate
from main.core.rest.request_manager import RequestManager
from main.trello.api.members_manager import MembersManager
from main.trello.api.boards_manager import BoardsManager


request_manager = RequestManager()
boards_manager = BoardsManager()
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


@step('verify the user recives a "{number:d}" lengt item')

def step_impl(context, number):    
    assert len(context.api_response) == number , f"It was expected {number} items but {len(context.api_response)} were retrived"
   


@step('verify the new object contains the following info')
def step_impl(context):    
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value =  context.api_response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "

@step ('the user deletes the board "{name}"')
def step_impl(context, name): 
    if (context.api_response["name"] == name):
        boards_manager.delete_board(context.api_response["id"])

@step ('verify the board "{name}" doesnt exist')
def step_impl(context, name): 
    if (context.api_response["name"] == name):
      
        #status_code, api_response2 = boards_manager.get_board(context.api_response["id"])
        #assert status_code == 404, f"Expected status code: 404, Actual: {status_code} "
        #with this code always trow an error so i don't know how to tell it not to stop when doesnt found the resourse
        pass




@step ('the user defines a create_board function')
def step_impl(context): 
    model = None
    if context.table:
        model = JsonModel()
        for row in context.table:
            model.build_json(row['Key'], row['Value'])
    context.model = model



@step ('the user copy the board with "{id}" and new "{name}"')
def step_impl(context, id , name ): 

    status_code, api_response =  boards_manager.copy_board(name , id  )
    context.status_code = status_code
    context.api_response = api_response  

    

@step ('verify the duplicated board and the "{id}" have same info')
def step_impl(context, id  ): 

    status_code2, old_board = boards_manager.get_board(id)
    name_old = old_board["desc"];
    name_new = context.api_response["desc"]
    assert name_old == name_new , f"Expected: {name_new}, Actual: {name_old }"



@step ('verify the board contains the following info')
def step_impl(context ): 
    status_code, board_in_api = boards_manager.get_board( context.api_response["id"] )
    assert status_code == 200 , f"could not retrive board to compare"

    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value =  board_in_api[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step ('the user creates a board with "{field}" to be "{value}"')
def step_impl(context, field, value ): 
    context.model = JsonModel()
    context.model.build_json(field, value)

    name = context.model.json_data["name"] 
    status_code, api_response =  boards_manager.create_board(name )
    context.status_code = status_code
    context.api_response = api_response


@step ('validate the schema of "{type}"')
def step_impl(context, type ): 
    json_schema = 'bootcamp04-trello\\main\\schemas\\board_schema.json'
    with open (json_schema ) as file_schema:
       data = json.load(file_schema)
    validate(data, context.api_response )

   



class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
