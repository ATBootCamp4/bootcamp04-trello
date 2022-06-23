from main.utils.common_globals import USER, USERNAME, PASSWORD
from main.core.selenium.webdriver_factory import WebdriverFactory

def before_scenario(context, scenario):
    context.driver = WebdriverFactory.driver_instance(context, context.config.userdata['BROWSER'])
    context.driver.maximize_window()

    context.username = USERNAME
    if USERNAME is None:
        print('Username is None')
        context.username = context.config.userdata['USERNAME']

    context.password = PASSWORD
    if PASSWORD is None:
        print('Password is none')
        context.password = context.config.userdata['PASSWORD']

    context.user = USER
    if USER is None:
        print('User is none')
        context.user = context.config.userdata['USER']

    context.base_url = context.config.userdata['BASE_URL']

def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
