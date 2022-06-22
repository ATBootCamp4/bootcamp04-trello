from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main.core.selenium.WebDriverUtils import WebdriverUtils
from selenium.webdriver.support.ui import WebDriverWait

class CardsPage:

    create_card_input = (By.XPATH, "//textarea[contains(@class, 'list-card-composer-textarea')]")
    submit_create_card_button = (By.XPATH, "//div[contains(@class,'cc-controls-section')]//input")
    Example_board = (By.CSS_SELECTOR, "div[title='Example']")
    card_title_by_name = (By.XPATH, "//span[contains(@class,'list-card-title')][text()='Another_name']")
    # Card_title = (By.CSS_SELECTOR, "//h2[text()='List example']/ancestor::div/div[contains(@class,'list-cards')]/a[last()]/span")
    modal_card_title = (By.XPATH, "//div[@class='window-title']/textarea")
    modal_archive_card = (By.XPATH, "//a[contains(@class,'js-archive-card')]")
    modal_delete_card = (By.XPATH, "//a[contains(@class,'js-delete-card negate')]")
    modal_delete_card_confirm = (By.XPATH, "//input[contains(@class,'js-confirm')]")

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)
    
    def create_card(self, name, list_name):
        create_a_card_button = (By.XPATH, f"//h2[text()='{list_name}']/ancestor::div[contains(@class,'js-list-content')]//a[contains(.,'Add a card')]")
        self.driver.click_button(create_a_card_button)
        self.driver.send_keys(name, self.create_card_input)
        self.driver.click_button(self.submit_create_card_button)
        self.driver.wait_page_is_fully_loaded()

    def get_card_title(self, list_name):
        Last_card_title = (By.XPATH, f"//h2['{list_name}']/ancestor::div/div[contains(@class,'list-cards')]/a[last()]")
        return self.driver.get_text(Last_card_title)

    def update_card_title(self, list_name, text):
        Last_card_title = (By.XPATH, f"//h2['{list_name}']/ancestor::div/div[contains(@class,'list-cards')]/a[last()]")
        self.driver.click_button(Last_card_title)
        self.driver.click_button(self.modal_card_title)
        self.driver.find_element(self.modal_card_title).clear()
        self.driver.send_keys(text, self.modal_card_title)
        self.driver.send_keys(Keys.ENTER, self.modal_card_title)
        self.driver.wait_page_is_fully_loaded()

    def delete_card(self, text):
        card_title_by_name = (By.XPATH, f"//span[contains(@class,'list-card-title')][text()='{text}']")
        self.driver.click_button(card_title_by_name)
        self.driver.click_button(self.modal_archive_card)
        self.driver.click_button(self.modal_delete_card)
        self.driver.click_button(self.modal_delete_card_confirm)
        self.driver.wait_page_is_fully_loaded()
