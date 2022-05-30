import re
import json
from jsonschema import validate
from main.utils.common_globals import DEFAULT_SCHEMA_PATH


def find_ids(endpoint: str, regex=r'\{(.*?)\}') -> list:
    """Finds all ids in the endpoint and returns them as a list of strings
    usage in gherkin: '{name_of_the_context_variable}'
    example: 'cards/{card}/checklists/{checklist}'
    """
    return re.findall(regex, endpoint)


def replace_ids(context, endpoint: str) -> str:
    """Finds all ids in the endpoint and replaces them with the corresponding id from the context
    usage in gherkin: '{name_of_the_context_variable}'
    example: 'cards/{card}/checklists/{checklist}'
    """
    replacements = find_ids(endpoint)
    for replacement in replacements:
        endpoint = endpoint.replace("{" + replacement + "}", getattr(context, replacement)['id'])
    return endpoint


def fill_payload(context, payload: dict) -> dict:
    """Fills a paylod from a Data table with the following (case-sensitive) headers:
    | Key | Value |
    if the value needs to be replaced with the value from the context,
    the syntax is as follows: '{attribute_name}:item_name'
    example: '{id}:card'
    """
    if context.table:
        for row in context.table:
            key, value = row['Key'], row['Value']
            to_replace = find_ids(value)
            if to_replace:
                value = getattr(context, value.split(':')[1])[to_replace[0]]
            payload[key] = value
    return payload


def validate_schema(context, schema_name: str):
    with open(DEFAULT_SCHEMA_PATH.format(schema_name), 'r') as f:
        schema = json.load(f)
    return validate(context.response, schema)
