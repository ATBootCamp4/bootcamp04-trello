from behave import step
from main.trello.api.lists_manager import ListsManager


manager = ListsManager()


@step('I created a list on the board with name "{list_name}"')
def step_impl(context, list_name):
    if not getattr(context, 'list'):
        context.status_code, context.list = manager.create_list(list_name, context.board["id"])
