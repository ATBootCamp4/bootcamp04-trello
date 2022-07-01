from main.trello.gui.page_objects.login_page import LoginPage
from main.trello.gui.page_objects.board_page import BoardPage
from main.trello.gui.page_objects.home_page import HomePage


class PageObjectFactory:

    def __init__(self, driver):
        self.factory = {
            "login": LoginPage,
            "board": BoardPage,
            "home": HomePage
        }
        self.driver = driver

    def get_page(self, page_name):
        return self.factory[page_name](self.driver)
