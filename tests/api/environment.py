from main.core.rest.request_manager import RequestManager
from main.utils.logger import Logger

LOGGER = Logger(__name__)


def before_all(context):
    context.request_manager = RequestManager()
    _, context.board = context.request_manager.post_request('boards/', payload={'name': 'Behave board'})
    _, context.lists = context.request_manager.get_request(f"boards/{context.board['id']}/lists")
    LOGGER.info("Executed 'before_all' hook, created context.board and context.lists")
    LOGGER.info("Starting Test Suite", is_title=True)


def before_feature(context, feature):
    LOGGER.info(f"Starting Feature: {feature.name}", is_title=True)
    if feature.background:
        LOGGER.info(f"Executing Background: {feature.background.name}")


def before_scenario(context, scenario):
    context.list = context.lists[0]
    LOGGER.info("Executed 'before_scenario' hook, created context.list")
    LOGGER.info(f"Starting Scenario: {scenario.name}")
    if scenario.tags:
        LOGGER.info(f"Tags: {scenario.tags}")


def after_scenario(context, scenario):
    LOGGER.info(f"Status: {scenario.status}")


def after_feature(context, feature):
    LOGGER.info(f"Status for Feature: {feature.name}: {feature.status}", is_title=True)


def after_all(context):
    context.request_manager.delete_request('boards/' + context.board['id'])
    LOGGER.info("Executed 'after_all' hook, deleted context.board")
    LOGGER.info("Test Suite End", is_title=True)
