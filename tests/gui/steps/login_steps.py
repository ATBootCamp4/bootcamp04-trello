from behave import then, step, given, when
from main.trello.gui.page_objects.login_page import LoginPage


@given('the user goes to log in page')
def step_impl(context):
    context.loginPage = LoginPage(context.driver)


@when('the user sends its credentials')
def step_impl(context):
    context.loginPage.login(context.username, context.password)


@then('the user should be logged in')
def step_impl(context):
    assert context.loginPage.check_if_log_in(f'https://trello.com/{context.user}/boards'), "The user couldn't log in"
