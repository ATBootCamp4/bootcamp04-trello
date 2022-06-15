from behave import step
from main.core.rest.request_manager import RequestManager
from main.trello.api.boards_manager import BoardsManager
from main.utils.json_model import JsonModel

request_manager = RequestManager()
boards_manager = BoardsManager()


@step('verify the new object contains the following info')
def step_impl(context):
    """
    Construct a Json with the table of the .features and compare it with the
    response from the API
    """
    model = JsonModel()
    for row in context.table:
        model.build_json(row['Key'], row['Value'])
    context.model = model
    for key, value in model.json_data.items():
        actual_value = context.response[key]
        assert value == actual_value, f"Expected: {value}, Actual: {actual_value} "


@step('the user creates a board with "{field}" to be "{value}"')
def step_impl(context, field, value):
    """
    Construct a Json with the table of the .features in order to send that as
    the payload and then creates a board using the payload

    :param field:   String  string with the name of the field that will be filled when creating the board
    :param value:   String  string with the infomation that would be placed in the field
    """
    context.model = JsonModel()
    context.model.build_json(field, value)
    name = context.model.json_data["name"]
    status_code, response = boards_manager.create_board(name)
    context.status_code = status_code
    context.response = response


@step('the user deletes the board "{name}"')
def step_impl(context, name):
    """
    recives a name of a board and compares it with the board in the context,
    if they are the same, it uses the board manager to delete the board

    :param name:   String  string with the name of the board that will be deleted
    """
    if (context.response["name"] == name):
        context.status_code, _ = boards_manager.delete_board(context.response["id"])

    assert context.status_code == 200, f'could not delete board with id {context.response["id"]}'


@step('A board is created')
def step_impl(context):
    """
    this function verifies if a board exists, if it doesn't exist, it creates one
    """
    if not context.board:
        _, context.board = context.request_manager.post_request('boards/', payload={'name': 'Behave board'})
