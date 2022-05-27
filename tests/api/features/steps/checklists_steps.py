from behave import then, step
from main.trello.api.checklists_manager import ChecklistsManager

checklist_manager = ChecklistsManager()


@step('I created a checklist on the card')
def step_impl(context):
    """This step will create a checklist on the card that's currently
    in the context, using a default name."""
    dflt_name = "Behave checklist"
    _, checklist = checklist_manager.create_checklist(context.card['id'], dflt_name)
    context.checklist = checklist


@step('I created a completed item on the checklist')
def step_impl(context):
    """This step will create a completed item on the checklist that's currently
    in the context, using a default name, and marking it as completed."""
    dflt_name = "Completed item"
    _, checkitem = checklist_manager.create_checkitem(context.checklist['id'], dflt_name, checked=True)
    context.checkitem = checkitem


@then('the checklist is created on the card')
def step_impl(context):
    """This step intends to verify that the checklist was created on the card."""
    status_code, response = checklist_manager.get_checklist(context.response['id'])
    assert status_code == 200, 'Checklist was not created'
    assert response['idCard'] == context.card['id'], 'Checklist was not created on the card'


@then('the checklist is updated')
def step_impl(context):
    """This step intends to verify that the checklist was updated."""
    _, response = checklist_manager.get_checklist(context.checklist['id'])
    assert response['name'] == context.payload['name'], 'Checklist was not updated'


@then('the checklist is deleted')
def step_impl(context):
    """This step intends to verify that the checklist was deleted."""
    status_code, response = checklist_manager.get_checklist(context.checklist['id'])
    assert status_code >= 400, f"Expected status code >= 400, got {status_code}"
    assert 'not found' in response.lower(), f"Expected error message 'not found' but received: \n '{response}'"


@then('the checklist item is created on the checklist')
def step_impl(context):
    """This step intends to verify that the checklist item was created on the checklist."""
    status_code, response = checklist_manager.get_checkitem(context.checklist['id'], context.response['id'])
    assert status_code == 200, 'Checklist item was not created'
    assert response['idChecklist'] == context.checklist['id'], 'Checklist item was not created on the checklist'


@then('the checklist item is updated')
def step_impl(context):
    """This step intends to verify that the checklist item was updated."""
    _, response = checklist_manager.get_checkitem(context.checklist['id'], context.checkitem['id'])
    assert response['name'] == context.payload['name'], f"Expected name '{context.payload['name']}' but got '{response['name']}'"
    assert response['state'] == context.payload['state'], f"Expected name '{context.payload['state']}' but got '{response['state']}'"


@then('the checklist item is deleted')
def step_impl(context):
    """This step intends to verify that the checklist item was deleted."""
    status_code, response = checklist_manager.get_checkitem(context.checklist['id'], context.checkitem['id'])
    assert status_code >= 400, f"Expected status code >= 400, got {status_code}"
    assert 'not found' in response.lower(), f"Expected error message 'not found' but received: \n '{response}'"
