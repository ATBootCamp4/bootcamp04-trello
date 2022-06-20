from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from web_drivers_names import WebDriverNames as name

class WebdriverFactory:
    
    @staticmethod
    def driver_instance(driver_name):

        match driver_name:
            case name.CHROME:
                driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            case name.FIREFOX:
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            case name.EDGE:
                driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        
        return driver
