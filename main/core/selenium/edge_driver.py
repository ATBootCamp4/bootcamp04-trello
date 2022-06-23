from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium import webdriver


class EdgeDriver:

    @staticmethod
    def initial(context):

        edge_service = Service(EdgeChromiumDriverManager().install())
        edge_options = Options()
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
            edge_options.add_argument(option)

        context.driver = webdriver.Edge(service=edge_service, options=edge_options)
        return context.driver
