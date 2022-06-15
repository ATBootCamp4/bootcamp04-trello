# """Module for Dashboard Page"""
# from dataclasses import asdict
# from selenium.webdriver.common.by import By
# from main.core.selenium.webdriver_utils import WebdriverUtils
# from main.jira.ui.page_objects.dashboards.dashboard_modal import DashboardModal


# class DashboardPage:
#     """Class to manage Dashboard Page actions"""

#     dashboard_content = (By.ID, 'dashboard-content')
#     favourite_btn = (By.CSS_SELECTOR, 'button[class*="favourite-btn"]')
#     dropdown_menu = (By.ID, 'tools-dropdown-icon')
#     dashboard_title = (By.XPATH, '//div[contains(@class, "header")]//h1')

#     def __init__(self, driver):
#         self.driver = WebdriverUtils(driver)
#         self.webdriver = driver
#         self.driver.wait_for_visibility_of(self.dashboard_content)

#     def click_button(self, button_label):
#         """Click on a button of dashboard page

#         :param button_label: label of a button
#         :type button_label: string
#         """
#         button_locator = (By.XPATH, f'//div[@id="dashboard-content"]//a[text()="{button_label}"]')
#         self.driver.wait_for_element_to_be_clickable(button_locator).click()
