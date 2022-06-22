import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver


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

    context.username = os.getenv('TRELLO_USERNAME', None)
    if not context.username:
        context.username = context.config.userdata['USERNAME']

    context.password = os.getenv('TRELLO_PASSWORD', None)
    if not context.password:
        context.password = context.config.userdata['PASSWORD']

    context.user = os.getenv('TRELLO_USER', None)
    if not context.user:
        context.user = context.config.userdata['USER']

    context.base_url = context.config.userdata['BASE_URL']


def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
