from behave import fixture
from main.core.rest.request_manager import RequestManager

request_manager = RequestManager()

def after_scenario(context, scenario): 
    if scenario.feature.name == 'Trello API Checklists':
        request_manager.delete_request('cards/' + context.card['id'])