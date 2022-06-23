from main.trello.gui.page_objects.login_page import LoginPage
from main.trello.gui.page_objects.cards_page import CardsPage
from main.trello.gui.page_objects.home_page import HomePage


class PageObjectFactory:

    def __init__(self):
        self.factory = {
            "login": LoginPage,
            "board": CardsPage,
            "home": HomePage
        }

    def get_page(self, page_name):
        return self.factory[page_name]
