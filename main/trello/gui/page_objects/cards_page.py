from time import sleep
from selenium.webdriver.common.by import By
from main.core.selenium.WebDriverUtils import WebdriverUtils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CardsPage:

    create_a_card_button = (By.XPATH, "//h2[text()='Title example']/ancestor::div[contains(@class,'js-list-content')]//a[contains(.,'Add a card')]")
    create_card_input = (By.XPATH, "//textarea[contains(@class, 'list-card-composer-textarea')]")
    submit_create_card_button = (By.XPATH, "//div[contains(@class,'cc-controls-section')]//input")
    Example_board = (By.CSS_SELECTOR, "div[title='Example']")
    Example_card = (By.XPATH, "//span[contains(@class,'list-card-title')][text()='Example card']")
    Card_title = (By.CSS_SELECTOR, "textarea.mod-card-back-title")

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)
    
    def create_card(self, name):
        self.driver.click_button(self.create_a_card_button)
        self.driver.send_keys(name, self.create_card_input)
        self.driver.click_button(self.submit_create_card_button)
        # sleep(1)

    def check_card_title(self, text):
        self.driver.wait_for_text_to_be_present_in_element(self.Example_card, text)
    #     sleep(1)
