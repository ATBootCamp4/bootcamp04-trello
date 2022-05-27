from behave import then, step
from main.trello.api.attachments_manager import AttachmentsManager

attachments_manager = AttachmentsManager()


@step('I created an attachment on the card')
def step_impl(context):
    dflt_attachment = "https://source.unsplash.com/user/c_v_r"
    dflt_name = "Behave attachment"
    _, context.attachment = attachments_manager.create_attachment_from_url(dflt_attachment, context.card['id'], dflt_name)


@then('the attachment is created on the card')
def step_impl(context):
    status_code, response = attachments_manager.get_attachment(context.card['id'], context.response['id'])
    assert status_code == 200, 'Attachment was not created'
    assert response['name'] == context.payload['name'], 'Attachment was not created on the card'


@then("the attachment isn't created on the card")
def step_impl(context):
    assert not context.response.get('id'), 'Attachment was created'
