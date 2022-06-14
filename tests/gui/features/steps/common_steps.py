from behave import given, step
from main.utils.ui_interactions import UIInteractions, UILocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given('the user is logged in')
def step_impl(context):

    context.driver.get("https://trello.com/login")
    input_user = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#user"))
    )

    input_user.send_keys("emc935.testing@gmail.com")

    next_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#login"))
    )

    next_input.click()

    input_password = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#password"))
    )

    input_password.send_keys("testingaccount")

    login_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button#login-submit"))
    )

    login_input.click()

    input_password = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#password"))
    )

    input_password.send_keys("testingaccount")

    login_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button#login-submit"))
    )

    login_input.click()


@step('the user clicks on button "{locator}"')
def step_impl(context, locator):
    UIInteractions.do_click(context.driver, UILocators.locators[locator])


@step('the board "{locator}" is selected')
def step_impl(context, locator):
    UIInteractions.do_click(context.driver, UILocators.locators[locator])


@step('send input value "{input_value}" to field "{locator}"')
def step_impl(context, input_value, locator):
    UIInteractions.send_keys(context.driver, UILocators.locators[locator], input_value)


@step('element "{locator}" is displayed')
def step_impl(context, locator):
    assert UIInteractions.is_displayed(context.driver, UILocators.locators[locator]), "Is not displayed"


@step('element text is "{text}"')
def step_impl(context, element):
    UIInteractions.get_element_text(context.driver, element)