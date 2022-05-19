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
ID_BOARD = "627c0cb01e98336259fa1ae2"
NAME_BOARD = "API Testing Tasks"
ID_LIST = "627c0cb01e98336259fa1ae4"
NAME_LIST = "Doing"