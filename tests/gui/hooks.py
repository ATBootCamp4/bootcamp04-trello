from behave import fixture

from main.core.rest.request_manager import RequestManager


@fixture
def create_board(context, endpoint, board_name):
    context.request_manager = RequestManager()
    _, context.board = context.request_manager.post_request(endpoint, payload={'name': board_name})


@fixture
def delete_board(context, endpoint):
    context.request_manager = RequestManager()
    if context.board:
        context.request_manager.delete_request(endpoint + context.board['id'])
