from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebdriverFactory:
    
    @staticmethod
    def driver_instance(driver_name):

        match driver_name:
            case 'chrome':
                driver =  webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            case 'firefox':
                driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            case 'edge':
                driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        
        return driver
