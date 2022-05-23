"""
Module that contains global variables which are used for all classes in the Framework
"""
import os

# retrieve Trello API key and Token from environments variables
APIKEY = os.getenv("TRELLO_APIKEY", None)
TOKEN = os.getenv("TRELLO_TOKEN", None)
# Default Headers information
HEADERS = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'OAuth oauth_consumer_key="{APIKEY}", oauth_token="{TOKEN}"'
         }
# Default API URL and Version
DEFAULT_API_URL = "https://api.trello.com"
API_VERSION = "1"

DEFAULT_SCHEMAS = {
   "organizations": "./main/schemas/organization_schema.json"
}


DEFAULT_BOARD = 'DefaultBoard'
DEFAULT_MEMBER = 'me'
DEFAULT_WORKSPACE = 'DoNotDeleteWorkspace'

DEFAULT_GET_REQUESTS = {
   "organizations": ("/members/me/organizations", DEFAULT_WORKSPACE),
   "boards": ("/members/me/boards", DEFAULT_BOARD),
}