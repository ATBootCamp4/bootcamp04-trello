from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver
from main.utils.common_globals import USER, USERNAME, PASSWORD


def before_scenario(context, scenario):

    chrome_service = Service(ChromeDriverManager(
        chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        # "--headless",
        "--disable-gpu",
        "--start-maximized",
        "--lang=en-US",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    context.driver = webdriver.Chrome(
        service=chrome_service, options=chrome_options)

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
