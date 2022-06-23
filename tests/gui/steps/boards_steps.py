from behave import then, when, step
from main.trello.gui.page_objects.cards_page import CardsPage

from main.trello.gui.page_objects.home_page import HomePage


@when('the user sends the boards name "{board_name}"')
def step_impl(context, board_name):
    context.home_page = HomePage(context.driver)
    context.home_page.create_board(board_name)
    context.board_name = board_name


@then('the board is created')
def step_impl(context):
    assert context.home_page.check_if_board_is_created(context.board_name), "Board was not created"


@when('the user goes to board "{board_name}"')
def step_impl(context, board_name):
    context.home_page = HomePage(context.driver)
    context.home_page.go_to_board(board_name)
    context.board_name = board_name


@step('the user sends the new board name "{new_board_name}"')
def step_impl(context, new_board_name):
    context.cards_page = CardsPage(context.driver)
    context.cards_page.update_title(context.board_name, new_board_name)
    context.new_board_name = new_board_name


@then('the board is updated')
def step_impl(context):
    assert context.cards_page.check_if_board_title_is_updated(context.new_board_name), "Could not update the board name"


@step('the user deletes the board')
def step_impl(context):
    context.cards_page = CardsPage(context.driver)
    context.cards_page.delete_board()


@then('the board should not be displayed')
def step_impl(context):

    assert context.home_page.check_if_board_is_deleted(context.board_name), "Could not delete the board"
