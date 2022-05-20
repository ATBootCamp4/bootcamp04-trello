from behave import fixture
from main.core.rest.request_manager import RequestManager

request_manager = RequestManager()

def after_scenario(context, scenario): 
    if 'Trello API' in scenario.feature.name:
        request_manager.delete_request('cards/' + context.card['id'])