from behave import given
from main.trello.gui.page_objects.login_page import LoginPage


@given('the user is logged in')
def step_impl(context):
    context.loginPage = LoginPage(context.driver)
    context.loginPage.send_keys(context.username, "username input")

    context.loginPage.wait_for_element_to_disapear("password input")
    context.loginPage.click_button("login button")

    context.loginPage.send_keys(context.password, "password input")
    context.loginPage.click_button("submit loggin button")
