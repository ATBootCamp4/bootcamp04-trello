from behave import then, when

from main.trello.gui.page_objects.login_page import LoginPage


@when('the user sends its credentials')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.login(context.username, context.password)


@then('the user should be logged in')
def step_impl(context):
    assert context.login_page.check_if_log_in(f'https://trello.com/{context.user}/boards'), "The user couldn't log in"
