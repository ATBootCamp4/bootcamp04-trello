from behave import given, when, then, step
from main.trello.api.checklists_manager import ChecklistsManager

manager = ChecklistsManager()

@given('I created a checklist on a card with id:"{card_id}"')
def step_impl(context, card_id):
    _, created_checklist = manager.create_checklist(card_id, "Behave checklist", "bottom")
    context.created_checklist = created_checklist

@when('I send a GET request to /cards/"{card_id}"/checklists')
def step_impl(context, card_id):
    status_code, checklists = manager.get_checklists(card_id)
    context.status_code = status_code
    context.checklists = checklists

@then('I receive a list with at least one checklist')
def step_impl(context):
    assert len(context.checklists) > 0, "Checklists length isn't greater than 0"

@step('the status code is 200')
def step_impl(context):
    assert context.status_code == 200, "Status code isn't 200"