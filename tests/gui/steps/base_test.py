# import unittest
# from selenium import webdriver
# import urllib3
# # from core.selenium.webdriver_factory import WebdriverFactory
# # from pages.config import TestData

# class BaseTest(unittest.TestCase):

#     def setUp(self):
#         urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#         self.driver = WebdriverFactory.get_driver("chrome")
#         # self.driver = webdriver.Firefox(executable_path=TestData.FIREFOX_PATH)
#         # self.driver = webdriver.Edge(TestData.EDGE_PATH)
#         self.driver.implicitly_wait(10)
#         self.driver.maximize_window()
 
#     def tearDown(self):
#         if (self.driver != None):
#             print("Cleanup of test environment")
#             self.driver.close()
#             self.driver.quit()