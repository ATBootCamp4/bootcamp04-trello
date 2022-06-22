
from main.core.selenium.WebDriverUtils import WebdriverUtils
from selenium.webdriver.common.by import By


class CardsPage:

    create_a_card_button = (
        By.XPATH,
        "//h2[text()='Title example']/ancestor::div[contains(@class,'js-list-content')]//a[contains(.,'Add a card')]")
    create_card_input = (By.XPATH, "//textarea[contains(@class, 'list-card-composer-textarea')]")
    submit_create_card_button = (By.XPATH, "//div[contains(@class,'cc-controls-section')]//input")
    Example_board = (By.CSS_SELECTOR, "div[title='Example']")
    Example_card = (By.XPATH, "//span[contains(@class,'list-card-title')][text()='Example card']")
    Card_title = (By.CSS_SELECTOR, "textarea.mod-card-back-title")
    update_board_title_locator = (By.CSS_SELECTOR, "input.board-name-input")
    CREATED_BOARD_LOCATOR_STRING = "//h1[contains(text(),'{board_name}')]"

    show_menu_button = (By.CSS_SELECTOR, "a.js-show-sidebar")
    more_options_button = (By.CSS_SELECTOR, "a.js-open-more")
    close_board_option_button = (By.CSS_SELECTOR, "a.js-close-board")
    close_board_button = (By.XPATH, "//input[@value='Close']")
    delete_board_button = (By.XPATH, "//button[@data-test-id='close-board-delete-board-button']")
    confirm_delete_board_button = (By.XPATH, "//button[@data-test-id='close-board-delete-board-confirm-button']")

    CREATED_BOARD_LOCATOR_STRING = "//h1[contains(text(),'{board_name}')]"

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)

    def create_card(self, name):
        self.driver.click_button(self.create_a_card_button)
        self.driver.send_keys(name, self.create_card_input)
        self.driver.click_button(self.submit_create_card_button)

    def check_card_title(self, text):
        self.driver.wait_for_text_to_be_present_in_element(self.Example_card, text)

    def update_title(self, title, new_title):
        title_locator = self.CREATED_BOARD_LOCATOR_STRING.replace('{board_name}', title)
        self.driver.click_button((By.XPATH, title_locator))
        self.driver.send_keys(new_title, self.update_board_title_locator)
        self.driver.send_enter(self.update_board_title_locator)

    def check_if_board_title_is_updated(self, board_name):
        board_locator = self.CREATED_BOARD_LOCATOR_STRING.replace('{board_name}', board_name)

        return self.driver.is_element_found((By.XPATH, board_locator))

    def delete_board(self):
        self.driver.click_button(self.show_menu_button)
        self.driver.click_button(self.more_options_button)
        self.driver.click_button(self.close_board_option_button)
        self.driver.click_button(self.close_board_button)
        self.driver.click_button(self.delete_board_button)
        self.driver.click_button(self.confirm_delete_board_button)
