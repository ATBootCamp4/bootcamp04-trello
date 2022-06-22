from selenium.webdriver.common.by import By
from main.core.selenium.WebDriverUtils import WebdriverUtils


class HomePage:

    create_a_board_button = (By.XPATH, "//div[contains(@class, 'mod-add')]")

    create_board_input = (By.XPATH, "//input[contains(@class, 'nch-textfield__input')]")

    submit_create_board_button = (By.CSS_SELECTOR, "button[data-test-id='create-board-submit-button']")

    board_title_locator_string0 = "//div[not(@class) and not(@id)][h3]//div[contains(@class,'boards-page-board-section')]"

    board_title_locator_string1 = "//ul[contains(@class,'boards-page-board-section-list')]"
    board_title_locator_string2 = "//li[contains(@class,'boards-page-board-section-list-item')]" + \
        "//a[contains(@href,'{board_name}')]"
    CREATED_BOARD_LOCATOR_STRING = "//h1[contains(text(),'{board_name}')]"

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)

    def create_board(self, board_name):
        self.driver.click_button(self.create_a_board_button)
        self.driver.send_keys(board_name, self.create_board_input)

        self.driver.click_button(self.submit_create_board_button)

    def check_if_board_is_created(self, board_name):
        board_locator = self.CREATED_BOARD_LOCATOR_STRING.replace('{board_name}', board_name)

        return self.driver.is_element_found((By.XPATH, board_locator))

    def go_to_board(self, board_name):
        last_board_locator = self.board_title_locator_string2.replace('{board_name}', board_name.lower())
        board_locator = self.board_title_locator_string0 + self.board_title_locator_string1 + last_board_locator
        final_board_locator = (By.XPATH, board_locator)
        self.driver.click_button(final_board_locator)

    def check_if_board_is_deleted(self, board_name):
        last_board_locator = self.board_title_locator_string2.replace('{board_name}', board_name.lower())
        board_locator = self.board_title_locator_string0 + self.board_title_locator_string1 + last_board_locator
        final_board_locator = (By.XPATH, board_locator)
        return not self.driver.is_element_found(final_board_locator)

    def wait_for_page_to_load(self):
        self.driver.wait_page_is_fully_loaded_no_jquery()
