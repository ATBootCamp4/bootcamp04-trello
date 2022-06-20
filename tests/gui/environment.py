from main.core.selenium.webdriver_factory import WebdriverFactory
from web_drivers_names import WebDriverNames

def before_feature(context, feature):
    context.driver = WebdriverFactory.driver_instance(WebDriverNames.EDGE)
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.close()
    context.driver.quit()
