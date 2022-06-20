from behave import when, then
from main.trello.gui.page_objects.cards_page import CardsPage

@when('the user create a card "{text}"')
def step_impl(context, text):
    context.cards_page = CardsPage(context.driver)
    context.cards_page.create_card(text)

@then('element "{text}" is displayed')
def step_impl(context, text):
    context.cards_page = CardsPage(context.driver)
    context.cards_page.check_card_title(text)
