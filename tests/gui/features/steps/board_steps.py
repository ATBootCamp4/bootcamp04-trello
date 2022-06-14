from behave import then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@then('a board is created')
def step_impl(context):
    board_created = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'board-header-btn-text')]"))
    )

    assert board_created.is_displayed()
    assert board_created.get_attribute("innerText") == "Test", "No board created"
