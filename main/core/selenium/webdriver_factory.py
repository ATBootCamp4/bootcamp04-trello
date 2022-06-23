from main.core.selenium.chrome_driver import ChromeDriver
from main.core.selenium.firefox_driver import FirefoxDriver
from main.core.selenium.edge_driver import EdgeDriver


class WebdriverFactory:

    @staticmethod
    def driver_instance(context, driver_name):

        match driver_name:
            case 'chrome':
                context.driver = ChromeDriver.initial(context)
            case 'firefox':
                context.driver = FirefoxDriver.initial(context)
            case 'edge':
                context.driver = EdgeDriver.initial(context)

        return context.driver
