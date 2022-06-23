from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.utils import ChromeType
from selenium import webdriver


class ChromeDriver:

    @staticmethod
    def initial(context):

        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        chrome_options = Options()
        options = [
            # "--headless",
            "--disable-gpu",
            "--lang=en-US",
            "--ignore-certificate-errors",
            "--disable-extensions",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)

        context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        return context.driver
