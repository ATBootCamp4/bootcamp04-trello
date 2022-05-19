from urllib import response
from main.trello.api.rest_base_manager import RESTBaseManager
from main.utils.common_globals import ID_BOARD, ID_LIST


class ListsManager(RESTBaseManager):

    def __init__(self, request_method=None):
        super().__init__(request_method)
    
    def create_list(self, new_name):
        endpoint = f"lists/?name={new_name}&idBoard={ID_BOARD}"
        payload = { "name": new_name}
        status_code, response = self.method.post_request(endpoint, payload)
        return status_code, response

    def get_list(self, idList):
        endpoint = f"lists/{idList}"
        status_code, response = self.method.get_request(endpoint)
        return status_code, response
        
    def get_board_list_is_on(self, idList):
        endpoint = f"lists/{idList}/board"
        status_code, response = self.method.get_request(endpoint)
        return status_code, response
    