"""
Module that contains global variables which are used for all classes in the Framework
"""
import os

# retrieve Trello API key and Token from environments variables
APIKEY = os.getenv("TRELLO_APIKEY", None)
TOKEN = os.getenv("TRELLO_TOKEN", None)
USERNAME = os.getenv("TRELLO_USERNAME", None)
PASSWORD = os.getenv("TRELLO_PASSWORD", None)
USER = os.getenv("TRELLO_USER", None)
# Default Headers information
HEADERS = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'Authorization': f'OAuth oauth_consumer_key="{APIKEY}", oauth_token="{TOKEN}"'}
# Default API URL and Version
DEFAULT_API_URL = "https://api.trello.com"
API_VERSION = "1"

# Default Schema Path
DEFAULT_SCHEMA_PATH = "./main/schemas/{}.json"
