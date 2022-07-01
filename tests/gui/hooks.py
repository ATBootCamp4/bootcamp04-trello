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


@fixture
def create_list(context, endpoint, list_name):
    context.request_manager = RequestManager()
    if context.board:
        _, context.list = context.request_manager.post_request(
            endpoint, payload={"name": list_name, "idBoard": context.board['id']})


@fixture
def delete_list(context, endpoint):
    context.request_manager = RequestManager()
    if context.board and context.list:
        put_endpoint = endpoint.replace('{id}', context.list['id'])
        status_code, response = context.request_manager.put_request(put_endpoint, payload={'closed': 'true'})
