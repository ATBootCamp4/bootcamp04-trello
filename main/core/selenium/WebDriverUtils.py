"""Module for Webdriver utilities"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from main.core.environment_variable_reader import EnvironmentVariableReader as ENV


TIMEOUT = int(ENV().get_variable('DRIVER', 'EXPLICIT_TIMEOUT'))
IMPLICIT_TIMEOUT = int(ENV().get_variable('DRIVER', 'IMPLICIT_TIMEOUT'))


class WebdriverUtils:
    """Class for managing the utilities for webdrivers"""

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        """Return the current title of the driver"""
        return self.driver.title

    def wait_for_visibility_of(self, locator):
        """Verify if an element is visible

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of(self.driver.find_element(*locator)))

    def wait_for_visibility_of_element_located(self, locator):
        """Verify if an element located is visible

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(locator))

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

    def wait_for_text_to_be_present_in_element(self, locator, text):
        """Verify if a given text is present in an element

        :param locator: locator used to catch an element
        :type locator: tuple
        :param text: text expected to be in element
        :type text: string
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.text_to_be_present_in_element(locator, text))

    def wait_page_is_fully_loaded(self):
        """Wait until web page is fully loaded"""
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return jQuery.active == 0'))
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def wait_page_is_fully_loaded_no_jquery(self):
        """Wait until web page is fully loaded with no jquery"""
        WebDriverWait(self.driver, TIMEOUT).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def wait_for_invisibility_of_element_located(self, locator):
        """Verify if an element is visible and clickable

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return WebDriverWait(self.driver, TIMEOUT).until(
            EC.invisibility_of_element_located(locator))

    def find_element(self, locator):
        """Find an element by its locator

        :param locator: locator used to catch an element
        :type locator: tuple
        """
        return self.driver.find_element(*locator)

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
