"""Module for Webdriver utilities"""
import functools
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from main.core.environment_variable_reader import EnvironmentVariableReader as ENV
from selenium.webdriver.common.keys import Keys
from main.utils.logger import Logger


TIMEOUT = int(ENV().get_variable('DRIVER', 'EXPLICIT_TIMEOUT'))
IMPLICIT_TIMEOUT = int(ENV().get_variable('DRIVER', 'IMPLICIT_TIMEOUT'))

LOGGER = Logger(__name__)


def catch_exception(f):
    @functools.wraps(f)
    def func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            LOGGER.error(f'Something failed within function: {str(f.__name__)} and stacktrace: {repr(e)}')
    return func


class WebdriverUtils:
    """Class for managing the utilities for webdrivers"""

    def __init__(self, driver):
        self.driver = driver

    @catch_exception
    def get(self, url):
        self.driver.get(url)

    @catch_exception
    def send_keys(self, keys, input_locator):
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(
            input_locator)).send_keys(keys)

    @catch_exception
    def send_enter(self, input_locator):
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(
            input_locator)).send_keys(Keys.RETURN)

    @catch_exception
    def click_button(self, locator):
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @catch_exception
    def is_url(self, url):
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.url_to_be(url))

    @catch_exception
    def get_text(self, locator):
        return WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(
            locator)).text

    @catch_exception
    def get_title(self):
        """Return the current title of the driver"""
        return self.driver.title

    @catch_exception
    def wait_for_visibility_of(self, locator):
        """Verify if an element is visible

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of(self.driver.find_element(*locator)))

    @catch_exception
    def wait_for_visibility_of_element_located(self, locator):
        """Verify if an element located is visible

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator))

    @catch_exception
    def wait_for_element_to_be_clickable(self, locator):
        """Verify if an element is visible and clickable

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(locator))

    def wait_for_presence_of_element_located(self, locator):
        """Verify if an element is present on the DOM

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(EC.presence_of_element_located(locator))

    @catch_exception
    def wait_for_staleness_of(self, locator):
        """Wait for an element to be not longer attached to the DOM

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        self.driver.implicitly_wait(TIMEOUT)
        element = self.driver.find_element(*locator)
        element = WebDriverWait(self.driver, TIMEOUT).until(EC.staleness_of(element))
        self.driver.implicitly_wait(IMPLICIT_TIMEOUT)
        return element

    @catch_exception
    def wait_for_text_to_be_present_in_element(self, locator, text):
        """Verify if a given text is present in an element

        :param locator: locator used to catch an element
        :type locator: tuple
        :param text: text expected to be in element
        :type text: string
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.text_to_be_present_in_element(locator, text))

    @catch_exception
    def wait_page_is_fully_loaded(self):
        """Wait until web page is fully loaded"""
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return jQuery.active == 0'))
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    @catch_exception
    def wait_page_is_fully_loaded_no_jquery(self):
        """Wait until web page is fully loaded with no jquery"""
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    @catch_exception
    def wait_for_invisibility_of_element_located(self, locator):
        """Verify if an element is visible and clickable

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.invisibility_of_element_located(locator))

    @catch_exception
    def find_element(self, locator):
        """Find an element by its locator

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return self.driver.find_element(*locator)

    @catch_exception
    def find_elements(self, locator):
        """Find all elements matching a locator

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return self.driver.find_elements(*locator)

    def is_element_found(self, locator):
        """Verify if an element can be found on the DOM

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        try:
            self.wait_for_presence_of_element_located(locator)
            return True
        except NoSuchElementException:
            return False
        except StaleElementReferenceException:
            return False
        except TimeoutException:
            return False

    @catch_exception
    def clear_input(self, locator):
        self.wait_for_presence_of_element_located(locator).clear()

    @catch_exception
    def refresh(self):
        self.driver.refresh()
