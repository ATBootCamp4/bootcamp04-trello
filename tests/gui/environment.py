from main.trello.PageObjectFactory import PageObjectFactory
from main.utils.common_globals import USER, USERNAME, PASSWORD
from main.core.selenium.webdriver_factory import WebdriverFactory
import allure
import datetime
from behave.fixture import use_fixture_by_tag, fixture_call_params
from hooks import create_board, delete_board, create_list, delete_list
from main.utils.logger import Logger
# from main.core.rest.request_manager import RequestManager

LOGGER = Logger(__name__)

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
    "fixture.before.create.list": fixture_call_params(
        create_list,
        endpoint="lists/",
        list_name="ListTest"
    ),
    "fixture.after.delete.list": fixture_call_params(
        delete_list,
        endpoint="lists/{id}"
    )
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

    LOGGER.info(f"Starting Scenario: {scenario.name}")
    if scenario.tags:
        LOGGER.info(f"Tags: {scenario.tags}")


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name=f"{context.scenario}{datetime.datetime.now()}",
                      attachment_type=allure.attachment_type.PNG)
    context.driver.close()
    context.driver.quit()
    LOGGER.info(f"Status: {scenario.status}")


def before_tag(context, tag):
    if tag.startswith('fixture.before.'):
        use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)


def after_tag(context, tag):
    if tag.startswith('fixture.after.'):
        use_fixture_by_tag(tag, context, FIXTURE_REGISTRY)


def before_feature(context, feature):
    LOGGER.info(f"Starting Feature: {feature.name}", is_title=True)
    if feature.background:
        LOGGER.info(f"Executing Background: {feature.background.name}")


def after_feature(context, feature):
    LOGGER.info(f"Status for Feature: {feature.name}: {feature.status}", is_title=True)


def before_all(context):

    LOGGER.info("Starting GUI Test Suite", is_title=True)


def after_all(context):
    LOGGER.info("GUI Test Suite End", is_title=True)
