from main.trello.gui.page_objects.PageObjectFactory import PageObjectFactory
from main.utils.common_globals import USER, USERNAME, PASSWORD
from main.core.selenium.webdriver_factory import WebdriverFactory
from behave.fixture import use_fixture_by_tag, fixture_call_params
from hooks import create_board, delete_board
# from main.core.rest.request_manager import RequestManager

FIXTURE_REGISTRY = {
    "fixture.before.create.board": fixture_call_params(
        create_board,
        endpoint='boards/',
        board_name='CreateBoardExample'
    ),
    "fixture.after.delete.board": fixture_call_params(
        delete_board,
        endpoint='boards/'
    ),
}


def before_scenario(context, scenario):
    context.driver = WebdriverFactory.driver_instance(context, context.config.userdata['BROWSER'])
    context.driver.maximize_window()

    context.page_factory = PageObjectFactory(context.driver)

    context.username = USERNAME
    if USERNAME is None:
        context.username = context.config.userdata['USERNAME']

    context.password = PASSWORD
    if PASSWORD is None:
        context.password = context.config.userdata['PASSWORD']

    context.user = USER
    if USER is None:
        context.user = context.config.userdata['USER']

    context.base_url = context.config.userdata['BASE_URL']


def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()


def before_tag(context, tag):
    if tag.startswith('fixture.before.'):
        use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)


def after_tag(context, tag):
    if tag.startswith('fixture.after.'):
        use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)


""" def before_feature(context, feature):
    context.request_manager = RequestManager()
    if feature.name.strip() == 'Trello UI Lists':
        _, context.board = context.request_manager.post_request('boards/', payload={'name': 'ManageListsBoard'})


def after_feature(context, feature):
    if feature.name.strip() == 'Trello UI Lists':
        context.request_manager.delete_request('boards/' + context.board['id']) """
