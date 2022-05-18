from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager


request_manager = RequestManager()
BOARD_ID = '6281405050ec165192c2f521'

@given('the user defines a GET request to /boards/id/members')
def step_impl(context):
    context.endpoint = f'/boards/{BOARD_ID}/members'
    

@when('the user sends the request')
def step_impl(context):
    status_code, member_list = request_manager.get_request(context.endpoint)
    context.status_code = status_code
    context.member_list = member_list

@then('verify the status code is 200')
def step_impl(context):
    assert context.status_code == 200, f"It was expected status code 200 but was {context.status_code}"

@step('verify there is at least 1 member')
def step_impl(context):
    assert bool(context.member_list), f"cound't retrieve members from board {BOARD_ID}"