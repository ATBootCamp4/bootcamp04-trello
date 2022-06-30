from behave import step, then

from main.trello.api.lists_manager import ListsManager

lists_manager = ListsManager()


@step('the user sends the list name "{list_name}"')
def step_impl(context, list_name):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.create_list(list_name)
    context.list_name = list_name


@then('the list is displayed')
def step_impl(context):
    assert context.cards_page.check_if_list_is_created(context.list_name), "Could not create the list"


@step('the list appears in the API')
def step_impl(context):
    context.list = lists_manager.does_list_exists(
        context.list_name, context.board['id'])
    assert context.list, "Could not create list, does not appear in API"


@step('the user updates the list name "{list_name}" to "{new_list_name}"')
def step_impl(context, list_name, new_list_name):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.update_list_title(list_name, new_list_name)
    context.list_name = new_list_name


@step('the user deletes the list "{list_name}"')
def step_impl(context, list_name):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.delete_list(list_name)
    context.list_name = list_name


@then('the list should not be displayed')
def step_impl(context):
    assert not context.cards_page.check_if_list_is_created(context.list_name), "Could not delete the list"


@step('the list should not appear in the API')
def step_impl(context):
    context.list_deleted = lists_manager.does_list_exists(
        context.list_name, context.board['id'])
    assert context.list_deleted is None, "Could not delete list, still appearing in API"
