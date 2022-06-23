from behave import given, step
from main.trello.gui.page_objects.login_page import LoginPage


@given('the user goes to "{page}"')
def step_impl(context, page):
    context.driver.get(context.base_url + page)


@step('the user logs in')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.login(context.username, context.password)
