from behave import given
from main.trello.gui.page_objects.login_page import LoginPage


@given('the user is logged in')
def step_impl(context):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.login(context.username, context.password)
    assert context.loginPage.check_if_log_in(f'https://trello.com/{context.user}/boards'), "The user couldn't log in"
