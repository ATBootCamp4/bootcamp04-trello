from behave import then, step, given, when
from main.trello.gui.page_objects.login_page import LoginPage


@given('the user send its username to "{locator}"')
def step_impl(context, locator):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.send_keys(context.username, locator)


@step('the user waits for "{locator}" to disapear')
def step_impl(context, locator):
    context.loginPage.wait_for_element_to_disapear(locator)


@step('the user presses the "{locator}"')
def step_impl(context, locator):
    context.loginPage.click_button(locator)


@step('the user send its password to "{locator}"')
def step_impl(context, locator):
    context.loginPage.send_keys(context.password, locator)


@then('the user is logged in')
def step_impl(context):
    assert context.loginPage.is_url(f'https://trello.com/{context.user}/boards'), "The user couldn't log in"
