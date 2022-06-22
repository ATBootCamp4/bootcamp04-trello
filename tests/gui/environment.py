from main.core.selenium.webdriver_factory import WebdriverFactory

def before_scenario(context, feature):
    context.driver = WebdriverFactory.driver_instance(context.config.userdata['BROWSER'])
    context.driver.maximize_window()

def after_scenario(context, feature):
    context.driver.close()
    context.driver.quit()
