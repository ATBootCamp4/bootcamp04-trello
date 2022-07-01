from selenium.webdriver.common.keys import Keys
from main.core.selenium.WebDriverUtils import WebdriverUtils
from selenium.webdriver.common.by import By


class BoardPage:

    create_a_card_button = (
        "//h2[text()='{name_list}']/ancestor::div[contains(@class,'js-list-content')]//a[contains(.,'Add a card')]")
    create_card_input = (By.XPATH, "//textarea[contains(@class, 'list-card-composer-textarea')]")
    submit_create_card_button = (By.XPATH, "//div[contains(@class,'cc-controls-section')]//input")
    Example_board = (By.CSS_SELECTOR, "div[title='Example']")
    Example_card = (By.XPATH, "//span[contains(@class,'list-card-title')][text()='Example card']")
    Card_title = (By.CSS_SELECTOR, "textarea.mod-card-back-title")
    card_title_by_name = "//span[contains(@class,'list-card-title')][text()='{text}']"
    last_card_title = "//h2['{name_list}']/ancestor::div/div[contains(@class,'list-cards')]/a[last()]"
    modal_card_title = (By.XPATH, "//div[@class='window-title']/textarea")
    modal_archive_card = (By.XPATH, "//a[contains(@class,'js-archive-card')]")
    modal_delete_card = (By.XPATH, "//a[contains(@class,'js-delete-card negate')]")
    modal_delete_card_confirm = (By.XPATH, "//input[contains(@class,'js-confirm')]")

    update_board_title_locator = (By.CSS_SELECTOR, "input.board-name-input")
    CREATED_BOARD_LOCATOR_STRING = "//h1[contains(text(),'{board_name}')]"
    # show_menu_button = (By.CSS_SELECTOR, "a.js-show-sidebar")
    show_menu_button = (By.XPATH, "//a[contains(.,'Show menu')]")
    more_options_button = (By.CSS_SELECTOR, "a.js-open-more")
    close_board_option_button = (By.CSS_SELECTOR, "a.js-close-board")
    close_board_button = (By.XPATH, "//input[@value='Close']")
    delete_board_button = (By.XPATH, "//button[@data-test-id='close-board-delete-board-button']")
    confirm_delete_board_button = (By.XPATH, "//button[@data-test-id='close-board-delete-board-confirm-button']")

    CREATED_BOARD_LOCATOR_STRING = "//h1[contains(text(),'{board_name}')]"

    add_list_button = (By.CSS_SELECTOR, "a.open-add-list")
    add_list_input = (By.CSS_SELECTOR, "input.list-name-input")
    confirm_list_input = (By.XPATH, "//input[@value='Add list']")

    list_title_string_input = "//textarea[contains(@class,'js-list-name-input')][text() = '{list_title}']"
    list_title_string_h2 = "//div[contains(@class,'list-header')]//h2[text() = '{list_title}']"
    list_more_options_string = "//div[contains(@class,'list-header')]" +\
        "//h2[text() = '{list_title}']//following-sibling::div[contains(@class,'list-header-extras')]//a"

    list_close_option = (By.CSS_SELECTOR, 'a.js-close-list')

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)

    def create_card(self, card_name, list_name):
        create_card_button = self.create_a_card_button.replace('{name_list}', list_name)
        self.driver.click_button((By.XPATH, create_card_button))
        self.driver.send_keys(card_name, self.create_card_input)
        self.driver.click_button(self.submit_create_card_button)
        self.driver.wait_page_is_fully_loaded()

    def get_card_title(self, list_name):
        last_card_title = self.last_card_title.replace('{name_list}', list_name)
        return self.driver.get_text((By.XPATH, last_card_title))

    def check_card_title(self, text):
        self.driver.wait_for_text_to_be_present_in_element(self.Example_card, text)

    def update_card_title(self, list_name, text):
        last_card_title = self.last_card_title.replace('{name_list}', list_name)
        self.driver.click_button((By.XPATH, last_card_title))
        self.driver.click_button(self.modal_card_title)
        self.driver.find_element(self.modal_card_title).clear()
        self.driver.send_keys(text, self.modal_card_title)
        self.driver.send_keys(Keys.ENTER, self.modal_card_title)
        self.driver.wait_page_is_fully_loaded()

    def delete_card(self, text):
        card_title_by_name = self.card_title_by_name.replace('{text}', text)
        self.driver.click_button((By.XPATH, card_title_by_name))
        self.driver.click_button(self.modal_archive_card)
        self.driver.click_button(self.modal_delete_card)
        self.driver.click_button(self.modal_delete_card_confirm)
        self.driver.wait_page_is_fully_loaded()

    def update_title(self, title, new_title):
        title_locator = self.CREATED_BOARD_LOCATOR_STRING.replace('{board_name}', title)
        self.driver.click_button((By.XPATH, title_locator))
        self.driver.send_keys(new_title, self.update_board_title_locator)
        self.driver.send_enter(self.update_board_title_locator)
        self.driver.refresh()

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

    def create_list(self, list_name):
        self.driver.click_button(self.add_list_button)
        self.driver.send_keys(list_name, self.add_list_input)
        self.driver.click_button(self.confirm_list_input)
        self.driver.refresh()

    def check_if_list_is_created(self, list_name):
        find_list_name_string = self.list_title_string_h2.replace('{list_title}', list_name)
        locator = (By.XPATH, find_list_name_string)
        return self.driver.is_element_found(locator)

    def update_list_title(self, list_name, new_list_name):
        find_list_title = self.list_title_string_input.replace('{list_title}', list_name)
        list_title_input = (By.XPATH, find_list_title)
        self.driver.clear_input(list_title_input)
        self.driver.send_keys(new_list_name, list_title_input)
        self.driver.send_enter(list_title_input)
        self.driver.refresh()

    def delete_list(self, list_name):
        find_list = self.list_more_options_string.replace('{list_title}', list_name)
        self.driver.click_button((By.XPATH, find_list))
        self.driver.click_button(self.list_close_option)
        self.driver.refresh()
