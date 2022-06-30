from behave import then, when, step

from main.trello.api.boards_manager import BoardsManager

boards_manager = BoardsManager()


@when('the user sends the boards name "{board_name}"')
def step_impl(context, board_name):
    context.home_page = context.page_factory.get_page("home")
    context.home_page.create_board(board_name)
    context.board_name = board_name


@then('the board "{board_name}" is displayed')
def step_impl(context, board_name):
    assert context.home_page.check_if_board_is_created(board_name), "Board was not created"


@step('the board appears in the API')
def step_impl(context):
    context.board = boards_manager.check_if_board_exists(context.board_name)
    assert context.board is not None, "Couldn't find board with given name in the API"


@step('the user goes to board "{board_name}"')
def step_impl(context, board_name):
    context.home_page = context.page_factory.get_page("home")
    context.home_page.go_to_board(board_name)
    context.board_name = board_name


@step('the user sends the new board name "{new_board_name}"')
def step_impl(context, new_board_name):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.update_title(context.board_name, new_board_name)
    context.board_name = new_board_name


@then('the board "{board_name}" is updated with name "{new_board_name}"')
def step_impl(context, board_name, new_board_name):
    assert context.cards_page.check_if_board_title_is_updated(context.board_name), "Could not update the board name"


@step('the user deletes the board')
def step_impl(context):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.delete_board()


@then('the board should not be displayed')
def step_impl(context):
    assert context.home_page.check_if_board_is_deleted(context.board_name), "Could not delete the board"


@step('the board should not appear in the API')
def step_impl(context):
    context.board = boards_manager.check_if_board_exists(context.board_name)
    assert context.board is None, "Board remains in the API"
