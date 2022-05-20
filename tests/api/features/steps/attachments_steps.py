from behave import given, when, then, step
from requests import request 
from main.trello.api.attachments_manager import AttachmentsManager
from main.core.rest.request_manager import RequestManager

request_manager = RequestManager()
attachments_manager = AttachmentsManager()

@step('the card has an attachment')
def step_impl(context):
    _, attachment = attachments_manager.create_attachment_from_url("https://source.unsplash.com/user/c_v_r", context.card['id'], 'New attachment')
    context.attachment = attachment

@then('I receive a list with at least one attachment')
def step_impl(context):
    assert len(context.response) > 0, 'No attachments were found'

@then('the attachment is created on the card')
def step_impl(context):
    status_code, response = attachments_manager.get_attachment(context.card['id'], context.response['id'])
    assert status_code == 200, 'Attachment was not created'
    assert response['name'] == context.payload['name'], 'Attachment was not created on the card'