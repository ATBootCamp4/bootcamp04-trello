from behave import fixture
from main.core.rest.request_manager import RequestManager

def before_all(context):
    context.request_manager = RequestManager()
    _, context.board = context.request_manager.post_request('boards/', payload={'name': 'Behave board'})
    _, context.lists = context.request_manager.get_request(f"boards/{context.board['id']}/lists")
    context.list = context.lists[0]

def after_all(context):
    context.request_manager.delete_request('boards/' + context.board['id'])