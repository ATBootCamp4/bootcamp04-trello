from behave import when, then


@when('the user create a card "{text}" in the list "{list_name}"')
def step_impl(context, text, list_name):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.create_card(text, list_name)


@then('the card in the list "{list_name}" shows "{text}"')
def step_impl(context, list_name, text):
    context.cards_page = context.page_factory.get_page("board")
    title = context.cards_page.get_card_title(list_name)
    assert title == text, f"Expected {text}, but received {title}"


@when('the user update the last card name in the list "{list_name}" with "{text}"')
def step_impl(context, list_name, text):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.update_card_title(list_name, text)


@when('the user delete the card "{text}"')
def step_impl(context, text):
    context.cards_page = context.page_factory.get_page("board")
    context.cards_page.delete_card(text)


@then('the card "{text}" is not shown in the list "{list_name}"')
def step_impl(context, list_name, text):
    context.cards_page = context.page_factory.get_page("board")
    title = context.cards_page.get_card_title(list_name)
    assert title != text, f"Expected nothing, but received {title}"
