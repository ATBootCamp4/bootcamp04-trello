from behave import then, step
from main.trello.api.attachments_manager import AttachmentsManager

attachments_manager = AttachmentsManager()


@step('I created an attachment on the card')
def step_impl(context):
    """This step will create an attachment on the card that's currently
    in the context, using a default image and name."""
    dflt_attachment = "https://source.unsplash.com/user/c_v_r"
    dflt_name = "Behave attachment"
    _, context.attachment = attachments_manager.create_attachment_from_url(dflt_attachment, context.card['id'], dflt_name)


@then('the attachment is created on the card')
def step_impl(context):
    """This step intends to verify that the attachment was created on the card."""
    status_code, response = attachments_manager.get_attachment(context.card['id'], context.response['id'])
    assert status_code == 200, 'Attachment was not created on the card'
    assert response['name'] == context.payload['name'], \
        f"Expected attachment's name to be {context.payload['name']} but it was {response['name']}"


@then('the attachment is deleted')
def step_impl(context):
    """This step intends to verify that the attachment was deleted."""
    status_code, response = attachments_manager.get_attachment(context.card['id'], context.attachment['id'])
    assert status_code >= 400, f"Expected status code >= 400, got {status_code}"
    assert 'invalid attachment' in response.lower(), f"Expected error message 'not found' but received: \n '{response}'"
