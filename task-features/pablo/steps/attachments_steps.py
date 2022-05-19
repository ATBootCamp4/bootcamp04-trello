from behave import given, when, then, step
from main.trello.api.attachments_manager import AttachmentsManager

manager = AttachmentsManager()

@given("there is a card with attachments")
def step_impl(context):
    context.card_id = "6281250ff6f1e04b7edd712c"

@when("I request to GET all attachments from that card")
def step_impl(context):
    status_code, attachments = manager.get_all_attachments(context.card_id)
    context.status_code = status_code
    context.attachments = attachments

@then("I receive a list that contains at least one attachment")
def step_impl(context):
    assert len(context.attachments) > 0, "Attachments length isn't greater than 0"

@step("the status code is 200")
def step_impl(context):
    assert context.status_code == 200, "Status code isn't 200"