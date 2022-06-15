@step('I login')
def step_login(context):
    navigate(HOME);
    home_page = HomePage(context.driver)
    home_page.click("Login")
    login_page = LoginPage(context.driver)
    