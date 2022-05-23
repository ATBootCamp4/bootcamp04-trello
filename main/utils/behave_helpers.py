import re
import json
from jsonschema import validate

def replace_ids(context, endpoint: str)-> str:
    """Finds all ids in the endpoint and replaces them with the corresponding id from the context
    usage in gherkin: '{name_of_the_context_variable}'
    example: 'cards/{card}/checklists/{checklist}'
    """
    replacements = re.findall(r'\{(.*?)\}', endpoint) 
    for replacement in replacements:
        endpoint = endpoint.replace("{" + replacement + "}", getattr(context, replacement)['id'])
    return endpoint

def fill_payload(context, payload: dict)-> dict:
    """Fills a paylod from a Data table with the following (case-sensitive) headers:
    | Key | Value |
    """
    if context.table:
        for row in context.table:
            key, value = row['Key'], row['Value']
            if "{id}" in value:
                value = getattr(context, value.split(':')[1])['id']
            payload[key] = value
    return payload

def validate_schema(context, schema_name: str):
    with open(f'./main/schemas/{schema_name}.json', 'r') as f:
        schema = json.load(f)
    return validate(context.response, schema)