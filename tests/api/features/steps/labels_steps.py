from behave import step

'''
this step saves an id of any item that can be reused if the object
is neded again using the common step: 'I send a "{method}" request to "{endpoint}"'
'''


@step('the item id is saved before deletion')
def step_impl(context):
    context.to_be_deleted_id = context.response['id']


'''
this step is for negative tests, if a label is deleted will use its id to do a
get/post/put request and returns checks the error message
'''


@step('after deleted if I "{method}" the label the message is "{message}" and "{http_response:d}" status code')
def step_impl(context, message, http_response, method):
    if context.to_be_deleted_id is True:
        status_code, response = context.request_manager.do_request(method, f'/labels/{context.to_be_deleted_id}')
        assert response == message, f'it was expected {message} but was received {response}'
        assert status_code == http_response, f'it was expected {http_response} but was received {status_code}'
