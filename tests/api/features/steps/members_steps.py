
from behave import given, when, then, step

from main.utils.common_globals import DEFAULT_BOARD

@step('verify there is at least 1 member')
def step_impl(context):    
    assert len(context.api_response), f"cound't retrieve members from board {DEFAULT_BOARD}"
