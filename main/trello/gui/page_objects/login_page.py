from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = {
            "username input": (By.CSS_SELECTOR, "input#user"),
            "password input": (By.CSS_SELECTOR, "input#password"),
            "login button": (By.CSS_SELECTOR, "input#login"),
            "submit loggin button": (By.CSS_SELECTOR, "button#login-submit")
        }
        self.driver.get('https://trello.com/login')

    def click_button(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                self.locators[locator])
        ).click()

    def send_keys(self, keys, input_locator):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            self.locators[input_locator])).send_keys(keys)

    def wait_for_element_to_disapear(self, locator):
        WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located(self.locators[locator]))

    def is_url(self, url):
        return WebDriverWait(self.driver, 5).until(
            EC.url_to_be(url))
