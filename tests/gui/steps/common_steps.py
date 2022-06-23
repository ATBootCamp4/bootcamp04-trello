from behave import given


@given('the user goes to "{page}"')
def step_impl(context, page):
    context.driver.get(context.base_url + page)


@given('the user is logged in')
def step_impl(context):
    context.driver.get(context.base_url + '/login')
    context.login_page = context.page_factory.get_page('login')
    context.login_page.login(context.username, context.password)
