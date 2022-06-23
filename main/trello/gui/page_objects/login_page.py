from selenium.webdriver.common.by import By
from main.core.selenium.WebDriverUtils import WebdriverUtils


class LoginPage:

    username_input = (By.CSS_SELECTOR, "input#user")
    password_input = (By.CSS_SELECTOR, "input#password")
    login_button = (By.CSS_SELECTOR, "input#login")
    submit_loggin_button = (By.CSS_SELECTOR, "button#login-submit")

    def __init__(self, driver):
        self.driver = WebdriverUtils(driver)

    def login(self, username, password):
        self.driver.send_keys(username, self.username_input)
        self.driver.wait_for_invisibility_of_element_located(self.password_input)
        self.driver.click_button(self.login_button)
        self.driver.send_keys(password, self.password_input)
        self.driver.click_button(self.submit_loggin_button)

    def check_if_log_in(self, url):
        return self.driver.is_url(url)
