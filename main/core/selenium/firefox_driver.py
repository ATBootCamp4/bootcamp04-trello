# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

class FirefoxDriver:
    
    @staticmethod
    def initial(context):
        firefox_service = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # firefox_options = Options()
        # firefox_options.add_argument("--lang=en-US")
        # firefox_options.add_argument("-headless")
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference('intl.accept_languages', 'en-GB')
        # context.driver = webdriver.Firefox(firefox_service, options=firefoxOptions)
        context.driver = firefox_service
        
        return context.driver
