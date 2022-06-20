from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class UIInteractions:

    @staticmethod
    def do_click(driver, by_locator):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(by_locator)).click()

#     @staticmethod
#     def send_keys(driver, by_locator, text):
#         WebDriverWait(driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

#     @staticmethod
#     def get_element_text(driver, by_locator):
#         element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(by_locator))
#         return element.text

#     @staticmethod
#     def get_title(driver, title):
#         WebDriverWait(driver, 5).until(EC.title_contains(title))
#         return driver.title

#     @staticmethod
#     def is_displayed(driver, by_locator):
#         return WebDriverWait(driver, 5).until(EC.presence_of_element_located(by_locator)).is_displayed()


class UILocators:

    locators = {
#         "create_a_board_button": (By.XPATH, "//div[contains(@class, 'mod-add')]"),
#         "create_board_input": (By.XPATH, "//input[contains(@class, 'nch-textfield__input')]"),
#         "submit_create_board_button": (By.CSS_SELECTOR, "button[data-test-id='create-board-submit-button']"),
#         "create_a_card_button": (By.XPATH, "//a[contains(@class,'open-card-composer')]"),
#         "create_card_input": (By.XPATH, "//textarea[contains(@class, 'list-card-composer-textarea')]"),
#         "submit_create_card_button": (By.XPATH, "//div[contains(@class,'cc-controls-section')]//input"),
        "Example_board": (By.CSS_SELECTOR, "div[title='Example']")
#         "Example_card": (By.XPATH, "//span[contains(@class,'list-card-title')][text()='Example card']"),
#         "Card_title": (By.CSS_SELECTOR, "textarea.mod-card-back-title")

    }
