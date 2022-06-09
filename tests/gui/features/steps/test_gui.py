from behave import when, step, then
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@when('I go to youtube page')
def step_impl(context):

    chrome_service = Service(ChromeDriverManager(
        chrome_type=ChromeType.GOOGLE).install())

    chrome_options = Options()
    options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    for option in options:
        chrome_options.add_argument(option)

    context.driver = webdriver.Chrome(
        service=chrome_service, options=chrome_options)

    context.driver.get("https://www.youtube.com/")


@step('make a Search')
def step_impl(context):
    input_search = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )

    input_search.send_keys("java brains")

    input_search.submit()


@then('main result channel is displayed')
def step_impl(context):
    yt_channel = WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, "main-link"))
    )

    assert yt_channel.is_displayed()
