from behave import given, when, then, step
from main.core.rest.request_manager import RequestManager
from main.trello.api.cards_manager import ID_LIST

request_manager = RequestManager()


@given('the user defines a "{http_method}" request to "{endpoint}"')
def step_impl(context, http_method, endpoint):
    context.endpoint = endpoint
    context.http_method = http_method
    model = None
    if context.table:
        model = JsonModel()
        for row in context.table:
            row_value = row['Value']
            if row['Key'] == 'idList':
                row_value = ID_LIST
            model.build_json(row['Key'], row_value)
    context.model = model


@when('the user sends the request')
def step_impl(context):
    status_code, api_response = request_manager.do_request(
        context.http_method, context.endpoint, payload=context.model.json_data)
    context.status_code = status_code
    context.api_response.append(api_response)


@then('verify the status code is "{code:d}"')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"


@Given('the user defines a "{http_method}" request with name and desc to "{endpoint}"')
def step_impl(context, http_method, endpoint):
    print('ID CARD:', context.api_response[0]['id'])
    context.endpoint = endpoint.replace(
        '{idCard}', context.api_response[0]['id'])
    context.http_method = http_method
    model = None

    if context.table:
        print('HAY TABLE')
        model = JsonModel()
        for row in context.table:
            model.build_json(row['Key'], row['Value'])
            print('KEY Y VALUE ----->', row['Key'], row['Value'])
    context.model = model


@when('the user sends the request for updating')
def step_impl(context):
    status_code, api_response = request_manager.do_request(
        context.http_method, context.endpoint, payload=context.model.json_data)
    context.status_code = status_code
    context.api_response[0] = api_response


@then('verify the status code is "{code:d}" for updating')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"


@step('verify the card name and desc is updated')
def step_impl(context):
    assert context.model.json_data['name'] == context.api_response[0][
        'name'], f"Description '{context.model.json_data['name']}' was expected but '{context.api_response[0]['name']}' was found"
    assert context.model.json_data['desc'] == context.api_response[0][
        'desc'], f"Description '{context.model['desc']}' was expected but '{context.api_response[0]['desc']}' was found"


@Given('the user defines a "{http_method}" request to "{endpoint}" with text for a comment')
def step_impl(context, http_method, endpoint):
    context.endpoint = endpoint.replace(
        '{idCard}', context.api_response[0]['id'])
    context.http_method = http_method
    context.id_card = context.api_response[0]['id']
    model = None
    if context.table:
        model = JsonModel()
        for row in context.table:
            model.build_json(row['Key'], row['Value'])
    context.model = model


@when('the user sends the request for creating comment')
def step_impl(context):
    status_code, api_response = request_manager.do_request(
        context.http_method, context.endpoint, payload=context.model.json_data)
    context.status_code = status_code
    context.comment_api_response = api_response


@then('verify the status code is "{code:d}" for commenting')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"


@step('verify the comment has been added to the card')
def step_impl(context):
    assert context.model.json_data['text'] == context.comment_api_response['data'][
        'text'], f"Expected comment text '{context.model.json_data['text']}' but '{context.comment_api_response['data']['text']}' was found"
    assert context.comment_api_response['data']['card'][
        'id'] == context.id_card, f"Comment on card id '{context.comment_api_response['data']['card']['id']}' doesnt match with used card with id '{context.id_card}'"


@Given('the user defines a "{http_method}" request to "{endpoint}" with an existing ID')
def step_impl(context, http_method, endpoint):
    context.endpoint = endpoint.replace(
        '{idCard}', context.api_response[0]['id'])
    context.http_method = http_method


@when('the user sends the request for deleting')
def step_impl(context):
    context.status_code, _ = request_manager.do_request(
        context.http_method, context.endpoint)


@then('verify status code is "{code:d}" for deleting')
def step_impl(context, code):
    assert context.status_code == code, f"It was expected status code {code} but was {context.status_code}"


class JsonModel():
    def __init__(self):
        self.json_data = {}

    def build_json(self, key, value):
        self.json_data[key] = value
