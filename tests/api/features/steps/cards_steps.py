
from behave import given, step
from main.core.rest.request_manager import RequestManager
request_manager = RequestManager()


@given('I created a new card')
def step_impl(context):
    context.status_code, context.card = context.request_manager.post_request(
        'cards', payload={'name': 'Behave card', 'idList': context.list['id']})


'''
    This method verifies if a comment has been added to a card
    by checking if its ID is present in the list of actions of a card
'''


@step('verify the comment has been added')
def step_impl(context):
    comment_id = context.response['id']
    card_id = context.response['data']['card']['id']
    context.status_code, context.response = request_manager.do_request(
        "GET", "cards/" + card_id + "/actions")
    error_msg = f"Comment {comment_id} is not present on card {card_id}"
    assert comment_id in [action['id']
                          for action in context.response], error_msg


'''
    This method verifies if a comment has been deleted from a card
    by checking if its ID is not present in the list of actions of a card
'''


@step('verify the comment has been deleted')
def step_impl(context):
    comment_id = context.comment['id']
    card_id = context.card['id']
    context.status_code, context.response = request_manager.do_request(
        "GET", "cards/" + card_id + "/actions")

    assert comment_id not in [action['id']
                              for action in context.response], f"Comment {comment_id} is present on card {card_id}"


'''
    This method creates comment in a card with some text.
    It is used along with another steps and has no
    major functionality
'''


@step('I created a comment in the card')
def step_impl(context):
    context.status_code, context.comment = request_manager.do_request(
        "POST", "cards/" + context.card['id'] + "/actions/comments", payload={"text": "InitialComment"})

    assert context.status_code == 200, f"Couldn't create card, status code is {context.status_code}, expected 200"
