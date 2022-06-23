from behave import given, step


@given('the user goes to "{page}" page')
def step_impl(context, page):
    context.login_page = context.page_factory.get_page(page)(context.driver)
    if page == "login":
        context.driver.get(context.base_url + '/login')


@step('the user logs in')
def step_impl(context):
    context.login_page = context.page_factory.get_page('login')(context.driver)
    context.login_page.login(context.username, context.password)
