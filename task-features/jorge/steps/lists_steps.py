from behave import *
from main.trello.api.lists_manager import ListsManager

manager = ListsManager()

@given('I send a GET request to /boards/"{id_list}"/lists')
def step_impl(context, id_list):
    status_code, lists = manager.get_board_list_is_on(id_list)
    context.status_code = status_code
    context.lists = lists

@when('I receive a response with at least one list')
def step_impl(context):
    assert len(context.lists) > 0, f"{context.lists} was received but it was expected at least one list"

@then('the status code is "{code:d}"')
def step_impl(context, code):
    assert context.status_code == code, f"Code {context.status_code} but it was expected {code}"

###################################################

@given('I send a GET request to lists/"{id_list}"')
def step_impl(context, id_list):
    status_code, one_list = manager.get_list(id_list)
    context.status_code = status_code
    context.list = one_list

@when('I receive a response with id: "{id_list}"')
def step_impl(context, id_list):
    assert context.list['id'] == id_list, f"{context.list['id']} was received but it was expected {id_list}"

@then('status code is "{code:d}"')
def step_impl(context, code):
    assert context.status_code == code, f"Code {context.status_code} but it was expected {code}"

###################################################